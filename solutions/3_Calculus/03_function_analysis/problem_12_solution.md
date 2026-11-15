# Problem 12: Function with an Absolute Value and Non-Differentiable Points

## 1. Original Problem
Analyze
$$f(x) = |x^2 - 4|.$$
First sketch $x^2 - 4$, then explain the effect of the absolute value. Indicate the points where the derivative does not exist and justify the reason geometrically.

---

## 2. What We Are Trying to Find
1. The behavior and graph of the base parabola $g(x) = x^2 - 4$.
2. The geometric transformation applied by the absolute value operation $|g(x)|$.
3. The piecewise definition of $f(x)$ on different real intervals.
4. The exact points where the derivative does not exist, supported by one-sided derivative calculations.
5. The geometric explanation of why differentiability fails at those points (sharp corners/creases).
6. The classification of all local and global extrema.

---

## 3. Key Concepts and Theorems
1. **Definition of Absolute Value:**
   $$|u| = \begin{cases} u & \text{if } u \ge 0, \\ -u & \text{if } u < 0. \end{cases}$$
2. **Geometric Reflection:**
   Applying the absolute value to a function $y = |g(x)|$ keeps all points with $g(x) \ge 0$ unchanged, and reflects the parts where $g(x) < 0$ across the $x$-axis into positive $y$-values.
3. **Differentiability and One-Sided Derivatives:**
   A function $f$ is differentiable at $x_0$ if and only if both one-sided derivatives exist and are equal:
   $$f'_-(x_0) = \lim_{x \to x_0^-} \frac{f(x) - f(x_0)}{x - x_0} = \lim_{x \to x_0^+} \frac{f(x) - f(x_0)}{x - x_0} = f'_+(x_0).$$
   If $f'_-(x_0) \neq f'_+(x_0)$, the function has a sharp corner (cusp) and is non-differentiable at $x_0$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze the base parabola $g(x) = x^2 - 4$
The base function is the quadratic polynomial:
$$g(x) = x^2 - 4.$$
- **Zeros:** $x^2 - 4 = 0 \iff (x - 2)(x + 2) = 0 \implies x = -2$ and $x = 2$.
- **Vertex:** At $x = 0$, $g(0) = -4$.
- **Sign:**
  - $g(x) \ge 0$ on $(-\infty, -2] \cup [2, \infty)$.
  - $g(x) < 0$ on $(-2, 2)$.

The graph of $g(x)$ is a standard symmetric parabola opening upward, dipping below the $x$-axis between $-2$ and $2$.

### Step 2: Effect of the absolute value
The absolute value $f(x) = |g(x)| = |x^2 - 4|$ forces the function output to be non-negative:
$$f(x) = \begin{cases}
x^2 - 4 & \text{for } x \le -2 \text{ or } x \ge 2, \\
-(x^2 - 4) = 4 - x^2 & \text{for } -2 < x < 2.
\end{cases}$$

**Geometric effect:**
- For $x \le -2$ and $x \ge 2$, the graph is identical to the parabola $y = x^2 - 4$.
- For $-2 < x < 2$, the negative dip is reflected vertically across the $x$-axis. The vertex $(0, -4)$ flips up to $(0, 4)$, forming an inverted dome between $-2$ and $2$.

```text
       Base: g(x) = x^2 - 4                   Transformed: f(x) = |x^2 - 4|
              y                                      y
              |                                      |       (0,4)
         \    |    /                                 \      .---.      /
          \   |   /                                   \    /     \    /
       ----+--+--+----> x                         -----+--*-------*--+----> x
          -2  |  2                                    -2 /|       |\ 2
              |                                         Cusp     Cusp
              * (0,-4)
```

### Step 3: Compute one-sided derivatives at the boundary points
We examine differentiability at the transition roots $x = 2$ and $x = -2$.

#### At $x = 2$:
- **Left-hand derivative (approaching from $x < 2$ where $f(x) = 4 - x^2$):**
  $$f'_-(2) = \lim_{x \to 2^-} \frac{(4 - x^2) - 0}{x - 2} = \lim_{x \to 2^-} \frac{-(x - 2)(x + 2)}{x - 2} = \lim_{x \to 2^-} [-(x + 2)] = -(2 + 2) = -4.$$
- **Right-hand derivative (approaching from $x > 2$ where $f(x) = x^2 - 4$):**
  $$f'_+(2) = \lim_{x \to 2^+} \frac{(x^2 - 4) - 0}{x - 2} = \lim_{x \to 2^+} \frac{(x - 2)(x + 2)}{x - 2} = \lim_{x \to 2^+} (x + 2) = 2 + 2 = +4.$$
Since $f'_-(2) = -4 \neq +4 = f'_+(2)$, the two-sided limit does not exist:
$$f'(2) \quad \text{does not exist}.$$

