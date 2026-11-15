# Problem 01: Antiderivative, Family of Solutions, and Verification

## 1. Original Problem
For
$$f(x) = 3x^2 - 4x + 5$$
find one antiderivative $F(x)$. Write the entire family of antiderivatives, verify the result by differentiation, and explain the meaning of the constant $C$.

---

## 2. What We Are Trying to Find
1. A specific antiderivative $F(x)$ such that $F'(x) = f(x)$.
2. The general indefinite integral (the full family of antiderivatives) containing an arbitrary constant $C \in \mathbb{R}$.
3. Rigorous verification that differentiating the general antiderivative reproduces $f(x)$.
4. A clear conceptual and geometric explanation of the constant of integration $C$.

---

## 3. Key Concepts and Theorems
1. **Definition of an Antiderivative:**
   A differentiable function $F(x)$ is an antiderivative (primitive function) of $f(x)$ on an interval $I$ if $F'(x) = f(x)$ for all $x \in I$.
2. **Indefinite Integral and the Constant $C$:**
   If $F(x)$ is an antiderivative of $f(x)$, then any other antiderivative differs from $F(x)$ by a constant:
   $$\int f(x)\,dx = F(x) + C, \quad C \in \mathbb{R}.$$
   This follows from the Mean Value Theorem: if two functions have the same derivative on an interval, their difference has zero derivative, hence their difference is a constant.
3. **Power Rule for Integration:**
   For any real exponent $n \neq -1$:
   $$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C.$$
4. **Linearity of the Integral:**
   $$\int [a \cdot g(x) + b \cdot h(x)]\,dx = a \int g(x)\,dx + b \int h(x)\,dx.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Find one specific antiderivative $F(x)$
We integrate the polynomial $f(x) = 3x^2 - 4x + 5$ term by term using the power rule:
- For $3x^2$:
  $$\int 3x^2\,dx = 3 \cdot \frac{x^{2+1}}{2+1} = 3 \cdot \frac{x^3}{3} = x^3.$$
- For $-4x = -4x^1$:
  $$\int (-4x)\,dx = -4 \cdot \frac{x^{1+1}}{1+1} = -4 \cdot \frac{x^2}{2} = -2x^2.$$
- For $5 = 5x^0$:
  $$\int 5\,dx = 5x.$$

Choosing the integration constant to be $0$, one specific antiderivative is:
$$F(x) = x^3 - 2x^2 + 5x.$$

### Step 2: Write the entire family of antiderivatives
Because any constant disappears upon differentiation, the most general antiderivative (the indefinite integral) is given by adding an arbitrary real constant $C$:
$$\int (3x^2 - 4x + 5)\,dx = x^3 - 2x^2 + 5x + C, \quad C \in \mathbb{R}.$$

### Step 3: Verify the result by differentiation
We differentiate our general antiderivative candidate $F(x) + C$ with respect to $x$:
$$\frac{d}{dx}\left(x^3 - 2x^2 + 5x + C\right) = \frac{d}{dx}(x^3) - \frac{d}{dx}(2x^2) + \frac{d}{dx}(5x) + \frac{d}{dx}(C).$$
Applying standard differentiation rules:
- $\frac{d}{dx}(x^3) = 3x^2$.
- $\frac{d}{dx}(2x^2) = 2(2x) = 4x$.
- $\frac{d}{dx}(5x) = 5$.
- $\frac{d}{dx}(C) = 0$ (the derivative of any constant is zero).

Adding these together:
$$F'(x) = 3x^2 - 4x + 5 = f(x).$$
The derivative identically matches the original function $f(x)$, verifying the calculation.

### Step 4: Explain the meaning of the constant $C$
1. **Algebraic meaning:** 
   Differentiation is an operation with a non-trivial kernel: the derivative of any constant is zero ($\frac{d}{dx}(C) = 0$). When we reverse differentiation (integrate), we cannot determine what constant was originally present. Hence, integration produces an infinite set (family) of functions, parameterized by $C \in \mathbb{R}$.
2. **Geometric meaning:**
   The parameter $C$ corresponds to a pure **vertical translation (shift)** of the graph. For any two members of the family $F_1(x) = F(x) + C_1$ and $F_2(x) = F(x) + C_2$, the curves are parallel vertically. At any chosen $x$-coordinate, the tangent lines to both curves have the exact same slope: $F_1'(x) = F_2'(x) = f(x)$. To select one specific curve from this infinite family, an additional piece of information (such as an initial value or point on the graph) is required.

---

## 5. Why Each Step Is Valid
- **Step 1:** By linearity, the integral of a sum is the sum of integrals, and the power rule applies to each monomial term.
- **Step 2:** By Corollaries of the Mean Value Theorem, if two functions have identical derivatives on a connected interval, they differ by a constant.
- **Step 3:** Differentiation is the inverse operation to indefinite integration; $\frac{d}{dx}\int f(x)\,dx = f(x)$.
- **Step 4:** Shifting a graph vertically does not alter its slope at any $x$.

---

## 6. Final Answer in Words
One specific antiderivative of $f(x) = 3x^2 - 4x + 5$ is $F(x) = x^3 - 2x^2 + 5x$. 
The entire family of antiderivatives is $F(x) + C = x^3 - 2x^2 + 5x + C$, where $C \in \mathbb{R}$ is an arbitrary constant of integration. 
Differentiating $x^3 - 2x^2 + 5x + C$ yields $3x^2 - 4x + 5 + 0 = f(x)$, verifying the result. 
The constant $C$ represents an arbitrary vertical translation of the curve: because vertical shifts do not change the slope of tangent lines, every member of this family shares the exact same derivative $f(x)$ at every point.

---

## 7. Quick Verification
Pick $C = 7$. Then $H(x) = x^3 - 2x^2 + 5x + 7$.
$H'(x) = 3x^2 - 4x + 5$.
At $x = 1$: $f(1) = 3(1) - 4(1) + 5 = 4$.
$H'(1) = 3(1) - 4 + 5 = 4$.
Matches perfectly.

---

## 8. Common Mistakes to Avoid
- **Omitting $+ C$:** Treating indefinite integration as yielding a single function rather than an infinite family of antiderivatives.
- **Differentiating instead of integrating:** Accidentally computing $f'(x) = 6x - 4$ instead of $\int f(x)\,dx$.
- **Incorrect power rule denominator:** Writing $3 \cdot \frac{x^3}{2}$ instead of dividing by the new exponent ($3$).

---

## 9. Classroom Presentation (3-Sentence Summary)
Using the power rule for integration, we find a specific antiderivative of $f(x) = 3x^2 - 4x + 5$ to be $F(x) = x^3 - 2x^2 + 5x$. The full indefinite integral includes an arbitrary constant $C$, giving the family $x^3 - 2x^2 + 5x + C$, which we verify by differentiating back to $3x^2 - 4x + 5$. Geometrically, the constant $C$ represents vertical translations of the curve that leave tangent line slopes unchanged.
