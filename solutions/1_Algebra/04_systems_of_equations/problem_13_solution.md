# Exercise 13: Does Every Equation Add New Information?

## 1. Original Problem
Consider the system:
$$x_1 + x_2 = 10, \qquad x_2 + x_3 = 8, \qquad x_1 - x_3 = 2$$
Solve it and check whether all three equations are independently necessary to describe the solution set. If one follows from the others, show this by calculation.

---

## 2. What We Are Trying to Find
We need to:
- Solve the system of 3 equations with 3 variables using elimination.
- Determine whether all three equations provide independent constraints or if one equation is mathematically redundant.
- If an equation is redundant, prove it explicitly by deriving it directly as a linear combination of the other two equations.
- Write down the complete solution set in parametric form.

---

## 3. Key Concepts and Theorems
1. **Linear Dependence of Equations (Redundancy):**
   An equation in a linear system is **redundant** (adds no new information) if it can be written as a linear combination of the remaining equations:
   $$\text{Eq}_3 = c_1 \text{Eq}_1 + c_2 \text{Eq}_2$$
2. **Dimension and Free Variables:**
   If a system of $n$ variables has $m$ equations, but one equation is redundant, the effective number of independent equations (the rank $r$) drops by $1$.
   If $r < n$, the solution set is not a single point, but an infinite family with $n - r$ degrees of freedom.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Check for Redundancy Algebraically
Let the three equations be:
$$\begin{cases} x_1 + x_2 = 10 & \text{(Equation 1)} \\ x_2 + x_3 = 8 & \text{(Equation 2)} \\ x_1 - x_3 = 2 & \text{(Equation 3)} \end{cases}$$

Notice the variable structure:
- Equation 1 contains $x_1$ and $x_2$.
- Equation 2 contains $x_2$ and $x_3$.
- If we subtract Equation 2 from Equation 1, the shared variable $x_2$ cancels out completely:
  $$\text{Left-hand side: } (x_1 + x_2) - (x_2 + x_3) = x_1 + x_2 - x_2 - x_3 = x_1 - x_3$$
  $$\text{Right-hand side: } 10 - 8 = 2$$
Combining the two sides gives:
$$x_1 - x_3 = 2$$
Notice that this resulting equation is **identically equal to Equation 3**!

**Formal Proof of Redundancy:**
$$\text{Equation 3} = \text{Equation 1} - \text{Equation 2}$$
Because Equation 3 is a direct consequence of Equations 1 and 2, it is **not independently necessary**. It provides zero new information about the variables $x_1, x_2, x_3$.

---

### Step 2: Set Up and Solve the Augmented Matrix
Write down the augmented matrix:
$$M_0 = \left(\begin{array}{ccc|c} 1 & 1 & 0 & 10 \\ 0 & 1 & 1 & 8 \\ 1 & 0 & -1 & 2 \end{array}\right)$$

Apply Gaussian elimination:
- Eliminate $x_1$ from Row 3 using Row 1 ($R_3 \leftarrow R_3 - R_1$):
  $$(1, 0, -1 \mid 2) - (1, 1, 0 \mid 10) = (1 - 1, 0 - 1, -1 - 0 \mid 2 - 10) = (0, -1, -1 \mid -8)$$

The matrix becomes:
$$M_1 = \left(\begin{array}{ccc|c} 1 & 1 & 0 & 10 \\ 0 & 1 & 1 & 8 \\ 0 & -1 & -1 & -8 \end{array}\right)$$

Now eliminate Row 3 using Row 2 ($R_3 \leftarrow R_3 + R_2$):
$$(0, -1, -1 \mid -8) + (0, 1, 1 \mid 8) = (0, 0, 0 \mid 0)$$

