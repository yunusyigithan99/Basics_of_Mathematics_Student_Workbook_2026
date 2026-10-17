# Exercise 10: A Polynomial Through Three Points

## 1. Original Problem
Find a polynomial:
$$p(x) = ax^2 + bx + c$$
whose graph passes through $(0, 1)$, $(1, 3)$, and $(2, 9)$. Reduce the problem to a system of equations and check the result by substituting all three points.

---

## 2. What We Are Trying to Find
We need to:
- Translate the condition that a parabola passes through three specified Cartesian points into a system of 3 linear equations for the unknown polynomial coefficients $a, b, c$.
- Solve the resulting system systematically.
- State the explicit quadratic polynomial $p(x)$.
- Verify the solution by evaluating $p(0)$, $p(1)$, and $p(2)$ to show that all three target points lie precisely on the curve.

---

## 3. Key Concepts and Theorems
1. **Polynomial Interpolation:**
   A point $(x_k, y_k)$ lies on the curve $y = p(x)$ if and only if $p(x_k) = y_k$.
   For a degree-2 polynomial $p(x) = ax^2 + bx + c$, evaluating at three distinct points $x_1, x_2, x_3$ generates a linear system in the unknowns $a, b, c$:
   $$\begin{pmatrix} x_1^2 & x_1 & 1 \\ x_2^2 & x_2 & 1 \\ x_3^2 & x_3 & 1 \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix} = \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix}$$
2. **Vandermonde Theorem:**
   The coefficient matrix is a **Vandermonde matrix**. Because the $x$-coordinates ($0, 1, 2$) are distinct, the Vandermonde determinant is non-zero, guaranteeing that there is a unique quadratic polynomial passing through any three non-collinear points.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the System of Equations
Evaluate $p(x) = ax^2 + bx + c$ at each of the three given points:

1. **Point $(0, 1)$:**
   $$p(0) = a(0)^2 + b(0) + c = 1 \implies c = 1$$
   *Immediate result:* The constant term is directly determined: $c = 1$.

2. **Point $(1, 3)$:**
   $$p(1) = a(1)^2 + b(1) + c = 3 \implies a + b + c = 3$$
   Substitute $c = 1$:
   $$a + b + 1 = 3 \implies a + b = 2 \quad \text{(Equation A)}$$

3. **Point $(2, 9)$:**
   $$p(2) = a(2)^2 + b(2) + c = 9 \implies 4a + 2b + c = 9$$
   Substitute $c = 1$:
   $$4a + 2b + 1 = 9 \implies 4a + 2b = 8$$
   Divide by $2$ to simplify:
   $$2a + b = 4 \quad \text{(Equation B)}$$

---

### Step 2: Solve the Linear System for $a$ and $b$
We now have a simple $2 \times 2$ system for $a$ and $b$:
$$\begin{cases} a + b = 2 & \text{(Equation A)} \\ 2a + b = 4 & \text{(Equation B)} \end{cases}$$

- **Eliminate $b$:**
  Subtract Equation A from Equation B:
  $$(2a + b) - (a + b) = 4 - 2$$
  $$a = 2$$

- **Solve for $b$:**
  Substitute $a = 2$ into Equation A:
  $$2 + b = 2 \implies b = 2 - 2 = 0$$

We have found all three coefficients:
$$a = 2, \qquad b = 0, \qquad c = 1$$

---

### Step 3: Write Down the Polynomial
Substitute the coefficients into $p(x) = ax^2 + bx + c$:
$$p(x) = 2x^2 + 0x + 1 \implies p(x) = 2x^2 + 1$$

---

### Step 4: Check by Substituting All Three Points
1. **Check Point $(0, 1)$:**
   $$p(0) = 2(0)^2 + 1 = 0 + 1 = 1 \quad \implies (0, 1) \text{ is on the graph} \quad \checkmark$$
2. **Check Point $(1, 3)$:**
   $$p(1) = 2(1)^2 + 1 = 2(1) + 1 = 3 \quad \implies (1, 3) \text{ is on the graph} \quad \checkmark$$
3. **Check Point $(2, 9)$:**
   $$p(2) = 2(2)^2 + 1 = 2(4) + 1 = 8 + 1 = 9 \quad \implies (2, 9) \text{ is on the graph} \quad \checkmark$$

All three points match the polynomial curve exactly.

---

## 5. Why Each Step Is Valid
- **Point-Curve Incidence Definition:** A point belongs to the graph of a function if and only if its coordinates satisfy the defining formula.
- **Vandermonde Determinant Invertibility:** For distinct nodes $x_0=0, x_1=1, x_2=2$, the determinant is $\prod_{i>j} (x_i - x_j) = (1-0)(2-0)(2-1) = 2 \neq 0$, ensuring unique solvability.

---

## 6. Final Answer in Words
The problem reduces to the linear system $c = 1$, $a + b = 2$, and $2a + b = 4$. Solving this system yields the coefficients $a = 2$, $b = 0$, and $c = 1$. The required polynomial is $p(x) = 2x^2 + 1$. Substituting the inputs $x = 0, 1, 2$ returns $1, 3, 9$, verifying that the graph passes through all three points.

---

## 7. Quick Verification
- **Second difference calculus check:**
  - $y$-values for evenly spaced $x = 0, 1, 2$: $y = (1, 3, 9)$.
  - First differences: $\Delta y = (3 - 1, 9 - 3) = (2, 6)$.
  - Second difference: $\Delta^2 y = 6 - 2 = 4$.
  - In quadratic polynomials, the second difference equals $2a \cdot (\Delta x)^2 = 2a(1)^2 = 2a$.
  - $2a = 4 \implies a = 2$.
  - Matches $a = 2$ perfectly! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Treating $x$ as Unknown Instead of $a, b, c$:** Confusing the roles of variables: in curve fitting, $x$ and $y$ are known constants, while the coefficients $a, b, c$ are the unknowns to solve for.
- **Forgetting $x^2$ at $x=2$:** Computing $a(2) + b(2) + c$ instead of $a(2^2) = 4a$.
- **Assuming $b$ Cannot Be Zero:** Hesitating when $b = 0$ is obtained; a quadratic polynomial can have an axis of symmetry along the $y$-axis where the linear term vanishes.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Substituting the three points into $p(x) = ax^2 + bx + c$ yields the linear equations $c = 1$, $a + b = 2$, and $4a + 2b = 8$. Subtracting the equations immediately isolates $a = 2$ and $b = 0$, giving the quadratic polynomial $p(x) = 2x^2 + 1$. Evaluating this polynomial at $x = 0, 1, 2$ produces $1, 3, 9$, confirming that it passes exactly through all three given coordinates."

