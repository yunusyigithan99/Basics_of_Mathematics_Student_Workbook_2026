# Exercise 1: From a System to a Matrix

## 1. Original Problem
Write the system:
$$\begin{cases} 2x - y + z = 4 \\ x + 3y - 2z = 1 \\ 3x + y + z = 7 \end{cases}$$
in the form $Ax = b$.
Identify the coefficient matrix, the vector of unknowns, and the right-hand side vector. Explain how each row of the matrix corresponds to one equation.

---

## 2. What We Are Trying to Find
We need to:
- Convert the given system of 3 linear equations in 3 variables into the compact matrix-vector equation $Ax = b$.
- Explicitly identify and write down:
  - The coefficient matrix $A$,
  - The vector of unknowns $\mathbf{x}$,
  - The right-hand side constant vector $\mathbf{b}$.
- Explain the row-by-vector multiplication mechanism that connects each row of $A$ to an equation in the system.

---

## 3. Key Concepts and Theorems
1. **Matrix Form of a Linear System:**
   Any system of $m$ linear equations in $n$ unknowns:
   $$\sum_{j=1}^n a_{ij} x_j = b_i \quad (i = 1, \dots, m)$$
   can be written compactly as:
   $$A\mathbf{x} = \mathbf{b}$$
   where:
   - $A \in \mathbb{R}^{m \times n}$ is the **coefficient matrix** containing the scalar coefficients of the variables.
   - $\mathbf{x} \in \mathbb{R}^{n \times 1}$ is the **vector of unknowns**.
   - $\mathbf{b} \in \mathbb{R}^{m \times 1}$ is the **right-hand side vector** of constants.
2. **Row Interpretation of Matrix Multiplication:**
   The $i$-th entry of the product vector $A\mathbf{x}$ is the dot product of the $i$-th row of $A$ with $\mathbf{x}$:
   $$(A\mathbf{x})_i = (\text{Row } i \text{ of } A) \cdot \mathbf{x} = a_{i1}x_1 + a_{i2}x_2 + \dots + a_{in}x_n$$
   Setting $(A\mathbf{x})_i = b_i$ exactly reproduces the $i$-th equation.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Align the System by Variables
Write the equations with variables $x, y, z$ in strict column alignment:
$$\begin{array}{rrrrrcc}
2x & - & 1y & + & 1z & = & 4 \\
1x & + & 3y & - & 2z & = & 1 \\
3x & + & 1y & + & 1z & = & 7
\end{array}$$

---

### Step 2: Extract the Components
- **The coefficient matrix $A$ ($3 \times 3$):**
  Collect the numbers multiplying $x, y, z$ row by row:
  $$A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix}$$

- **The vector of unknowns $\mathbf{x}$ ($3 \times 1$):**
  List the variable symbols vertically:
  $$\mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$$

- **The right-hand side vector $\mathbf{b}$ ($3 \times 1$):**
  Collect the constants from the right-hand side of the equals signs:
  $$\mathbf{b} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}$$

---

### Step 3: Write the Complete Matrix Equation $A\mathbf{x} = \mathbf{b}$
$$\begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}$$

---

### Step 4: Explain How Each Row Corresponds to One Equation
When we carry out the standard row-by-column matrix multiplication $A\mathbf{x}$:
1. **Row 1 $\cdot \mathbf{x}$:**
   $$\begin{pmatrix} 2 & -1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 2(x) + (-1)(y) + 1(z) = 2x - y + z$$
   Equating this to the first entry of $\mathbf{b}$ gives:
   $$2x - y + z = 4 \quad \text{(Equation 1)}$$

2. **Row 2 $\cdot \mathbf{x}$:**
   $$\begin{pmatrix} 1 & 3 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 1(x) + 3(y) + (-2)(z) = x + 3y - 2z$$
   Equating this to the second entry of $\mathbf{b}$ gives:
   $$x + 3y - 2z = 1 \quad \text{(Equation 2)}$$

3. **Row 3 $\cdot \mathbf{x}$:**
   $$\begin{pmatrix} 3 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 3(x) + 1(y) + 1(z) = 3x + y + z$$
   Equating this to the third entry of $\mathbf{b}$ gives:
   $$3x + y + z = 7 \quad \text{(Equation 3)}$$

Each row of matrix $A$ acts as a linear weighting functional that pairs each variable with its coefficient, while the corresponding entry in $\mathbf{b}$ specifies the required target value.

---

## 5. Why Each Step Is Valid
- **Bilinear Mapping Correspondence:** The algebraic system is a system of linear affine functionals on $\mathbb{R}^3$. Representing them as rows of a matrix is the canonical coordinate representation of a linear map $T: \mathbb{R}^3 \to \mathbb{R}^3$.
- **Index Preservation:** Variable positions in $\mathbf{x}$ correspond strictly to column indices in $A$, ensuring coefficients always multiply the correct variable.

---

## 6. Final Answer in Words
The matrix equation is $\begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}$. The coefficient matrix is $A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix}$, the vector of unknowns is $\mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$, and the right-hand side vector is $\mathbf{b} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}$. Each row of $A$ corresponds to one equation because computing the dot product of row $i$ with $\mathbf{x}$ expands to the left-hand side of the $i$-th linear equation, which equals $b_i$.

---

## 7. Quick Verification
- Compute $A\mathbf{x}$ directly:
  $$A\mathbf{x} = \begin{pmatrix} 2x - y + z \\ x + 3y - 2z \\ 3x + y + z \end{pmatrix}$$
  Setting this equal to $\mathbf{b} = \begin{pmatrix} 4 \\ 1 \\ 7 \end{pmatrix}$ yields the exact three original equations line for line. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Writing $\mathbf{x}$ or $\mathbf{b}$ as Row Vectors:** Writing $\mathbf{x} = (x, y, z)$ horizontally. In $Ax = b$, $\mathbf{x}$ and $\mathbf{b}$ must be column vectors ($3 \times 1$).
- **Missing Signs on Negative Coefficients:** Writing $+1$ for the coefficient of $-y$ instead of $-1$.
- **Omitting Variables with Coefficient 1:** Forgetting that an implicit $+z$ means the entry is $+1$, not $0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"We extract the coefficients of $x, y, z$ to form the $3 \times 3$ matrix $A$, place the variables in the column vector $\mathbf{x}$, and put the constants in the right-hand vector $\mathbf{b}$ to write $A\mathbf{x} = \mathbf{b}$. Each row of matrix $A$ represents one equation because the row-by-vector dot product computes the sum of the coefficients times the variables. Setting each row dot product equal to the matching entry in $\mathbf{b}$ exactly recovers the original three equations."

