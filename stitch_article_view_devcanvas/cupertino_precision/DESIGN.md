# Design System Specification: High-End Editorial

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Digital Gallery."** 

This system moves beyond a standard commercial website to treat every interface as a curated exhibition. By prioritizing extreme negative space, intentional asymmetry, and a rejection of traditional structural lines, we create an environment that feels expensive, precise, and quiet. 

To break the "template" look, we leverage high-contrast typography scales—pairing massive, cinematic headlines with delicate, high-tracked labels. Layouts should feel "breathtaking" rather than "efficient," using overlapping elements and shifted grids to guide the eye through a narrative rather than a list of features.

---

## 2. Colors & Surface Philosophy
The palette is rooted in a monochromatic foundation, but its "soul" is found in the subtle shifts of temperature and depth.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders for sectioning or containment. 
Boundaries must be defined solely through background color shifts. For example, a `surface-container-low` section should sit directly against a `surface` background. The transition between these two tones is the only "line" allowed.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of fine paper. Use the following tiers to define depth without shadows:
*   **Base Layer:** `surface` (#f9f9fb) – The canvas for the experience.
*   **The Inset:** `surface-container-low` (#f2f4f6) – Used for subtle secondary content areas.
*   **The Focus:** `surface-container-highest` (#dde3e9) – Used for high-emphasis interactive zones.
*   **The Floating Sheet:** `surface-container-lowest` (#ffffff) – Reserved for primary cards or modals that need to "pop" off a tinted background.

### The Glass & Gradient Rule
To achieve a signature premium feel, use Glassmorphism for floating navigation and context menus.
*   **Token:** `surface` at 80% opacity with a `20px` backdrop-blur. 
*   **Gradients:** Use a subtle linear gradient (Top-Down) from `primary` (#5e5e5e) to `primary-container` (#e2e2e2) for Hero CTAs to provide a tactile, metallic sheen.

---

### 3. Typography
Typography is our primary tool for expressing sophistication. We use the **Inter** family (as a highly legible web alternative to SF Pro) with specific intent.

| Role | Token | Size | Tracking | Weight |
| :--- | :--- | :--- | :--- | :--- |
| **Cinematic Display** | `display-lg` | 3.5rem | -0.02em | Bold (700) |
| **Editorial Headline** | `headline-lg` | 2.0rem | -0.01em | Semi-Bold (600) |
| **Precision Label** | `label-md` | 0.75rem | 0.08em | Medium (500) / All Caps |
| **Standard Body** | `body-lg` | 1.0rem | 0.01em | Regular (400) |

**The Signature Move:** Always pair a `display-lg` headline with a `label-md` tag (All Caps, high tracking) placed precisely above it. This creates an "archival" look used by luxury brands.

---

## 4. Elevation & Depth
In this design system, shadows are a last resort, not a default. We utilize **Tonal Layering**.

*   **The Layering Principle:** Place a `surface-container-lowest` (#ffffff) card on a `surface-container-low` (#f2f4f6) background. The 4% difference in luminosity creates a clean, sophisticated lift.
*   **Ambient Shadows:** For floating elements (e.g., Modals), use a "Long Shadow" approach: `0px 20px 40px rgba(45, 51, 56, 0.06)`. The shadow color must be a tinted version of `on-surface` (#2d3338), never pure black.
*   **The Ghost Border:** If accessibility requires a border, use `outline-variant` (#acb3b8) at **15% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons
*   **Primary:** Background: `primary` (#5e5e5e); Text: `on-primary` (#f8f8f8). Shape: `full` (9999px) or `xl` (1.5rem).
*   **Secondary:** Background: `surface-container-high`; Text: `on-surface`. No border.
*   **Tertiary:** Text only with `label-md` styling and a `1.5` (0.5rem) underline offset.

### Input Fields
*   **Style:** Minimalist underline or subtle background fill (`surface-container-low`). 
*   **Corners:** `md` (0.75rem).
*   **Interaction:** On focus, the background shifts to `surface-container-lowest` and the label slides up using a 300ms cubic-bezier transition.

### Cards & Lists
*   **Constraint:** **Strictly forbid divider lines.** 
*   **Structure:** Separate list items using the `spacing-6` (2rem) scale. Use `surface-container-low` as a hover state for list items to define the hit area.
*   **Rounding:** All cards must use `xl` (1.5rem) corner radius for a friendly yet architectural feel.

### Premium Component Suggestion: The "Hero Parallax Scroller"
Use high-resolution imagery where the text (`display-lg`) scrolls at a different speed than the image, partially overlapping. Use the "Glassmorphism" rule for the text container to ensure legibility while maintaining depth.

---

## 6. Do's and Don'ts

### Do
*   **Embrace the Void:** If a layout feels empty, leave it. Negative space is a feature, not a bug.
*   **Optical Alignment:** Align text to the baseline of icons rather than the center for a more "printed" look.
*   **Subtle Animation:** Use "Slow-In, Fast-Out" easing for all transitions to mimic the movement of high-end physical hardware.

### Don't
*   **No Hard Borders:** Never use a 100% opaque border. It breaks the "Gallery" illusion.
*   **No Pure Black Shadows:** Avoid `rgba(0,0,0,x)`. Always tint shadows with the surface color for a natural, ambient effect.
*   **Don't Over-Color:** Stick to the monochromatic scale. Use `tertiary` or `error` only for functional feedback, never for decoration.