# Problem 05: Structural Recognition of Substitution across Contexts

## 1. Original Problem
Compute
$$\int x e^{x^2}\,dx.$$
First compare the structure with Problem 4 and explain what is common despite the different appearance of the function.

---

## 2. What We Are Trying to Find
1. A structural comparison between the algebraic integral in Problem 4 ($\int 2x(x^2+1)^4\,dx$) and the exponential integral here ($\int xe^{x^2}\,dx$).
2. The choice of the substitution variable $u = x^2$ and adjustment for the constant factor.
3. The evaluation of the transformed integral.
4. Back-substitution into terms of $x$.
5. Verification of the antiderivative by differentiation.

---

## 3. Key Concepts and Theorems
1. **Structural Pattern of Substitution:**
   Any integral of the form
   $$\int f(g(x)) \cdot g'(x)\,dx$$
   is solvable by substitution $u = g(x)$, regardless of whether the outer function $f(u)$ is a polynomial, a radical, a trigonometric function, or an exponential function.
2. **Exponential Antiderivative:**
   $$\int e^u\,du = e^u + C.$$
3. **Chain Rule for Exponentials:**
   $$\frac{d}{dx}\left(e^{g(x)}\right) = e^{g(x)} \cdot g'(x).$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Structural comparison with Problem 4
Let us place both problems side by side:
- **Problem 4:** $\int 2x (x^2 + 1)^4\,dx$
  - Inner function: $g(x) = x^2 + 1$, quadratic.
  - Outer function: $f(u) = u^4$, a power function.
  - Multiplicative factor: $2x\,dx = g'(x)\,dx$, linear.
- **Problem 5:** $\int x e^{x^2}\,dx$
  - Inner function: $g(x) = x^2$, quadratic.
  - Outer function: $f(u) = e^u$, an exponential function.
  - Multiplicative factor: $x\,dx = \frac{1}{2} g'(x)\,dx$, linear.

**What is common:**
Despite the superficial difference—one being an algebraic polynomial power and the other being a transcendental exponential—the core calculus structure is identical. In both cases, an inner quadratic expression $x^2$ is trapped inside an outer function, while outside sits a linear factor of $x\,dx$. Because the derivative of a degree-$2$ polynomial is a degree-$1$ polynomial, the presence of $x\,dx$ is the exact key that unlocks substitution for both.

### Step 2: Set up the substitution
Let:
$$u = x^2.$$
Compute the differential:
$$du = 2x\,dx \iff x\,dx = \frac{1}{2}du.$$

### Step 3: Transform and evaluate the integral
Substitute $u$ and $x\,dx = \frac{1}{2}du$ into the integral:
$$\int x e^{x^2}\,dx = \int e^{x^2} \cdot (x\,dx) = \int e^u \cdot \left(\frac{1}{2}du\right).$$
Pull out the scalar constant $\frac{1}{2}$ by linearity:
$$= \frac{1}{2} \int e^u\,du.$$
Since the antiderivative of $e^u$ is simply $e^u$:
$$= \frac{1}{2} e^u + C.$$

### Step 4: Back-substitute into terms of $x$
Replace $u$ with $x^2$:
$$\frac{1}{2} e^{x^2} + C.$$

### Step 5: Verify by differentiation
Differentiating $F(x) = \frac{1}{2}e^{x^2} + C$ using the Chain Rule:
$$F'(x) = \frac{d}{dx}\left[\frac{1}{2}e^{x^2} + C\right] = \frac{1}{2} \cdot e^{x^2} \cdot \frac{d}{dx}(x^2) + 0$$
$$= \frac{1}{2} \cdot e^{x^2} \cdot (2x)$$
$$= x e^{x^2}.$$
The derivative matches the original integrand $f(x)$ exactly.

---

## 5. Why Each Step Is Valid
- **Step 1:** The mathematical structure of an integral is governed by derivative relationships between terms, not the qualitative category of the outer function.
- **Step 2:** $x^2$ is differentiable everywhere on $\mathbb{R}$, with $\frac{d}{dx}(x^2) = 2x$.
- **Step 3:** The constant multiple rule allows factoring out $\frac{1}{2}$, and $\int e^u\,du = e^u + C$ is standard.
- **Step 4:** Substituting back expresses the solution in the original independent variable $x$.
- **Step 5:** The Chain Rule for $e^{u(x)}$ states $(e^{u})' = e^u \cdot u'$, which cancels the factor of $1/2$ with $2x$.

---

## 6. Final Answer in Words
The structure is fundamentally the same as Problem 4 because both integrands consist of an inner quadratic term ($x^2$) composed within an outer function, multiplied by its linear derivative $x\,dx$. 
Setting $u = x^2$ yields $x\,dx = \frac{1}{2}du$, transforming the integral into $\frac{1}{2}\int e^u\,du = \frac{1}{2}e^u + C$. 
Back-substituting gives the final antiderivative:
$$\frac{1}{2}e^{x^2} + C, \quad C \in \mathbb{R}.$$
Differentiating $\frac{1}{2}e^{x^2}$ using the Chain Rule gives $\frac{1}{2}e^{x^2}(2x) = xe^{x^2}$, verifying the solution.

---

## 7. Quick Verification
- At $x = 0$:
  Integrand: $f(0) = 0 \cdot e^0 = 0$.
  Derivative: $F'(0) = 0 \cdot e^0 = 0$.
- At $x = 1$:
  Integrand: $f(1) = 1 \cdot e^1 = e \approx 2.718$.
  Derivative: $F'(1) = \frac{1}{2} e^1 \cdot 2(1) = e$.
Values match.

---

## 8. Common Mistakes to Avoid
- **Attempting integration by parts:** Choosing $u = x$ and $dv = e^{x^2}\,dx$ fails immediately because $e^{x^2}$ has no elementary antiderivative.
- **Forgetting the factor of $1/2$:** Writing $du = x\,dx$ instead of $du = 2x\,dx \implies x\,dx = \frac{1}{2}du$.
- **Confusing $\int xe^{x^2}\,dx$ with $\int x e^x\,dx$:** The latter requires integration by parts, whereas the presence of $x^2$ in the exponent demands substitution.

---

## 9. Classroom Presentation (3-Sentence Summary)
Just like in Problem 4, the integrand contains an inner quadratic whose derivative supplies the linear factor $x\,dx$, proving that substitution is recognized by functional structure rather than function type. Letting $u = x^2$ gives $x\,dx = \frac{1}{2}du$, reducing the problem to integrating the exponential function $\frac{1}{2}\int e^u\,du$. The resulting antiderivative is $\frac{1}{2}e^{x^2} + C$, which differentiation immediately verifies via the chain rule.
