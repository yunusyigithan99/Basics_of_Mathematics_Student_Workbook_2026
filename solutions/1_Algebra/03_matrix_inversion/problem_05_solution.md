# Exercise 5: Inverting a 3×3 Matrix via Gauss–Jordan Elimination

## 1. Original Problem
Use Gauss–Jordan elimination to find the inverse of:
$$A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$$
Check the result by multiplication.

---

## 2. What We Are Trying to Find
We need to:
- Construct the $3 \times 6$ augmented block matrix $[A \mid I_3]$.
- Apply Gaussian elimination to achieve an upper triangular form on the left.
- Apply Jordan back-elimination to clear the entries above the pivots and reduce the left block to $I_3$.
- Read off the inverse matrix $A^{-1}$ from the right block.
- Verify the solution by explicitly multiplying $A$ by $A^{-1}$ to confirm $A A^{-1} = I_3$.

---

## 3. Key Concepts and Theorems
1. **The Gauss–Jordan Inversion Method for $3 \times 3$ Matrices:**
   We form the partitioned matrix:
   $$[A \mid I] = \left(\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 & 0 & 1 \end{array}\right)$$
   and apply elementary row operations until the left half becomes the identity matrix $I$:
   $$[A \mid I] \xrightarrow{\text{EROs}} [I \mid A^{-1}]$$
2. **Verification Condition:**
   $A A^{-1} = I_3$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Augmented Matrix
Write $A$ and the $3 \times 3$ identity matrix side by side:
$$M_0 = \left(\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 & 0 & 1 \end{array}\right)$$

---

### Step 2: Eliminate the First Entry of Row 3
Using the pivot $a_{11} = 1$, eliminate the entry in Row 3 (entry $(2, 1)$ is already $0$):
$$R_3 \leftarrow R_3 - R_1$$
- Left block: $(1, 0, 1) - (1, 1, 0) = (0, -1, 1)$
- Right block: $(0, 0, 1) - (1, 0, 0) = (-1, 0, 1)$

The matrix becomes:
$$M_1 = \left(\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & -1 & 1 & -1 & 0 & 1 \end{array}\right)$$

---

### Step 3: Eliminate the Second Entry of Row 3
Using the pivot $a_{22} = 1$, eliminate $-1$ in Row 3:
$$R_3 \leftarrow R_3 + R_2$$
- Left block: $(0, -1, 1) + (0, 1, 1) = (0, 0, 2)$
- Right block: $(-1, 0, 1) + (0, 1, 0) = (-1, 1, 1)$

The matrix becomes:
$$M_2 = \left(\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 2 & -1 & 1 & 1 \end{array}\right)$$

---

### Step 4: Scale Row 3 to Make Pivot 1
Multiply Row 3 by $\frac{1}{2}$:
$$R_3 \leftarrow \frac{1}{2} R_3$$
- Left block: $(0, 0, 2) \times \frac{1}{2} = (0, 0, 1)$
- Right block: $(-1, 1, 1) \times \frac{1}{2} = \left(-\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right)$

The matrix becomes:
$$M_3 = \left(\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{array}\right)$$

---

### Step 5: Eliminate Entry $(2, 3)$ Above the Pivot
Using the pivot in Row 3, eliminate the $1$ in Row 2:
$$R_2 \leftarrow R_2 - R_3$$
- Left block: $(0, 1, 1) - (0, 0, 1) = (0, 1, 0)$
- Right block:
  $$(0, 1, 0) - \left(-\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right) = \left(\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\right)$$

The matrix becomes:
$$M_4 = \left(\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ 0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{array}\right)$$

---

### Step 6: Eliminate Entry $(1, 2)$ Above the Pivot
Using the pivot in Row 2, eliminate the $1$ in Row 1:
$$R_1 \leftarrow R_1 - R_2$$
- Left block: $(1, 1, 0) - (0, 1, 0) = (1, 0, 0)$
- Right block:
  $$(1, 0, 0) - \left(\frac{1}{2}, \frac{1}{2}, -\frac{1}{2}\right) = \left(\frac{1}{2}, -\frac{1}{2}, \frac{1}{2}\right)$$

