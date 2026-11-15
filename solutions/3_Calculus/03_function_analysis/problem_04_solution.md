# Problem 4 Solution: A Function with Two Vertical Asymptotes

## 1. Original Problem
Perform a detailed mathematical analysis of the rational function:
$$f(x) = \frac{1}{x^2 - 1}$$
1. Determine the natural domain $\operatorname{Dom}(f)$ and identify the equations of all vertical and horizontal asymptotes.
2. Analyze the algebraic sign of $f(x)$ across the disjoint intervals of the domain.
3. Compute the derivative $f'(x)$, find any critical points, and determine the monotonicity and local extrema on each interval.
4. Explain why each disjoint interval of the domain must be analyzed separately rather than combined into a single statement.

---

## 2. What We Are Trying to Find
We need to:
1. Factor the denominator $x^2 - 1 = (x - 1)(x + 1)$ to exclude the singularities $x = \pm 1$.
2. Compute the left-hand and right-hand limits at $x = -1$ and $x = 1$ to classify the two vertical asymptotes.
3. Compute the limits as $x \to \pm\infty$ to establish the horizontal asymptote $y = 0$.
4. Determine the sign of $f(x)$ on $(-\infty, -1)$, $(-1, 1)$, and $(1, \infty)$.
5. Differentiate $f(x) = (x^2 - 1)^{-1}$ to get $f'(x) = \frac{-2x}{(x^2 - 1)^2}$, find the critical point at $x = 0$, and prove it is a local maximum.
6. Provide the topological explanation of why disconnected domain components require separate interval-wise monotonicity statements.

---

## 3. Key Concepts and Theorems
1. **Factoring Denominators for Vertical Asymptotes:**
   For $f(x) = \frac{1}{(x - c_1)(x - c_2)}$, vertical asymptotes occur at $x = c_1$ and $x = c_2$.
2. **Even Function Symmetry:**
   A function is even if $f(-x) = f(x)$ for all $x \in \operatorname{Dom}(f)$.
   The graph of an even function has reflectional bilateral symmetry across the $y$-axis.
3. **Chain/Power Rule for Reciprocals:**
   $$\frac{d}{dx}\left[(u(x))^{-1}\right] = -(u(x))^{-2} \cdot u'(x) = -\frac{u'(x)}{[u(x)]^2}.$$
4. **Disconnected Domain Components:**
   The Mean Value Theorem and monotonicity theorems apply strictly to **intervals** (connected subsets of $\mathbb{R}$). On a union of disconnected intervals, function values can jump arbitrarily across the asymptotes.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Domain and Symmetry
1. **Domain:**
   Set the denominator equal to zero:
   $$x^2 - 1 = 0 \iff (x - 1)(x + 1) = 0 \iff x = 1 \quad \text{or} \quad x = -1.$$
   Therefore, the domain consists of three disconnected intervals:
   $$\operatorname{Dom}(f) = (-\infty, -1) \cup (-1, 1) \cup (1, \infty).$$
2. **Symmetry:**
   $$f(-x) = \frac{1}{(-x)^2 - 1} = \frac{1}{x^2 - 1} = f(x).$$
   The function is **even**; its graph is symmetric across the $y$-axis.
3. **Intercepts:**
   - $x$-intercepts: The numerator is $1 \neq 0$, so there are **no roots** (the curve never crosses the $x$-axis).
   - $y$-intercept: At $x = 0$, $f(0) = \frac{1}{0^2 - 1} = -1$. The intercept is $(0, -1)$.

---

### Step 2: Asymptotes and Boundary Limits
1. **Vertical Asymptote at $x = -1$:**
   - Left limit ($x \to -1^-$): $x < -1 \implies x^2 > 1 \implies x^2 - 1 \to 0^+$:
     $$\lim_{x\to-1^-} \frac{1}{x^2 - 1} = \left[\frac{1}{0^+}\right] = +\infty.$$
   - Right limit ($x \to -1^+$): $|x| < 1 \implies x^2 < 1 \implies x^2 - 1 \to 0^-$:
     $$\lim_{x\to-1^+} \frac{1}{x^2 - 1} = \left[\frac{1}{0^-}\right] = -\infty.$$
   The line **$x = -1$** is a vertical asymptote.