The matrix in row echelon form is:
$$M_2 = \left(\begin{array}{ccc|c} \mathbf{1} & 1 & 0 & 10 \\ 0 & \mathbf{1} & 1 & 8 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

The third row reduces completely to $0 = 0$, confirming algebraically that the third equation was redundant.

---

### Step 3: Write the Solution in Parametric Form
- Number of variables: $n = 3$.
- Number of pivots: $r = 2$ (in Columns 1 and 2).
- Number of free variables: $n - r = 3 - 2 = 1$ free variable (Column 3 has no pivot $\implies x_3$ is free).

Let $x_3 = t$, where $t \in \mathbb{R}$:
1. **From Row 2:**
   $$x_2 + x_3 = 8 \implies x_2 = 8 - t$$
2. **From Row 1:**
   $$x_1 + x_2 = 10 \implies x_1 = 10 - x_2 = 10 - (8 - t) = 2 + t$$

Collecting the solution in vector form:
$$\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 2 + t \\ 8 - t \\ t \end{pmatrix} = \begin{pmatrix} 2 \\ 8 \\ 0 \end{pmatrix} + t \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \qquad t \in \mathbb{R}$$
The system has **infinitely many solutions** forming a straight line in $\mathbb{R}^3$.

---

## 5. Why Each Step Is Valid
- **Linear Span Invariance:** $\operatorname{span}\{\text{Eq}_1, \text{Eq}_2, \text{Eq}_3\} = \operatorname{span}\{\text{Eq}_1, \text{Eq}_2\}$ because $\text{Eq}_3 = 1 \cdot \text{Eq}_1 - 1 \cdot \text{Eq}_2$. An equation lying in the span of other equations can be removed without changing the affine solution space.
- **Consistency of the Nullspace:** The rank of the coefficient matrix is $2 < 3$, guaranteeing by the rank-nullity theorem that the solution set is 1-dimensional.

---

## 6. Final Answer in Words
All three equations are not independently necessary to describe the solution set; Equation 3 is redundant because it follows directly from subtracting Equation 2 from Equation 1: $(x_1 + x_2 = 10) - (x_2 + x_3 = 8) \implies x_1 - x_3 = 2$. Eliminating this redundant equation leaves a system of rank 2 with one free variable, producing infinitely many solutions given by $x_1 = 2 + t$, $x_2 = 8 - t$, and $x_3 = t$ for all $t \in \mathbb{R}$.

---

## 7. Quick Verification
- **Test with parameter $t = 0$:**
  $\mathbf{x} = (2, 8, 0)$.
  - Eq 1: $2 + 8 = 10 \checkmark$
  - Eq 2: $8 + 0 = 8 \checkmark$
  - Eq 3: $2 - 0 = 2 \checkmark$
- **Test with parameter $t = 3$:**
  $\mathbf{x} = (5, 5, 3)$.
  - Eq 1: $5 + 5 = 10 \checkmark$
  - Eq 2: $5 + 3 = 8 \checkmark$
  - Eq 3: $5 - 3 = 2 \checkmark$
Both test points satisfy all three equations.

---

## 8. Common Mistakes to Avoid
- **Assuming 3 Equations with 3 Unknowns Always Yield 1 Solution:** Overlooking that equations can be linearly dependent, assuming a unique solution must exist.
- **Algebraic Sign Error in $x_1 = 10 - (8 - t)$:** Writing $10 - 8 - t = 2 - t$ instead of distributing the negative sign to get $2 + t$.
- **Not Showing the Calculation for Redundancy:** Stating that an equation is redundant without explicitly displaying the linear combination $(x_1 + x_2) - (x_2 + x_3) = 10 - 8 = 2$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"By subtracting the second equation from the first, we obtain $(x_1+x_2) - (x_2+x_3) = 10 - 8$, which simplifies exactly to $x_1 - x_3 = 2$, proving that the third equation is redundant and provides no new information. In the augmented matrix, this redundancy appears as a row of zeros, reducing the rank to 2 with one free variable. The system therefore has infinitely many solutions forming the line $\begin{pmatrix}2\\8\\0\end{pmatrix} + t\begin{pmatrix}1\\-1\\1\end{pmatrix}$."