The matrix is now in reduced row echelon form $[I \mid A^{-1}]$:
$$M_5 = \left(\begin{array}{ccc|ccc} 1 & 0 & 0 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ 0 & 1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ 0 & 0 & 1 & -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{array}\right)$$

---

### Step 7: Read Off the Inverse Matrix
Factoring out the common scalar $\frac{1}{2}$:
$$A^{-1} = \frac{1}{2} \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ -\frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{pmatrix}$$

---

### Step 8: Check by Matrix Multiplication
Compute $A A^{-1}$:
$$A A^{-1} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \left[ \frac{1}{2} \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix} \right] = \frac{1}{2} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}$$

Evaluate the product entry by entry:
- **Row 1:**
  - $(1)(1) + (1)(1) + (0)(-1) = 2$
  - $(1)(-1) + (1)(1) + (0)(1) = 0$
  - $(1)(1) + (1)(-1) + (0)(1) = 0$
- **Row 2:**
  - $(0)(1) + (1)(1) + (1)(-1) = 0$
  - $(0)(-1) + (1)(1) + (1)(1) = 2$
  - $(0)(1) + (1)(-1) + (1)(1) = 0$
- **Row 3:**
  - $(1)(1) + (0)(1) + (1)(-1) = 0$
  - $(1)(-1) + (0)(1) + (1)(1) = 0$
  - $(1)(1) + (0)(-1) + (1)(1) = 2$

Multiply by the outer scalar $\frac{1}{2}$:
$$A A^{-1} = \frac{1}{2} \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3$$
The check completely confirms the inverse!

---

## 5. Why Each Step Is Valid
- **Reversible Row Equivalences:** Every step preserves the solution set of $A X = I$.
- **Complete Back-Substitution:** Eliminating entries above the pivots in reverse order ($R_2 - R_3$, then $R_1 - R_2$) decouples each variable completely, isolating the solution vectors for each column of the inverse.

---

## 6. Final Answer in Words
Using Gauss–Jordan elimination on the augmented matrix $[A \mid I]$, the row operations reduce $A$ to the $3 \times 3$ identity matrix, transforming the right block into $A^{-1} = \frac{1}{2}\begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}$. Direct multiplication confirms $A A^{-1} = I_3$.

---

## 7. Quick Verification
- **Determinant Check:**
  $\det A = 1(1\cdot 1 - 0) - 1(0 - 1) + 0 = 1 + 1 = 2$.
  $\det(A^{-1}) = \left(\frac{1}{2}\right)^3 \det\begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix} = \frac{1}{8} \cdot 4 = \frac{1}{2} = \frac{1}{\det A} \quad \checkmark$

---

## 8. Common Mistakes to Avoid
- **Fractions in Early Steps:** Scaling rows by fractions too early. It is best to keep integers until the echelon form is established, then divide by $2$.
- **Sign Error in $R_1 - R_2$:** Subtracting the negative entries in the right block: $0 - (-1/2) = +1/2$.
- **Skipping Verification:** Assuming the right-hand side is correct without computing $A A^{-1}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"We augment the $3 \times 3$ matrix with the identity matrix and use row operations $R_3 - R_1$ and $R_3 + R_2$ to achieve upper triangular form with a pivot of 2 in the bottom row. Scaling by $\frac{1}{2}$ and eliminating upward with $R_2 - R_3$ and $R_1 - R_2$ isolates the identity matrix on the left side. The right side yields the inverse $A^{-1} = \frac{1}{2}\begin{pmatrix}1&-1&1\\1&1&-1\\-1&1&1\end{pmatrix}$, which we verify by multiplying back to obtain the identity matrix."

