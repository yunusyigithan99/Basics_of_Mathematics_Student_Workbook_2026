# Exercise 2: Formula for a 2×2 Matrix

## 1. Original Problem
Find the inverse of:
$$A = \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix}$$
using the formula for a $2\times2$ matrix. At the end, check the result by computing one product with $A$.

---

## 2. What We Are Trying to Find
We need to:
- Compute the determinant of the given $2 \times 2$ matrix $A$.
- Apply the explicit adjugate formula for the inverse of a $2 \times 2$ matrix.
- Express the resulting inverse matrix $A^{-1}$ with simplified entries.
- Verify the solution by multiplying $A$ by $A^{-1}$ to confirm that the product equals the identity matrix $I$.

---

## 3. Key Concepts and Theorems
1. **The $2 \times 2$ Matrix Inverse Formula:**
   For any $2 \times 2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with determinant $\det M = ad - bc \neq 0$, the inverse is given explicitly by:
   $$M^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$
   *Recipe:*
   - Swap the two entries on the main diagonal ($a \leftrightarrow d$).
   - Negate the two off-diagonal entries (change signs of $b$ and $c$).
   - Divide every entry by the determinant $\det M$.
2. **Verification Condition:**
   $A A^{-1} = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Determinant of $A$
For matrix $A = \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix}$:
$$\det A = (3 \cdot 4) - (2 \cdot 5) = 12 - 10 = 2$$
Since $\det A = 2 \neq 0$, the matrix is invertible.

---

### Step 2: Apply the Inversion Formula
Using the formula:
$$A^{-1} = \frac{1}{\det A} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$
Substitute $a = 3$, $b = 2$, $c = 5$, $d = 4$, and $\det A = 2$:
- Swap diagonal elements: $3$ and $4$ become $4$ and $3$.
- Negate off-diagonal elements: $2$ and $5$ become $-2$ and $-5$.

$$A^{-1} = \frac{1}{2} \begin{pmatrix} 4 & -2 \\ -5 & 3 \end{pmatrix}$$

Distribute the scalar factor $\frac{1}{2}$ into the matrix:
$$A^{-1} = \begin{pmatrix} \frac{4}{2} & \frac{-2}{2} \\ \frac{-5}{2} & \frac{3}{2} \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -\frac{5}{2} & \frac{3}{2} \end{pmatrix}$$

---

### Step 3: Check by Computing the Product $A A^{-1}$
Multiply $A$ by $A^{-1}$:
$$A A^{-1} = \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -\frac{5}{2} & \frac{3}{2} \end{pmatrix}$$

Calculate each entry:
- **Top-left $(1, 1)$:**
  $$3(2) + 2\left(-\frac{5}{2}\right) = 6 - 5 = 1$$
- **Top-right $(1, 2)$:**
  $$3(-1) + 2\left(\frac{3}{2}\right) = -3 + 3 = 0$$
- **Bottom-left $(2, 1)$:**
  $$5(2) + 4\left(-\frac{5}{2}\right) = 10 - 10 = 0$$
- **Bottom-right $(2, 2)$:**
  $$5(-1) + 4\left(\frac{3}{2}\right) = -5 + 6 = 1$$

Assembling the result:
$$A A^{-1} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$$
The result matches the identity matrix perfectly!

---

## 5. Why Each Step Is Valid
- **Adjugate Matrix Theorem:** For any invertible matrix $M$, $M \operatorname{adj}(M) = \det(M) I$. For a $2 \times 2$ matrix, the classical adjugate is precisely $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.
- **Distributivity of Scalars:** Dividing by $\det A$ scales the product $A \operatorname{adj}(A) = (\det A) I$ down to $I$.

---

## 6. Final Answer in Words
The determinant of $A$ is $2$. Applying the $2 \times 2$ inversion formula yields $A^{-1} = \frac{1}{2}\begin{pmatrix} 4 & -2 \\ -5 & 3 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -5/2 & 3/2 \end{pmatrix}$. Multiplying $A$ by this inverse gives the identity matrix $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, confirming the solution.

---

## 7. Quick Verification
- **Left product check ($A^{-1} A$):**
  $$\begin{pmatrix} 2 & -1 \\ -5/2 & 3/2 \end{pmatrix} \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix} = \begin{pmatrix} 2(3)-1(5) & 2(2)-1(4) \\ -\frac{5}{2}(3)+\frac{3}{2}(5) & -\frac{5}{2}(2)+\frac{3}{2}(4) \end{pmatrix} = \begin{pmatrix} 6-5 & 4-4 \\ -\frac{15}{2}+\frac{15}{2} & -5+6 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$
- **Determinant check:**
  $\det(A^{-1}) = 2(3/2) - (-1)(-5/2) = 3 - 5/2 = 1/2 = \frac{1}{\det A} \quad \checkmark$

---

## 8. Common Mistakes to Avoid
- **Swapping the Wrong Diagonals:** Swapping the off-diagonal entries instead of the main diagonal entries.
- **Forgetting to Negate the Off-Diagonal:** Leaving $b$ and $c$ positive.
- **Dropping the Scalar Fraction:** Forgetting to divide by $\det A = 2$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"To invert this $2 \times 2$ matrix, we first compute its determinant, which is $3(4) - 2(5) = 2$. Applying the standard inversion formula, we swap the main diagonal entries, negate the off-diagonal entries, and divide by the determinant, yielding $A^{-1} = \begin{pmatrix} 2 & -1 \\ -5/2 & 3/2 \end{pmatrix}$. Multiplying $A$ by this result produces the identity matrix $\begin{pmatrix}1&0\\0&1\end{pmatrix}$, which confirms our calculation."