2. **Vertical Asymptote at $x = 1$:**
   By even symmetry (or direct limit computation):
   - Left limit ($x \to 1^-$): $x^2 < 1 \implies x^2 - 1 \to 0^-$:
     $$\lim_{x\to1^-} \frac{1}{x^2 - 1} = \left[\frac{1}{0^-}\right] = -\infty.$$
   - Right limit ($x \to 1^+$): $x^2 > 1 \implies x^2 - 1 \to 0^+$:
     $$\lim_{x\to1^+} \frac{1}{x^2 - 1} = \left[\frac{1}{0^+}\right] = +\infty.$$
   The line **$x = 1$** is a vertical asymptote.

3. **Horizontal Asymptote as $x \to \pm\infty$:**
   $$\lim_{x\to\pm\infty} \frac{1}{x^2 - 1} = 0.$$
   The line **$y = 0$** (the $x$-axis) is a horizontal asymptote. Since $x^2 - 1 > 0$ for $|x| > 1$, the curve approaches $y = 0$ strictly from above ($0^+$) in both directions.

---

### Step 3: Sign Analysis of $f(x)$
The numerator is always $+1 > 0$. The sign of $f(x)$ is determined solely by $x^2 - 1$:
1. On $(-\infty, -1)$: $x^2 > 1 \implies f(x) > 0$ (**positive**).
2. On $(-1, 1)$: $x^2 < 1 \implies f(x) < 0$ (**negative**).
3. On $(1, \infty)$: $x^2 > 1 \implies f(x) > 0$ (**positive**).

---

### Step 4: Derivative, Monotonicity, and Extrema
Rewrite $f(x) = (x^2 - 1)^{-1}$ and apply the Chain Rule:
$$f'(x) = -1(x^2 - 1)^{-2} \cdot \frac{d}{dx}[x^2 - 1] = -\frac{2x}{(x^2 - 1)^2}.$$

**Critical Points:**
Set $f'(x) = 0$:
$$-\frac{2x}{(x^2 - 1)^2} = 0 \implies -2x = 0 \implies x = 0.$$
Since $0 \in \operatorname{Dom}(f)$, $x = 0$ is the unique critical point.

