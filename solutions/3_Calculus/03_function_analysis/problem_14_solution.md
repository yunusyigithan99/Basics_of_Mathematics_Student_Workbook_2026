# Problem 14: Reconstructing Function Behavior from its Derivative

## 1. Original Problem
It is known that
$$f'(x) = (x - 1)(x + 2).$$
Determine the monotonicity and the locations of the extrema, and sketch a possible qualitative shape of the function. Then, for
$$g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x$$
verify that $g'(x) = (x - 1)(x + 2)$, and compare the specific graph with the earlier qualitative sketch.

---

## 2. What We Are Trying to Find
1. The sign chart of $f'(x)$ and intervals of monotonicity of $f(x)$.
2. The locations and classification of all local extrema of $f(x)$.
3. A qualitative sketch of the family of functions $f(x)$ whose derivative is $f'(x)$.
4. The verification by differentiation that $g'(x) = (x - 1)(x + 2)$.
5. The specific key points (extrema values, intercepts, inflection point) of $g(x)$ and comparison with the general qualitative shape.

---

## 3. Key Concepts and Theorems
1. **Reading Monotonicity from the Derivative:**
   - $f'(x) > 0$ on an interval implies $f$ is strictly increasing.
   - $f'(x) < 0$ on an interval implies $f$ is strictly decreasing.
2. **First Derivative Test for Local Extrema:**
   - If $f'(x)$ transitions from positive to negative at $x_0$, $f$ has a local maximum at $x_0$.
   - If $f'(x)$ transitions from negative to positive at $x_0$, $f$ has a local minimum at $x_0$.
3. **Antiderivative Family:**
   If $f'(x) = g'(x)$, then $f(x) = g(x) + C$ for some real constant $C$. The constant $C$ represents an arbitrary vertical shift, meaning all antiderivatives share the exact same shape, slopes, and $x$-coordinates of extrema.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze the derivative $f'(x)$
We are given:
$$f'(x) = (x - 1)(x + 2) = x^2 + x - 2.$$
Setting $f'(x) = 0$ yields two stationary points:
$$x_1 = -2, \qquad x_2 = 1.$$

Because $f'(x)$ is a quadratic parabola with a positive leading coefficient ($a = 1 > 0$), it is negative strictly between its roots and positive outside:
- **On $(-\infty, -2)$:** $f'(x) > 0 \implies f$ is **strictly increasing**.
- **On $(-2, 1)$:** $f'(x) < 0 \implies f$ is **strictly decreasing**.
- **On $(1, \infty)$:** $f'(x) > 0 \implies f$ is **strictly increasing**.

### Step 2: Classify the local extrema
- At $x = -2$: $f'$ changes sign from positive to negative. Therefore, $f$ has a **local maximum** at $x = -2$.
- At $x = 1$: $f'$ changes sign from negative to positive. Therefore, $f$ has a **local minimum** at $x = 1$.

