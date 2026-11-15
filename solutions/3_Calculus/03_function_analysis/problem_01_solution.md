# Problem 1 Solution: A Cubic Polynomial

## 1. Original Problem
For the cubic polynomial function:
$$f(x) = x^3 - 3x^2 + 2$$
1. Find the intervals of monotonicity (where the function is strictly increasing or strictly decreasing).
2. Determine the local extrema (local maxima and local minima) and compute their exact coordinates.
3. Provide a guide for sketching the graph based on the analytical results, marking all critical points and axes intercepts.

---

## 2. What We Are Trying to Find
We need to:
1. Compute the first derivative $f'(x)$ and determine its critical points by solving $f'(x) = 0$.
2. Construct a sign chart for $f'(x)$ across the real line.
3. Apply the First Derivative Test to classify the critical points into local extrema.
4. Calculate the corresponding $y$-coordinates and axial intercepts.
5. Synthesize these properties to sketch the characteristic cubic S-curve.

---

## 3. Key Concepts and Theorems
1. **Critical Points:**
   Points in the domain where $f'(x) = 0$ or where $f'(x)$ does not exist.
2. **First Derivative Test for Monotonicity:**
   - If $f'(x) > 0$ on an interval, $f$ is **strictly increasing** ($\nearrow$).
   - If $f'(x) < 0$ on an interval, $f$ is **strictly decreasing** ($\searrow$).
3. **Classification of Local Extrema:**
   - If $f'(x)$ changes sign from $+$ to $-$ across $c$, then $f(c)$ is a **local maximum**.
   - If $f'(x)$ changes sign from $-$ to $+$ across $c$, then $f(c)$ is a **local minimum**.
4. **Behavior at Infinity for Polynomials:**
   As $x \to +\infty$, $x^3 \to +\infty$. As $x \to -\infty$, $x^3 \to -\infty$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the First Derivative
Differentiate $f(x) = x^3 - 3x^2 + 2$ using the power rule:
$$f'(x) = \frac{d}{dx}[x^3] - 3\frac{d}{dx}[x^2] + \frac{d}{dx}[2] = 3x^2 - 6x.$$

---

### Step 2: Find the Critical Points
Set the derivative equal to zero:
$$f'(x) = 0 \implies 3x^2 - 6x = 0.$$
Factor out the common term $3x$:
$$3x(x - 2) = 0.$$
This yields two real critical points:
$$x_1 = 0 \quad \text{and} \quad x_2 = 2.$$

---

### Step 3: Construct the Sign Chart for $f'(x)$
The two critical points divide the real line into three disjoint test intervals:
$$(-\infty, 0), \qquad (0, 2), \qquad (2, \infty).$$

We test the sign of $f'(x) = 3x(x - 2)$ in each interval:
1. **Interval $(-\infty, 0)$:**
   Choose test point $x = -1$:
   $$f'(-1) = 3(-1)(-1 - 2) = (-3)(-3) = +9 > 0.$$
   Therefore, $f'(x) > 0$, so $f(x)$ is **strictly increasing** on $(-\infty, 0]$.
2. **Interval $(0, 2)$:**
   Choose test point $x = 1$:
   $$f'(1) = 3(1)(1 - 2) = 3(-1) = -3 < 0.$$
   Therefore, $f'(x) < 0$, so $f(x)$ is **strictly decreasing** on $[0, 2]$.
3. **Interval $(2, \infty)$:**
   Choose test point $x = 3$:
   $$f'(3) = 3(3)(3 - 2) = 9(1) = +9 > 0.$$
   Therefore, $f'(x) > 0$, so $f(x)$ is **strictly increasing** on $[2, \infty)$.

---

### Step 4: Determine the Local Extrema
1. **At $x = 0$:**
   The derivative changes sign from positive to negative ($+ \to -$).
   Therefore, $f$ has a **local maximum** at $x = 0$.
   Compute the $y$-coordinate:
   $$f(0) = 0^3 - 3(0)^2 + 2 = 2.$$
   Local maximum point:
   $$M = (0, 2).$$
2. **At $x = 2$:**
   The derivative changes sign from negative to positive ($- \to +$).
   Therefore, $f$ has a **local minimum** at $x = 2$.
   Compute the $y$-coordinate:
   $$f(2) = 2^3 - 3(2)^2 + 2 = 8 - 12 + 2 = -2.$$
   Local minimum point:
   $$m = (2, -2).$$

