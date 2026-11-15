# Problem 14: Integration of a Piecewise-Defined Function and Geometric Verification

## 1. Original Problem
Let
$$f(x) = \begin{cases} x + 1, & -1 \le x < 1, \\ 2, & 1 \le x \le 3. \end{cases}$$
Sketch the graph, decide where to split the integral, compute
$$\int_{-1}^{3}f(x)\,dx$$
and verify the result geometrically.

---

## 2. What We Are Trying to Find
1. A visual and structural analysis of the piecewise function, checking continuity at the partition boundary.
2. The determination of the exact point where the integral must be split.
3. The analytical evaluation of the definite integral across both sub-intervals using the Fundamental Theorem of Calculus.
4. The geometric calculation of the areas (triangle and rectangle) under each section of the curve.
5. The comparison and verification of the analytical integral with the geometric area.

---

## 3. Key Concepts and Theorems
1. **Interval Additivity Property of Integrals:**
   For any partition point $c \in [a, b]$:
   $$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx.$$
2. **Piecewise Continuity:**
   If a function is continuous or piecewise continuous on $[a, b]$, its Riemann integral exists and equals the sum of integrals over each individual piece.
3. **Geometric Area Formulas:**
   - Right triangle: $\text{Area} = \frac{1}{2} \cdot \text{base} \cdot \text{height}$.
   - Rectangle: $\text{Area} = \text{width} \cdot \text{height}$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze the piecewise function and check continuity
The function is defined piecewise on $[-1, 3]$:
- For $-1 \le x < 1$: $f(x) = x + 1$ (a straight line with slope $1$).
  - At $x = -1$: $f(-1) = -1 + 1 = 0$.
  - As $x \to 1^-$: $\lim_{x \to 1^-} (x + 1) = 1 + 1 = 2$.
- For $1 \le x \le 3$: $f(x) = 2$ (a horizontal line at height $2$).
  - At $x = 1$: $f(1) = 2$.
  - At $x = 3$: $f(3) = 2$.

Notice that the left limit at $x = 1$ equals the function value $f(1) = 2$. Thus, $f(x)$ is continuous at $x = 1$ (the pieces meet seamlessly).

### Step 2: Sketch the graph
The curve begins on the $x$-axis at $(-1, 0)$, rises linearly to $(1, 2)$, and then continues as a horizontal line segment from $(1, 2)$ to $(3, 2)$:

```text
                  y
                2 |                *---------------+* (3, 2)
                  |               /|               |
                  |              / |               |
                1 |             /  |               |
                  |            /   |   Rectangle   |
                  |  Triangle /    |    Area A2    |
        ----------+----------*-----+---------------+----> x
                 -1          0     1               3
                             <--2--> <------2------>
```

### Step 3: Decide where to split the integral
Because the analytical rule defining $f(x)$ changes from $x + 1$ to $2$ at $x = 1$, we must split the integral at $x = 1$:
$$\int_{-1}^{3} f(x)\,dx = \int_{-1}^{1} (x + 1)\,dx + \int_{1}^{3} 2\,dx.$$

### Step 4: Compute the definite integrals analytically
We evaluate each integral using the Newton-Leibniz formula:

1. **First piece (on $[-1, 1]$):**
   An antiderivative of $x + 1$ is $\frac{x^2}{2} + x$:
   $$\int_{-1}^{1} (x + 1)\,dx = \left[\frac{x^2}{2} + x\right]_{-1}^{1}$$
   $$= \left(\frac{1^2}{2} + 1\right) - \left(\frac{(-1)^2}{2} + (-1)\right)$$
   $$= \left(\frac{1}{2} + 1\right) - \left(\frac{1}{2} - 1\right)$$
   $$= \frac{3}{2} - \left(-\frac{1}{2}\right) = \frac{3}{2} + \frac{1}{2} = 2.$$

2. **Second piece (on $[1, 3]$):**
   An antiderivative of $2$ is $2x$:
   $$\int_{1}^{3} 2\,dx = [2x]_{1}^{3} = 2(3) - 2(1) = 6 - 2 = 4.$$

3. **Total integral:**
   $$\int_{-1}^{3} f(x)\,dx = 2 + 4 = 6.$$

