# Problem 9 Solution: A Logarithm and the Chain Rule

## 1. Original Problem
For the function:
$$f(x) = \ln(x^2 + 1)$$
1. Compute the derivative $f'(x)$ using the Chain Rule.
2. Determine the algebraic sign of $f'(x)$ on the three intervals/points:
   - for $x < 0$,
   - for $x = 0$,
   - for $x > 0$.
3. Based on this sign analysis, describe qualitatively how the function behaves around zero (monotonicity, local extrema, and curvature).

---

## 2. What We Are Trying to Find
We need to:
1. Identify the domain of the function, noting that $x^2 + 1 \ge 1 > 0$ for all $x \in \mathbb{R}$.
2. Differentiate $f(x) = \ln(u(x))$ using the formula $\frac{d}{dx}[\ln u] = \frac{u'}{u}$.
3. Analyze the sign of the derivative by examining the signs of its numerator $2x$ and denominator $x^2 + 1$.
4. Translate the sign of $f'(x)$ into geometric behavior: strictly decreasing for $x < 0$, stationary minimum at $x = 0$, and strictly increasing for $x > 0$.

---

## 3. Key Concepts and Theorems
1. **Chain Rule for Natural Logarithms:**
   For any strictly positive, differentiable function $u(x) > 0$:
   $$\frac{d}{dx}[\ln(u(x))] = \frac{1}{u(x)} \cdot u'(x) = \frac{u'(x)}{u(x)}.$$
2. **First Derivative Test for Monotonicity:**
   - If $f'(x) > 0$ on an interval, then $f(x)$ is **strictly increasing** on that interval.
   - If $f'(x) < 0$ on an interval, then $f(x)$ is **strictly decreasing** on that interval.
   - If $f'(x_0) = 0$ and $f'(x)$ changes sign from negative to positive at $x_0$, then $f(x)$ has a **strict local minimum** at $x_0$.
3. **Always Positive Expressions:**
   For any real number $x \in \mathbb{R}$, $x^2 \ge 0$, which guarantees:
   $$x^2 + 1 \ge 1 > 0.$$
   Therefore, the denominator $x^2 + 1$ is strictly positive for all real numbers and does not affect the sign of the quotient.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Check the Domain of $f(x)$
The natural logarithm $\ln(A)$ is defined only when its argument is strictly positive ($A > 0$).
Here, the argument is $A = x^2 + 1$.
Since $x^2 \ge 0$ for all real $x$:
$$x^2 + 1 \ge 1 > 0 \quad \text{for all } x \in \mathbb{R}.$$
Thus, the argument is always strictly positive, and the domain is the entire real line:
$$\operatorname{Dom}(f) = \mathbb{R} = (-\infty, \infty).$$

---

### Step 2: Compute the Derivative Using the Chain Rule
Let $u(x) = x^2 + 1$.
- Outer function: $g(u) = \ln u \implies g'(u) = \frac{1}{u}$
- Inner function: $u(x) = x^2 + 1 \implies u'(x) = 2x$

Apply the Chain Rule:
$$f'(x) = g'(u(x)) \cdot u'(x) = \frac{1}{u(x)} \cdot u'(x) = \frac{1}{x^2 + 1} \cdot (2x) = \frac{2x}{x^2 + 1}.$$

---

