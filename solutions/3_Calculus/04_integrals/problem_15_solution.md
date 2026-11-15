# Problem 15: Initial Value Problem and Recovering a Function

## 1. Original Problem
The function $F$ satisfies
$$F'(x) = 2xe^{x^2}$$
and
$$F(0) = 3.$$

1. Recognize the method needed to find the function $F$.
2. Determine the entire family of functions with the given derivative.
3. Use the condition $F(0) = 3$ to determine the correct constant.
4. Verify the final result by differentiation and substitution of $x = 0$.

---

## 2. What We Are Trying to Find
1. Identification of the appropriate integration method based on the structure of $F'(x)$.
2. Evaluation of the general indefinite integral to find the family of all antiderivatives $F(x) + C$.
3. Application of the initial condition $F(0) = 3$ to pinpoint the unique value of $C$.
4. Double verification:
   - Differentiating the resulting function to confirm $F'(x) = 2xe^{x^2}$.
   - Substituting $x = 0$ to confirm $F(0) = 3$.

---

## 3. Key Concepts and Theorems
1. **Initial Value Problem (IVP):**
   A differential equation $F'(x) = f(x)$ specifies an infinite family of curves separated by vertical shifts $+ C$. An initial condition $F(x_0) = y_0$ selects the unique curve passing through the point $(x_0, y_0)$.
2. **Integration by Substitution:**
   When an integrand has the form $f(g(x)) g'(x)$, substituting $u = g(x)$ and $du = g'(x)\,dx$ reduces the integral to $\int f(u)\,du$.
3. **Euler's Number Base Identity:**
   $$e^0 = 1.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Recognize the method needed to find $F(x)$
To recover $F(x)$ from its rate of change $F'(x)$, we must compute its indefinite integral:
$$F(x) = \int F'(x)\,dx = \int 2x e^{x^2}\,dx.$$

**Method Recognition:**
The integrand consists of the transcendental exponential $e^{x^2}$ whose exponent is the quadratic $x^2$. Multiplying the exponential is the factor $2x$, which is the exact derivative of the exponent ($\frac{d}{dx}(x^2) = 2x$). 
Therefore, this problem requires **$u$-substitution (reversing the chain rule)**.

### Step 2: Determine the entire family of functions
We perform the substitution:
$$u = x^2 \implies du = 2x\,dx.$$
Rewriting the integral in terms of $u$:
$$\int 2x e^{x^2}\,dx = \int e^{x^2} \cdot (2x\,dx) = \int e^u\,du.$$
Integrating the basic exponential function:
$$\int e^u\,du = e^u + C.$$
Back-substitute $u = x^2$:
$$F(x) = e^{x^2} + C, \quad C \in \mathbb{R}.$$
This represents the complete family of all possible antiderivatives.

### Step 3: Determine the constant $C$ using the condition $F(0) = 3$
We are given the initial condition:
$$F(0) = 3.$$
Substitute $x = 0$ into our general family formula:
$$F(0) = e^{0^2} + C = e^0 + C.$$
Since any non-zero number to the power of zero equals $1$, $e^0 = 1$:
$$1 + C = 3.$$
Subtract $1$ from both sides:
$$C = 3 - 1 = 2.$$

Substituting $C = 2$ back into the formula yields the unique function:
$$F(x) = e^{x^2} + 2.$$

### Step 4: Verify the result
We verify both conditions independently:
1. **Verification of the derivative condition ($F'(x) = 2xe^{x^2}$):**
   Differentiate $F(x) = e^{x^2} + 2$ with respect to $x$:
   $$F'(x) = \frac{d}{dx}\left(e^{x^2} + 2\right) = \frac{d}{dx}\left(e^{x^2}\right) + \frac{d}{dx}(2).$$
   Using the Chain Rule $\frac{d}{dx}(e^u) = e^u \frac{du}{dx}$:
   $$F'(x) = e^{x^2} \cdot \frac{d}{dx}(x^2) + 0 = e^{x^2} \cdot (2x) = 2x e^{x^2}.$$
   The derivative condition is satisfied.

2. **Verification of the initial condition ($F(0) = 3$):**
   Substitute $x = 0$ into $F(x)$:
   $$F(0) = e^{0^2} + 2 = e^0 + 2 = 1 + 2 = 3.$$
   The initial condition is satisfied.

Both conditions hold with absolute mathematical rigor.

---

## 5. Why Each Step Is Valid
- **Step 1:** By the Fundamental Theorem of Calculus, any function whose derivative is given can be recovered up to a constant by indefinite integration.
- **Step 2:** The Chain Rule reversal via substitution is valid because $x^2$ is differentiable on all of $\mathbb{R}$.
- **Step 3:** The initial condition supplies an equation in one unknown $C$ with a unique real solution.
- **Step 4:** Direct differentiation and substitution provide an unambiguous two-fold verification.

---

## 6. Final Answer in Words
1. The method needed is **$u$-substitution**, recognized because the derivative of the exponent $x^2$ is $2x$, which multiplies the exponential term.
2. The entire family of antiderivatives is:
   $$F(x) = e^{x^2} + C, \quad C \in \mathbb{R}.$$
3. Setting $F(0) = e^0 + C = 1 + C = 3$ gives $C = 2$, yielding the unique function:
   $$F(x) = e^{x^2} + 2.$$
4. Differentiating $e^{x^2} + 2$ produces $2xe^{x^2}$, and evaluating at $x = 0$ yields $e^0 + 2 = 3$, completely verifying both conditions.

---

## 7. Quick Verification
- Check at $x = 1$:
  $F(1) = e^1 + 2 = e + 2 \approx 4.718$.
  $F'(1) = 2(1)e^{1^2} = 2e \approx 5.436$.
- Tangent line at $(0, 3)$:
  $F'(0) = 2(0)e^0 = 0$.
  The graph has a horizontal tangent at $(0, 3)$ and curves upward as a minimum, matching $e^{x^2} + 2 \ge 3$.

---

## 8. Common Mistakes to Avoid
- **Assuming $e^0 = 0$:** Concluding that $F(0) = 0 + C = 3 \implies C = 3$. Remember that $e^0 = 1$, which makes $1 + C = 3 \implies C = 2$.
- **Integrating without substitution:** Writing $\frac{2x^2}{2} e^{x^2} = x^2 e^{x^2}$, which treats the integral of a product as the product of integrals (a fatal calculus error).
- **Omitting the constant $C$ initially:** Writing $F(x) = e^{x^2}$ and then wondering why $F(0) = 1 \neq 3$.

---

## 9. Classroom Presentation (3-Sentence Summary)
We recognize that finding $F(x)$ requires $u$-substitution with $u = x^2$ because its derivative $2x$ is present in the integrand, producing the general family $F(x) = e^{x^2} + C$. Applying the initial condition $F(0) = 3$ gives $e^0 + C = 1 + C = 3$, uniquely fixing the constant of integration to $C = 2$. Differentiating $F(x) = e^{x^2} + 2$ reproduces $2xe^{x^2}$ via the chain rule, and evaluating at zero gives $3$, verifying our solution completely.
