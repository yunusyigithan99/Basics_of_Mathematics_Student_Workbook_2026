# Problem 02: Integration of Powers, Roots, and Domain Considerations

## 1. Original Problem
Compute
$$\int\left(2\sqrt{x} + \frac{3}{x^2} - x^{1/3}\right)\,dx.$$
First rewrite the terms as powers, determine the domain of the original expression, and verify the result by differentiation.

---

## 2. What We Are Trying to Find
1. The domain of definition $D_f$ for the integrand expression.
2. The algebraic reformulation of roots and fractions into standard exponential powers $x^p$.
3. The evaluation of the indefinite integral term by term using the generalized power rule.
4. Direct verification of the antiderivative by differentiating back to the original expression.

---

## 3. Key Concepts and Theorems
1. **Exponent Laws for Radicals and Reciprocals:**
   $$\sqrt{x} = x^{1/2}, \qquad \frac{1}{x^n} = x^{-n}, \qquad \sqrt[n]{x} = x^{1/n}.$$
2. **Domain Restrictions:**
   - Real square roots require non-negative inputs: $x \ge 0$.
   - Denominators cannot be zero: $x \neq 0$.
   Hence the combined domain is $x > 0$.
3. **Power Rule for Integration:**
   For any real exponent $p \neq -1$:
   $$\int x^p\,dx = \frac{x^{p+1}}{p+1} + C.$$
4. **Linearity of the Indefinite Integral:**
   Integrals can be split across sums and differences, with multiplicative constants factored out.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Determine the domain of the integrand
Let $f(x) = 2\sqrt{x} + \frac{3}{x^2} - x^{1/3}$.
We examine the domain constraints for each term:
- For $2\sqrt{x}$: The square root in the real numbers requires $x \ge 0$.
- For $\frac{3}{x^2}$: Division by zero is undefined, so $x \neq 0$.
- For $x^{1/3}$: The cube root is defined for all real numbers, but within the context of the whole expression, it must satisfy the most restrictive condition.

Intersecting these conditions:
$$x \ge 0 \quad \text{and} \quad x \neq 0 \implies x > 0.$$
Therefore, the domain of definition is:
$$D_f = (0, \infty).$$
All integration and differentiation steps take place on this interval.

### Step 2: Rewrite the integrand terms as powers
Expressing each term in power form $x^p$:
- $2\sqrt{x} = 2x^{1/2}$.
- $\frac{3}{x^2} = 3x^{-2}$.
- $-x^{1/3} = -x^{1/3}$.

The integral becomes:
$$\int\left(2\sqrt{x} + \frac{3}{x^2} - x^{1/3}\right)\,dx = \int\left(2x^{1/2} + 3x^{-2} - x^{1/3}\right)\,dx.$$

### Step 3: Compute the antiderivative term by term
Applying the power rule $\int x^p\,dx = \frac{x^{p+1}}{p+1}$ to each component:

1. **First term:**
   $$\int 2x^{1/2}\,dx = 2 \cdot \frac{x^{1/2 + 1}}{\frac{1}{2} + 1} = 2 \cdot \frac{x^{3/2}}{\frac{3}{2}} = 2 \cdot \frac{2}{3} x^{3/2} = \frac{4}{3}x^{3/2} = \frac{4}{3}x\sqrt{x}.$$

2. **Second term:**
   $$\int 3x^{-2}\,dx = 3 \cdot \frac{x^{-2 + 1}}{-2 + 1} = 3 \cdot \frac{x^{-1}}{-1} = -3x^{-1} = -\frac{3}{x}.$$

3. **Third term:**
   $$\int \left(-x^{1/3}\right)\,dx = -\frac{x^{1/3 + 1}}{\frac{1}{3} + 1} = -\frac{x^{4/3}}{\frac{4}{3}} = -\frac{3}{4}x^{4/3} = -\frac{3}{4}x\sqrt[3]{x}.$$

Combining the three terms and adding the arbitrary constant of integration $C$:
$$\int\left(2\sqrt{x} + \frac{3}{x^2} - x^{1/3}\right)\,dx = \frac{4}{3}x^{3/2} - \frac{3}{x} - \frac{3}{4}x^{4/3} + C.$$