### Step 3: Qualitative shape of $f(x)$
Without knowing an integration constant $C$, any function in the family $f(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x + C$ has the qualitative behavior of a standard cubic curve:
- Starts at $-\infty$ as $x \to -\infty$.
- Climbs monotonically to a peak (local maximum) at $x = -2$.
- Turns downward and descends through an inflection point at $x = -1/2$.
- Reaches a valley (local minimum) at $x = 1$.
- Turns upward and climbs monotonically toward $+\infty$ as $x \to \infty$.

```text
       Qualitative Shape of f(x)
                 y
                 |       Local Max (x = -2)
                 |           *
                 |         /   \
                 |        /     \   Inflection (x = -0.5)
                 |       /        \
       ----------+------+----------*--------+----------> x
                -2      |           \      / 1
                        |            `---*
                        |             Local Min (x = 1)
```

### Step 4: Differentiate $g(x)$ and verify the formula
We are given the specific function:
$$g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x.$$
Differentiating term by term:
$$g'(x) = \frac{d}{dx}\left(\frac{x^3}{3}\right) + \frac{d}{dx}\left(\frac{x^2}{2}\right) - \frac{d}{dx}(2x) = \frac{3x^2}{3} + \frac{2x}{2} - 2 = x^2 + x - 2.$$
Factoring the quadratic polynomial:
$$x^2 + x - 2 = (x - 1)(x + 2).$$
This matches $f'(x) = (x - 1)(x + 2)$ identically.

### Step 5: Compute specific values for $g(x)$ and compare with qualitative sketch
For $g(x)$, the constant of integration is $C = 0$, which anchors the curve in the coordinate plane:
1. **$y$-intercept:**
   $$g(0) = 0 \implies \text{passes through the origin } (0, 0).$$
2. **Local maximum at $x = -2$:**
   $$g(-2) = \frac{(-2)^3}{3} + \frac{(-2)^2}{2} - 2(-2) = -\frac{8}{3} + 2 + 4 = 6 - \frac{8}{3} = \frac{10}{3} \approx 3.33.$$
   The local maximum is at $\left(-2, \frac{10}{3}\right)$.
3. **Local minimum at $x = 1$:**
   $$g(1) = \frac{1^3}{3} + \frac{1^2}{2} - 2(1) = \frac{1}{3} + \frac{1}{2} - 2 = \frac{5}{6} - 2 = -\frac{7}{6} \approx -1.17.$$
   The local minimum is at $\left(1, -\frac{7}{6}\right)$.
4. **Inflection point:**
   $$g''(x) = 2x + 1 = 0 \iff x = -\frac{1}{2}.$$
   $$g\left(-\frac{1}{2}\right) = \frac{-1/8}{3} + \frac{1/4}{2} - 2\left(-\frac{1}{2}\right) = -\frac{1}{24} + \frac{1}{8} + 1 = \frac{26}{24} = \frac{13}{12} \approx 1.08.$$
   The inflection point is at $\left(-\frac{1}{2}, \frac{13}{12}\right)$.

**Comparison:**
The specific curve $g(x)$ perfectly confirms the qualitative sketch: the peak is above the $x$-axis at $y = 10/3$, the trough is below the $x$-axis at $y = -7/6$, and the curve passes through the origin midway between them. The qualitative sketch captured all structural turning points correctly.

---

## 5. Why Each Step Is Valid
- **Step 1:** The sign of a factored quadratic expression is determined by the signs of its linear factors or standard parabolic curvature.
- **Step 2:** The First Derivative Test applies because $f'$ is continuous and changes sign across its zeros.
- **Step 3:** The derivative determines a function up to an additive constant $C$, which preserves all horizontal coordinates of turning points.
- **Step 4:** Applying the standard power rule $\frac{d}{dx}(x^n) = n x^{n-1}$ confirms equality.
- **Step 5:** Substituting $x = -2$ and $x = 1$ yields the exact heights of the peaks and valleys, anchoring the qualitative curve.

---

## 6. Final Answer in Words
The derivative $f'(x) = (x - 1)(x + 2)$ reveals that the function is **strictly increasing** on $(-\infty, -2]$ and on $[1, \infty)$, and **strictly decreasing** on $[-2, 1]$. 
It has a **local maximum** at $x = -2$ and a **local minimum** at $x = 1$. 
Differentiating $g(x) = \frac{x^3}{3} + \frac{x^2}{2} - 2x$ yields $g'(x) = x^2 + x - 2 = (x - 1)(x + 2)$, confirming that $g$ belongs to this exact family of functions with $C = 0$. 
The specific graph of $g(x)$ matches the qualitative sketch identically, featuring a local maximum at $\left(-2, \frac{10}{3}\right)$, passing through the origin $(0, 0)$, having an inflection point at $\left(-\frac{1}{2}, \frac{13}{12}\right)$, and reaching a local minimum at $\left(1, -\frac{7}{6}\right)$.

---

## 7. Quick Verification
- Second Derivative Test on $g(x)$:
  $g''(x) = 2x + 1$.
  $g''(-2) = 2(-2) + 1 = -3 < 0 \implies$ local maximum at $x = -2$.
  $g''(1) = 2(1) + 1 = 3 > 0 \implies$ local minimum at $x = 1$.
This confirms both extrema classifications independently.

---

## 8. Common Mistakes to Avoid
- **Confusing the zeros of $f'$ with zeros of $f$:** The points $x = -2$ and $x = 1$ are where the slope is zero, NOT where the function crosses the $x$-axis.
- **Assuming $f$ has a fixed vertical position:** A derivative formula alone does not fix the function value; any vertical shift $f(x) + C$ has the exact same derivative.
- **Sign error when factoring:** Mistaking $x^2 + x - 2$ for $(x + 1)(x - 2)$. Note that the sum of the roots is $-1$, so $(x - 1)(x + 2)$ is correct.

---

## 9. Classroom Presentation (3-Sentence Summary)
From the derivative $f'(x) = (x - 1)(x + 2)$, we immediately see that $f$ is an increasing cubic curve with a local maximum at $x = -2$ and a local minimum at $x = 1$. Differentiating $g(x) = x^3/3 + x^2/2 - 2x$ gives $x^2 + x - 2$, verifying that $g(x)$ is the specific member of this function family passing through the origin. Evaluating $g(x)$ at the critical points gives a maximum peak of $10/3$ at $x = -2$ and a minimum valley of $-7/6$ at $x = 1$, which perfectly matches our qualitative sketch.
