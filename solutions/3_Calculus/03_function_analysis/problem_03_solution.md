# Problem 3 Solution: A Rational Function

## 1. Original Problem
Perform a structured analysis of the rational function:
$$f(x) = \frac{x + 1}{x - 2}$$
1. Determine the natural domain $\operatorname{Dom}(f)$ and find the coordinates of any roots (zeros) and axial intercepts.
2. Find the equations of all vertical and horizontal asymptotes using one-sided and infinite limits.
3. Compute the derivative $f'(x)$ and analyze the intervals of monotonicity and extrema.
4. Synthesize all findings to sketch a complete and consistent graph of the function.

---

## 2. What We Are Trying to Find
We need to:
1. Exclude the denominator's root to establish $\operatorname{Dom}(f) = \mathbb{R} \setminus \{2\}$.
2. Set $f(x) = 0$ to find the $x$-intercept, and evaluate $f(0)$ to find the $y$-intercept.
3. Compute the limits as $x \to 2^-$ and $x \to 2^+$ to confirm the vertical asymptote $x = 2$.
4. Compute the limits as $x \to \pm\infty$ to confirm the horizontal asymptote $y = 1$.
5. Differentiate via the Quotient Rule to prove that $f'(x) < 0$ everywhere on its domain, showing the function is strictly decreasing on both disjoint branches with no local extrema.

---

## 3. Key Concepts and Theorems
1. **Domain of a Rational Function:**
   Points where the denominator vanishes are excluded from the domain.
2. **Vertical Asymptote Criterion:**
   If $\lim_{x\to c^\pm} f(x) = \pm\infty$, the line $x = c$ is a vertical asymptote.
3. **Horizontal Asymptote Criterion:**
   If $\lim_{x\to\pm\infty} f(x) = L$, the line $y = L$ is a horizontal asymptote.
4. **Quotient Rule:**
   $$\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}.$$
5. **Monotonicity Across Disconnected Intervals:**
   When a function is strictly decreasing on $(-\infty, 2)$ and strictly decreasing on $(2, \infty)$, one **must not** state that it is decreasing on $(-\infty, 2) \cup (2, \infty)$ as a single set, because values jump across the asymptote.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Domain and Intercepts
1. **Domain:**
   The denominator is $x - 2$.
   $$x - 2 = 0 \iff x = 2.$$
   Therefore:
   $$\operatorname{Dom}(f) = \mathbb{R} \setminus \{2\} = (-\infty, 2) \cup (2, \infty).$$
2. **$x$-intercept (Zero of the function):**
   Set the numerator equal to zero:
   $$x + 1 = 0 \implies x = -1.$$
   Since $-1 \in \operatorname{Dom}(f)$, the unique zero is:
   $$(-1, 0).$$
3. **$y$-intercept:**
   Evaluate at $x = 0$:
   $$f(0) = \frac{0 + 1}{0 - 2} = -\frac{1}{2}.$$
   The $y$-intercept is:
   $$\left(0, -\frac{1}{2}\right).$$

---

### Step 2: Asymptotes and Limits
1. **Vertical Asymptote at $x = 2$:**
   Compute the one-sided limits as $x \to 2$:
   - Left-hand limit ($x \to 2^-$): $x < 2 \implies x - 2 \to 0^-$, while $x + 1 \to 3 > 0$:
     $$\lim_{x\to2^-} \frac{x + 1}{x - 2} = \left[\frac{3}{0^-}\right] = -\infty.$$
   - Right-hand limit ($x \to 2^+$): $x > 2 \implies x - 2 \to 0^+$, while $x + 1 \to 3 > 0$:
     $$\lim_{x\to2^+} \frac{x + 1}{x - 2} = \left[\frac{3}{0^+}\right] = +\infty.$$
   Because both one-sided limits are infinite, the vertical line:
   $$x = 2$$
   is a **vertical asymptote**.

2. **Horizontal Asymptote as $x \to \pm\infty$:**
   Divide numerator and denominator by $x$:
   $$\lim_{x\to\pm\infty} \frac{x + 1}{x - 2} = \lim_{x\to\pm\infty} \frac{1 + \frac{1}{x}}{1 - \frac{2}{x}} = \frac{1 + 0}{1 - 0} = 1.$$
   Because the limit as $x \to \pm\infty$ is $1$, the horizontal line:
   $$y = 1$$
   is a **horizontal asymptote** in both directions ($x \to +\infty$ and $x \to -\infty$).

---

### Step 3: Derivative, Monotonicity, and Extrema
Apply the Quotient Rule to $f(x) = \frac{x + 1}{x - 2}$:
- $u(x) = x + 1 \implies u'(x) = 1$
- $v(x) = x - 2 \implies v'(x) = 1$

$$f'(x) = \frac{u'v - uv'}{v^2} = \frac{(1)(x - 2) - (x + 1)(1)}{(x - 2)^2} = \frac{x - 2 - x - 1}{(x - 2)^2} = \frac{-3}{(x - 2)^2}.$$