### Step 5: Verify the result geometrically
Because $f(x) \ge 0$ everywhere on $[-1, 3]$, the definite integral represents the exact geometric area under the curve:

1. **Area of the first region ($A_1$ on $[-1, 1]$):**
   The region under the line segment from $x = -1$ to $x = 1$ is a right triangle:
   - Base = $1 - (-1) = 2$,
   - Height = $f(1) - 0 = 2$.
   $$\text{Area}(A_1) = \frac{1}{2} \cdot \text{base} \cdot \text{height} = \frac{1}{2} \cdot 2 \cdot 2 = 2.$$
   This matches the first integral: $\int_{-1}^1 (x + 1)\,dx = 2$.

2. **Area of the second region ($A_2$ on $[1, 3]$):**
   The region under the constant function $f(x) = 2$ from $x = 1$ to $x = 3$ is a rectangle:
   - Width = $3 - 1 = 2$,
   - Height = $2$.
   $$\text{Area}(A_2) = \text{width} \times \text{height} = 2 \times 2 = 4.$$
   This matches the second integral: $\int_1^3 2\,dx = 4$.

3. **Total area:**
   $$\text{Total Geometric Area} = A_1 + A_2 = 2 + 4 = 6.$$

The analytical integral and the geometric area agree completely.

---

## 5. Why Each Step Is Valid
- **Step 1:** Checking limits from the left and right verifies continuity and establishes the boundary coordinates of the shapes.
- **Step 2:** Graphing reveals the exact boundary curves and verifies non-negativity across the interval.
- **Step 3:** The interval additivity property allows splitting an integral at any interior point where the functional formula transitions.
- **Step 4:** The Fundamental Theorem of Calculus applies to each smooth piece separately.
- **Step 5:** Elementary geometry provides an independent, exact cross-check for non-negative piecewise linear functions.

---

## 6. Final Answer in Words
The integral is split at $x = 1$ where the definition changes, giving:
$$\int_{-1}^3 f(x)\,dx = \int_{-1}^1 (x + 1)\,dx + \int_1^3 2\,dx = 2 + 4 = 6.$$
Geometrically, the region under the curve on $[-1, 1]$ forms a right triangle with base $2$ and height $2$ (area $= \frac{1}{2} \cdot 2 \cdot 2 = 2$), while the region on $[1, 3]$ forms a rectangle with width $2$ and height $2$ (area $= 2 \cdot 2 = 4$). The total geometric area is $2 + 4 = 6$, confirming the analytical calculation.

---

## 7. Quick Verification
- Trapezoid formula alternative for the first piece:
  Left height $= 0$, right height $= 2$, width $= 2$.
  $\text{Area} = \frac{0 + 2}{2} \cdot 2 = 2$.
- Rectangle formula:
  Height $= 2$, width $= 2 \implies 4$.
- Total $= 2 + 4 = 6$.
Matches.

---

## 8. Common Mistakes to Avoid
- **Integrating the wrong formula across the whole interval:**
  Computing $\int_{-1}^3 (x + 1)\,dx = [\frac{x^2}{2} + x]_{-1}^3 = (\frac{9}{2} + 3) - (\frac{1}{2} - 1) = 7.5 - (-0.5) = 8$, which completely ignores the fact that the function caps at $2$ past $x = 1$.
- **Arithmetic errors with $(-1)^2$:**
  Writing $\frac{(-1)^2}{2} + (-1) = \frac{-1}{2} - 1 = -\frac{3}{2}$. The square of $-1$ is $+1$, so $\frac{1}{2} - 1 = -\frac{1}{2}$.
- **Assuming the function is discontinuous at $x = 1$ without checking:**
  Both pieces equal $2$ at $x = 1$, making the curve continuous.

---

## 9. Classroom Presentation (3-Sentence Summary)
Because the function definition changes at $x = 1$, we split the integral into $\int_{-1}^1 (x + 1)\,dx$ and $\int_1^3 2\,dx$, which evaluate to $2$ and $4$ respectively, totaling $6$. Geometrically, the first piece forms a right triangle with base $2$ and height $2$, yielding an area of $2$. The second piece forms a rectangle with width $2$ and height $2$, yielding an area of $4$, which together confirm the exact integral value of $6$.
