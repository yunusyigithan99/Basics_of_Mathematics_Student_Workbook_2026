# Problem 9 Solution: One-Sided Limits and an Asymptote

## 1. Original Problem
Consider the rational function:
$$f(x) = \frac{1}{x - 2}.$$
1. Analyze and compute the left-hand limit $\lim_{x\to2^-} f(x)$ and the right-hand limit $\lim_{x\to2^+} f(x)$.
2. Determine whether the two-sided limit $\lim_{x\to2} f(x)$ exists.
3. Interpret the analytical results geometrically on a sketch of the graph and identify the equation of the vertical asymptote.

---

## 2. What We Are Trying to Find
We need to:
1. Examine the behavior of the denominator $(x - 2)$ as $x$ approaches $2$ from below ($x < 2$) and from above ($x > 2$).
2. Evaluate both one-sided infinite limits $\left[\frac{1}{0^-}\right]$ and $\left[\frac{1}{0^+}\right]$.
3. Apply the criterion for the existence of a two-sided limit.
4. Define the vertical asymptote $x = 2$ and describe the hyperbolic shape of the graph.

---

## 3. Key Concepts and Theorems
1. **One-Sided Limits:**
   - The left-hand limit $\lim_{x\to c^-} f(x)$ considers only values of $x < c$.
   - The right-hand limit $\lim_{x\to c^+} f(x)$ considers only values of $x > c$.
2. **Criterion for Existence of a Two-Sided Limit:**
   The two-sided limit $\lim_{x\to c} f(x) = L$ exists (where $L$ may be finite or $\pm\infty$) if and only if both one-sided limits exist and are strictly equal:
   $$\lim_{x\to c} f(x) = L \iff \lim_{x\to c^-} f(x) = L \quad \text{and} \quad \lim_{x\to c^+} f(x) = L.$$
   If $\lim_{x\to c^-} f(x) \neq \lim_{x\to c^+} f(x)$, the two-sided limit **does not exist**.
3. **Signed Zero Rules for Division:**
   $$\frac{1}{0^+} = +\infty, \qquad \frac{1}{0^-} = -\infty.$$
4. **Definition of a Vertical Asymptote:**
   The vertical line $x = c$ is a vertical asymptote of the graph of $y = f(x)$ if at least one of the one-sided limits $\lim_{x\to c^\pm} f(x)$ is $+\infty$ or $-\infty$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze the Left-Hand Limit ($x \to 2^-$)
Consider $x$ approaching $2$ strictly from the left, meaning $x < 2$:
- Since $x < 2$, the difference $x - 2$ is strictly **negative**:
  $$x - 2 < 0.$$
- As $x \to 2^-$, the quantity $x - 2$ approaches $0$ through negative values, denoted by $0^-$:
  $$x - 2 \to 0^-.$$
- Dividing a positive constant ($+1$) by an arbitrarily small negative number produces an arbitrarily large negative number:
  $$\lim_{x\to2^-} \frac{1}{x - 2} = \left[\frac{1}{0^-}\right] = -\infty.$$
Thus, the left-hand limit is $-\infty$.

### Step 2: Analyze the Right-Hand Limit ($x \to 2^+$)
Consider $x$ approaching $2$ strictly from the right, meaning $x > 2$:
- Since $x > 2$, the difference $x - 2$ is strictly **positive**:
  $$x - 2 > 0.$$
- As $x \to 2^+$, the quantity $x - 2$ approaches $0$ through positive values, denoted by $0^+$:
  $$x - 2 \to 0^+.$$
- Dividing a positive constant ($+1$) by an arbitrarily small positive number produces an arbitrarily large positive number:
  $$\lim_{x\to2^+} \frac{1}{x - 2} = \left[\frac{1}{0^+}\right] = +\infty.$$
Thus, the right-hand limit is $+\infty$.

### Step 3: Determine Whether the Two-Sided Limit Exists
Compare the two one-sided results:
$$\lim_{x\to2^-} f(x) = -\infty, \qquad \lim_{x\to2^+} f(x) = +\infty.$$
Because the left-hand limit and the right-hand limit approach opposite infinities:
$$-\infty \neq +\infty.$$
Therefore, the two-sided limit:
$$\lim_{x\to2} \frac{1}{x - 2} \quad \textbf{does not exist (DNE)}.$$

