# Problem 12 Solution: Several Rules at Once

## 1. Original Problem
For the function:
$$f(x) = (x^2 + 1)^3 e^x$$
1. Formulate a structured plan before calculating: identify which differentiation rule governs the entire expression overall, and which rule applies internally to one of its factors.
2. Compute the derivative $f'(x)$ following your plan step by step.
3. Organize and factor the final result by factoring out all common algebraic and exponential factors.

---

## 2. What We Are Trying to Find
We need to:
1. Establish the hierarchy of operations: the top-level structure is a product of two factors, and the first factor is a composite function.
2. Apply the Product Rule as the overarching framework: $(uv)' = u'v + uv'$.
3. Apply the Chain Rule internally to differentiate the first factor $u(x) = (x^2 + 1)^3$.
4. Differentiate the second factor $v(x) = e^x$.
5. Factor out the greatest common factors $(x^2 + 1)^2$ and $e^x$ to produce the simplest factored form.

---

## 3. Key Concepts and Theorems
1. **The Product Rule (Top-Level Rule):**
   $$\frac{d}{dx}[u(x) v(x)] = u'(x) v(x) + u(x) v'(x).$$
2. **The Chain Rule (Sub-Rule for $u(x)$):**
   For $u(x) = [g(x)]^n$:
   $$u'(x) = n [g(x)]^{n-1} \cdot g'(x).$$
3. **Common Factor Extraction:**
   When combining terms involving powers of a common binomial $(x^2 + 1)^p$ and $e^x$, always factor out the lowest power present, $(x^2 + 1)^2 e^x$, leaving a simple polynomial in brackets.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Write Down the Differentiation Plan
- **Overall Structure:** The expression $f(x) = (x^2 + 1)^3 e^x$ is a **product** of two distinct functions:
  $$u(x) = (x^2 + 1)^3 \quad \text{and} \quad v(x) = e^x.$$
  Therefore, the **Product Rule** governs the entire expression at the highest level.
- **Internal Structure:** The first factor $u(x) = (x^2 + 1)^3$ is not a simple variable; it is a **composition** of an inner quadratic $x^2 + 1$ and an outer cubic power $(\cdot)^3$.
  Therefore, the **Chain Rule** must be applied to differentiate $u(x)$.
- **Execution Order:**
  1. Differentiate $u(x)$ using the Chain Rule.
  2. Differentiate $v(x)$ using the exponential rule.
  3. Combine using the Product Rule.
  4. Factor out common factors.

---

### Step 2: Differentiate the Factors
1. **Differentiate $u(x) = (x^2 + 1)^3$ via the Chain Rule:**
   - Outer power: $3(x^2 + 1)^{3-1} = 3(x^2 + 1)^2$
   - Inner derivative: $\frac{d}{dx}[x^2 + 1] = 2x$
   Combine:
   $$u'(x) = 3(x^2 + 1)^2 \cdot (2x) = 6x(x^2 + 1)^2.$$
2. **Differentiate $v(x) = e^x$:**
   $$v'(x) = e^x.$$

---

### Step 3: Apply the Product Rule
Substitute $u, u', v, v'$ into $(uv)' = u'v + uv'$:
$$f'(x) = u'(x) v(x) + u(x) v'(x)$$
$$f'(x) = \big[6x(x^2 + 1)^2\big] e^x + \big[(x^2 + 1)^3\big] e^x.$$

---

### Step 4: Factor Out Common Factors
Examine both terms in the sum:
- Term 1: $6x \cdot (x^2 + 1)^2 \cdot e^x$
- Term 2: $(x^2 + 1) \cdot (x^2 + 1)^2 \cdot e^x$

Both terms share the common factors:
$$e^x \quad \text{and} \quad (x^2 + 1)^2.$$
Factor out $(x^2 + 1)^2 e^x$:
$$f'(x) = (x^2 + 1)^2 e^x \cdot \Big[ 6x + (x^2 + 1) \Big].$$
Simplify the bracketed polynomial by writing it in descending powers of $x$:
$$6x + x^2 + 1 = x^2 + 6x + 1.$$
Thus, the fully factored and organized derivative is:
$$f'(x) = (x^2 + 1)^2 (x^2 + 6x + 1) e^x.$$

---

## 5. Why Each Step Is Valid
1. **The Product Rule** is the governing rule because the top-level algebraic operation connecting $(x^2 + 1)^3$ and $e^x$ is multiplication.
2. **The Chain Rule on $u(x)$** is valid because $u$ is a differentiable composition of a polynomial and a power function.
3. **Factoring $(x^2 + 1)^2 e^x$** follows from the distributive property $A B C + A D C = A C (B + D)$.

---

## 6. Final Answer in Words
The overarching rule governing the expression is the Product Rule, while the first factor $(x^2 + 1)^3$ internally requires the Chain Rule. Applying the Chain Rule gives $u'(x) = 6x(x^2 + 1)^2$, and applying the Product Rule produces $f'(x) = 6x(x^2 + 1)^2 e^x + (x^2 + 1)^3 e^x$. Factoring out the common terms $(x^2 + 1)^2 e^x$ yields the simplified, fully organized derivative $f'(x) = (x^2 + 1)^2 (x^2 + 6x + 1) e^x$.

---

## 7. Quick Verification
- Evaluate at $x = 0$:
  $$f(0) = (0^2 + 1)^3 e^0 = 1^3 \cdot 1 = 1.$$
  - Using factored derivative:
    $$f'(0) = (0 + 1)^2 (0 + 0 + 1) e^0 = 1 \cdot 1 \cdot 1 = 1.$$
  - Using expanded Product Rule:
    $$f'(0) = 6(0)(1)^2 e^0 + (1)^3 e^0 = 0 + 1 = 1.$$
  Both match.
- Numerical difference quotient check at $x = 0$ with $h = 0.001$:
  $$f(0.001) = (0.001^2 + 1)^3 e^{0.001} = (1.000001)^3 e^{0.001} \approx (1.000003)(1.0010005) \approx 1.0010035.$$
  $$\frac{f(0.001) - f(0)}{0.001} = \frac{1.0010035 - 1}{0.001} = \frac{0.0010035}{0.001} \approx 1.0035 \approx 1.0.$$
  Confirms $f'(0) = 1$.

---

## 8. Common Mistakes to Avoid
- **Attempting to expand $(x^2 + 1)^3$ fully before differentiating:** Expanding into $x^6 + 3x^4 + 3x^2 + 1$ makes the algebra prone to arithmetic errors and makes factoring out the common roots at the end much more difficult.
- **Forgetting the inner derivative $2x$ in the Chain Rule:** Writing $u'(x) = 3(x^2 + 1)^2$, which drops the factor of $2x$.
- **Leaving the derivative in an unsimplified sum:** Omitting the factorization step, which is essential for subsequent applications such as finding critical points and inflection points.

---

## 9. Classroom Presentation (3-Sentence Summary)
Before differentiating, we establish our plan: the overall expression is a product of two functions governed by the Product Rule, where the first factor $(x^2 + 1)^3$ requires the Chain Rule. Differentiating the first factor gives $6x(x^2 + 1)^2$ and differentiating $e^x$ gives $e^x$, which together yield $6x(x^2 + 1)^2 e^x + (x^2 + 1)^3 e^x$. Factoring out the greatest common factor $(x^2 + 1)^2 e^x$ leaves $6x + (x^2 + 1)$ inside the brackets, producing the final organized derivative $(x^2 + 1)^2 (x^2 + 6x + 1) e^x$.