**Sign of $f'(x)$ and Monotonicity on the Intervals:**
Notice that the denominator $(x^2 - 1)^2$ is strictly positive for all $x \in \operatorname{Dom}(f)$.
Thus, $\operatorname{sgn}(f'(x)) = \operatorname{sgn}(-2x)$:
1. On $(-\infty, -1)$: $x < 0 \implies -2x > 0 \implies f'(x) > 0$.
   The function is **strictly increasing** on $(-\infty, -1)$.
2. On $(-1, 0)$: $x < 0 \implies -2x > 0 \implies f'(x) > 0$.
   The function is **strictly increasing** on $(-1, 0]$.
3. On $(0, 1)$: $x > 0 \implies -2x < 0 \implies f'(x) < 0$.
   The function is **strictly decreasing** on $[0, 1)$.
4. On $(1, \infty)$: $x > 0 \implies -2x < 0 \implies f'(x) < 0$.
   The function is **strictly decreasing** on $(1, \infty)$.

**Local Extrema:**
At $x = 0$, $f'(x)$ changes sign from positive to negative ($+ \to -$) on the interval $(-1, 1)$.
Therefore, the point:
$$(0, f(0)) = (0, -1)$$
is a **strict local maximum**.

---

### Step 5: Why Each Disjoint Interval Must Be Analyzed Separately
- **The Pitfall of Combining Disjoint Sets:**
  A student might mistakenly write: *"The function is decreasing for $x > 0$, so it is decreasing on $(0, 1) \cup (1, \infty)$."*
  This statement is **mathematically false**!
  To see why, pick two test points across the asymptote $x = 1$:
  - Choose $x_1 = 0.5 \in (0, 1) \implies f(0.5) = \frac{1}{0.25 - 1} = -\frac{1}{0.75} \approx -1.33$.
  - Choose $x_2 = 2 \in (1, \infty) \implies f(2) = \frac{1}{4 - 1} = \frac{1}{3} \approx +0.33$.
  Notice that $0.5 < 2$, but $f(0.5) < f(2)$!
  The function value actually *increased* from $-1.33$ to $+0.33$ between these two points!
- **Topological Cause:**
  The definition of a decreasing function ($x_1 < x_2 \implies f(x_1) \ge f(x_2)$) requires a connected path between inputs. The vertical asymptote at $x = 1$ is a catastrophic disruption that breaks the real line into disjoint components, allowing values to jump from $-\infty$ up to $+\infty$.
  Therefore, monotonicity theorems apply strictly to individual connected intervals, and each interval must be stated separately.

---

## 5. Why Each Step Is Valid
1. **The domain exclusions $\pm 1$** are required because $x^2 - 1 = 0$ causes division by zero.
2. **The one-sided limits** confirm true vertical asymptotic behavior at both boundaries.
3. **The derivative sign $\operatorname{sgn}(-2x)$** is exact because the denominator $(x^2 - 1)^2$ is a positive square.

---

## 6. Final Answer in Words
The domain of $f(x) = \frac{1}{x^2 - 1}$ is $\operatorname{Dom}(f) = (-\infty, -1) \cup (-1, 1) \cup (1, \infty)$. The lines $x = -1$ and $x = 1$ are vertical asymptotes, and the line $y = 0$ is a horizontal asymptote. The function is positive on $(-\infty, -1) \cup (1, \infty)$ and negative on $(-1, 1)$, with $y$-intercept $(0, -1)$ and no real roots. Its derivative is $f'(x) = \frac{-2x}{(x^2 - 1)^2}$; $f$ is strictly increasing on $(-\infty, -1)$ and $(-1, 0]$, and strictly decreasing on $[0, 1)$ and $(1, \infty)$, attaining a local maximum at $(0, -1)$. Each interval must be analyzed separately because the vertical asymptotes interrupt the domain, causing values to jump across the breaks so that monotonicity does not hold across the union of disjoint intervals.

---

## 7. Quick Verification
- **Second derivative test at $x = 0$:**
  $$f''(x) = \frac{-2(x^2 - 1)^2 - (-2x) \cdot 2(x^2 - 1)(2x)}{(x^2 - 1)^4} = \frac{-2(x^2 - 1) + 8x^2}{(x^2 - 1)^3} = \frac{6x^2 + 2}{(x^2 - 1)^3}.$$
  At $x = 0$:
  $$f''(0) = \frac{0 + 2}{(0 - 1)^3} = \frac{2}{-1} = -2 < 0.$$
  Since $f'(0) = 0$ and $f''(0) = -2 < 0$, the Second Derivative Test rigorously confirms a local maximum.
- **Symmetry check:** $f(2) = 1/3 = f(-2)$, $f'(2) = -4/9 = -f'(-2)$. Perfectly matches even-function properties.

---

## 8. Common Mistakes to Avoid
- **Writing monotonicity over unions:** Claiming $f$ is decreasing on $(0, 1) \cup (1, \infty)$. One must write "decreasing on $(0, 1)$ and decreasing on $(1, \infty)$".
- **Claiming $(0, -1)$ is a minimum because it is negative:** Overlooking that on $(-1, 1)$, all other values are *more negative* (approaching $-\infty$), making $-1$ the local maximum on that branch.
- **Sign error in derivative:** Forgetting the minus sign from $(u^{-1})' = -u^{-2} u'$, which would flip all monotonicity conclusions.

---

## 9. Classroom Presentation (3-Sentence Summary)
The function $f(x) = 1/(x^2 - 1)$ is an even function with vertical asymptotes at $x = -1$ and $x = 1$ and a horizontal asymptote at $y = 0$. Differentiating gives $f'(x) = -2x / (x^2 - 1)^2$, which proves the function increases on $(-\infty, -1)$ and $(-1, 0]$ and decreases on $[0, 1)$ and $(1, \infty)$, reaching a local maximum at the central peak $(0, -1)$. We must state monotonicity on each interval separately because the infinite jumps at the vertical asymptotes break the domain, making statements across the combined union false.
