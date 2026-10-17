# Exercise 1: Determinant of a 2×2 Matrix

## 1. Original Problem
Compute:
$$\det\begin{pmatrix} 3 & -2 \\ 5 & 4 \end{pmatrix}, \qquad \det\begin{pmatrix} 1 & 7 \\ 2 & 14 \end{pmatrix}$$
Which matrix is invertible? Justify your answer.

---

## 2. What We Are Trying to Find
We need to:
- Compute the numerical value of the determinant for two given $2 \times 2$ matrices using the diagonal difference formula.
- Determine which of the two matrices is invertible (non-singular).
- Provide a clear mathematical justification connecting the determinant value to the property of invertibility.

---

## 3. Key Concepts and Theorems
1. **Determinant of a $2 \times 2$ Matrix:**
   For any $2 \times 2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the determinant is defined as the product of the main diagonal entries minus the product of the off-diagonal entries:
   $$\det M = ad - bc$$
2. **Invertibility Criterion (Non-Singularity Theorem):**
   A square matrix $M$ is invertible if and only if its determinant is non-zero:
   $$M \text{ is invertible} \iff \det M \neq 0$$
   If $\det M = 0$, the matrix is singular and has no inverse.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Determinant of the First Matrix
Let $M_1 = \begin{pmatrix} 3 & -2 \\ 5 & 4 \end{pmatrix}$.
- Main diagonal product: $a \cdot d = 3 \cdot 4 = 12$
- Off-diagonal product: $b \cdot c = (-2) \cdot 5 = -10$
- Subtract the off-diagonal product from the main diagonal product:
  $$\det M_1 = (3 \cdot 4) - ((-2) \cdot 5) = 12 - (-10) = 12 + 10 = 22$$

---

### Step 2: Compute the Determinant of the Second Matrix
Let $M_2 = \begin{pmatrix} 1 & 7 \\ 2 & 14 \end{pmatrix}$.
- Main diagonal product: $a \cdot d = 1 \cdot 14 = 14$
- Off-diagonal product: $b \cdot c = 7 \cdot 2 = 14$
- Subtract the off-diagonal product:
  $$\det M_2 = (1 \cdot 14) - (7 \cdot 2) = 14 - 14 = 0$$

---

### Step 3: Determine Invertibility
- For $M_1$: $\det M_1 = 22 \neq 0$. Therefore, $M_1$ is **invertible**. Its inverse exists and is given by:
  $$M_1^{-1} = \frac{1}{22} \begin{pmatrix} 4 & 2 \\ -5 & 3 \end{pmatrix}$$
- For $M_2$: $\det M_2 = 0$. Therefore, $M_2$ is **not invertible** (singular). Notice that Row 2 is exactly twice Row 1 ($2 \cdot (1, 7) = (2, 14)$), meaning the rows are linearly dependent.

---

## 5. Why Each Step Is Valid
- **Determinant Formula:** The formula $ad - bc$ gives the signed area scaling factor of the linear mapping defined by the matrix; if this factor is non-zero, the mapping does not collapse area and can be inverted.
- **Invertibility Equivalence:** An inverse formula requires dividing by the determinant ($\frac{1}{\det M}$); division by zero is undefined, so an inverse exists if and only if $\det M \neq 0$.

---

## 6. Final Answer in Words
The determinant of $\begin{pmatrix} 3 & -2 \\ 5 & 4 \end{pmatrix}$ is $22$, and the determinant of $\begin{pmatrix} 1 & 7 \\ 2 & 14 \end{pmatrix}$ is $0$. Therefore, only the first matrix is invertible, because its determinant is non-zero, whereas the second matrix has a determinant of zero due to linearly dependent rows.

---

## 7. Quick Verification
- **Inverse verification for $M_1$:**
  $$M_1 M_1^{-1} = \begin{pmatrix} 3 & -2 \\ 5 & 4 \end{pmatrix} \left[ \frac{1}{22} \begin{pmatrix} 4 & 2 \\ -5 & 3 \end{pmatrix} \right] = \frac{1}{22} \begin{pmatrix} 12 + 10 & 6 - 6 \\ 20 - 20 & 10 + 12 \end{pmatrix} = \frac{1}{22} \begin{pmatrix} 22 & 0 \\ 0 & 22 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$
- **Linear dependence in $M_2$:**
  $$R_2 - 2R_1 = (2, 14) - 2(1, 7) = (0, 0)$$
  A matrix containing a dependent row has rank $1 < 2$, confirming $\det M_2 = 0$. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Sign Error with Negative Entries:** In $M_1$, writing $12 - 10 = 2$ instead of $12 - (-10) = 22$.
- **Reversing the Terms:** Subtracting the main diagonal from the off-diagonal ($bc - ad$), which gives the opposite sign.
- **Concluding Invertibility without Reason:** Stating a matrix is invertible without explicitly citing that $\det M \neq 0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Using the $ad - bc$ formula, the first matrix has a determinant of $12 - (-10) = 22$, while the second matrix evaluates to $14 - 14 = 0$. Because a square matrix is invertible if and only if its determinant is non-zero, only the first matrix has an inverse. The second matrix is singular because its second row is an exact multiple of its first row, collapsing the area to zero."

