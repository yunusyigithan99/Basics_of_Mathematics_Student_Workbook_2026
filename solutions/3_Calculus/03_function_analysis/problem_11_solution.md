# Problem 11: Parameter Study and Bifurcation of Critical Points

## 1. Original Problem
For
$$f_a(x) = x^3 - 3ax$$
depending on the real parameter $a$, determine the number of critical points and their character. Separate the parameter cases and justify why the structure of the graph changes.

---

## 2. What We Are Trying to Find
1. The first derivative $f'_a(x)$ in terms of $x$ and the parameter $a$.
2. The number and locations of all real critical points where $f'_a(x) = 0$.
3. A systematic division into parameter cases ($a > 0$, $a = 0$, $a < 0$).
4. The exact character of each critical point (local maximum, local minimum, or stationary inflection point).
5. A geometric and algebraic explanation of why the qualitative structure of the graph changes across $a = 0$.

---

## 3. Key Concepts and Theorems
1. **Critical (Stationary) Points:**
   Points $x \in \mathbb{R}$ where $f'_a(x) = 0$.
2. **Second Derivative Test:**
   Let $x_0$ be a critical point of a twice-differentiable function:
   - If $f''(x_0) < 0$, then $x_0$ is a strict local maximum.
   - If $f''(x_0) > 0$, then $x_0$ is a strict local minimum.
   - If $f''(x_0) = 0$, the test is inconclusive and the sign change of $f'$ must be examined.
3. **Bifurcation of Critical Points:**
   A qualitative change in the number or stability of stationary points as a parameter crosses a critical threshold (here $a = 0$).

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the first and second derivatives
For any fixed real parameter $a \in \mathbb{R}$, $f_a(x) = x^3 - 3ax$ is a polynomial defined on all of $\mathbb{R}$.
Differentiating with respect to $x$:
$$f'_a(x) = 3x^2 - 3a = 3(x^2 - a).$$
Differentiating a second time:
$$f''_a(x) = 6x.$$

### Step 2: Set the derivative to zero
Critical points satisfy:
$$f'_a(x) = 0 \iff 3(x^2 - a) = 0 \iff x^2 = a.$$
The number of real solutions to $x^2 = a$ depends entirely on the sign of $a$. We therefore analyze three distinct cases: $a > 0$, $a = 0$, and $a < 0$.

### Step 3: Case 1: $a > 0$ (Two critical points)
When $a > 0$, the equation $x^2 = a$ has two distinct real roots:
$$x_1 = -\sqrt{a}, \qquad x_2 = \sqrt{a}.$$

- **At $x_1 = -\sqrt{a}$:**
  Evaluate the second derivative:
  $$f''_a(-\sqrt{a}) = 6(-\sqrt{a}) = -6\sqrt{a} < 0.$$
  By the Second Derivative Test, $x = -\sqrt{a}$ is a **strict local maximum**.
  The maximum value is:
  $$f_a(-\sqrt{a}) = (-\sqrt{a})^3 - 3a(-\sqrt{a}) = -a\sqrt{a} + 3a\sqrt{a} = 2a\sqrt{a}.$$
- **At $x_2 = \sqrt{a}$:**
  Evaluate the second derivative:
  $$f''_a(\sqrt{a}) = 6\sqrt{a} > 0.$$
  By the Second Derivative Test, $x = \sqrt{a}$ is a **strict local minimum**.
  The minimum value is:
  $$f_a(\sqrt{a}) = (\sqrt{a})^3 - 3a(\sqrt{a}) = a\sqrt{a} - 3a\sqrt{a} = -2a\sqrt{a}.$$
- **Monotonicity for $a > 0$:**
  $f'_a(x) = 3(x + \sqrt{a})(x - \sqrt{a})$:
  - Strictly increasing on $(-\infty, -\sqrt{a}]$ and on $[\sqrt{a}, \infty)$.
  - Strictly decreasing on $[-\sqrt{a}, \sqrt{a}]$.

### Step 4: Case 2: $a = 0$ (One critical point, no local extremum)
When $a = 0$, the function simplifies to:
$$f_0(x) = x^3.$$
The derivative is:
$$f'_0(x) = 3x^2.$$
Setting $f'_0(x) = 0$ yields a single solution:
$$x = 0.$$
- **Sign of $f'_0(x)$:**
  For all $x \neq 0$, $3x^2 > 0$. The derivative does not change sign across $x = 0$.
- **Character:**
  Since $f'_0(x) \ge 0$ everywhere, $f_0(x)$ is **strictly increasing** on all of $\mathbb{R}$.
  The point $(0, 0)$ is a **stationary inflection point** (a saddle/terrace point), not a local extremum.

