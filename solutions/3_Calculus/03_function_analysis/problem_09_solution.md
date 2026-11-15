# Problem 09: Oblique and Vertical Asymptotes via Polynomial Division

## 1. Original Problem
Analyze the asymptotes of
$$f(x) = \frac{x^2 + 1}{x - 1}.$$
Perform polynomial division and explain why the remainder term vanishes for large $|x|$.

---

## 2. What We Are Trying to Find
1. The domain of definition $D_f$.
2. Any vertical asymptotes by evaluating one-sided limits at domain boundaries.
3. The polynomial division of $\frac{x^2 + 1}{x - 1}$ into a quotient linear term and a rational remainder.
4. The equation of the oblique (slant) asymptote and a rigorous explanation of why the remainder term vanishes as $|x| \to \infty$.
5. The relative position of the graph with respect to its asymptotes.

---

## 3. Key Concepts and Theorems
1. **Vertical Asymptote:**
   The vertical line $x = x_0$ is a vertical asymptote if at least one of the one-sided limits is infinite:
   $$\lim_{x \to x_0^+} f(x) = \pm\infty \quad \text{or} \quad \lim_{x \to x_0^-} f(x) = \pm\infty.$$
2. **Oblique (Slant) Asymptote:**
   The line $y = mx + b$ is an asymptote of $f(x)$ as $x \to \pm\infty$ if and only if
   $$\lim_{x \to \pm\infty} [f(x) - (mx + b)] = 0.$$
3. **Polynomial Decomposition Theorem:**
   For a rational function $P(x)/Q(x)$ where the degree of the numerator exceeds the degree of the denominator by exactly $1$:
   $$\frac{P(x)}{Q(x)} = (mx + b) + \frac{R(x)}{Q(x)}, \quad \text{where } \deg(R) < \deg(Q).$$
   Since the denominator grows faster than the numerator in $R(x)/Q(x)$, this remainder term approaches $0$ as $|x| \to \infty$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Find the domain of definition
The function is a quotient of two polynomials:
$$f(x) = \frac{x^2 + 1}{x - 1}.$$
The denominator cannot be zero:
$$x - 1 \neq 0 \iff x \neq 1.$$
Hence, the domain is:
$$D_f = (-\infty, 1) \cup (1, \infty).$$

### Step 2: Determine vertical asymptotes
We investigate the behavior of $f(x)$ as $x$ approaches the domain boundary $x = 1$:
- **Right-hand limit ($x \to 1^+$):**
  $$\lim_{x \to 1^+} \frac{x^2 + 1}{x - 1} = \frac{1^2 + 1}{0^+} = \frac{2}{0^+} = +\infty.$$
- **Left-hand limit ($x \to 1^-$):**
  $$\lim_{x \to 1^-} \frac{x^2 + 1}{x - 1} = \frac{1^2 + 1}{0^-} = \frac{2}{0^-} = -\infty.$$
Since both one-sided limits are infinite, the vertical line:
$$x = 1$$
is a two-sided **vertical asymptote**.

### Step 3: Perform polynomial long division
The degree of the numerator $x^2 + 1$ is $2$, and the degree of the denominator $x - 1$ is $1$. Because $2 - 1 = 1$, an oblique asymptote exists.
Performing the division:
1. Divide the leading term: $\frac{x^2}{x} = x$.
2. Multiply and subtract: $(x^2 + 1) - x(x - 1) = (x^2 + 1) - (x^2 - x) = x + 1$.
3. Divide the new leading term: $\frac{x}{x} = 1$.
4. Multiply and subtract: $(x + 1) - 1(x - 1) = (x + 1) - (x - 1) = 2$.

Therefore:
$$\frac{x^2 + 1}{x - 1} = (x + 1) + \frac{2}{x - 1}.$$

### Step 4: Explain why the remainder term vanishes and establish the oblique asymptote
From the division in Step 3, the vertical difference between the function $f(x)$ and the linear function $y = x + 1$ is:
$$f(x) - (x + 1) = \frac{2}{x - 1}.$$
Taking the limit as $|x| \to \infty$:
$$\lim_{x \to \infty} [f(x) - (x + 1)] = \lim_{x \to \infty} \frac{2}{x - 1} = \frac{2}{\infty} = 0,$$
$$\lim_{x \to -\infty} [f(x) - (x + 1)] = \lim_{x \to -\infty} \frac{2}{x - 1} = \frac{2}{-\infty} = 0.$$

