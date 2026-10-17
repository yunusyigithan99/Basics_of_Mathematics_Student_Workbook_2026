# Exercise 5: Row Operations and Determinants

## 1. Original Problem
For the matrix:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 0 \\ -1 & 4 & 2 \end{pmatrix}$$
find $\det A$ by simplifying the matrix with row operations. At each step, indicate whether and how the determinant changes.

---

## 2. What We Are Trying to Find
We need to:
- Transform matrix $A$ into an upper triangular matrix using elementary row operations.
- Explicitly state how each specific row operation affects (or leaves unchanged) the value of the determinant.
- Compute the final determinant by multiplying the diagonal entries of the resulting triangular matrix and accounting for any accumulated factors.

---

## 3. Key Concepts and Theorems
1. **Row Operations and Determinants:**
   - **Row Addition ($R_i \leftarrow R_i + cR_j$, $i \neq j$):** Adding a multiple of one row to another row **does not change** the determinant at all: $\det(\text{new}) = \det(\text{old})$.
   - **Row Swap ($R_i \leftrightarrow R_j$):** Interchanging two rows **multiplies the determinant by $-1$**: $\det(\text{new}) = -\det(\text{old})$.
   - **Row Scaling ($R_i \leftarrow cR_i$):** Multiplying a row by a scalar $c$ **multiplies the determinant by $c$**: $\det(\text{new}) = c \cdot \det(\text{old})$.
2. **Strategy:**
   Use row addition operations exclusively whenever possible, because row additions preserve the determinant value exactly without introducing negative signs or scalar factors.

---

## 4. Detailed Step-by-Step Solution

We start with:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 0 \\ -1 & 4 & 2 \end{pmatrix}$$

---

### Step 1: Eliminate the First Entry of Row 2
Perform the operation:
$$R_2 \leftarrow R_2 - 2R_1$$
- Row 2 calculation:
  $$(2, 1, 0) - 2(1, 2, 3) = (2 - 2, 1 - 4, 0 - 6) = (0, -3, -6)$$
- **Effect on Determinant:** Adding a multiple of one row to another row does not change the determinant.
  $$\det A^{(1)} = \det A$$

The matrix becomes:
$$A^{(1)} = \begin{pmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ -1 & 4 & 2 \end{pmatrix}$$

---

### Step 2: Eliminate the First Entry of Row 3
Perform the operation:
$$R_3 \leftarrow R_3 + R_1$$
- Row 3 calculation:
  $$(-1, 4, 2) + (1, 2, 3) = (-1 + 1, 4 + 2, 2 + 3) = (0, 6, 5)$$
- **Effect on Determinant:** Adding a multiple of one row to another row does not change the determinant.
  $$\det A^{(2)} = \det A^{(1)} = \det A$$

The matrix becomes:
$$A^{(2)} = \begin{pmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 0 & 6 & 5 \end{pmatrix}$$

---

### Step 3: Eliminate the Second Entry of Row 3
Notice that the second entry of Row 3 is $6$, while the pivot entry in Row 2 is $-3$. Since $6 + 2(-3) = 0$, perform:
$$R_3 \leftarrow R_3 + 2R_2$$
- Row 3 calculation:
  $$(0, 6, 5) + 2(0, -3, -6) = (0 + 0, 6 - 6, 5 - 12) = (0, 0, -7)$$
- **Effect on Determinant:** This is a row addition, so the determinant remains completely unchanged.
  $$\det A^{(3)} = \det A^{(2)} = \det A$$

The matrix is now in **upper triangular form**:
$$A^{(3)} = \begin{pmatrix} 1 & 2 & 3 \\ 0 & -3 & -6 \\ 0 & 0 & -7 \end{pmatrix}$$

---

### Step 4: Compute the Determinant from the Triangular Matrix
Because $A^{(3)}$ is upper triangular and all operations performed were row additions, the determinant is the product of its diagonal entries:
$$\det A = \det A^{(3)} = a_{11}^{(3)} \cdot a_{22}^{(3)} \cdot a_{33}^{(3)}$$
$$\det A = 1 \cdot (-3) \cdot (-7) = 21$$

---

## 5. Why Each Step Is Valid
- **Invariance under Shear Operations:** Geometrically, adding a multiple of one row vector to another shears the parallelotope along one of its faces without changing its height or base area; hence the oriented volume (determinant) is strictly invariant.
- **Triangular Diagonal Theorem:** Once in upper-triangular echelon form, every minor off the main diagonal is multiplied by a zero, leaving the product of the pivot elements as the exact determinant.

---

## 6. Final Answer in Words
By performing three successive row addition operations ($R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 + R_1$, and $R_3 \leftarrow R_3 + 2R_2$), none of which changes the value of the determinant, matrix $A$ is transformed into an upper triangular matrix with diagonal entries $1$, $-3$, and $-7$. The determinant is the product of these diagonal entries: $1 \cdot (-3) \cdot (-7) = 21$.

---

## 7. Quick Verification
- **Verification via Sarrus' Rule on the original matrix $A$:**
  $$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 1 & 0 \\ -1 & 4 & 2 \end{pmatrix}$$
  - Downward diagonals:
    $$(1)(1)(2) + (2)(0)(-1) + (3)(2)(4) = 2 + 0 + 24 = 26$$
  - Upward diagonals:
    $$(-1)(1)(3) + (4)(0)(1) + (2)(2)(2) = -3 + 0 + 8 = 5$$
  - Combine:
    $$\det A = 26 - 5 = 21$$
  Both methods produce exactly $21$. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Scaling a Row without Compensating:** Dividing Row 2 by $-3$ to get a pivot of $1$ without multiplying the outer determinant by $-3$ to balance the equation.
- **Arithmetic Error in $R_3 + 2R_2$:** Calculating $5 + 2(-6)$ as $5 - 12 = -7$; mistakes often happen with negative numbers (e.g., writing $+17$).
- **Swapping Rows without Tracking the Sign:** If a row swap is used, forgetting to introduce a negative sign factor.

---

## 9. Classroom Presentation (3-Sentence Summary)
"We reduce the matrix to upper triangular form using only row addition operations: $R_2 - 2R_1$, $R_3 + R_1$, and $R_3 + 2R_2$. Because adding a scalar multiple of one row to another preserves the determinant exactly, the determinant remains unchanged throughout the process. Multiplying the diagonal entries of the resulting triangular matrix gives $\det A = 1 \cdot (-3) \cdot (-7) = 21$."

