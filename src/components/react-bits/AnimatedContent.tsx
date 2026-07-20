import { useRef, type ReactNode } from "react";
import { motion, useInView, useReducedMotion } from "motion/react";

interface AnimatedContentProps {
  children: ReactNode;
  className?: string;
  distance?: number;
  direction?: "vertical" | "horizontal";
  reverse?: boolean;
  duration?: number;
  delay?: number;
}

export default function AnimatedContent({
  children,
  className = "",
  distance = 36,
  direction = "vertical",
  reverse = false,
  duration = 0.8,
  delay = 0,
}: AnimatedContentProps) {
  const rootRef = useRef<HTMLDivElement>(null);
  const isInView = useInView(rootRef, { once: true, amount: 0.12, margin: "0px 0px -8% 0px" });
  const shouldReduceMotion = useReducedMotion();
  const signedDistance = reverse ? -distance : distance;
  const initialTransform = direction === "horizontal" ? { x: signedDistance, y: 0 } : { x: 0, y: signedDistance };
  const isVisible = isInView || shouldReduceMotion;

  return (
    <motion.div
      ref={rootRef}
      className={`react-bits-animated-content ${className}`}
      initial={{ opacity: shouldReduceMotion ? 1 : 0, ...initialTransform }}
      animate={isVisible ? { opacity: 1, x: 0, y: 0 } : undefined}
      transition={{ duration: shouldReduceMotion ? 0 : duration, delay, ease: [0.22, 1, 0.36, 1] }}
    >
      {children}
    </motion.div>
  );
}
