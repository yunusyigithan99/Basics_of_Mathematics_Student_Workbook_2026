# Problem 2 Solution: Powers, Roots, and the Domain

## 1. Original Problem
For the function:
$$f(x) = 2\sqrt{x} - \frac{3}{x^2} + x^{3/2}$$
1. Rewrite the entire function using rational and negative exponents in standard power form $x^\alpha$.
2. Determine the natural domain $\operatorname{Dom}(f)$ of the function.
3. Compute the derivative $f'(x)$.
4. Determine the domain $\operatorname{Dom}(f')$ of the derivative, and compare it with the domain of the original function.

---

## 2. What We Are Trying to Find
We need to:
1. Convert the square root $\sqrt{x}$ and reciprocal fraction $\frac{1}{x^2}$ into power form $x^{1/2}$ and $x^{-2}$.
2. Intersect the domain restrictions for square roots ($x \ge 0$) and denominators ($x \neq 0$).
3. Apply the generalized power rule $\frac{d}{dx}[x^\alpha] = \alpha x^{\alpha - 1}$ for real exponents $\alpha \in \mathbb{R}$.
4. Find the domain of the resulting derivative and explain why the endpoint $x = 0$ is lost during differentiation (vertical tangent / unbounded rate of change).

---

## 3. Key Concepts and Theorems
1. **Exponential and Radical Conversions:**
   $$\sqrt[n]{x} = x^{1/n}, \qquad \frac{1}{x^n} = x^{-n}, \qquad x^{m/n} = \sqrt[n]{x^m}.$$
2. **Generalized Power Rule:**
   For any real exponent $\alpha \neq 0$:
   $$\frac{d}{dx}[x^\alpha] = \alpha x^{\alpha - 1}.$$
3. **Domain Comparison Between Function and Derivative:**
   A function can only be differentiable at points where it is defined, so $\operatorname{Dom}(f') \subseteq \operatorname{Dom}(f)$. However, if the tangent line becomes vertical at a boundary point, the derivative does not exist at that point, making $\operatorname{Dom}(f')$ a strictly smaller set than $\operatorname{Dom}(f)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Rewrite the Function Using Powers
Express each term of $f(x) = 2\sqrt{x} - \frac{3}{x^2} + x^{3/2}$ as a power of $x$:
1. $2\sqrt{x} = 2 x^{1/2}$
2. $-\frac{3}{x^2} = -3 x^{-2}$
3. $x^{3/2} = x^{3/2}$

Thus, the function in standard power form is:
$$f(x) = 2x^{1/2} - 3x^{-2} + x^{3/2}.$$

---

### Step 2: Determine the Domain of $f(x)$
Inspect the requirements for each individual term:
1. For $2\sqrt{x} = 2x^{1/2}$: The square root requires $x \ge 0$.
2. For $-\frac{3}{x^2} = -3x^{-2}$: Division by zero requires $x^2 \neq 0 \implies x \neq 0$.
3. For $x^{3/2} = (\sqrt{x})^3$: The radical requires $x \ge 0$.

Intersecting these conditions:
$$x \ge 0 \quad \text{and} \quad x \neq 0 \implies x > 0.$$
Therefore, the domain of the function is:
$$\operatorname{Dom}(f) = (0, \infty) = \{x \in \mathbb{R} \mid x > 0\}.$$

---

### Step 3: Compute the Derivative $f'(x)$
Differentiate term by term using the power rule $\frac{d}{dx}[x^\alpha] = \alpha x^{\alpha - 1}$:

1. For $2x^{1/2}$:
   $$\frac{d}{dx}[2x^{1/2}] = 2 \cdot \left(\frac{1}{2} x^{\frac{1}{2} - 1}\right) = 1 \cdot x^{-1/2} = \frac{1}{\sqrt{x}}.$$
2. For $-3x^{-2}$:
   $$\frac{d}{dx}[-3x^{-2}] = -3 \cdot \left(-2 x^{-2 - 1}\right) = +6 x^{-3} = \frac{6}{x^3}.$$
3. For $x^{3/2}$:
   $$\frac{d}{dx}[x^{3/2}] = \frac{3}{2} x^{\frac{3}{2} - 1} = \frac{3}{2} x^{1/2} = \frac{3}{2}\sqrt{x}.$$

Combine the three terms:
$$f'(x) = x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2} = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3\sqrt{x}}{2}.$$

---

### Step 4: Compare the Domains
Examine the algebraic requirements of the derivative:
$$f'(x) = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3\sqrt{x}}{2}.$$
- The square root $\sqrt{x}$ requires $x \ge 0$.
- The terms $\frac{1}{\sqrt{x}}$ and $\frac{6}{x^3}$ appear in denominators, requiring $x \neq 0$.
Thus, $x$ must be strictly positive:
$$\operatorname{Dom}(f') = (0, \infty).$$

**Comparison:**
$$\operatorname{Dom}(f) = (0, \infty) \quad \text{and} \quad \operatorname{Dom}(f') = (0, \infty).$$
In this particular case, the domain of the function and the domain of the derivative are **identical**:
$$\operatorname{Dom}(f') = \operatorname{Dom}(f) = (0, \infty).$$
*Remark on Radical Functions in General:* If the function had only been $g(x) = 2\sqrt{x}$, its domain would have included zero ($\operatorname{Dom}(g) = [0, \infty)$), while its derivative $g'(x) = \frac{1}{\sqrt{x}}$ would have excluded zero ($\operatorname{Dom}(g') = (0, \infty)$) due to a vertical tangent. Here, however, the presence of the fractional term $-\frac{3}{x^2}$ already excluded $x = 0$ from the original domain of $f$, keeping the two domains identical.

---

## 5. Why Each Step Is Valid
1. **Converting roots and fractions to powers** is valid by the definition of rational and negative exponents for positive real numbers.
2. **The power rule** $\frac{d}{dx}[x^\alpha] = \alpha x^{\alpha - 1}$ is a standard theorem of calculus valid for all real exponents $\alpha \in \mathbb{R}$ on the domain $x > 0$.
3. **The domain intersection** follows the axiom that a compound function is defined only where every component sub-expression is well-defined.

---

## 6. Final Answer in Words
In power form, the function is $f(x) = 2x^{1/2} - 3x^{-2} + x^{3/2}$. Its natural domain is $\operatorname{Dom}(f) = (0, \infty)$ because the square roots require $x \ge 0$ while the denominator requires $x \neq 0$. The derivative is $f'(x) = x^{-1/2} + 6x^{-3} + \frac{3}{2}x^{1/2} = \frac{1}{\sqrt{x}} + \frac{6}{x^3} + \frac{3\sqrt{x}}{2}$. The domain of the derivative is also $\operatorname{Dom}(f') = (0, \infty)$, which is identical to the domain of the original function because the singularity at $x = 0$ was already excluded by the reciprocal term.

---

## 7. Quick Verification
- Evaluate at $x = 1$:
  $$f(1) = 2\sqrt{1} - \frac{3}{1^2} + 1^{3/2} = 2 - 3 + 1 = 0.$$
  $$f'(1) = \frac{1}{\sqrt{1}} + \frac{6}{1^3} + \frac{3\sqrt{1}}{2} = 1 + 6 + 1.5 = 8.5.$$
- Difference quotient check with $h = 0.001$:
  $$f(1.001) = 2\sqrt{1.001} - \frac{3}{(1.001)^2} + (1.001)^{1.5} \approx 2(1.00049987) - 3(0.998004) + 1.0015004 \approx 0.0085037.$$
  $$\frac{f(1.001) - f(1)}{0.001} \approx \frac{0.0085037}{0.001} = 8.5037 \approx 8.5.$$
  Matches $f'(1) = 8.5$ with high precision.

---

## 8. Common Mistakes to Avoid
- **Negative sign error when differentiating $x^{-2}$:** Writing $\frac{d}{dx}[-3x^{-2}] = -6x^{-3}$ instead of $-3(-2)x^{-3} = +6x^{-3}$.
- **Subtracting 1 incorrectly from negative exponents:** Writing $-2 - 1 = -1$ instead of $-3$.
- **Assuming the domain includes 0:** Writing $\operatorname{Dom}(f) = [0, \infty)$ while forgetting that $\frac{3}{0^2}$ is undefined.

---

## 9. Classroom Presentation (3-Sentence Summary)
We first rewrite the function in standard power form as $2x^{1/2} - 3x^{-2} + x^{3/2}$, which has domain $(0, \infty)$ because square roots require non-negative numbers while the denominator strictly forbids zero. Applying the power rule to each term yields the derivative $x^{-1/2} + 6x^{-3} + (3/2)x^{1/2}$, or $1/\sqrt{x} + 6/x^3 + (3\sqrt{x})/2$. The domain of the derivative is also $(0, \infty)$, which matches the function's domain exactly because the division by zero already excluded the origin from the original function.
