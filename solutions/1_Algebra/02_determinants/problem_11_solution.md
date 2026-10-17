# Exercise 11: Shortening the Calculation with Row Operations

## 1. Original Problem
Compute:
$$\det\begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 4 \\ 1 & 4 & 6 \end{pmatrix}$$
by first performing row operations that create as many zeros as possible. State which operations do not change the determinant.

---

## 2. What We Are Trying to Find
We need to:
- Use strategically planned elementary row operations to introduce leading zeros into the first column of the matrix.
- Clearly identify and state which row operations leave the determinant completely unchanged.
- Continue row operations to transform the matrix into upper triangular form (or expand along a column with zeros).
- Compute the final determinant easily from the simplified matrix.

---

## 3. Key Concepts and Theorems
1. **Determinant-Preserving Operations:**
   Adding a scalar multiple of one row to another row:
   $$R_i \leftarrow R_i + cR_j \quad (i \neq j)$$
   **does not change** the value of the determinant:
   $$\det(\text{new matrix}) = \det(\text{original matrix})$$
   Because all three entries in the first column are equal to $1$, subtracting Row 1 from Row 2 and from Row 3 immediately creates two zeros in the first column at zero computational cost to the determinant.
2. **Determinant of an Upper Triangular Matrix:**
   Once in echelon form, the determinant equals the product of the main diagonal elements:
   $$\det = d_1 \cdot d_2 \cdots d_n$$

---

## 4. Detailed Step-by-Step Solution

We begin with matrix:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 4 \\ 1 & 4 & 6 \end{pmatrix}$$

---

### Step 1: Create Zeros in Column 1
Notice that the pivot in entry $(1, 1)$ is $1$, and the entries below it are also $1$.
Perform the following two row operations:
1. $R_2 \leftarrow R_2 - R_1$
2. $R_3 \leftarrow R_3 - R_1$

- **Calculation for Row 2:**
  $$(1, 3, 4) - (1, 2, 3) = (1 - 1, 3 - 2, 4 - 3) = (0, 1, 1)$$
- **Calculation for Row 3:**
  $$(1, 4, 6) - (1, 2, 3) = (1 - 1, 4 - 2, 6 - 3) = (0, 2, 3)$$

- **Statement on Determinants:**
  Both operations are row additions (adding $-1$ times $R_1$), so **neither operation changes the determinant**:
  $$\det A = \det\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 2 & 3 \end{pmatrix}$$

---

### Step 2: Eliminate the Remaining Non-Zero Entry Below the Pivot
The matrix is now:
$$A^{(1)} = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 2 & 3 \end{pmatrix}$$
To eliminate the $2$ in entry $(3, 2)$, use the pivot in Row 2:
$$R_3 \leftarrow R_3 - 2R_2$$

- **Calculation for Row 3:**
  $$(0, 2, 3) - 2(0, 1, 1) = (0 - 0, 2 - 2, 3 - 2) = (0, 0, 1)$$

- **Statement on Determinants:**
  This is also a row addition (adding $-2$ times $R_2$), so **it does not change the determinant**:
  $$\det A = \det\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$

---

### Step 3: Compute the Determinant
The matrix is now in **upper triangular form**:
$$A^{(2)} = \begin{pmatrix} \mathbf{1} & 2 & 3 \\ 0 & \mathbf{1} & 1 \\ 0 & 0 & \mathbf{1} \end{pmatrix}$$

Since all row operations preserved the determinant exactly, the determinant is simply the product of the main diagonal entries:
$$\det A = 1 \cdot 1 \cdot 1 = 1$$

---

## 5. Why Each Step Is Valid
- **Elementary Matrix Determinants:** The elementary matrices corresponding to $R_2 - R_1$, $R_3 - R_1$, and $R_3 - 2R_2$ are unitriangular with $1$s on the diagonal, so $\det(E) = 1$. By the product rule $\det(EA) = \det(E)\det(A) = 1 \cdot \det A = \det A$.
- **Triangular Simplification:** Eliminating the lower triangle leaves only the main diagonal contributing to the non-zero terms of the permutation expansion.

---

## 6. Final Answer in Words
By applying the three row operations $R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - R_1$, and $R_3 \leftarrow R_3 - 2R_2$—none of which alters the determinant—the matrix is reduced to an upper triangular matrix with diagonal entries $1, 1, 1$. The determinant is the product of these diagonal entries, which equals $1$.

---

## 7. Quick Verification
- **Verification via Sarrus' Rule on the original matrix:**
  $$A = \begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 4 \\ 1 & 4 & 6 \end{pmatrix}$$
  - Downward diagonals:
    $$(1)(3)(6) + (2)(4)(1) + (3)(1)(4) = 18 + 8 + 12 = 38$$
  - Upward diagonals:
    $$(1)(3)(3) + (4)(4)(1) + (6)(1)(2) = 9 + 16 + 12 = 37$$
  - Combine:
    $$\det A = 38 - 37 = 1$$
  Both methods produce exactly $1$. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Subtracting the Wrong Rows:** Subtracting $R_3 - R_2$ first without creating clean column zeros, leading to unnecessary fractions or messier terms.
- **Scaling Rows to Clear Numbers:** Multiplying a row by a constant to clear numbers without dividing the determinant by that same constant.
- **Arithmetic Slips in the Final Subtraction:** In $R_3 - 2R_2$, writing $3 - 2(1) = 0$ instead of $1$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Because the first column consists entirely of ones, we subtract the first row from the second and third rows to create two leading zeros without altering the determinant. A final operation of $R_3 - 2R_2$, which also preserves the determinant, reduces the matrix into an upper triangular form with ones along the main diagonal. The determinant is therefore simply the product of the diagonal entries: $1 \cdot 1 \cdot 1 = 1$."

