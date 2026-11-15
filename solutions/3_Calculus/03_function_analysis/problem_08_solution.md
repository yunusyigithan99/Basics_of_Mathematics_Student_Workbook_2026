# Problem 08: Second Derivative, Extrema, and Curvature Analysis

## 1. Original Problem
For
$$f(x) = x^4 - 4x^2$$
find the local extrema, intervals of convexity and concavity, and inflection points. Sketch the graph and mark all the identified features on it.

---

## 2. What We Are Trying to Find
1. The domain, symmetry, and real zeros of $f(x)$.
2. The first derivative $f'(x)$ and all local extrema (locations, values, and classification).
3. The second derivative $f''(x)$ and the intervals where the graph is convex (concave up) or concave (concave down).
4. All inflection points of the graph.
5. A clear qualitative diagram/sketch marking roots, extrema, and inflection points.

---

## 3. Key Concepts and Theorems
1. **Symmetry (Even Function):**
   If $f(-x) = f(x)$, the function is even, meaning its graph is symmetric with respect to the $y$-axis.
2. **First Derivative and Extrema:**
   Critical points satisfy $f'(x) = 0$. By the First Derivative Test:
   - A change from negative to positive derivative indicates a local minimum.
   - A change from positive to negative derivative indicates a local maximum.
3. **Second Derivative and Curvature:**
   - Where $f''(x) > 0$, the function is **strictly convex** (concave up).
   - Where $f''(x) < 0$, the function is **strictly concave** (concave down).
4. **Inflection Points:**
   A point $(x_0, f(x_0))$ is an inflection point if $f$ has a tangent line at $x_0$ and $f''(x)$ strictly changes sign across $x_0$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Basic properties, domain, and roots
- **Domain:** $D_f = \mathbb{R}$ since $f$ is a polynomial.
- **Symmetry:**
  $$f(-x) = (-x)^4 - 4(-x)^2 = x^4 - 4x^2 = f(x).$$
  The graph is symmetric with respect to the $y$-axis ($f$ is an even function).
- **Roots / $x$-intercepts:**
  $$x^4 - 4x^2 = 0 \iff x^2(x^2 - 4) = 0 \iff x^2(x - 2)(x + 2) = 0.$$
  The roots are $x = -2$, $x = 0$ (double root, tangent to the $x$-axis), and $x = 2$.

### Step 2: First derivative and local extrema
Differentiating $f(x)$:
$$f'(x) = 4x^3 - 8x = 4x(x^2 - 2) = 4x(x - \sqrt{2})(x + \sqrt{2}).$$
Setting $f'(x) = 0$ gives three stationary points:
$$x_1 = -\sqrt{2}, \qquad x_2 = 0, \qquad x_3 = \sqrt{2}.$$

Let us analyze the sign of $f'(x)$:
- For $x \in (-\infty, -\sqrt{2})$: $f'(x) < 0 \implies f$ is strictly decreasing.
- For $x \in (-\sqrt{2}, 0)$: $f'(x) > 0 \implies f$ is strictly increasing.
- For $x \in (0, \sqrt{2})$: $f'(x) < 0 \implies f$ is strictly decreasing.
- For $x \in (\sqrt{2}, \infty)$: $f'(x) > 0 \implies f$ is strictly increasing.

Evaluating function values:
- At $x = -\sqrt{2}$:
  $$f(-\sqrt{2}) = (-\sqrt{2})^4 - 4(-\sqrt{2})^2 = 4 - 4(2) = -4 \quad (\text{local and global minimum}).$$
- At $x = 0$:
  $$f(0) = 0 \quad (\text{local maximum}).$$
- At $x = \sqrt{2}$:
  $$f(\sqrt{2}) = (\sqrt{2})^4 - 4(\sqrt{2})^2 = 4 - 8 = -4 \quad (\text{local and global minimum}).$$

### Step 3: Second derivative, convexity, and concavity
Differentiating $f'(x) = 4x^3 - 8x$:
$$f''(x) = 12x^2 - 8 = 4(3x^2 - 2).$$
Set $f''(x) = 0$ to find candidate points for curvature changes:
$$3x^2 - 2 = 0 \iff x^2 = \frac{2}{3} \iff x = \pm \sqrt{\frac{2}{3}} = \pm \frac{\sqrt{6}}{3} \approx \pm 0.816.$$

Determining intervals of convexity:
- **On $\left(-\infty, -\sqrt{\frac{2}{3}}\right)$:**
  $3x^2 - 2 > 0 \implies f''(x) > 0 \implies f$ is **strictly convex** (concave up).
- **On $\left(-\sqrt{\frac{2}{3}}, \sqrt{\frac{2}{3}}\right)$:**
  $3x^2 - 2 < 0 \implies f''(x) < 0 \implies f$ is **strictly concave** (concave down).