---

### Step 5: Intercepts and Sketching Guide
- **$y$-intercept:** $(0, 2)$.
- **$x$-intercepts (Roots):**
  Set $f(x) = x^3 - 3x^2 + 2 = 0$.
  Notice that $x = 1$ is a root: $1^3 - 3(1)^2 + 2 = 1 - 3 + 2 = 0$.
  Divide by $(x - 1)$:
  $$x^3 - 3x^2 + 2 = (x - 1)(x^2 - 2x - 2) = 0.$$
  The roots of $x^2 - 2x - 2 = 0$ are $x = \frac{2 \pm \sqrt{4 + 8}}{2} = 1 \pm \sqrt{3} \approx 1 \pm 1.732$.
  Roots: $x_1 = 1$, $x_2 \approx 2.732$, $x_3 \approx -0.732$.
- **Inflection Point:**
  $f''(x) = 6x - 6 = 0 \implies x = 1, f(1) = 0$. The inflection point is $(1, 0)$, which is the point of point-symmetry for the cubic.
- **Sketching Instructions:**
  1. Plot the local maximum at $(0, 2)$ with a flat horizontal tangent.
  2. Plot the local minimum at $(2, -2)$ with a flat horizontal tangent.
  3. Mark the inflection point at $(1, 0)$ where the curve changes from concave down to concave up.
  4. Draw the curve rising from $-\infty$ in the third quadrant, crossing the $x$-axis at $\approx -0.732$, peaking at $(0, 2)$, descending through $(1, 0)$ to the trough at $(2, -2)$, and rising through $\approx 2.732$ to $+\infty$.

---

## 5. Why Each Step Is Valid
1. **Factoring $f'(x) = 3x(x - 2)$** finds all roots where the tangent line is horizontal.
2. **The First Derivative Test** is a proven theorem based on the Mean Value Theorem.
3. **The factorization $(x - 1)(x^2 - 2x - 2)$** is verified by polynomial long division.

---

## 6. Final Answer in Words
The function $f(x) = x^3 - 3x^2 + 2$ is strictly increasing on $(-\infty, 0]$ and $[2, \infty)$, and strictly decreasing on $[0, 2]$. It has a local maximum at the point $(0, 2)$ and a local minimum at the point $(2, -2)$. The curve crosses the $y$-axis at $(0, 2)$, has roots at $x = 1$ and $x = 1 \pm \sqrt{3}$, and changes curvature at the inflection point $(1, 0)$.

---

## 7. Quick Verification
- **Second Derivative Test:**
  $$f''(x) = 6x - 6.$$
  - At $x = 0$: $f''(0) = -6 < 0 \implies$ confirms local maximum.
  - At $x = 2$: $f''(2) = 12 - 6 = 6 > 0 \implies$ confirms local minimum.
- **Symmetry check around inflection point $(1, 0)$:**
  $$f(1 + t) = (1+t)^3 - 3(1+t)^2 + 2 = (1 + 3t + 3t^2 + t^3) - 3(1 + 2t + t^2) + 2 = t^3 - 3t.$$
  $$f(1 - t) = (1-t)^3 - 3(1-t)^2 + 2 = -t^3 + 3t = -f(1 + t).$$
  The function is perfectly anti-symmetric about $(1, 0)$.

---

## 8. Common Mistakes to Avoid
- **Confusing $x$-coordinates with extrema values:** Stating the maximum is 0 (the $x$-value) instead of 2 (the $y$-value).
- **Miscalculating $f(2)$:** Getting $8 - 12 + 2 = 2$ instead of $-2$.
- **Writing open vs. closed intervals:** Monotonicity can be stated on closed intervals $[0, 2]$ because continuity at the endpoints preserves the ordering $f(a) \le f(b)$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Differentiating the cubic gives $f'(x) = 3x(x - 2)$, which reveals two critical points at $x = 0$ and $x = 2$. Testing the signs of the derivative shows that the function increases on $(-\infty, 0]$, decreases on $[0, 2]$, and increases on $[2, \infty)$, establishing a local maximum at $(0, 2)$ and a local minimum at $(2, -2)$. Connecting these extrema with the inflection point at $(1, 0)$ produces the classic S-shaped cubic graph rising smoothly from negative infinity to positive infinity.
