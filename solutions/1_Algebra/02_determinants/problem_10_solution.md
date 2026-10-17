# Exercise 10: Detecting Dependence

## 1. Original Problem
Without carrying out a full determinant calculation, explain why:
$$\det\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 5 \end{pmatrix} = 0$$
Identify a specific dependence between the rows and connect it with noninvertibility of the matrix.

---

## 2. What We Are Trying to Find
We need to:
- Explain why the given $3 \times 3$ determinant is zero by inspecting the internal relationships between its rows, without performing Sarrus' rule or Laplace expansion.
- Pinpoint the exact algebraic relationship (linear dependence) connecting the rows.
- Connect this linear dependence directly to the concept of matrix non-invertibility (singularity) and geometric dimension collapse.

---

## 3. Key Concepts and Theorems
1. **Linear Dependence of Rows Theorem:**
   If one row of a matrix is a scalar multiple of another row (or a linear combination of other rows), the rows are **linearly dependent**.
2. **Determinant of Dependent Rows:**
   A square matrix has a determinant equal to zero if and only if its rows (or columns) are linearly dependent:
   $$\det M = 0 \iff \text{rows of } M \text{ are linearly dependent}$$
3. **Invertibility and Rank:**
   - For an $n \times n$ matrix to be invertible, its rows must form a basis of $\mathbb{R}^n$ (full rank $n$).
   - If rows are dependent, the rank is strictly less than $n$, meaning the linear map squashes $\mathbb{R}^n$ into a lower-dimensional subspace.
   - A transformation that loses dimension cannot be inverted (it is not bijective).

---

## 4. Detailed Step-by-Step Solution

### Step 1: Inspect the Rows of the Matrix
Label the rows of the matrix:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 5 \end{pmatrix}$$
- Row 1: $R_1 = (1, 2, 3)$
- Row 2: $R_2 = (2, 4, 6)$
- Row 3: $R_3 = (0, 1, 5)$

---

### Step 2: Identify the Specific Dependence
Compare Row 1 and Row 2 entry-by-entry:
- First entry: $\frac{2}{1} = 2$
- Second entry: $\frac{4}{2} = 2$
- Third entry: $\frac{6}{3} = 2$

Every entry of Row 2 is exactly twice the corresponding entry of Row 1.
Thus, the specific dependence relation is:
$$R_2 = 2 R_1 \quad \iff \quad R_2 - 2 R_1 = \mathbf{0}$$

---

### Step 3: Explain Why the Determinant Must Be Zero
By the linearity of determinants with respect to rows:
- We can perform the row operation $R_2 \leftarrow R_2 - 2R_1$.
- This row operation **does not change** the determinant:
  $$\det A = \det\begin{pmatrix} 1 & 2 & 3 \\ 2 - 2(1) & 4 - 2(2) & 6 - 2(3) \\ 0 & 1 & 5 \end{pmatrix} = \det\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 1 & 5 \end{pmatrix}$$
- Because the resulting matrix has an **entire row of zeros** ($R_2 = (0, 0, 0)$), expanding along that row immediately yields:
  $$\det A = 0 \cdot C_{21} + 0 \cdot C_{22} + 0 \cdot C_{23} = 0$$

---

### Step 4: Connect Linear Dependence with Non-Invertibility
1. **Rank and Dimension:** Since Row 2 provides no new directional information beyond Row 1, the three rows span at most a 2-dimensional plane in $\mathbb{R}^3$, so $\operatorname{rank}(A) \le 2 < 3$.
2. **Loss of Injectivity:** Because the rows are dependent, there exists a non-zero vector $\mathbf{v}$ such that $\mathbf{v}^T A = \mathbf{0}$, meaning multiple input vectors are mapped to the exact same output vector (for example, $A\mathbf{x} = \mathbf{0}$ has non-trivial solutions).
3. **Impossibility of Inversion:** A function that maps distinct inputs to the same output cannot be reversed. Furthermore, the algebraic formula for the inverse requires dividing by $\det A$ ($A^{-1} = \frac{1}{\det A}\operatorname{adj}(A)$). Since $\det A = 0$, division by zero is undefined, and $A^{-1}$ cannot exist.

---

## 5. Why Each Step Is Valid
- **Alternating Tensor Axiom:** Any multilinear alternating form evaluates to zero if two arguments are linearly dependent.
- **Fundamental Theorem of Invertible Matrices:** An $n \times n$ matrix is invertible $\iff \operatorname{rank} = n \iff \det \neq 0 \iff$ rows are linearly independent. Breaking any of these breaks all of them simultaneously.

---

## 6. Final Answer in Words
The determinant is zero without any full calculation because the second row is an exact scalar multiple of the first row ($R_2 = 2R_1$). Performing the row operation $R_2 - 2R_1$ produces a row of zeros, making the determinant zero. This linear dependence reduces the matrix rank below $3$, collapsing 3D space into a 2D plane, which makes the transformation non-injective and therefore non-invertible.

---

## 7. Quick Verification
- **Quick Sarrus verification:**
  - Downward diagonals: $(1)(4)(5) + (2)(6)(0) + (3)(2)(1) = 20 + 0 + 6 = 26$.
  - Upward diagonals: $(0)(4)(3) + (1)(6)(1) + (5)(2)(2) = 0 + 6 + 20 = 26$.
  - $\det = 26 - 26 = 0$. Confirmed! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Performing Sarrus or Expansion First:** Doing the full arithmetic computation when the problem explicitly says *"Without carrying out a full determinant calculation"*.
- **Looking Only at Adjacent Entries:** Trying to compare entries horizontally within a row rather than comparing matching coordinates vertically across different rows.
- **Vague Statements of Dependence:** Saying "the numbers look related" instead of writing the precise mathematical equation $R_2 = 2R_1$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Without computing the full determinant, we can see immediately that the second row is exactly twice the first row: $R_2 = 2R_1$. Subtracting $2R_1$ from $R_2$ produces a row of zeros without changing the determinant, which immediately proves that $\det A = 0$. Because the rows are linearly dependent, the matrix has rank less than 3 and collapses space, which prevents the matrix from being invertible."

