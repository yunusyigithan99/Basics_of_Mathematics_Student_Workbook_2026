# Problem 06: Logarithmic Integrals and the $\frac{g'(x)}{g(x)}$ Structure

## 1. Original Problem
Compute
$$\int\frac{2x}{x^2 + 5}\,dx.$$
Identify the denominator as a candidate for substitution, compare the numerator with its derivative, and explain the source of the logarithm in the result.

---

## 2. What We Are Trying to Find
1. Identification of the denominator as the substitution variable $u = g(x)$.
2. Comparison between the numerator and the differential $du = g'(x)\,dx$.
3. Clear conceptual explanation of why and how the natural logarithm arises from this algebraic fraction.
4. Evaluation of the integral and back-substitution into terms of $x$.
5. Explanation of why absolute value bars can be dropped for $x^2 + 5$.
6. Verification of the antiderivative by differentiation.

---

## 3. Key Concepts and Theorems
1. **The Logarithmic Antiderivative Rule:**
   For the reciprocal function $u^{-1} = \frac{1}{u}$, the standard power rule fails ($n = -1$). Its antiderivative is defined by the natural logarithm:
   $$\int \frac{1}{u}\,du = \ln|u| + C.$$
2. **The "Derivative over Function" Quotient Rule:**
   Whenever an integrand has the structure of the derivative of the denominator divided by the denominator:
   $$\int \frac{g'(x)}{g(x)}\,dx = \ln|g(x)| + C.$$
3. **Chain Rule for Logarithms:**
   $$\frac{d}{dx}[\ln(g(x))] = \frac{1}{g(x)} \cdot g'(x) = \frac{g'(x)}{g(x)}.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the denominator as a candidate for substitution
The integrand is the rational function $\frac{2x}{x^2 + 5}$.
We choose the entire denominator as our new variable:
$$u = x^2 + 5.$$

### Step 2: Compare the numerator with the derivative of the denominator
Differentiating our choice of $u$:
$$\frac{du}{dx} = \frac{d}{dx}(x^2 + 5) = 2x \implies du = 2x\,dx.$$
Comparing this with the numerator of the original integral:
- The numerator is $2x\,dx$.
- This is an **exact match** for $du$.
The integrand can therefore be rewritten as:
$$\int \frac{2x}{x^2 + 5}\,dx = \int \frac{1}{x^2 + 5} \cdot (2x\,dx) = \int \frac{1}{u}\,du.$$

### Step 3: Explain the source of the logarithm in the result
In the power rule:
$$\int u^n\,du = \frac{u^{n+1}}{n+1} + C,$$
the formula is valid for every real number $n$ **except $n = -1$**. 
When $n = -1$, the exponent formula produces division by zero: $\frac{u^0}{0}$, which is undefined. 
Because the derivative of the natural logarithm is $\frac{d}{du}(\ln u) = \frac{1}{u} = u^{-1}$, the unique operation that reverses the reciprocal power $u^{-1}$ is the natural logarithm:
$$\int \frac{1}{u}\,du = \ln|u| + C.$$
Thus, the logarithm arises because the degree of the numerator is exactly 1 less than the degree of the denominator, creating a reciprocal $1/u$ structure upon substitution.

### Step 4: Complete the integration and back-substitute
Using the logarithmic integration rule:
$$\int \frac{1}{u}\,du = \ln|u| + C.$$
Substitute back $u = x^2 + 5$:
$$\ln|x^2 + 5| + C.$$

### Step 5: Address the absolute value
For all real numbers $x \in \mathbb{R}$:
$$x^2 \ge 0 \implies x^2 + 5 \ge 5 > 0.$$
Because $x^2 + 5$ is strictly positive for every real $x$, the absolute value bars are mathematically redundant: $|x^2 + 5| = x^2 + 5$.
We write the final result cleanly as:
$$\ln(x^2 + 5) + C.$$

### Step 6: Verify by differentiation
Differentiating $F(x) = \ln(x^2 + 5) + C$ with respect to $x$ using the Chain Rule:
$$F'(x) = \frac{d}{dx}[\ln(x^2 + 5)] + 0 = \frac{1}{x^2 + 5} \cdot \frac{d}{dx}(x^2 + 5) = \frac{1}{x^2 + 5} \cdot 2x = \frac{2x}{x^2 + 5}.$$
The derivative matches the original integrand identically.

---

## 5. Why Each Step Is Valid
- **Step 1:** $x^2 + 5$ is smooth and never zero on $\mathbb{R}$.
- **Step 2:** The differential substitution directly replaces $2x\,dx$ with $du$.
- **Step 3:** By definition, the natural logarithm is the unique antiderivative of $1/u$.
- **Step 4:** Back-substitution restores the original variable $x$.
- **Step 5:** $|a| = a$ whenever $a > 0$.
- **Step 6:** The derivative of $\ln(g(x))$ is $\frac{g'(x)}{g(x)}$ by the chain rule.

---

## 6. Final Answer in Words
Choosing $u = x^2 + 5$ gives $du = 2x\,dx$, which matches the numerator perfectly. 
This transforms the integral into $\int \frac{1}{u}\,du$. 
The logarithm appears because $\frac{1}{u} = u^{-1}$ is the singular power where the polynomial power rule fails due to division by zero, having $\ln|u|$ as its unique antiderivative. 
Since $x^2 + 5 > 0$ for all real $x$, the absolute value can be dropped, giving:
$$\ln(x^2 + 5) + C, \quad C \in \mathbb{R}.$$
Differentiating $\ln(x^2 + 5)$ yields $\frac{2x}{x^2 + 5}$, confirming the result.

---

## 7. Quick Verification
- At $x = 0$:
  Integrand: $f(0) = \frac{0}{0 + 5} = 0$.
  Derivative: $F'(0) = \frac{2(0)}{0 + 5} = 0$.
- At $x = 2$:
  Integrand: $f(2) = \frac{2(2)}{4 + 5} = \frac{4}{9}$.
  Derivative: $F'(2) = \frac{2(2)}{4 + 5} = \frac{4}{9}$.
Exact match.

---

## 8. Common Mistakes to Avoid
- **Using the power rule incorrectly on $1/u$:** Writing $\int u^{-1}\,du = \frac{u^0}{0}$.
- **Keeping unnecessary absolute values or forgetting them when an expression CAN be negative:** Here $x^2 + 5 > 0$ so parentheses are standard, but for $\int \frac{1}{x}\,dx$, writing $\ln x$ without absolute values on domains where $x < 0$ is a mistake.
- **Trying partial fractions:** The denominator $x^2 + 5$ is irreducible over $\mathbb{R}$, so partial fractions are neither possible nor necessary.

---

## 9. Classroom Presentation (3-Sentence Summary)
Setting the denominator to $u = x^2 + 5$ reveals that its derivative $du = 2x\,dx$ is precisely the numerator, converting the problem into $\int (1/u)\,du$. The natural logarithm appears because $u^{-1}$ is the exception to the power rule where the antiderivative is logarithmic. Because $x^2 + 5$ is strictly positive for all real $x$, the solution is simply $\ln(x^2 + 5) + C$, which differentiates straight back to the original rational function.