- **On $\left(\sqrt{\frac{2}{3}}, \infty\right)$:**
  $3x^2 - 2 > 0 \implies f''(x) > 0 \implies f$ is **strictly convex** (concave up).

### Step 4: Inflection points
Because $f''(x)$ strictly changes sign at $x = -\sqrt{2/3}$ and $x = \sqrt{2/3}$, both correspond to genuine inflection points.
Compute the $y$-coordinates:
$$f\left(\pm \sqrt{\frac{2}{3}}\right) = \left(\frac{2}{3}\right)^2 - 4\left(\frac{2}{3}\right) = \frac{4}{9} - \frac{8}{3} = \frac{4 - 24}{9} = -\frac{20}{9} \approx -2.222.$$
Thus, the inflection points are:
$$I_1 = \left(-\frac{\sqrt{6}}{3}, -\frac{20}{9}\right), \qquad I_2 = \left(\frac{\sqrt{6}}{3}, -\frac{20}{9}\right).$$

### Step 5: Qualitative sketch and summary of features
The curve has the classic symmetric "W" shape:
```text
           y
           |
           |             *             *
           |              *           *
       ----+-----*---------*---------*-----+-----> x
          -2     |        (0,0)             2
                 |
      I1 (-0.82, -2.22)       I2 (0.82, -2.22)
                 |
                 * (-√2, -4)   * (√2, -4)
                 |
```
- **Roots:** $(-2, 0)$, $(0, 0)$, $(2, 0)$.
- **Local minima (global):** $(-\sqrt{2}, -4)$ and $(\sqrt{2}, -4)$.
- **Local maximum:** $(0, 0)$.
- **Inflection points:** $\left(-\frac{\sqrt{6}}{3}, -\frac{20}{9}\right)$ and $\left(\frac{\sqrt{6}}{3}, -\frac{20}{9}\right)$.

---

## 5. Why Each Step Is Valid
- **Step 1:** Polynomials are defined everywhere; finding zeros allows factoring out $x^2$.
- **Step 2:** The derivative is a cubic polynomial with three distinct real roots; alternating signs confirm two troughs and one crest.
- **Step 3:** The second derivative is a quadratic parabola with a positive leading coefficient, making it negative strictly between its roots and positive outside them.
- **Step 4:** A change in the sign of $f''$ is the defining criterion for a transition between convex and concave curvature.

---

## 6. Final Answer in Words
The function $f(x) = x^4 - 4x^2$ has two symmetric global minima at $x = -\sqrt{2}$ and $x = \sqrt{2}$, both with minimum value $-4$, and one local maximum at $x = 0$ with value $0$.
The graph is strictly convex on $\left(-\infty, -\frac{\sqrt{6}}{3}\right]$ and on $\left[\frac{\sqrt{6}}{3}, \infty\right)$, and strictly concave on $\left[-\frac{\sqrt{6}}{3}, \frac{\sqrt{6}}{3}\right]$.
The inflection points occur where the curvature switches sign, at $\left(-\frac{\sqrt{6}}{3}, -\frac{20}{9}\right)$ and $\left(\frac{\sqrt{6}}{3}, -\frac{20}{9}\right)$.

---

## 7. Quick Verification
Using the Second Derivative Test directly at the critical points:
- At $x = \pm\sqrt{2}$: $f''(\pm\sqrt{2}) = 12(2) - 8 = 16 > 0 \implies$ confirms local minima.
- At $x = 0$: $f''(0) = -8 < 0 \implies$ confirms local maximum.
The symmetry $f(-x) = f(x)$ is fully preserved in the locations of the extrema and inflection points.

---

## 8. Common Mistakes to Avoid
- **Confusing local extrema with inflection points:** Extrema occur where $f'(x) = 0$, whereas inflection points occur where $f''(x) = 0$ and changes sign.
- **Neglecting to verify the sign change for inflection points:** Simply having $f''(x_0) = 0$ does not guarantee an inflection point (e.g., $y = x^4$ at $x = 0$ has $y'' = 0$ but no inflection point). Here, the sign genuinely changes.
- **Arithmetic errors in evaluating $f(\pm\sqrt{2/3})$:** Carefully calculate $(2/3)^2 - 4(2/3) = 4/9 - 24/9 = -20/9$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The function $f(x) = x^4 - 4x^2$ is an even function whose first derivative yields two symmetric minima at $x = \pm\sqrt{2}$ with value $-4$ and a local maximum at the origin $(0,0)$. Analyzing the second derivative $f''(x) = 12x^2 - 8$ reveals that the graph is concave down between $-\sqrt{6}/3$ and $\sqrt{6}/3$, and concave up elsewhere. Consequently, the curve transitions between concavity and convexity at two inflection points, located symmetrically at $(\pm\sqrt{6}/3, -20/9)$.