#### At $x = -2$:
- **Left-hand derivative (approaching from $x < -2$ where $f(x) = x^2 - 4$):**
  $$f'_-(-2) = \lim_{x \to -2^-} \frac{(x^2 - 4) - 0}{x - (-2)} = \lim_{x \to -2^-} (x - 2) = -2 - 2 = -4.$$
- **Right-hand derivative (approaching from $x > -2$ where $f(x) = 4 - x^2$):**
  $$f'_+(-2) = \lim_{x \to -2^+} \frac{(4 - x^2) - 0}{x - (-2)} = \lim_{x \to -2^+} [-(x - 2)] = -(-2 - 2) = +4.$$
Since $f'_-(-2) = -4 \neq +4 = f'_+(-2)$, the two-sided limit does not exist:
$$f'(-2) \quad \text{does not exist}.$$

### Step 4: Geometric justification for non-differentiability
Differentiability geometrically means that as we zoom into a point on a curve, the curve looks increasingly like a unique straight line (the tangent line). 
At the points $x = -2$ and $x = 2$, the reflection produces an abrupt direction change:
- Approaching $x = 2$ from the left, the curve descends with slope $-4$.
- Immediately exiting $x = 2$ to the right, the curve ascends with slope $+4$.
The graph forms a sharp corner (a "V"-shaped cusp/crease) with an instantaneous jump of $\Delta m = 8$ in slope. Because there is no single, unique tangent line at a sharp corner, the derivative cannot exist.

### Step 5: Identification of all extrema
- **Global Minima:**
  Since $f(x) = |x^2 - 4| \ge 0$ for all $x$, and $f(\pm 2) = 0$, the points:
  $$x = -2 \quad \text{and} \quad x = 2$$
  are **strict global minima** (which are non-differentiable critical points).
- **Local Maximum:**
  Inside $(-2, 2)$, $f(x) = 4 - x^2$ is smooth with $f'(x) = -2x = 0 \implies x = 0$.
  Since $f''(0) = -2 < 0$, the point:
  $$x = 0$$
  is a smooth **local maximum** with value $f(0) = 4$.

---

## 5. Why Each Step Is Valid
- **Step 1:** $x^2 - 4$ is a standard parabola whose sign is determined by its real roots.
- **Step 2:** The piecewise definition follows directly from the definition of the absolute value function.
- **Step 3:** The definition of the derivative requires the two-sided limit of the difference quotient; distinct left- and right-hand limits prove non-existence.
- **Step 4:** Non-differentiability corresponds visually to a failure of local linearity (a sharp vertex).
- **Step 5:** Fermat's theorem applies to smooth interior extrema, while the absolute value minimum occurs at boundary/corner points where $f(x)$ hits its lower bound of zero.

---

## 6. Final Answer in Words
The base graph $y = x^2 - 4$ is an upward-opening parabola with roots at $x = \pm 2$ and vertex at $(0, -4)$. Applying the absolute value reflects the negative section on $(-2, 2)$ upward, turning the vertex into a smooth local maximum at $(0, 4)$. 
The derivative does not exist at $x = -2$ and $x = 2$ because the one-sided slopes are unequal ($f'_- = -4$ and $f'_+ = +4$ at $x = 2$, and vice versa at $x = -2$). Geometrically, this reflection creates sharp corners where no unique tangent line exists. The function has global minima of $0$ at the sharp corners $x = \pm 2$ and a local maximum of $4$ at $x = 0$.

---

## 7. Quick Verification
- At $x = 3$: $f(3) = |9 - 4| = 5$, and $f'(3) = 2(3) = 6 > 0$ (increasing on $(2, \infty)$).
- At $x = 1$: $f(1) = |1 - 4| = 3$, and $f'(1) = -2(1) = -2 < 0$ (decreasing on $(0, 2)$).
This confirms that between $0$ and $2$, $f$ decreases from $4$ down to $0$, and for $x > 2$, $f$ increases from $0$ up toward infinity, meeting at a sharp minimum at $x = 2$.

---

## 8. Common Mistakes to Avoid
- **Blindly applying the chain rule:** Writing $f'(x) = \frac{x^2 - 4}{|x^2 - 4|} \cdot 2x$ and plugging in $x = 2$, which gives an undefined $0/0$ without explaining the one-sided limits.
- **Thinking non-differentiable points cannot be extrema:** $x = \pm 2$ are valid global minima despite being non-differentiable.
- **Forgetting that the vertex at $(0, 4)$ IS differentiable:** At $x = 0$, $f'(0) = 0$ exists and is completely smooth.

---

## 9. Classroom Presentation (3-Sentence Summary)
The graph of $f(x) = |x^2 - 4|$ is formed by reflecting the negative section of the parabola $y = x^2 - 4$ across the $x$-axis, creating a smooth local maximum at $(0, 4)$ and global minima at $x = \pm 2$. At $x = \pm 2$, the derivative does not exist because the left- and right-hand limits of the difference quotient produce unequal values of $-4$ and $+4$. Geometrically, this discrepancy creates sharp corners on the curve where a unique tangent line cannot be defined.
