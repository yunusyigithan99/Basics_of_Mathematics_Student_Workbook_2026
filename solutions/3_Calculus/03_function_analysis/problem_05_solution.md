# Problem 5 Solution: An Exponential Function with a Maximum

## 1. Original Problem
For the function:
$$f(x) = x e^{-x}$$
1. Find the natural domain $\operatorname{Dom}(f)$ and the axial intercepts.
2. Compute the derivative $f'(x)$, determine the critical points, and analyze the intervals of monotonicity and local extrema.
3. Examine the asymptotic behavior of the function as $x \to +\infty$ and as $x \to -\infty$.
4. Explain in detail how the limit $\lim_{x\to\infty} f(x)$ dictates the geometric shape of the graph on the right-hand side.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the domain as $\mathbb{R}$ and find the unique zero at $(0, 0)$.
2. Differentiate $f(x)$ using the Product Rule and Chain Rule: $f'(x) = (1 - x)e^{-x}$.
3. Solve $f'(x) = 0$ to locate the critical point $x = 1$, and classify it as a strict global maximum at $(1, e^{-1})$.
4. Compute the limits at both infinities, resolving the indeterminate form $[\infty \cdot 0]$ as $x \to +\infty$ to show $y = 0$ is a horizontal asymptote.
5. Explain how the curve rises to its peak at $(1, 1/e)$ and then flattens asymptotically against the positive $x$-axis without crossing it.

---

## 3. Key Concepts and Theorems
1. **Product Rule with Exponential Chain Rule:**
   $$\frac{d}{dx}[x e^{-x}] = (1)e^{-x} + x(-e^{-x}) = (1 - x)e^{-x}.$$
2. **Hierarchy of Growth (Exponential vs. Polynomial):**
   Exponential decay $e^{-x} = \frac{1}{e^x}$ overpowers any polynomial growth as $x \to +\infty$:
   $$\lim_{x\to+\infty} x e^{-x} = \lim_{x\to+\infty} \frac{x}{e^x} = 0.$$
3. **Horizontal Asymptote from Below or Above:**
   Since $x > 0$ and $e^{-x} > 0$ for all $x > 0$, $f(x) > 0$. The curve approaches $0$ strictly through positive values ($0^+$), hugging the positive $x$-axis from above.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Domain and Intercepts
1. **Domain:**
   Both $x$ and $e^{-x}$ are defined for all real numbers.
   $$\operatorname{Dom}(f) = \mathbb{R} = (-\infty, \infty).$$
2. **Intercepts:**
   Set $f(x) = 0 \implies x e^{-x} = 0$.
   Since the exponential function $e^{-x} > 0$ is strictly positive for all real $x$, the only solution is:
   $$x = 0.$$
   The graph passes through the origin $(0, 0)$, which is both the $x$-intercept and the $y$-intercept.

---

### Step 2: Compute the First Derivative
Let $u(x) = x$ and $v(x) = e^{-x}$.
- $u'(x) = 1$
- $v'(x) = e^{-x} \cdot (-1) = -e^{-x}$ (by the Chain Rule)

Apply the Product Rule:
$$f'(x) = u'(x) v(x) + u(x) v'(x) = (1)(e^{-x}) + (x)(-e^{-x}) = e^{-x} - x e^{-x}.$$
Factor out the common term $e^{-x}$:
$$f'(x) = (1 - x) e^{-x}.$$

---

### Step 3: Critical Points and Monotonicity
Set $f'(x) = 0$:
$$(1 - x) e^{-x} = 0.$$
Since $e^{-x} > 0$ for all $x \in \mathbb{R}$, we can divide by $e^{-x}$:
$$1 - x = 0 \implies x = 1.$$
There is a single critical point at $x = 1$.

**Sign Chart for $f'(x) = (1 - x)e^{-x}$:**
Since $e^{-x} > 0$ everywhere, the sign of $f'(x)$ is identical to the sign of $(1 - x)$:
1. **On $(-\infty, 1)$:**
   $x < 1 \implies 1 - x > 0 \implies f'(x) > 0$.
   The function is **strictly increasing** on $(-\infty, 1]$.
2. **On $(1, \infty)$:**
   $x > 1 \implies 1 - x < 0 \implies f'(x) < 0$.
   The function is **strictly decreasing** on $[1, \infty)$.

**Classification of the Local Extremum:**
At $x = 1$, the derivative changes sign from positive to negative ($+ \to -$).
Therefore, the function has a **strict local and global maximum** at $x = 1$.
Compute the maximum value:
$$f(1) = 1 \cdot e^{-1} = \frac{1}{e} \approx 0.367879.$$
Maximum point:
$$M = \left(1, \frac{1}{e}\right) \approx (1, 0.368).$$

---

### Step 4: Asymptotic Behavior at Infinity
1. **As $x \to +\infty$:**
   $$\lim_{x\to+\infty} f(x) = \lim_{x\to+\infty} x e^{-x} = \lim_{x\to+\infty} \frac{x}{e^x}.$$
   This has the indeterminate form $\left[\frac{\infty}{\infty}\right]$. Applying l'Hôpital's rule (or by the standard growth hierarchy of exponentials over polynomials):
   $$\lim_{x\to+\infty} \frac{x}{e^x} \stackrel{\text{H}}{=} \lim_{x\to+\infty} \frac{1}{e^x} = \left[\frac{1}{\infty}\right] = 0.$$
   Therefore, the line **$y = 0$** (the $x$-axis) is a **horizontal asymptote** as $x \to +\infty$.
   Furthermore, for all $x > 0$, both $x > 0$ and $e^{-x} > 0$, so $f(x) > 0$. The curve approaches $0$ from above ($0^+$).