**Explanation of the vanishing remainder:**
As $|x|$ becomes arbitrarily large, the numerator of the remainder remains constant ($2$), while the denominator $|x - 1|$ grows without bound. The fraction of a fixed number divided by an arbitrarily huge quantity converges to zero. Therefore, the graph of $f(x)$ becomes indistinguishable from the straight line:
$$y = x + 1$$
at both positive and negative infinity. This line is the **oblique asymptote**.

### Step 5: Determine the relative position to the oblique asymptote
- For $x > 1$: $x - 1 > 0$, so $\frac{2}{x - 1} > 0$. Hence, $f(x) > x + 1$, meaning the curve lies strictly **above** the oblique asymptote.
- For $x < 1$: $x - 1 < 0$, so $\frac{2}{x - 1} < 0$. Hence, $f(x) < x + 1$, meaning the curve lies strictly **below** the oblique asymptote.

---

## 5. Why Each Step Is Valid
- **Step 1:** The denominator of a fraction in real arithmetic cannot equal zero.
- **Step 2:** Approaching $1$ from either side gives a non-zero numerator ($2$) divided by an infinitesimal quantity approaching $0$, producing infinity.
- **Step 3:** By the Euclidean division theorem for polynomials, any rational function with $\deg(P) = \deg(Q) + 1$ decomposes uniquely into a linear quotient and a remainder of lower degree.
- **Step 4:** The definition of an asymptote is precisely that the vertical separation $\Delta y = f(x) - y_{\text{asymptote}}$ converges to zero as $x \to \pm\infty$.
- **Step 5:** The algebraic sign of the remainder term immediately dictates whether the curve approaches from above or from below.

---

## 6. Final Answer in Words
The function $f(x) = \frac{x^2 + 1}{x - 1}$ has:
1. A **vertical asymptote** at $x = 1$, where $\lim_{x \to 1^-} f(x) = -\infty$ and $\lim_{x \to 1^+} f(x) = +\infty$.
2. An **oblique asymptote** given by the line $y = x + 1$ both as $x \to +\infty$ and as $x \to -\infty$.
Polynomial division gives $f(x) = x + 1 + \frac{2}{x - 1}$. The remainder term $\frac{2}{x - 1}$ vanishes for large $|x|$ because dividing a fixed constant by an arbitrarily large quantity tends to zero, which forces the curve to approach the line $y = x + 1$.

---

## 7. Quick Verification
We can independently calculate the slope $m$ and intercept $b$ using the standard limit formulas:
$$m = \lim_{x \to \infty} \frac{f(x)}{x} = \lim_{x \to \infty} \frac{x^2 + 1}{x(x - 1)} = \lim_{x \to \infty} \frac{x^2 + 1}{x^2 - x} = 1,$$
$$b = \lim_{x \to \infty} [f(x) - mx] = \lim_{x \to \infty} \left[\frac{x^2 + 1}{x - 1} - x\right] = \lim_{x \to \infty} \frac{x^2 + 1 - (x^2 - x)}{x - 1} = \lim_{x \to \infty} \frac{x + 1}{x - 1} = 1.$$
Both methods yield the exact same line $y = 1\cdot x + 1 = x + 1$.

---

## 8. Common Mistakes to Avoid
- **Looking for a horizontal asymptote:** The degree of the numerator ($2$) is strictly greater than that of the denominator ($1$), so no horizontal asymptote exists ($\lim_{x \to \pm\infty} f(x) = \pm\infty$).
- **Polynomial division sign mistakes:** When subtracting $x(x - 1) = x^2 - x$, remember that $(x^2 + 1) - (x^2 - x) = +x + 1$, not $-x + 1$.
- **Confusing the vertical asymptote with a removable hole:** The numerator at $x = 1$ is $1^2 + 1 = 2 \neq 0$, so $x = 1$ is an infinite vertical asymptote, not a removable discontinuity.

---

## 9. Classroom Presentation (3-Sentence Summary)
The domain excludes $x = 1$, where one-sided limits diverge to $\pm\infty$, establishing the vertical asymptote $x = 1$. Dividing the numerator by the denominator rewrites the function as $f(x) = x + 1 + \frac{2}{x - 1}$. Because the remainder term $2/(x - 1)$ approaches zero as $|x|$ grows large, the straight line $y = x + 1$ is the oblique asymptote of the graph.