---

### Step 4: Geometric Interpretation and Vertical Asymptote
1. **Vertical Asymptote:**
   Because $\lim_{x\to2^-} f(x) = -\infty$ and $\lim_{x\to2^+} f(x) = +\infty$, the line:
   $$x = 2$$
   is a **vertical asymptote** of the curve.
2. **Geometric Behavior on the Graph:**
   - The graph of $f(x) = \frac{1}{x - 2}$ is a rectangular hyperbola shifted $2$ units to the right relative to the standard hyperbola $y = \frac{1}{x}$.
   - **As $x$ approaches $2$ from the left ($x \to 2^-$):** The curve dives downward infinitely into the fourth quadrant, hugging the vertical line $x = 2$ toward $-\infty$.
   - **As $x$ approaches $2$ from the right ($x \to 2^+$):** The curve shoots upward infinitely into the first quadrant, hugging the vertical line $x = 2$ toward $+\infty$.
   - **Horizontal Asymptote:** As $x \to \pm\infty$, $f(x) \to 0$, so the line $y = 0$ (the $x$-axis) is the horizontal asymptote.

---

## 5. Why Each Step Is Valid
1. **Distinguishing $0^+$ and $0^-$** is valid because the real number line is ordered; whether the denominator approaches zero from above or below determines the sign of the quotient.
2. **The non-existence of the two-sided limit** follows directly from the definition requiring directional uniqueness.
3. **The identification of $x = 2$ as an asymptote** satisfies the standard definition requiring at least one one-sided limit to diverge to $\pm\infty$.

---

## 6. Final Answer in Words
The left-hand limit is $\lim_{x\to2^-} \frac{1}{x-2} = -\infty$, and the right-hand limit is $\lim_{x\to2^+} \frac{1}{x-2} = +\infty$. Because these two one-sided limits are not equal ($-\infty \neq +\infty$), the two-sided limit $\lim_{x\to2} \frac{1}{x-2}$ does not exist. Geometrically, the line $x = 2$ is a vertical asymptote of the function; as the curve approaches $x = 2$ from the left it plunges downward to $-\infty$, while as it approaches from the right it rises upward to $+\infty$.

---

## 7. Quick Verification
- **Test left-hand values:**
  - $x = 1.9 \implies f(1.9) = \frac{1}{1.9 - 2} = \frac{1}{-0.1} = -10$.
  - $x = 1.99 \implies f(1.99) = \frac{1}{-0.01} = -100$.
  - $x = 1.999 \implies f(1.999) = \frac{1}{-0.001} = -1000 \to -\infty$.
- **Test right-hand values:**
  - $x = 2.1 \implies f(2.1) = \frac{1}{2.1 - 2} = \frac{1}{0.1} = +10$.
  - $x = 2.01 \implies f(2.01) = \frac{1}{0.01} = +100$.
  - $x = 2.001 \implies f(2.001) = \frac{1}{0.001} = +1000 \to +\infty$.
The numerical evidence completely confirms the opposite infinite divergences.

---

## 8. Common Mistakes to Avoid
- **Writing $\lim_{x\to2} \frac{1}{x-2} = \infty$ without a sign:** Using unsigned infinity obscures the fact that the two sides go in opposite directions; the two-sided limit does not exist.
- **Thinking $\frac{1}{0}$ is always $+\infty$:** Ignoring the negative sign when $x < 2$.
- **Confusing vertical and horizontal asymptotes:** Writing the vertical asymptote as $y = 2$ instead of $x = 2$.

---

## 9. Classroom Presentation (3-Sentence Summary)
As $x$ approaches 2 from the left, the denominator $x - 2$ is negative and approaches zero, driving $1/(x-2)$ down to negative infinity. When approaching from the right, the denominator is positive and approaches zero, sending the function value up to positive infinity. Because the two one-sided limits are opposite infinities and disagree, the two-sided limit does not exist, and the vertical line $x = 2$ forms a vertical asymptote where the hyperbolic branches diverge in opposite directions.
