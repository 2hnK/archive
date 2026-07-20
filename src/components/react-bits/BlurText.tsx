import { useRef } from "react";
import { motion, useInView, useReducedMotion, type TargetAndTransition } from "motion/react";

interface BlurTextProps {
  text: string;
  className?: string;
  delay?: number;
  animateBy?: "words" | "letters";
  direction?: "top" | "bottom";
}

export default function BlurText({
  text,
  className = "",
  delay = 70,
  animateBy = "words",
  direction = "top",
}: BlurTextProps) {
  const rootRef = useRef<HTMLSpanElement>(null);
  const isInView = useInView(rootRef, { once: true, amount: 0.55 });
  const shouldReduceMotion = useReducedMotion();
  const segments = animateBy === "letters" ? Array.from(text) : text.split(" ");
  const offset = direction === "top" ? -10 : 10;
  const hiddenState: TargetAndTransition = { opacity: 0, filter: "blur(10px)", y: offset };
  const visibleState: TargetAndTransition = { opacity: 1, filter: "blur(0px)", y: 0 };

  return (
    <span ref={rootRef} className={`react-bits-blur-text ${className}`} aria-label={text}>
      {segments.map((segment, index) => {
        const needsWordGap = animateBy === "words" && index < segments.length - 1;
        const renderedSegment = animateBy === "letters" && segment === " " ? "\u00A0" : segment;

        return (
          <motion.span
            key={`${segment}-${index}`}
            aria-hidden="true"
            className="inline-block"
            style={needsWordGap ? { marginRight: "0.22em" } : undefined}
            initial={shouldReduceMotion ? false : hiddenState}
            animate={isInView || shouldReduceMotion ? visibleState : undefined}
            transition={{ duration: 0.55, delay: (delay * index) / 1000, ease: [0.22, 1, 0.36, 1] }}
          >
            {renderedSegment}
          </motion.span>
        );
      })}
    </span>
  );
}
