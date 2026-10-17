# Exercise 4: Gauss–Jordan Elimination for Matrix Inversion

## 1. Original Problem
Find $A^{-1}$ using the Gauss–Jordan method for:
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix}$$
Show the augmented matrix $[A \mid I]$ after successive operations and explain why obtaining $I$ on the left gives the inverse on the right.

---

## 2. What We Are Trying to Find
We need to:
- Construct the block augmented matrix $[A \mid I]$.
- Apply Gaussian and Jordan elimination steps row-by-row until the left block becomes the identity matrix $I$.
- Display the full augmented matrix after every individual elementary row operation.
- Read off the resulting inverse matrix $A^{-1}$ from the right block.
- Explain the algebraic foundation of why this procedure works.

---

## 3. Key Concepts and Theorems
1. **The Augmented Matrix $[A \mid I]$:**
   Placing the identity matrix $I$ next to $A$ tracks the cumulative effect of elementary row operations:
   $$[A \mid I] = \begin{pmatrix} 1 & 2 & \mid & 1 & 0 \\ 3 & 5 & \mid & 0 & 1 \end{pmatrix}$$
2. **Elementary Matrix Representation:**
   Every elementary row operation corresponds to multiplying on the left by an invertible elementary matrix $E_k$.
   If a sequence of $p$ row operations transforms $A$ into $I$:
   $$(E_p \cdots E_2 E_1) A = I$$
   then the accumulated product $E = E_p \cdots E_2 E_1$ must equal $A^{-1}$.
   Applying these exact same operations simultaneously to $I$ on the right yields:
   $$(E_p \cdots E_2 E_1) I = A^{-1} I = A^{-1}$$
   Therefore:
   $$[A \mid I] \xrightarrow{\text{row operations}} [I \mid A^{-1}]$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Augmented Matrix
Write matrix $A$ on the left and the $2 \times 2$ identity matrix $I$ on the right:
$$M_0 = [A \mid I] = \begin{pmatrix} 1 & 2 & \mid & 1 & 0 \\ 3 & 5 & \mid & 0 & 1 \end{pmatrix}$$

---

### Step 2: Eliminate Entry $(2, 1)$
Using the pivot $1$ in Row 1, eliminate the $3$ in Row 2:
$$R_2 \leftarrow R_2 - 3R_1$$
- Left block calculation:
  $$(3, 5) - 3(1, 2) = (3 - 3, 5 - 6) = (0, -1)$$
- Right block calculation:
  $$(0, 1) - 3(1, 0) = (0 - 3, 1 - 0) = (-3, 1)$$

The augmented matrix after Step 2 is:
$$M_1 = \begin{pmatrix} 1 & 2 & \mid & 1 & 0 \\ 0 & -1 & \mid & -3 & 1 \end{pmatrix}$$

---

### Step 3: Scale Row 2 to Create a Pivot of $+1$
Multiply Row 2 by $-1$:
$$R_2 \leftarrow -R_2$$
- Left block: $(0, -1) \times (-1) = (0, 1)$
- Right block: $(-3, 1) \times (-1) = (3, -1)$

The augmented matrix after Step 3 is:
$$M_2 = \begin{pmatrix} 1 & 2 & \mid & 1 & 0 \\ 0 & 1 & \mid & 3 & -1 \end{pmatrix}$$

---

### Step 4: Eliminate Entry $(1, 2)$ Above the Pivot
Using the pivot $1$ in Row 2, eliminate the $2$ in Row 1:
$$R_1 \leftarrow R_1 - 2R_2$$
- Left block calculation:
  $$(1, 2) - 2(0, 1) = (1 - 0, 2 - 2) = (1, 0)$$
- Right block calculation:
  $$(1, 0) - 2(3, -1) = (1 - 6, 0 - (-2)) = (-5, 2)$$

The augmented matrix after Step 4 is:
$$M_3 = [I \mid A^{-1}] = \begin{pmatrix} 1 & 0 & \mid & -5 & 2 \\ 0 & 1 & \mid & 3 & -1 \end{pmatrix}$$

The left block is now the identity matrix $I$.

---

### Step 5: Read Off the Inverse Matrix
From the right block:
$$A^{-1} = \begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix}$$

---

### Step 6: Theoretical Explanation of Why the Method Works
- Every elementary row operation is mathematically equivalent to multiplying on the left by an elementary matrix $E_k$.
- In our three steps, we applied elementary matrices $E_1, E_2, E_3$ such that:
  $$(E_3 E_2 E_1) A = I$$
- By the definition of the inverse matrix, any matrix that multiplies $A$ to produce the identity $I$ must be the inverse $A^{-1}$. Therefore:
  $$E_3 E_2 E_1 = A^{-1}$$
- Because the exact same row operations were applied in parallel to the right-hand block (which started as $I$):
  $$(E_3 E_2 E_1) I = A^{-1} I = A^{-1}$$
This guarantees that as soon as the left block reaches $I$, the right block must contain $A^{-1}$.

---

## 5. Why Each Step Is Valid
- **Linear System Equivalence:** The Gauss-Jordan algorithm solves the matrix equation $A X = I$ for the column vectors of $X$ simultaneously.
- **Elementary Invertibility:** Each row operation is reversible and corresponds to a non-singular transformation, preserving all algebraic relationships.

---

## 6. Final Answer in Words
Using the Gauss–Jordan elimination method on the augmented matrix $[A \mid I]$, the row operations $R_2 \leftarrow R_2 - 3R_1$, $R_2 \leftarrow -R_2$, and $R_1 \leftarrow R_1 - 2R_2$ successfully transform the left block into the identity matrix $I$. The right block simultaneously becomes $\begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix}$, which is the inverse matrix $A^{-1}$.

---

## 7. Quick Verification
- **Verification via matrix multiplication ($A A^{-1}$):**
  $$A A^{-1} = \begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix} \begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix} = \begin{pmatrix} 1(-5) + 2(3) & 1(2) + 2(-1) \\ 3(-5) + 5(3) & 3(2) + 5(-1) \end{pmatrix} = \begin{pmatrix} -5 + 6 & 2 - 2 \\ -15 + 15 & 6 - 5 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$
- **Formula check:** $\det A = 1(5) - 2(3) = -1$.
  $A^{-1} = \frac{1}{-1}\begin{pmatrix} 5 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} -5 & 2 \\ 3 & -1 \end{pmatrix}$. Matches! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Forgetting to Apply Operations to the Right Side:** Modifying the left block but failing to update the identity matrix entries in parallel.
- **Sign Error in $R_1 - 2R_2$ on the Right Block:** Calculating $0 - 2(-1) = -2$ instead of $+2$.
- **Stopping at Echelon Form:** Stopping when the matrix is upper triangular instead of completing Jordan elimination (clearing entries above pivots to achieve $I$).

---

## 9. Classroom Presentation (3-Sentence Summary)
"We set up the augmented matrix $[A \mid I]$ and use row operations $R_2 - 3R_1$, scaling by $-1$, and $R_1 - 2R_2$ to reduce the left-hand side to the identity matrix. Because row operations represent multiplying on the left by elementary matrices, transforming $A$ into $I$ means the product of these operations equals $A^{-1}$. Since those same operations were applied to $I$ on the right side, the right block automatically becomes the inverse matrix $\begin{pmatrix}-5&2\\3&-1\end{pmatrix}$."