### Step 5: Case 3: $a < 0$ (Zero critical points)
When $a < 0$, we can write $a = -|a|$. The equation becomes:
$$x^2 = a = -|a| < 0.$$
Because the square of any real number is non-negative ($x^2 \ge 0$), this equation has **no real solutions**.
- **Sign of $f'_a(x)$:**
  $$f'_a(x) = 3(x^2 - a) = 3(x^2 + |a|) \ge 3|a| > 0 \quad \text{for all } x \in \mathbb{R}.$$
- **Character:**
  The derivative is strictly positive everywhere. The function has **no critical points** and **no local extrema**; it is strictly increasing across the entire real line $\mathbb{R}$.

### Step 6: Justification of the structural change (Bifurcation at $a = 0$)
The structure of the graph undergoes a qualitative transition (bifurcation) as $a$ passes through $0$:
- Geometrically, the graph of $f'_a(x) = 3x^2 - 3a$ is an upward-opening parabola with vertex at $(0, -3a)$.
- When $a > 0$, the vertex lies below the $x$-axis, so the parabola crosses the $x$-axis at two symmetric points $\pm\sqrt{a}$, generating a peak and a trough.
- As $a \to 0^+$, these two extrema move toward each other and merge at $x = 0$, where the local peak and trough annihilate each other into an inflection point with a horizontal tangent.
- When $a < 0$, the vertex shifts above the $x$-axis (at $+3|a| > 0$), so the parabola never touches the $x$-axis. The slope is strictly positive everywhere, completely eliminating all extrema.

---

## 5. Why Each Step Is Valid
- **Step 1:** Linear combination of powers differentiated via the power rule $\frac{d}{dx}(x^n) = n x^{n-1}$.
- **Step 2:** A critical point of a smooth polynomial occurs if and only if its derivative vanishes.
- **Step 3:** The quadratic equation $x^2 = a$ has two distinct real solutions $\pm\sqrt{a}$ if and only if $a > 0$; the non-zero second derivative guarantees local extrema.
- **Step 4:** A zero derivative without a sign change corresponds to a terrace/inflection point.
- **Step 5:** $x^2 \ge 0$ for all real $x$, so $x^2 - a > 0$ whenever $a < 0$, precluding any real zeros.
- **Step 6:** The vertical translation of the derivative parabola $y = 3x^2 - 3a$ governs the number of real roots.

---

## 6. Final Answer in Words
Depending on the parameter $a$:
1. If **$a > 0$**, there are **two critical points**:
   - $x = -\sqrt{a}$ is a **local maximum** with value $f_a(-\sqrt{a}) = 2a\sqrt{a}$.
   - $x = \sqrt{a}$ is a **local minimum** with value $f_a(\sqrt{a}) = -2a\sqrt{a}$.
2. If **$a = 0$**, there is **one critical point** at $x = 0$, which is a **stationary inflection point** (not a local extremum); the function is strictly increasing on $\mathbb{R}$.
3. If **$a < 0$**, there are **no critical points** and no extrema; the function is strictly increasing on $\mathbb{R}$.
The graph's structure changes because the derivative parabola $3x^2 - 3a$ shifts vertically: it intersects the $x$-axis twice for $a > 0$, touches it once at $a = 0$, and floats strictly above it for $a < 0$.

---

## 7. Quick Verification
- For $a = 1$: $f_1(x) = x^3 - 3x$, $f'_1(x) = 3(x^2 - 1) = 0 \implies x = \pm 1$. Local max at $x = -1$ ($y = 2$), local min at $x = 1$ ($y = -2$). Matches $2(1)\sqrt{1} = 2$.
- For $a = -1$: $f_{-1}(x) = x^3 + 3x$, $f'_{-1}(x) = 3x^2 + 3 \ge 3 > 0$, strictly increasing, no roots for $f'$. Correct.

---

## 8. Common Mistakes to Avoid
- **Claiming $x = 0$ is an extremum when $a = 0$:** Setting $3x^2 = 0$ gives $x = 0$, but because $3x^2 \ge 0$ everywhere, there is no sign change, so it is not an extremum.
- **Taking square roots of negative numbers:** Writing $x = \pm\sqrt{a}$ when $a < 0$ without realizing these are complex, not real critical points.
- **Confusing the sign of the parameter with the sign of the critical points:** $x_1 = -\sqrt{a}$ and $x_2 = +\sqrt{a}$ exist only when $a > 0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Setting the derivative $f'_a(x) = 3(x^2 - a) = 0$ leads directly to the equation $x^2 = a$, whose number of real solutions is governed by the sign of $a$. When $a > 0$, there are two critical points forming a local maximum at $-\sqrt{a}$ and a local minimum at $\sqrt{a}$; when $a = 0$, these two points merge into a single stationary inflection point at the origin; and when $a < 0$, no real critical points exist. The qualitative structure changes at $a = 0$ because the derivative parabola shifts vertically, transitioning from crossing the $x$-axis to floating strictly above it.
