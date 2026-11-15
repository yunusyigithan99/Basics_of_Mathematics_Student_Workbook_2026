# Problem 07: Integration by Parts as Reversing the Product Rule

## 1. Original Problem
Compute
$$\int xe^x\,dx.$$
First write the product differentiation rule and, on that basis, explain the meaning of the integration-by-parts formula. Verify the result by differentiation.

---

## 2. What We Are Trying to Find
1. The formal statement and algebraic derivation of the integration-by-parts formula from the product rule of differentiation.
2. The conceptual and pedagogical explanation of the formula's purpose.
3. The strategic choice of parts ($u$ and $dv$) for the integrand $x e^x$.
4. The complete step-by-step evaluation of the integral $\int x e^x\,dx$.
5. The factoring and simplification of the antiderivative family.
6. Verification of the result using the product rule of differentiation.

---

## 3. Key Concepts and Theorems
1. **Product Rule for Derivatives:**
   For any two differentiable functions $u(x)$ and $v(x)$:
   $$\frac{d}{dx}[u(x) \cdot v(x)] = u'(x) v(x) + u(x) v'(x).$$
2. **Formula for Integration by Parts:**
   Integrating both sides of the product rule yields:
   $$\int u(x) v'(x)\,dx = u(x) v(x) - \int v(x) u'(x)\,dx,$$
   or in differential notation:
   $$\int u\,dv = uv - \int v\,du.$$
3. **Core Strategy of Integration by Parts:**
   We assign $u$ to a part of the integrand that becomes strictly simpler upon differentiation, and $dv$ to a part that can be easily integrated without growing more complicated.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Derive the integration-by-parts formula from the product rule
We begin with the standard product rule for differentiation:
$$\frac{d}{dx}(u \cdot v) = u' v + u v'.$$
Integrate both sides with respect to $x$:
$$\int \frac{d}{dx}(u \cdot v)\,dx = \int (u' v + u v')\,dx.$$
By the Fundamental Theorem of Calculus, the integral of the derivative of $(u \cdot v)$ is simply $u \cdot v$ (up to an arbitrary constant absorbed later):
$$u \cdot v = \int v \cdot u'\,dx + \int u \cdot v'\,dx.$$
In terms of differentials, $du = u'\,dx$ and $dv = v'\,dx$:
$$u \cdot v = \int v\,du + \int u\,dv.$$
Subtracting $\int v\,du$ from both sides gives the celebrated **integration-by-parts formula**:
$$\int u\,dv = uv - \int v\,du.$$

**Meaning of the formula:**
Integration by parts does not solve an integral in a single step; rather, it **trades one integral for another**. If the original integral $\int u\,dv$ is difficult, we can shift the derivative off $v$ and onto $u$. If differentiating $u$ simplifies it (e.g., reduces a polynomial degree) while integrating $dv$ remains manageable, the second integral $\int v\,du$ will be substantially easier to evaluate.

### Step 2: Choose the factors $u$ and $dv$ for $\int xe^x\,dx$
In our integral $\int x e^x\,dx$:
- Differentiating $x$ eliminates the variable, giving a constant ($1$).
- Integrating $e^x$ reproduces $e^x$ without increasing complexity.

Therefore, we choose:
$$u = x \implies du = dx,$$
$$dv = e^x\,dx \implies v = \int e^x\,dx = e^x.$$

### Step 3: Apply the integration-by-parts formula
Substitute $u, v, du, dv$ into $\int u\,dv = uv - \int v\,du$:
$$\int x e^x\,dx = x \cdot e^x - \int e^x\,dx.$$
The remaining integral is elementary:
$$\int e^x\,dx = e^x.$$
Adding the arbitrary constant of integration $C$:
$$\int x e^x\,dx = x e^x - e^x + C.$$
Factoring out the common exponential factor $e^x$:
$$(x - 1)e^x + C.$$

### Step 4: Verify the result by differentiation (Product Rule)
We differentiate $F(x) = (x - 1)e^x + C$ using the product rule:
$$F'(x) = \frac{d}{dx}\left[(x - 1)e^x\right] + \frac{d}{dx}(C)$$
$$= \frac{d}{dx}(x - 1) \cdot e^x + (x - 1) \cdot \frac{d}{dx}(e^x) + 0$$
$$= 1 \cdot e^x + (x - 1) \cdot e^x$$
$$= e^x + x e^x - e^x$$
$$= x e^x.$$
The terms $+e^x$ and $-e^x$ cancel, leaving exactly $x e^x$. The solution is verified.

---

## 5. Why Each Step Is Valid
- **Step 1:** The derivative of a product is reversible by integration by parts due to the Fundamental Theorem of Calculus and linearity of integrals.
- **Step 2:** The LIATE rule (Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential) suggests picking the algebraic factor $x$ as $u$.
- **Step 3:** The replacement replaces an algebraic-exponential product with a pure exponential integral, which is directly solvable.
- **Step 4:** Differentiating via the product rule directly recovers the original integrand through algebraic cancellation.

---

## 6. Final Answer in Words
The product rule $(uv)' = u'v + uv'$ integrates to $uv = \int v\,du + \int u\,dv$, which rearranges to $\int u\,dv = uv - \int v\,du$. This formula allows us to transfer the burden of differentiation from one factor to another. 
Choosing $u = x$ ($du = dx$) and $dv = e^x\,dx$ ($v = e^x$) yields:
$$\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C = (x - 1)e^x + C, \quad C \in \mathbb{R}.$$
Differentiating $(x - 1)e^x$ by the product rule yields $e^x + (x - 1)e^x = xe^x$, confirming the antiderivative.

---

## 7. Quick Verification
- At $x = 0$:
  Integrand: $f(0) = 0 \cdot e^0 = 0$.
  Derivative: $F'(0) = (0 - 1)e^0 + e^0 = -1 + 1 = 0$.
- At $x = 2$:
  Integrand: $f(2) = 2e^2$.
  Derivative: $F'(2) = (2 - 1)e^2 + e^2 = 2e^2$.
Values match.

---

## 8. Common Mistakes to Avoid
- **Inverting the choice of parts:**
  Choosing $u = e^x$ and $dv = x\,dx$ gives $v = \frac{x^2}{2}$, leading to $\int \frac{x^2}{2}e^x\,dx$, which is more complicated than the original integral.
- **Sign error in the formula:**
  Writing $\int u\,dv = uv + \int v\,du$ instead of the correct subtraction $uv - \int v\,du$.
- **Omitting the product rule when checking:**
  Mistakenly differentiating $(x - 1)e^x$ as $1 \cdot e^x = e^x$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Integration by parts is the reverse of the product rule, allowing us to trade a difficult integral for a simpler one by shifting the derivative onto another factor. For $\int xe^x\,dx$, setting $u = x$ and $dv = e^x\,dx$ turns the linear term into a constant, resulting in $xe^x - \int e^x\,dx = (x - 1)e^x + C$. Differentiating this result with the product rule cancels out the extra exponential term and confirms the original integrand $xe^x$.
