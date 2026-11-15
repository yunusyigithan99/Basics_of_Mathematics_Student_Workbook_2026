# Problem 12: Symmetry, Parity, and Absolute Value in Definite Integrals

## 1. Original Problem
Compare
$$\int_{-2}^{2}x\,dx$$
and
$$\int_{-2}^{2}|x|\,dx.$$
Before calculating, predict the results from symmetry and a sketch, then carry out the calculation and explain the difference.

---

## 2. What We Are Trying to Find
1. Geometric and algebraic predictions for both integrals based on function parity (odd vs. even) over the symmetric interval $[-2, 2]$.
2. Clear sketches demonstrating the signed cancellation versus area addition.
3. The exact analytical evaluations of both definite integrals.
4. A conceptual explanation of why the two results differ so fundamentally.

---

## 3. Key Concepts and Theorems
1. **Symmetric Intervals and Odd Functions:**
   If $f(-x) = -f(x)$ (odd function) for all $x \in [-a, a]$, then:
   $$\int_{-a}^a f(x)\,dx = 0.$$
   The signed areas on the left and right of the origin have equal magnitude and opposite signs, canceling completely.
2. **Symmetric Intervals and Even Functions:**
   If $g(-x) = g(x)$ (even function) for all $x \in [-a, a]$, then:
   $$\int_{-a}^a g(x)\,dx = 2 \int_0^a g(x)\,dx.$$
   The areas on both sides of the $y$-axis are identical in magnitude and sign.
3. **Piecewise Splitting for Absolute Value:**
   $$|x| = \begin{cases} -x & \text{if } x < 0, \\ x & \text{if } x \ge 0. \end{cases}$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Predict the results from symmetry and sketches

#### Function 1: $f(x) = x$
- **Parity:** $f(-x) = -x = -f(x)$. The function is **odd**; its graph is symmetric with respect to the origin $(0, 0)$.
- **Sketch & Geometry:**
  - On $[-2, 0]$, the graph is a triangle below the $x$-axis with base $2$ and height $2$, yielding signed area $-2$.
  - On $[0, 2]$, the graph is a triangle above the $x$-axis with base $2$ and height $2$, yielding signed area $+2$.
- **Prediction:** The two equal and opposite triangular regions will cancel out completely:
  $$\int_{-2}^2 x\,dx = (-2) + (+2) = 0.$$

#### Function 2: $g(x) = |x|$
- **Parity:** $g(-x) = |-x| = |x| = g(x)$. The function is **even**; its graph is symmetric with respect to the $y$-axis.
- **Sketch & Geometry:**
  - On $[-2, 0]$, the reflection forces the triangle above the $x$-axis, yielding signed area $+2$.
  - On $[0, 2]$, the triangle lies above the $x$-axis, yielding signed area $+2$.
- **Prediction:** Because both triangles lie strictly above the axis, their areas reinforce each other:
  $$\int_{-2}^2 |x|\,dx = 2 + 2 = 4.$$

```text
       Graph of f(x) = x                      Graph of g(x) = |x|
              y                                      y
              |        * (2, 2)                      |
              |       /                              \       /
              |      /                                \     /
       -------+-----*-----+----> x             -------+----*----+----> x
           -2 |    0      2                        -2 |   0     2
             /|                                       |
    (-2,-2) * |                                 Both sides above axis!
       Opposite signs cancel!                      Areas add: 2 + 2 = 4
```

### Step 2: Compute $\int_{-2}^2 x\,dx$ analytically
Using the Fundamental Theorem of Calculus:
$$\int_{-2}^2 x\,dx = \left[\frac{x^2}{2}\right]_{-2}^2 = \frac{2^2}{2} - \frac{(-2)^2}{2} = \frac{4}{2} - \frac{4}{2} = 2 - 2 = 0.$$
This confirms the geometric prediction of $0$ exactly.

### Step 3: Compute $\int_{-2}^2 |x|\,dx$ analytically
Because $|x|$ is defined piecewise, we split the integral at the transition point $x = 0$:
$$\int_{-2}^2 |x|\,dx = \int_{-2}^0 (-x)\,dx + \int_0^2 x\,dx.$$
Evaluating each definite integral separately:
- **Left integral (on $[-2, 0]$):**
  $$\int_{-2}^0 (-x)\,dx = \left[-\frac{x^2}{2}\right]_{-2}^0 = \left(-\frac{0^2}{2}\right) - \left(-\frac{(-2)^2}{2}\right) = 0 - \left(-\frac{4}{2}\right) = 0 - (-2) = 2.$$