### Step 4: Verify the result by differentiation
Differentiating our result $F(x) = \frac{4}{3}x^{3/2} - 3x^{-1} - \frac{3}{4}x^{4/3} + C$ using the power rule $\frac{d}{dx}(x^n) = n x^{n-1}$:
$$F'(x) = \frac{4}{3} \cdot \left(\frac{3}{2}x^{3/2 - 1}\right) - 3 \cdot \left(-1 x^{-1 - 1}\right) - \frac{3}{4} \cdot \left(\frac{4}{3}x^{4/3 - 1}\right) + 0.$$
Simplify the coefficients and exponents:
- $\frac{4}{3} \cdot \frac{3}{2} = 2$, and $x^{3/2 - 1} = x^{1/2} = \sqrt{x}$.
- $-3 \cdot (-1) = +3$, and $x^{-2} = \frac{1}{x^2}$.
- $-\frac{3}{4} \cdot \frac{4}{3} = -1$, and $x^{4/3 - 1} = x^{1/3}$.

Putting it together:
$$F'(x) = 2\sqrt{x} + \frac{3}{x^2} - x^{1/3} = f(x).$$
The derivative matches the original integrand identically, confirming correctness.

---

## 5. Why Each Step Is Valid
- **Step 1:** An expression is only valid where all component elementary functions are simultaneously defined.
- **Step 2:** Standard algebraic exponent rules state that $\sqrt[m]{x^n} = x^{n/m}$ and $1/x^n = x^{-n}$.
- **Step 3:** The power rule for integration holds for all real powers $p \neq -1$; none of the exponents ($1/2, -2, 1/3$) equal $-1$.
- **Step 4:** The Fundamental Theorem of Calculus states that differentiation reverses indefinite integration on the open domain $(0, \infty)$.

---

## 6. Final Answer in Words
The domain of the integrand is $(0, \infty)$, determined by the square root ($x \ge 0$) and the fraction's denominator ($x \neq 0$). 
Rewriting the terms as powers yields $2x^{1/2} + 3x^{-2} - x^{1/3}$. 
Integrating term by term produces:
$$\frac{4}{3}x^{3/2} - \frac{3}{x} - \frac{3}{4}x^{4/3} + C \quad \left(\text{or } \frac{4}{3}x\sqrt{x} - \frac{3}{x} - \frac{3}{4}x\sqrt[3]{x} + C\right),$$
where $C \in \mathbb{R}$. 
Differentiating this antiderivative yields $2\sqrt{x} + \frac{3}{x^2} - x^{1/3}$, confirming the result.

---

## 7. Quick Verification
Evaluate at $x = 1$:
- Integrand: $f(1) = 2\sqrt{1} + \frac{3}{1^2} - 1^{1/3} = 2 + 3 - 1 = 4$.
- Derivative of antiderivative at $x = 1$:
  $F'(1) = \frac{4}{3} \left(\frac{3}{2} \cdot 1^{1/2}\right) + 3 \left(1^{-2}\right) - \frac{3}{4} \left(\frac{4}{3} \cdot 1^{1/3}\right) = 2 + 3 - 1 = 4$.
The numerical slopes match exactly.

---

## 8. Common Mistakes to Avoid
- **Integrating $x^{-2}$ as a logarithm:** Confusing $x^{-2}$ with $x^{-1}$. Remember that $\int \frac{1}{x}\,dx = \ln|x| + C$, but for $\int x^{-2}\,dx$, the standard power rule gives $\frac{x^{-1}}{-1} = -\frac{1}{x}$.
- **Fraction arithmetic errors:** Computing $\frac{1}{2} + 1 = \frac{3}{2}$ but forgetting to invert when dividing, incorrectly writing $\frac{1}{3/2} = \frac{3}{2}$ instead of $\frac{2}{3}$.
- **Overlooking the domain:** Stating that the result holds on $\mathbb{R} \setminus \{0\}$, forgetting that the square root $\sqrt{x}$ forbids negative inputs in real analysis.

---

## 9. Classroom Presentation (3-Sentence Summary)
We first establish the domain as $(0, \infty)$ because the square root forbids negative numbers and the rational term forbids zero. Rewriting the integrand in exponent form as $2x^{1/2} + 3x^{-2} - x^{1/3}$ allows us to apply the power rule to each term individually. The resulting antiderivative is $\frac{4}{3}x^{3/2} - \frac{3}{x} - \frac{3}{4}x^{4/3} + C$, which upon differentiation immediately reproduces the original expression.
