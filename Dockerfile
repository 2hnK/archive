FROM eclipse-temurin:21-jdk-alpine AS builder

RUN apk add --no-cache nodejs npm

WORKDIR /workspace

COPY gradle gradle
COPY gradlew build.gradle settings.gradle package.json package-lock.json ./
COPY src src

RUN chmod +x gradlew \
    && ./gradlew --no-daemon bootJar

FROM eclipse-temurin:21-jre-alpine

RUN addgroup -S devarchive \
    && adduser -S devarchive -G devarchive

WORKDIR /app

COPY --from=builder --chown=devarchive:devarchive \
    /workspace/build/libs/devarchive-0.0.1-SNAPSHOT.jar app.jar

USER devarchive

EXPOSE 8080

HEALTHCHECK --interval=15s --timeout=3s --start-period=20s --retries=3 \
    CMD wget -q -O /dev/null http://127.0.0.1:8080/ || exit 1

ENTRYPOINT ["java", "-jar", "/app/app.jar"]