### Step 3: Analyze the Sign of $f'(x)$
Examine the quotient $f'(x) = \frac{2x}{x^2 + 1}$:
- The denominator is $x^2 + 1 \ge 1 > 0$ for **all** $x \in \mathbb{R}$.
- Since the denominator is always strictly positive, the sign of the entire fraction $f'(x)$ is determined **solely by the sign of the numerator $2x$**:
  $$\operatorname{sgn}\big(f'(x)\big) = \operatorname{sgn}(2x) = \operatorname{sgn}(x).$$

Now evaluate the three cases:
1. **For $x < 0$ (negative numbers):**
   $$2x < 0 \implies f'(x) = \frac{2x}{x^2 + 1} < 0.$$
   The derivative is strictly **negative**.
2. **For $x = 0$:**
   $$2(0) = 0 \implies f'(0) = \frac{0}{0^2 + 1} = \frac{0}{1} = 0.$$
   The derivative is **zero** ($f'(0) = 0$).
3. **For $x > 0$ (positive numbers):**
   $$2x > 0 \implies f'(x) = \frac{2x}{x^2 + 1} > 0.$$
   The derivative is strictly **positive**.

---

### Step 4: Describe the Qualitative Behavior Around Zero
From the sign of the derivative, we deduce the complete qualitative behavior of $f(x)$ around $x = 0$:
1. **Monotonicity:**
   - On the interval $(-\infty, 0)$, $f'(x) < 0$, so the function is **strictly decreasing**. As $x$ approaches $0$ from the left, the graph slopes downward.
   - On the interval $(0, \infty)$, $f'(x) > 0$, so the function is **strictly increasing**. As $x$ moves to the right past $0$, the graph slopes upward.
2. **Local and Global Minimum at $x = 0$:**
   - Because $f'(x)$ transitions continuously from negative values ($f'(x) < 0$) to positive values ($f'(x) > 0$) as $x$ passes through $0$, the point:
     $$(0, f(0)) = (0, \ln(0^2 + 1)) = (0, \ln 1) = (0, 0)$$
     is a **strict global minimum**.
   - The tangent line at $(0, 0)$ is horizontal ($m = 0$).
3. **Symmetry:**
   - Notice that $f(-x) = \ln((-x)^2 + 1) = \ln(x^2 + 1) = f(x)$, so $f(x)$ is an **even function**.
   - The graph forms a symmetric, smooth, U-shaped valley resting on the origin $(0, 0)$, climbing toward $+\infty$ on both wings as $|x| \to \infty$.

---

## 5. Why Each Step Is Valid
1. **$\operatorname{Dom}(f) = \mathbb{R}$** holds because real squares satisfy $x^2 \ge 0$, precluding non-positive logarithm arguments.
2. **The logarithmic Chain Rule $\frac{d}{dx}[\ln u] = \frac{u'}{u}$** is an established theorem of calculus derived from the inverse function theorem.
3. **The First Derivative Test** guarantees a local minimum because $f'(x)$ changes sign from negative to positive across $x = 0$ on a continuous interval.

---

## 6. Final Answer in Words
The derivative of $f(x) = \ln(x^2 + 1)$ is $f'(x) = \frac{2x}{x^2 + 1}$. The sign analysis reveals:
- For $x < 0$, $f'(x) < 0$ (strictly negative),
- For $x = 0$, $f'(0) = 0$,
- For $x > 0$, $f'(x) > 0$ (strictly positive).
Consequently, the function is strictly decreasing on $(-\infty, 0)$ and strictly increasing on $(0, \infty)$, meaning that the origin $(0, 0)$ is a strict global minimum where the curve rests flatly against a horizontal tangent line before curving upward symmetrically on both sides.

---

## 7. Quick Verification
- Second derivative test:
  $$f''(x) = \frac{d}{dx}\left[\frac{2x}{x^2 + 1}\right] = \frac{2(x^2 + 1) - 2x(2x)}{(x^2 + 1)^2} = \frac{2x^2 + 2 - 4x^2}{(x^2 + 1)^2} = \frac{2 - 2x^2}{(x^2 + 1)^2}.$$
  At $x = 0$:
  $$f''(0) = \frac{2 - 0}{(0 + 1)^2} = \frac{2}{1} = 2 > 0.$$
  Since $f'(0) = 0$ and $f''(0) = 2 > 0$, the Second Derivative Test confirms that $x = 0$ is a strict local minimum.
- Numerical values:
  - $f(-1) = \ln(2) \approx 0.693$
  - $f(0) = \ln(1) = 0$
  - $f(1) = \ln(2) \approx 0.693$
  Values decrease from $0.693$ to $0$ and then increase back to $0.693$.

---

## 8. Common Mistakes to Avoid
- **Forgetting the inner derivative $2x$:** Writing $f'(x) = \frac{1}{x^2 + 1}$, which would make the derivative always positive and wrongly imply the function is increasing everywhere.
- **Thinking the logarithm argument can be zero:** Worrying about domain issues when $x^2 + 1 \ge 1 > 0$ is never zero or negative for real $x$.
- **Believing $f'(0) = 0$ implies an inflection point:** Missing the sign change from negative to positive, which confirms an extremum (minimum), not an inflection.

---

## 9. Classroom Presentation (3-Sentence Summary)
Using the Chain Rule for logarithms, the derivative of $\ln(x^2 + 1)$ evaluates to $u'/u$, giving $f'(x) = 2x / (x^2 + 1)$. Because the denominator $x^2 + 1$ is always strictly positive, the sign of the derivative is identical to the sign of $x$: negative for $x < 0$, zero at $x = 0$, and positive for $x > 0$. This sign pattern proves that the function decreases to the left of the origin and increases to the right, establishing that the origin $(0, 0)$ is a smooth global minimum with a horizontal tangent line.