**Sign Analysis of $f'(x)$:**
- The numerator is the constant $-3$, which is strictly negative.
- The denominator is $(x - 2)^2$, which is strictly positive for all $x \in \operatorname{Dom}(f)$ ($x \neq 2$).
- Therefore, for **every** point in the domain:
  $$f'(x) = \frac{-3}{(x - 2)^2} < 0 \quad \text{for all } x \neq 2.$$

**Conclusions on Monotonicity and Extrema:**
1. $f(x)$ is **strictly decreasing** on the interval $(-\infty, 2)$.
2. $f(x)$ is **strictly decreasing** on the interval $(2, \infty)$.
3. Because $f'(x) \neq 0$ everywhere and is never undefined on its domain, there are **no critical points** and **no local extrema** (no local maxima or local minima).

---

### Step 4: Sketching Guide
- Draw the coordinate axes.
- Draw the vertical dashed asymptote $x = 2$ and the horizontal dashed asymptote $y = 1$. The intersection of the asymptotes $(2, 1)$ serves as the center of point-symmetry for the hyperbola.
- **Left Branch ($x < 2$):** Starts just below the horizontal asymptote $y = 1$ as $x \to -\infty$, curves downward through the $x$-intercept $(-1, 0)$, crosses the $y$-intercept $(0, -0.5)$, and plunges toward $-\infty$ as it approaches the vertical asymptote $x = 2$.
- **Right Branch ($x > 2$):** Descends from $+\infty$ along the right side of the vertical asymptote $x = 2$, remaining entirely in the upper region $y > 1$, and flattens out asymptotically toward $y = 1$ from above as $x \to +\infty$.

---

## 5. Why Each Step Is Valid
1. **$x = 2$ is excluded** because division by zero is undefined.
2. **The limits $\pm\infty$** strictly satisfy the definition of a vertical asymptote.
3. **The Quotient Rule** expansion $(x - 2) - (x + 1) = -3$ is an exact algebraic reduction.
4. **$f'(x) < 0$** rigorously proves strict monotonic decrease via the Mean Value Theorem on each connected component of the domain.

---

## 6. Final Answer in Words
The domain of $f(x) = \frac{x + 1}{x - 2}$ is $\operatorname{Dom}(f) = (-\infty, 2) \cup (2, \infty)$. The function has a single zero at $(-1, 0)$ and a $y$-intercept at $(0, -0.5)$. The vertical asymptote is the line $x = 2$ (with $\lim_{x\to2^-} f(x) = -\infty$ and $\lim_{x\to2^+} f(x) = +\infty$), and the horizontal asymptote is the line $y = 1$ as $x \to \pm\infty$. The derivative is $f'(x) = \frac{-3}{(x - 2)^2}$, which is strictly negative everywhere on the domain, proving that the function is strictly decreasing on both $(-\infty, 2)$ and $(2, \infty)$ with no local extrema.

---

## 7. Quick Verification
- Point-symmetry check around $(2, 1)$:
  Let $x = 2 + t$.
  $$f(2 + t) = \frac{(2 + t) + 1}{(2 + t) - 2} = \frac{t + 3}{t} = 1 + \frac{3}{t}.$$
  Let $x = 2 - t$.
  $$f(2 - t) = \frac{(2 - t) + 1}{(2 - t) - 2} = \frac{3 - t}{-t} = 1 - \frac{3}{t}.$$
  Notice that:
  $$\frac{f(2 + t) + f(2 - t)}{2} = \frac{(1 + 3/t) + (1 - 3/t)}{2} = \frac{2}{2} = 1.$$
  The curve is perfectly point-symmetric about the center of its asymptotes $(2, 1)$!

---

## 8. Common Mistakes to Avoid
- **Claiming the function is decreasing on $(-\infty, 2) \cup (2, \infty)$ as a single statement:** Note that $f(0) = -0.5$, while $f(3) = 4$. If you mistakenly consider the union, $0 < 3$ but $f(0) < f(3)$, which would seem to violate decreasing behavior. One must specify that it is decreasing on each interval *separately*.
- **Numerator sign error in Quotient Rule:** Writing $(x - 2) + (x + 1) = 2x - 1$ instead of $-3$.
- **Believing $y = 1$ is crossed:** Setting $\frac{x + 1}{x - 2} = 1 \implies x + 1 = x - 2 \implies 1 = -2$ (no solution), confirming the curve never intersects its horizontal asymptote.

---

## 9. Classroom Presentation (3-Sentence Summary)
The rational function $f(x) = (x + 1)/(x - 2)$ has domain all real numbers except $x = 2$, with axial intercepts at $(-1, 0)$ and $(0, -0.5)$. One-sided and infinite limits establish a vertical asymptote at $x = 2$ and a horizontal asymptote at $y = 1$, which intersect at the hyperbola's center of symmetry $(2, 1)$. Applying the Quotient Rule gives the derivative $f'(x) = -3/(x - 2)^2$, which is strictly negative everywhere it is defined, proving that the graph consists of two separate branches that both decrease smoothly without any local extrema.
