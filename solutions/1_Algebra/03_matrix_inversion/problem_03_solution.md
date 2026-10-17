# Exercise 3: When Does the Inverse Not Exist?

## 1. Original Problem
For the matrix:
$$A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$$
explain in two ways why $A^{-1}$ does not exist: using the determinant and using dependence between the rows.

---

## 2. What We Are Trying to Find
We need to:
- Demonstrate that the given matrix $A$ is non-invertible (singular).
- Provide the first justification using the algebraic condition of the determinant.
- Provide the second justification using the structural/geometric condition of linear dependence between the rows.
- Unify both explanations to show they are two perspectives on the exact same underlying mathematical failure.

---

## 3. Key Concepts and Theorems
1. **Invertibility Criterion via Determinant:**
   A square matrix $A$ is invertible if and only if $\det A \neq 0$.
   If $\det A = 0$, the inverse formula $A^{-1} = \frac{1}{\det A}\operatorname{adj}(A)$ requires dividing by zero, which is mathematically undefined.
2. **Invertibility Criterion via Linear Independence:**
   An $n \times n$ matrix is invertible if and only if its rows (and columns) are **linearly independent** (rank equals $n$).
   If the rows are linearly dependent, the matrix has rank strictly less than $n$ and collapses the dimension of the space, destroying injectivity.

---

## 4. Detailed Step-by-Step Solution

### Method 1: Explanation Using the Determinant
For matrix $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, compute its determinant using the $ad - bc$ rule:
$$\det A = (2 \cdot 2) - (4 \cdot 1) = 4 - 4 = 0$$

- **Why this proves non-invertibility:**
  Suppose for contradiction that an inverse matrix $A^{-1}$ exists. Then by the fundamental product property of determinants:
  $$\det(A \cdot A^{-1}) = \det(I)$$
  $$\det(A) \cdot \det(A^{-1}) = 1$$
  Substituting $\det A = 0$ gives:
  $$0 \cdot \det(A^{-1}) = 1$$
  Because $0 \cdot c = 0$ for all real numbers $c$, no such value $\det(A^{-1})$ can exist. This contradiction proves that $A^{-1}$ cannot exist.

---

### Method 2: Explanation Using Dependence Between Rows
Examine the two rows of matrix $A$:
- Row 1: $R_1 = (2, 4)$
- Row 2: $R_2 = (1, 2)$

Notice the ratio between corresponding entries:
$$\frac{2}{1} = 2, \qquad \frac{4}{2} = 2$$
Row 1 is exactly twice Row 2:
$$R_1 = 2 R_2 \quad \iff \quad R_1 - 2 R_2 = \mathbf{0}$$

- **Why this proves non-invertibility:**
  Because the rows are scalar multiples of each other, they are **linearly dependent**.
  - The rows do not span a 2-dimensional space; their span is merely a 1-dimensional line in $\mathbb{R}^2$ along the vector $(1, 2)$.
  - Consequently, the rank of $A$ is $\operatorname{rank}(A) = 1 < 2$.
  - Geometrically, matrix $A$ compresses the entire 2D plane onto the single line $y = \frac{1}{2}x$.
  - Any transformation that collapses 2D space into a 1D line maps infinitely many distinct input vectors to the exact same output vector (it is not one-to-one/injective). For example:
    $$A \begin{pmatrix} -2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(-2) + 4(1) \\ 1(-2) + 2(1) \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} = A \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
  Because two different points map to $(0, 0)$, the transformation cannot be reversed uniquely. Hence, $A^{-1}$ cannot exist.

---

## 5. Why Each Step Is Valid
- **The Invertible Matrix Theorem:** A matrix has full rank $\iff$ its rows are independent $\iff \det \neq 0 \iff$ it is a bijective linear operator $\iff$ its inverse exists. Failure of any one condition implies failure of all.
- **Kernel Non-Triviality:** A row relationship $R_1 - 2R_2 = \mathbf{0}$ directly yields a non-zero nullspace vector $\mathbf{v} = (-2, 1)^T$ such that $A\mathbf{v} = \mathbf{0}$, which mathematically precludes injectivity.

---

## 6. Final Answer in Words
The inverse $A^{-1}$ does not exist for two interconnected reasons:
1. **Determinant view:** The determinant is $\det A = 2(2) - 4(1) = 0$. Since matrix inversion requires dividing by the determinant, a zero determinant makes inversion impossible.
2. **Row dependence view:** The first row is an exact multiple of the second row ($R_1 = 2R_2$), meaning the rows are linearly dependent. This reduces the rank of the matrix to $1$, collapsing the plane onto a single line and preventing the transformation from being reversed.

---

## 7. Quick Verification
- **Gauss-Jordan test:**
  $$\begin{pmatrix} 2 & 4 & \mid & 1 & 0 \\ 1 & 2 & \mid & 0 & 1 \end{pmatrix} \xrightarrow{R_1 - 2R_2} \begin{pmatrix} 0 & 0 & \mid & 1 & -2 \\ 1 & 2 & \mid & 0 & 1 \end{pmatrix}$$
  A row of zeros appears on the left side, proving it is impossible to form the identity matrix $I$. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Treating the Two Reasons as Unrelated:** Failing to see that the determinant is zero precisely *because* the rows are dependent.
- **Confusing Row Dependence with Column Dependence:** The columns are also dependent: Column 2 is twice Column 1 ($C_2 = 2C_1$). The prompt specifically asks about rows.
- **Saying the Matrix Has "No Solution":** A matrix itself does not have "solutions"; it is either invertible or singular.

---

## 9. Classroom Presentation (3-Sentence Summary)
"First, computing the determinant gives $2(2) - 4(1) = 0$, which immediately rules out an inverse because the inversion formula requires dividing by the determinant. Second, looking at the rows reveals that Row 1 is exactly twice Row 2, meaning the rows are linearly dependent and span only a 1-dimensional line. Because the transformation squashes the entire 2D plane onto a single line, it is not one-to-one and cannot be reversed."

