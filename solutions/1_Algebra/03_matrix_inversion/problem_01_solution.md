# Exercise 1: Definition of the Inverse

## 1. Original Problem
For the matrices:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$$
check, without using a formula, whether $B = A^{-1}$. Compute $AB$ and $BA$ and relate the result to the definition of the inverse.

---

## 2. What We Are Trying to Find
We need to:
- Test whether matrix $B$ is the mathematical inverse of matrix $A$ directly from first principles, without using any determinant or adjugate formulas.
- Compute the matrix products $AB$ and $BA$ explicitly.
- Connect both multiplication results to the formal definition of an invertible matrix and its identity matrix.

---

## 3. Key Concepts and Theorems
1. **Definition of the Inverse Matrix:**
   Let $A$ be a square $n \times n$ matrix. An $n \times n$ matrix $B$ is called the **inverse of $A$** (denoted $A^{-1}$) if and only if multiplying them in both orders yields the identity matrix $I$:
   $$AB = I \quad \text{and} \quad BA = I$$
   where $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ for $n = 2$.
2. **Two-Sided Inverse:**
   A true inverse must satisfy both the right-inverse condition ($AB = I$) and the left-inverse condition ($BA = I$).

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Product $AB$
Multiply $A$ by $B$ using row-by-column multiplication:
$$AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$$

Calculate each entry:
- **Top-left $(1, 1)$:** $2(1) + 1(-1) = 2 - 1 = 1$
- **Top-right $(1, 2)$:** $2(-1) + 1(2) = -2 + 2 = 0$
- **Bottom-left $(2, 1)$:** $1(1) + 1(-1) = 1 - 1 = 0$
- **Bottom-right $(2, 2)$:** $1(-1) + 1(2) = -1 + 2 = 1$

Assembling the matrix:
$$AB = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$$

---

### Step 2: Compute the Product $BA$
Multiply $B$ by $A$ in reverse order:
$$BA = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$$

Calculate each entry:
- **Top-left $(1, 1)$:** $1(2) + (-1)(1) = 2 - 1 = 1$
- **Top-right $(1, 2)$:** $1(1) + (-1)(1) = 1 - 1 = 0$
- **Bottom-left $(2, 1)$:** $-1(2) + 2(1) = -2 + 2 = 0$
- **Bottom-right $(2, 2)$:** $-1(1) + 2(1) = -1 + 2 = 1$

Assembling the matrix:
$$BA = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$$

---

### Step 3: Relate to the Definition of the Inverse
By definition, a matrix $B$ is the inverse of $A$ if and only if $AB = BA = I$.
Since both calculations produced the $2 \times 2$ identity matrix:
$$AB = I \quad \text{and} \quad BA = I$$
we conclude with mathematical certainty that:
$$B = A^{-1}$$

---

## 5. Why Each Step Is Valid
- **Axiomatic Definition of Inverses:** In any algebraic ring or monoid, an inverse is defined fundamentally by its neutralizing property under the binary operation ($a \cdot b = b \cdot a = e$).
- **Equivalence of Linear Operators:** If linear map $T_B$ maps every output of $T_A$ back to its original input, $T_B$ is the bijective inverse transformation $T_A^{-1}$.

---

## 6. Final Answer in Words
Computing the products directly gives $AB = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and $BA = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$. Because both products yield the identity matrix $I$, matrix $B$ satisfies the fundamental definition of an inverse matrix, confirming that $B = A^{-1}$.

---

## 7. Quick Verification
- **Determinant formula check:**
  $\det A = 2(1) - 1(1) = 1$.
  Using the explicit formula $A^{-1} = \frac{1}{\det A}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{1}\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = B$.
  The formula gives the identical matrix $B$. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Checking Only One Product:** Computing $AB = I$ and stopping. By strict definition, both $AB = I$ and $BA = I$ must be checked (even though for finite-dimensional square matrices over a field one implies the other, completing both demonstrates complete mastery of the definition).
- **Inverting Individual Entries:** Assuming $A^{-1} = \begin{pmatrix} 1/2 & 1 \\ 1 & 1 \end{pmatrix}$, which is completely false for matrix algebra.

---

## 9. Classroom Presentation (3-Sentence Summary)
"To verify whether $B$ is the inverse of $A$ from the definition, we compute their products in both orders without using any inversion formulas. Multiplying $AB$ gives the identity matrix $\begin{pmatrix}1&0\\0&1\end{pmatrix}$, and multiplying $BA$ likewise gives the identity matrix. Because both products yield the identity, $B$ satisfies the exact two-sided definition of the matrix inverse: $B = A^{-1}$."

