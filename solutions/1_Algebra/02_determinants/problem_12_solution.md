# Exercise 12: A Parameter Revealed by a Row Operation

## 1. Original Problem
For the matrix:
$$A(t) = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & t \\ 0 & 1 & 1 \end{pmatrix}$$
find the values of $t$ for which the matrix is not invertible.

Before computing the determinant, perform the operation:
$$R_2 \leftarrow R_2 - 2R_1$$
and use the resulting structure. At the end, explain what special thing happens to the rows for the value of the parameter you found.

---

## 2. What We Are Trying to Find
We need to:
- Apply the specified row operation $R_2 \leftarrow R_2 - 2R_1$ to the parameterized matrix $A(t)$.
- Exploit the zeros created by this operation to evaluate the determinant $\det A(t)$ rapidly via Laplace expansion.
- Find all values of $t$ that make the matrix non-invertible ($\det A(t) = 0$).
- Explain the geometric/structural degeneracy that occurs between the original rows when $t$ assumes this critical value.

---

## 3. Key Concepts and Theorems
1. **Determinant Invariance Under Row Addition:**
   Performing $R_2 \leftarrow R_2 - 2R_1$ leaves the determinant strictly unchanged:
   $$\det A(t) = \det(A^{(1)}(t))$$
2. **Invertibility Criterion:**
   A matrix fails to be invertible if and only if its determinant is zero:
   $$A(t) \text{ is not invertible} \iff \det A(t) = 0$$
3. **Linear Dependence and Row Proportionality:**
   When the determinant vanishes, the rows of the matrix become linearly dependent. A zero row after Gaussian reduction directly exposes a proportional relationship among the original rows.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Perform the Prescribed Row Operation
Start with matrix:
$$A(t) = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & t \\ 0 & 1 & 1 \end{pmatrix}$$

Apply $R_2 \leftarrow R_2 - 2R_1$:
- Row 2 calculation:
  $$(2, 4, t) - 2(1, 2, 3) = (2 - 2, 4 - 4, t - 6) = (0, 0, t - 6)$$

The simplified matrix is:
$$A^{(1)}(t) = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & t - 6 \\ 0 & 1 & 1 \end{pmatrix}$$
Because this operation is a row addition, the determinant is preserved:
$$\det A(t) = \det A^{(1)}(t)$$

---

### Step 2: Compute the Determinant Using the Resulting Structure
Look at Row 2 of $A^{(1)}(t)$: it contains two leading zeros and only one non-zero entry sitting at position $(2, 3)$, which is $t - 6$.
Expand along **Row 2** using Laplace cofactor expansion:
$$\det A^{(1)}(t) = (-1)^{2+3} (t - 6) \cdot \det M_{23}$$

- The cofactor sign is $(-1)^{2+3} = (-1)^5 = -1$.
- The minor matrix $M_{23}$ (obtained by deleting Row 2 and Column 3) is:
  $$M_{23} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$$
- Compute the $2 \times 2$ determinant:
  $$\det M_{23} = (1)(1) - (2)(0) = 1$$

Therefore:
$$\det A(t) = -(t - 6) \cdot 1 = -(t - 6) = 6 - t$$

---

### Step 3: Find the Critical Parameter Value
The matrix is not invertible if and only if its determinant is zero:
$$\det A(t) = 0 \iff 6 - t = 0 \implies t = 6$$

---

### Step 4: Explain What Happens to the Rows at $t = 6$
Substitute $t = 6$ into the original matrix:
$$A(6) = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 0 & 1 & 1 \end{pmatrix}$$
Observe Row 1 and Row 2:
- $R_1 = (1, 2, 3)$
- $R_2 = (2, 4, 6)$

Notice that Row 2 is exactly twice Row 1:
$$R_2 = 2 R_1$$
The first two rows are **strictly parallel (proportional)**. Because two rows point in the exact same direction, the row vectors fail to span 3-dimensional space, collapsing the matrix rank to $2$. This immediately explains why the determinant is zero and why the matrix cannot be inverted.

---

## 5. Why Each Step Is Valid
- **Equivalence of Determinants Under Shear:** The row operation matrix $E = \begin{pmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ has determinant $1$, so $\det(EA) = 1 \cdot \det A = \det A$.
- **Cofactor Formula Rigor:** The Laplace expansion theorem holds along any row; choosing Row 2 minimizes arithmetic since two of the three cofactor terms are identically zero.

---

## 6. Final Answer in Words
The matrix $A(t)$ is not invertible when $t = 6$. Performing the operation $R_2 - 2R_1$ produces Row 2 equal to $(0, 0, t-6)$, from which the determinant evaluates immediately to $6 - t$. Setting $6 - t = 0$ yields $t = 6$. For this value, the second row of the original matrix becomes $(2, 4, 6)$, which is an exact multiple of the first row ($R_2 = 2R_1$), creating linear dependence and destroying invertibility.

---

## 7. Quick Verification
- **Verification via Sarrus' rule on the original matrix $A(t)$:**
  - Downward diagonals: $(1)(4)(1) + (2)(t)(0) + (3)(2)(1) = 4 + 0 + 6 = 10$.
  - Upward diagonals: $(0)(4)(3) + (1)(t)(1) + (1)(2)(2) = 0 + t + 4 = t + 4$.
  - $\det A(t) = 10 - (t + 4) = 10 - t - 4 = 6 - t$.
  - Setting $6 - t = 0 \implies t = 6$. Matches! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Cofactor Sign Error:** Forgetting that entry $(2, 3)$ carries a negative checkerboard sign $(-1)^{2+3} = -1$, which would wrongly lead to $t - 6$ instead of $6 - t$.
- **Arithmetic in $R_2 - 2R_1$:** Writing $t - 2(3)$ as $t - 5$ instead of $t - 6$.
- **Skipping the Geometric Explanation:** Calculating $t = 6$ without addressing the second half of the prompt regarding what happens to the rows.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Applying the row operation $R_2 \leftarrow R_2 - 2R_1$ simplifies the second row to $(0, 0, t-6)$ without changing the determinant. Expanding along this row gives $\det A(t) = -(t-6) = 6-t$, which means the matrix is non-invertible precisely when $t = 6$. When $t=6$, the second row of the original matrix becomes $(2, 4, 6)$, which is directly proportional to the first row ($R_2 = 2R_1$), thereby causing the determinant to collapse to zero."