2. **As $x \to -\infty$:**
   Let $x = -t$ where $t \to +\infty$:
   $$\lim_{x\to-\infty} x e^{-x} = \lim_{t\to+\infty} (-t) e^{-(-t)} = \lim_{t\to+\infty} (-t) e^t = [-\infty \cdot \infty] = -\infty.$$
   As $x$ moves left into negative numbers, the linear term $-t$ is negative and the exponential factor $e^t$ grows without bound, driving $f(x) \to -\infty$ extremely rapidly.

---

### Step 5: How the Limit Shapes the Graph on the Right
The combination of the maximum at $x = 1$ and the limit $\lim_{x\to\infty} f(x) = 0$ produces a distinctive geometric profile on the right-hand side ($x \ge 1$):
1. **The Turnaround and Descent:**
   At $x = 1$, the function reaches its absolute peak of $\frac{1}{e} \approx 0.368$ with a horizontal tangent line. For $x > 1$, the function begins to decrease ($f'(x) < 0$).
2. **Preventing Crossing or Plunging:**
   Normally, a decreasing function might continue downwards into negative numbers. However, the limit as $x \to \infty$ is $0$, and $f(x) > 0$ for all $x > 0$.
   Therefore, the curve cannot cross the $x$-axis. It is trapped above $y = 0$.
3. **Deceleration and Inflection:**
   To transition from descending downward at a negative slope to flattening out asymptotically along the horizontal line $y = 0$, the curve must change its curvature from concave down to concave up.
   Checking the second derivative confirms this:
   $$f''(x) = \frac{d}{dx}[(1 - x)e^{-x}] = (-1)e^{-x} + (1 - x)(-e^{-x}) = (x - 2)e^{-x}.$$
   Setting $f''(x) = 0$ gives $x = 2$, where $f(2) = 2/e^2 \approx 0.271$.
   - For $1 < x < 2$, the curve is concave down ($\cap$), curving downward away from the peak.
   - At $x = 2$, the curve passes through an **inflection point** $(2, 2e^{-2})$.
   - For $x > 2$, the curve becomes concave up ($\cup$), flattening out into an extended, smooth horizontal tail that hugs the $x$-axis indefinitely as $x \to \infty$.

---

## 5. Why Each Step Is Valid
1. **The Product Rule and Chain Rule** applied to $x e^{-x}$ give the exact rate of change everywhere on $\mathbb{R}$.
2. **$e^{-x} > 0$** allows division without changing inequalities or missing roots.
3. **l'Hôpital's Rule** applies to $\frac{x}{e^x}$ because both numerator and denominator tend to $\infty$.

---

## 6. Final Answer in Words
The function $f(x) = x e^{-x}$ has domain $\mathbb{R}$ and passes through the origin $(0, 0)$. Its derivative is $f'(x) = (1 - x)e^{-x}$, which shows that the function is strictly increasing on $(-\infty, 1]$ and strictly decreasing on $[1, \infty)$, reaching a strict global maximum at $(1, 1/e) \approx (1, 0.368)$. As $x \to -\infty$, $f(x) \to -\infty$, while as $x \to +\infty$, $f(x) \to 0^+$. This limit establishes a horizontal asymptote $y = 0$ on the right, which forces the curve to inflect at $(2, 2/e^2)$ from concave down to concave up so that it can flatten smoothly against the positive $x$-axis without ever touching or crossing it.

---

## 7. Quick Verification
- Second derivative test at $x = 1$:
  $$f''(1) = (1 - 2)e^{-1} = -e^{-1} = -\frac{1}{e} < 0.$$
  Confirms a strict local maximum at $x = 1$.
- Numerical values:
  - $f(0) = 0$
  - $f(0.5) = 0.5 e^{-0.5} \approx 0.303$
  - $f(1) = 1 e^{-1} \approx 0.368$ (Peak)
  - $f(2) = 2 e^{-2} \approx 0.271$ (Inflection)
  - $f(5) = 5 e^{-5} \approx 0.0337$
  - $f(10) = 10 e^{-10} \approx 0.00045 \to 0$
  Values confirm the rise to $0.368$ and the smooth tail decay toward $0$.

---

## 8. Common Mistakes to Avoid
- **Product rule minus sign omission:** Writing $\frac{d}{dx}[e^{-x}] = e^{-x}$ instead of $-e^{-x}$, which gives $(1 + x)e^{-x}$ and puts the maximum at $x = -1$.
- **Assuming $x e^{-x} \to \infty$ as $x \to \infty$:** Overlooking that exponential decay $e^{-x}$ is infinitely stronger than polynomial growth $x$.
- **Believing the curve crosses the $x$-axis for $x > 0$:** Forgetting that for all $x > 0$, $x e^{-x}$ is strictly positive.

---

## 9. Classroom Presentation (3-Sentence Summary)
Applying the Product Rule with the Chain Rule gives $f'(x) = (1 - x)e^{-x}$, which shows that the function increases on $(-\infty, 1]$ and decreases on $[1, \infty)$, reaching a global maximum at $(1, 1/e)$. As $x$ tends to positive infinity, the exponential denominator in $x/e^x$ overpowers the linear numerator, pulling the function down to a limit of zero. This horizontal asymptote $y = 0$ prevents the curve from crossing into negative numbers, forcing it to pass through an inflection point at $x = 2$ and flatten out into an infinite asymptotic tail above the positive $x$-axis.
