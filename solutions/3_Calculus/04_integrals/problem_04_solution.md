# Problem 04: Integration by Substitution as Reversing the Chain Rule

## 1. Original Problem
Compute
$$\int 2x(x^2 + 1)^4\,dx.$$
Before calculating, identify a candidate for the new variable $u$ and show that its derivative appears in the integral. Finally, verify the result by differentiation.

---

## 2. What We Are Trying to Find
1. Identification of the composite function structure $f(g(x)) g'(x)$.
2. Choice of the substitution variable $u = g(x)$ and demonstration that $du = g'(x)\,dx$ is present in the integrand.
3. Complete evaluation of the transformed integral using the standard power rule.
4. Back-substitution into terms of the original variable $x$.
5. Verification of the result using the Chain Rule of differentiation.

---

## 3. Key Concepts and Theorems
1. **The Chain Rule for Derivatives:**
   $$\frac{d}{dx}[F(g(x))] = F'(g(x)) \cdot g'(x).$$
2. **Integration by Substitution (Reversing the Chain Rule):**
   If $u = g(x)$ is a differentiable function whose range is an interval where $f$ is continuous, then:
   $$\int f(g(x)) \cdot g'(x)\,dx = \int f(u)\,du = F(u) + C = F(g(x)) + C.$$
3. **Power Rule for Integrals:**
   $$\int u^n\,du = \frac{u^{n+1}}{n+1} + C \quad (n \neq -1).$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the candidate for substitution $u$
Examining the integrand $2x(x^2 + 1)^4$:
- The base expression raised to the power $4$ is $x^2 + 1$. This is our candidate for the inner function:
  $$u = x^2 + 1.$$
- Compute the derivative of this candidate:
  $$\frac{du}{dx} = \frac{d}{dx}(x^2 + 1) = 2x \implies du = 2x\,dx.$$

### Step 2: Show that the derivative appears in the integral
We rewrite the integrand to highlight the composite structure and differential:
$$\int 2x(x^2 + 1)^4\,dx = \int \underbrace{(x^2 + 1)^4}_{u^4} \cdot \underbrace{(2x\,dx)}_{du}.$$
The factor $2x$ multiplying $dx$ is exactly the differential $du$. Thus, no constant adjustments are necessary; the derivative of the inner function appears completely and cleanly.

### Step 3: Perform the substitution and integrate
Substitute $u = x^2 + 1$ and $du = 2x\,dx$ into the integral:
$$\int u^4\,du.$$
Applying the basic power rule with exponent $n = 4$:
$$\int u^4\,du = \frac{u^{4+1}}{4+1} + C = \frac{u^5}{5} + C.$$

### Step 4: Back-substitute into terms of $x$
Replace $u$ with its definition in terms of $x$, namely $u = x^2 + 1$:
$$\frac{(x^2 + 1)^5}{5} + C = \frac{1}{5}(x^2 + 1)^5 + C.$$

### Step 5: Verify the result by differentiation (Chain Rule)
We differentiate $F(x) = \frac{1}{5}(x^2 + 1)^5 + C$ with respect to $x$:
$$\frac{d}{dx}\left[\frac{1}{5}(x^2 + 1)^5 + C\right] = \frac{1}{5} \cdot \frac{d}{dx}\left[(x^2 + 1)^5\right] + 0.$$
Applying the Chain Rule: $\frac{d}{dx}[u^5] = 5u^4 \cdot \frac{du}{dx}$:
$$F'(x) = \frac{1}{5} \cdot \left[5(x^2 + 1)^4 \cdot \frac{d}{dx}(x^2 + 1)\right]$$
$$= 1 \cdot (x^2 + 1)^4 \cdot (2x)$$
$$= 2x(x^2 + 1)^4.$$
The derivative matches the original integrand identically, verifying the solution.

---

## 5. Why Each Step Is Valid
- **Step 1:** The polynomial $x^2 + 1$ is differentiable everywhere on $\mathbb{R}$.
- **Step 2:** Rearranging factors in a product is justified by the commutativity of real multiplication.
- **Step 3:** The change-of-variables formula transforms a complicated composite integral into an elementary power integral.
- **Step 4:** The original problem was posed in terms of $x$, so the antiderivative must be expressed as a function of $x$.
- **Step 5:** By the Chain Rule, differentiating the outer power function and multiplying by the inner derivative recovers the exact factors in the original integrand.

---

## 6. Final Answer in Words
Choosing $u = x^2 + 1$ gives the differential $du = 2x\,dx$, which is present verbatim in the integrand. 
Substituting converts the integral into $\int u^4\,du = \frac{1}{5}u^5 + C$. 
Back-substituting gives:
$$\frac{1}{5}(x^2 + 1)^5 + C, \quad C \in \mathbb{R}.$$
Differentiating this result using the Chain Rule yields $\frac{1}{5} \cdot 5(x^2 + 1)^4 \cdot 2x = 2x(x^2 + 1)^4$, confirming the correctness of the integration.

---

## 7. Quick Verification
- At $x = 0$:
  Integrand: $f(0) = 2(0)(0^2 + 1)^4 = 0$.
  Derivative: $F'(0) = 2(0)(0^2 + 1)^4 = 0$.
- At $x = 1$:
  Integrand: $f(1) = 2(1)(1 + 1)^4 = 2(16) = 32$.
  Derivative: $F'(1) = 2(1)(1 + 1)^4 = 32$.
Values match.

---

## 8. Common Mistakes to Avoid
- **Expanding $(x^2 + 1)^4$ by the Binomial Theorem:** While algebraically possible, it is tedious, prone to arithmetic errors, and misses the fundamental pedagogical purpose of recognizing the chain rule.
- **Forgetting $du$ requires $dx$:** Writing $u = x^2 + 1 \implies du = 2x$ without $dx$, leading to confusion when matching differentials.
- **Leaving the answer in terms of $u$:** Forgetting to back-substitute $u = x^2 + 1$ at the end of the calculation.

---

## 9. Classroom Presentation (3-Sentence Summary)
We recognize substitution as reversing the chain rule by choosing the inner function $u = x^2 + 1$, whose derivative $du = 2x\,dx$ is already multiplying the expression. This simplifies the problem to the elementary power integral $\int u^4\,du = u^5/5 + C$. Back-substituting yields $(x^2 + 1)^5/5 + C$, which upon differentiation immediately reproduces $2x(x^2 + 1)^4$ via the chain rule.
