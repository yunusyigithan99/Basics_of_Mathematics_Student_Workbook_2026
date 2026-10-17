# Exercise 3: Swapping Two Rows

## 1. Original Problem
For the matrix:
$$A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \\ 2 & 1 & 1 \end{pmatrix}$$
compute $\det A$. Then form a matrix $B$ by swapping the first and second rows of $A$.

First predict $\det B$ using a determinant property, and then verify your prediction by calculation.

---

## 2. What We Are Trying to Find
We need to:
- Compute the determinant of matrix $A$.
- Form matrix $B$ by interchanging Row 1 and Row 2 of $A$.
- Use the fundamental alternating property of determinants to predict the value of $\det B$ before calculating it.
- Explicitly calculate $\det B$ from scratch to verify the theoretical prediction.

---

## 3. Key Concepts and Theorems
1. **The Row-Swap (Alternating) Property:**
   Swapping any two rows (or columns) of a matrix reverses the sign of its determinant:
   $$\det(\text{matrix after 1 row swap}) = -\det(\text{original matrix})$$
   If $B$ is obtained from $A$ by the elementary row operation $R_i \leftrightarrow R_j$, then:
   $$\det B = -\det A$$
2. **Geometric Intuition:**
   The determinant represents oriented volume. Interchanging two coordinate axes (rows) reverses the geometric orientation of the coordinate frame (like switching between a right-handed and a left-handed system), flipping the sign from positive to negative or vice versa.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $\det A$
Let us expand along the first row of $A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 3 & 1 \\ 2 & 1 & 1 \end{pmatrix}$:
$$\det A = 1 \cdot \det\begin{pmatrix} 3 & 1 \\ 1 & 1 \end{pmatrix} - 2 \cdot \det\begin{pmatrix} 0 & 1 \\ 2 & 1 \end{pmatrix} + 0$$

Evaluate the $2 \times 2$ determinants:
- First minor: $3(1) - 1(1) = 3 - 1 = 2$
- Second minor: $0(1) - 1(2) = 0 - 2 = -2$

Substitute back:
$$\det A = 1(2) - 2(-2) = 2 + 4 = 6$$

---

### Step 2: Form Matrix $B$ and Predict $\det B$
Swap the first and second rows of $A$ ($R_1 \leftrightarrow R_2$):
$$B = \begin{pmatrix} 0 & 3 & 1 \\ 1 & 2 & 0 \\ 2 & 1 & 1 \end{pmatrix}$$

**Prediction using determinant properties:**
Because matrix $B$ is obtained by exactly one row swap from $A$, its determinant must be the negative of $\det A$:
$$\text{Predicted } \det B = -\det A = -6$$

---

### Step 3: Verify Prediction by Explicit Calculation of $\det B$
Expand $\det B$ along its first column, which has a convenient zero in entry $(1, 1)$:
$$B = \begin{pmatrix} 0 & 3 & 1 \\ 1 & 2 & 0 \\ 2 & 1 & 1 \end{pmatrix}$$

Using cofactor expansion along column 1 (signs: $+$, $-$, $+$):
- Entry $(1, 1) = 0$: contributes $0$.
- Entry $(2, 1) = 1$ (sign is $-$):
  $$-1 \cdot \det\begin{pmatrix} 3 & 1 \\ 1 & 1 \end{pmatrix} = -1 \cdot (3(1) - 1(1)) = -1 \cdot (3 - 1) = -1(2) = -2$$
- Entry $(3, 1) = 2$ (sign is $+$):
  $$+2 \cdot \det\begin{pmatrix} 3 & 1 \\ 2 & 0 \end{pmatrix} = +2 \cdot (3(0) - 1(2)) = +2 \cdot (0 - 2) = +2(-2) = -4$$

Summing these contributions:
$$\det B = 0 + (-2) + (-4) = -6$$
The calculation gives $-6$, confirming the prediction.

---

## 5. Why Each Step Is Valid
- **Alternating Multilinear Form:** The determinant is formally defined as the unique alternating multilinear form normalized on the identity matrix. The term "alternating" explicitly means swapping two inputs negates the value.
- **Elementary Matrix Connection:** Swapping rows corresponds to multiplying on the left by a permutation matrix $P = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$. Since $\det P = -1$, the product rule gives $\det B = \det(PA) = \det P \cdot \det A = (-1)(6) = -6$.

---

## 6. Final Answer in Words
The determinant of matrix $A$ is $6$. Matrix $B$, formed by swapping the first two rows of $A$, is predicted to have determinant $-6$ because interchanging two rows negates the determinant. Direct evaluation of $\det B$ produces $-2 - 4 = -6$, confirming the prediction.

---

## 7. Quick Verification
- Sarrus' rule for $B$:
  - Downward diagonals: $(0)(2)(1) + (3)(0)(2) + (1)(1)(1) = 0 + 0 + 1 = 1$.
  - Upward diagonals: $(2)(2)(1) + (1)(0)(0) + (1)(1)(3) = 4 + 0 + 3 = 7$.
  - $\det B = 1 - 7 = -6$. Exactly matches! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Assuming Row Swaps Do Not Change the Determinant:** Confusing row operations in solving linear systems (where solutions don't change) with determinants (where each swap multiplies the determinant by $-1$).
- **Losing Track of Laplace Signs:** Forgetting that entry $(2, 1)$ in a $3 \times 3$ matrix carries a negative cofactor sign $(-1)^{2+1} = -1$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Expanding along the first row gives $\det A = 6$. By the fundamental alternating property of determinants, swapping any two rows reverses the sign of the determinant, predicting that $\det B = -6$. Calculating $\det B$ directly confirms this prediction, illustrating that row swaps invert the orientation of the row vectors in space."