- **Right integral (on $[0, 2]$):**
  $$\int_0^2 x\,dx = \left[\frac{x^2}{2}\right]_0^2 = \frac{2^2}{2} - \frac{0^2}{2} = 2 - 0 = 2.$$

Summing the two components:
$$\int_{-2}^2 |x|\,dx = 2 + 2 = 4.$$
Using the symmetry property of even functions:
$$\int_{-2}^2 |x|\,dx = 2 \int_0^2 x\,dx = 2 \left[\frac{x^2}{2}\right]_0^2 = 2(2) = 4.$$
Both calculations confirm the geometric prediction of $4$.

### Step 4: Explain the difference between the two results
The fundamental difference lies in how each function handles signs across the origin:
1. **$\int_{-2}^2 x\,dx = 0$** represents **net signed accumulation**. For an odd function over a symmetric domain, negative values on the left balance positive values on the right in exact opposition ($\Delta y = -\Delta y$), summing algebraically to zero.
2. **$\int_{-2}^2 |x|\,dx = 4$** represents **total geometric area**. The absolute value reflects all negative outputs into positive outputs, transforming an odd function into an even one. Cancellation is completely eliminated, and every piece contributes positively to the total area.

---

## 5. Why Each Step Is Valid
- **Step 1:** Function parity theorems are rigorous consequences of Riemann sum definitions over symmetric partitions.
- **Step 2:** The antiderivative of $x$ is $x^2/2$, which is an even function, ensuring $F(a) - F(-a) = 0$.
- **Step 3:** The domain additivity property $\int_a^c = \int_a^b + \int_b^c$ allows evaluating piecewise functions by splitting at transition points.
- **Step 4:** The absolute value operation eliminates sign alternation, converting signed net balance into cumulative positive area.

---

## 6. Final Answer in Words
Before calculating, symmetry predicts that $\int_{-2}^2 x\,dx = 0$ because $f(x) = x$ is an odd function whose equal triangular areas below and above the $x$-axis cancel out. Conversely, $\int_{-2}^2 |x|\,dx = 4$ because $g(x) = |x|$ is an even function whose two positive triangular regions of area $2$ reinforce each other. 
Exact integration confirms:
$$\int_{-2}^2 x\,dx = \left[\frac{x^2}{2}\right]_{-2}^2 = 0,$$
$$\int_{-2}^2 |x|\,dx = \int_{-2}^0 (-x)\,dx + \int_0^2 x\,dx = 2 + 2 = 4.$$
The difference is that the first integral measures signed cancellation (net area), whereas the second measures total geometric area.

---

## 7. Quick Verification
- Triangle area formula:
  Each triangle has base $b = 2$ and height $h = 2$, so area $= \frac{1}{2}(2)(2) = 2$.
  - For $x$: Area$_{\text{signed}} = -2 + 2 = 0$.
  - For $|x|$: Area$_{\text{total}} = | -2 | + 2 = 2 + 2 = 4$.
Geometric and analytical methods agree completely.

---

## 8. Common Mistakes to Avoid
- **Treating $\int |x|\,dx$ as $\left|\int x\,dx\right|$:** Confusing $\int_{-2}^2 |x|\,dx$ with $|\int_{-2}^2 x\,dx| = |0| = 0$, which is false; the absolute value is inside the integral, preventing cancellation.
- **Sign errors when evaluating $-\frac{x^2}{2}$ at $-2$:** Carefully computing $- \left(-\frac{(-2)^2}{2}\right) = - (-2) = +2$.
- **Integrating $|x|$ without splitting:** Trying to find a single antiderivative formula for $|x|$ on $[-2, 2]$ without splitting at $x = 0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Because $f(x) = x$ is an odd function, the triangular region of area $2$ below the $x$-axis cancels the triangular region of area $2$ above it, producing an integral of $0$. Applying the absolute value reflects the left triangle above the axis, making the function even and causing both areas of $2$ to add together to $4$. This comparison highlights that a standard definite integral measures net signed balance, whereas integrating an absolute value calculates total geometric area.
