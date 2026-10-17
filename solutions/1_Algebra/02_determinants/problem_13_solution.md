# Exercise 13: Determinant by Elimination

## 1. Original Problem
Compute the determinant:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \\ 1 & 0 & 2 \end{pmatrix}$$
using elimination. Record the effect of every row operation used on the value of the determinant.

---

## 2. What We Are Trying to Find
We need to:
- Apply Gaussian elimination systematically to reduce matrix $A$ to an upper triangular matrix.
- Carefully record and justify the exact mathematical effect of every single row operation on the determinant's value.
- Compute the determinant directly from the product of the diagonal elements of the resulting triangular matrix.

---

## 3. Key Concepts and Theorems
1. **Gaussian Elimination for Determinants:**
   Any square matrix can be transformed into an upper triangular matrix $U$ using elementary row operations:
   - **Row replacement ($R_i \leftarrow R_i + cR_j$):** Determinant is **unchanged** ($\times 1$).
   - **Row swap ($R_i \leftrightarrow R_j$):** Determinant is **negated** ($\times (-1)$).
   - **Row scaling ($R_i \leftarrow cR_i$):** Determinant is **scaled** ($\times c$).
2. **Determinant of Echelon Form:**
   Once in upper triangular form $U$, the determinant of $U$ is:
   $$\det U = u_{11} \cdot u_{22} \cdots u_{nn}$$
   The original determinant is then recovered by accounting for any accumulated swap or scale factors.

---

## 4. Detailed Step-by-Step Solution

We start with the initial matrix:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \\ 1 & 0 & 2 \end{pmatrix}$$

---

### Step 1: Eliminate the First Entry of Row 2
Using the pivot $a_{11} = 1$, eliminate the entry in Row 2:
$$R_2 \leftarrow R_2 - 2R_1$$
- Row 2 calculation:
  $$(2, 5, 7) - 2(1, 2, 3) = (2 - 2, 5 - 4, 7 - 6) = (0, 1, 1)$$
- **Recorded Effect on Determinant:**
  This is a row addition. Adding a multiple of one row to another **leaves the determinant unchanged**:
  $$\det A^{(1)} = \det A$$

The matrix becomes:
$$A^{(1)} = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 1 & 0 & 2 \end{pmatrix}$$

---

### Step 2: Eliminate the First Entry of Row 3
Using the pivot $a_{11} = 1$, eliminate the entry in Row 3:
$$R_3 \leftarrow R_3 - R_1$$
- Row 3 calculation:
  $$(1, 0, 2) - (1, 2, 3) = (1 - 1, 0 - 2, 2 - 3) = (0, -2, -1)$$
- **Recorded Effect on Determinant:**
  This is a row addition. Adding a multiple of one row to another **leaves the determinant unchanged**:
  $$\det A^{(2)} = \det A^{(1)} = \det A$$

The matrix becomes:
$$A^{(2)} = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & -2 & -1 \end{pmatrix}$$

---

### Step 3: Eliminate the Second Entry of Row 3
Using the pivot $a_{22}^{(2)} = 1$, eliminate the entry $-2$ in Row 3:
$$R_3 \leftarrow R_3 + 2R_2$$
- Row 3 calculation:
  $$(0, -2, -1) + 2(0, 1, 1) = (0 + 0, -2 + 2, -1 + 2) = (0, 0, 1)$$
- **Recorded Effect on Determinant:**
  This is a row addition. It **leaves the determinant unchanged**:
  $$\det A^{(3)} = \det A^{(2)} = \det A$$

The matrix is now in **upper triangular form**:
$$A^{(3)} = \begin{pmatrix} \mathbf{1} & 2 & 3 \\ 0 & \mathbf{1} & 1 \\ 0 & 0 & \mathbf{1} \end{pmatrix}$$

---

### Step 4: Compute the Determinant
Since all three operations were row additions, no negative signs or scale factors were introduced:
$$\det A = \det A^{(3)}$$
Because $A^{(3)}$ is upper triangular, its determinant is the product of its main diagonal entries:
$$\det A = 1 \cdot 1 \cdot 1 = 1$$

---

## 5. Why Each Step Is Valid
- **Elementary Matrix Factorization:** We have $E_3 E_2 E_1 A = U$, where $E_1, E_2, E_3$ are lower unitriangular matrices representing the row operations. Because unitriangular matrices have all diagonal entries equal to $1$, $\det(E_i) = 1$ for all $i$.
- **Determinant Product Theorem:** $\det(U) = \det(E_3)\det(E_2)\det(E_1)\det(A) = 1 \cdot 1 \cdot 1 \cdot \det A = \det A$.

---

## 6. Final Answer in Words
Using Gaussian elimination, matrix $A$ is reduced to upper triangular form via three successive row operations: $R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - R_1$, and $R_3 \leftarrow R_3 + 2R_2$. Each of these operations adds a scalar multiple of one row to another, meaning none of them changes the determinant. The resulting upper triangular matrix has diagonal entries $1, 1, 1$, so the determinant is $1 \cdot 1 \cdot 1 = 1$.

---

## 7. Quick Verification
- **Verification via Sarrus' Rule on the original matrix $A$:**
  $$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 7 \\ 1 & 0 & 2 \end{pmatrix}$$
  - Downward diagonals:
    $$(1)(5)(2) + (2)(7)(1) + (3)(2)(0) = 10 + 14 + 0 = 24$$
  - Upward diagonals:
    $$(1)(5)(3) + (0)(7)(1) + (2)(2)(2) = 15 + 0 + 8 = 23$$
  - Combine:
    $$\det A = 24 - 23 = 1$$
  Both methods produce exactly $1$. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Unrecorded Sign Changes:** Swapping rows to make pivoting easier without multiplying by $-1$.
- **Arithmetic Error in $R_3 + 2R_2$:** Miscalculating $-1 + 2(1) = 1$ (for example, writing $-3$).
- **Dividing Rows by Leading Numbers:** Scaling a row to create a $1$ without noting that the determinant must be divided by that scalar factor.

---

## 9. Classroom Presentation (3-Sentence Summary)
"We perform Gaussian elimination by sequentially applying $R_2 - 2R_1$, $R_3 - R_1$, and $R_3 + 2R_2$ to clear the entries below the main diagonal. Because each step is a row addition, the determinant remains completely unchanged throughout the entire reduction. The resulting matrix is upper triangular with ones on the main diagonal, immediately giving a determinant of $1 \cdot 1 \cdot 1 = 1$."

