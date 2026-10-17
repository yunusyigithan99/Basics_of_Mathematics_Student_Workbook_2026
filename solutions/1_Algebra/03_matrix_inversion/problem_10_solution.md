# Exercise 10: Inverse of a Diagonal Matrix

## 1. Original Problem
Given the diagonal matrices:
$$D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 5 \end{pmatrix}, \qquad E = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 5 \end{pmatrix}$$
Without using Gauss–Jordan elimination, decide which matrix is invertible. For the invertible matrix, give the inverse and check the result by multiplication.

---

## 2. What We Are Trying to Find
We need to:
- Determine which of the two matrices ($D$ or $E$) is invertible by inspecting their diagonal entries and determinants directly, without performing row operations.
- State the necessary and sufficient condition for a diagonal matrix to have an inverse.
- Write down the explicit inverse matrix for the invertible matrix by inverting its diagonal entries.
- Verify the inverse by calculating the product with the original matrix to show it yields the $3 \times 3$ identity matrix $I_3$.

---

## 3. Key Concepts and Theorems
1. **Determinant of a Diagonal Matrix:**
   Because all off-diagonal entries are zero, the determinant of a diagonal matrix is simply the product of all its main diagonal entries:
   $$\det\begin{pmatrix} d_1 & 0 & 0 \\ 0 & d_2 & 0 \\ 0 & 0 & d_3 \end{pmatrix} = d_1 \cdot d_2 \cdot d_3$$
2. **Invertibility Criterion for Diagonal Matrices:**
   A diagonal matrix is invertible if and only if **all of its diagonal entries are non-zero**:
   $$\det D \neq 0 \iff d_i \neq 0 \quad \text{for all } i$$
   If even a single diagonal entry is zero, an entire row (and column) is zero, making the matrix singular.
3. **Explicit Inverse Formula:**
   For an invertible diagonal matrix, its inverse is also diagonal, with each diagonal entry replaced by its reciprocal:
   $$D^{-1} = \begin{pmatrix} \frac{1}{d_1} & 0 & 0 \\ 0 & \frac{1}{d_2} & 0 \\ 0 & 0 & \frac{1}{d_3} \end{pmatrix}$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze Invertibility of $D$ and $E$
- **For Matrix $D$:**
  $$D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 5 \end{pmatrix}$$
  - The diagonal entries are $2$, $-3$, and $5$.
  - None of the diagonal entries is zero.
  - The determinant is:
    $$\det D = 2 \cdot (-3) \cdot 5 = -30$$
  - Since $\det D = -30 \neq 0$, matrix $D$ is **invertible**.

- **For Matrix $E$:**
  $$E = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 5 \end{pmatrix}$$
  - The second diagonal entry is zero ($e_{22} = 0$).
  - The second row of $E$ consists entirely of zeros: $R_2 = (0, 0, 0)$.
  - The determinant is:
    $$\det E = 2 \cdot 0 \cdot 5 = 0$$
  - Since $\det E = 0$ (and the second row is all zeros, meaning it has rank at most $2 < 3$), matrix $E$ is **not invertible** (singular).

---

### Step 2: Write Down the Inverse Matrix $D^{-1}$
For the invertible matrix $D$, take the reciprocal of each non-zero diagonal entry:
- $d_{11} = 2 \implies \frac{1}{2}$
- $d_{22} = -3 \implies \frac{1}{-3} = -\frac{1}{3}$
- $d_{33} = 5 \implies \frac{1}{5}$

Therefore, the inverse is:
$$D^{-1} = \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -\frac{1}{3} & 0 \\ 0 & 0 & \frac{1}{5} \end{pmatrix}$$

---

### Step 3: Check by Matrix Multiplication
Compute the product $D D^{-1}$:
$$D D^{-1} = \begin{pmatrix} 2 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 5 \end{pmatrix} \begin{pmatrix} \frac{1}{2} & 0 & 0 \\ 0 & -\frac{1}{3} & 0 \\ 0 & 0 & \frac{1}{5} \end{pmatrix}$$

Because both matrices are diagonal, multiplying them multiplies matching diagonal entries directly:
- Entry $(1, 1)$: $2 \cdot \frac{1}{2} = 1$
- Entry $(2, 2)$: $(-3) \cdot \left(-\frac{1}{3}\right) = 1$
- Entry $(3, 3)$: $5 \cdot \frac{1}{5} = 1$
- All off-diagonal dot products are zero.

Thus:
$$D D^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3$$
The verification is complete.

---

## 5. Why Each Step Is Valid
- **Diagonal Ring Homomorphism:** The ring of $n \times n$ diagonal matrices is isomorphic to the direct product of $n$ copies of the field $\mathbb{R}$ ($\mathbb{R} \times \dots \times \mathbb{R}$). An element in a product ring is invertible if and only if each coordinate component is invertible in $\mathbb{R}$.
- **Zero-Row Non-Invertibility:** Any matrix with a complete row of zeros cannot be transformed into the identity matrix by row operations because no linear combination of other rows can create a pivot in a zero row.

---

## 6. Final Answer in Words
Matrix $D$ is invertible because all its diagonal entries are non-zero, giving a non-zero determinant of $-30$. Matrix $E$ is not invertible because its second diagonal entry is zero, giving a row of zeros and a determinant of $0$. The inverse of $D$ is the diagonal matrix $D^{-1} = \begin{pmatrix} 1/2 & 0 & 0 \\ 0 & -1/3 & 0 \\ 0 & 0 & 1/5 \end{pmatrix}$. Direct multiplication confirms $D D^{-1} = I_3$.

---

## 7. Quick Verification
- **Left product check:**
  $$D^{-1} D = \begin{pmatrix} 1/2 & 0 & 0 \\ 0 & -1/3 & 0 \\ 0 & 0 & 1/5 \end{pmatrix} \begin{pmatrix} 2 & 0 & 0 \\ 0 & -3 & 0 \\ 0 & 0 & 5 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = I_3 \quad \checkmark$$
- **Determinant product check:**
  $\det(D^{-1}) = \left(\frac{1}{2}\right)\left(-\frac{1}{3}\right)\left(\frac{1}{5}\right) = -\frac{1}{30} = \frac{1}{\det D} \quad \checkmark$

---

## 8. Common Mistakes to Avoid
- **Attempting to Invert Zero:** Writing $\frac{1}{0} = 0$ and claiming $E^{-1} = \operatorname{diag}(1/2, 0, 1/5)$. Division by zero is undefined.
- **Using Gauss-Jordan Elimination Unnecessarily:** Performing 10 steps of row operations when the diagonal structure allows writing the inverse down by inspection.
- **Negating Instead of Inverting:** Writing $D^{-1} = \operatorname{diag}(-2, 3, -5)$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"A diagonal matrix is invertible if and only if every single entry along its main diagonal is non-zero, which means $D$ is invertible with determinant $-30$, while $E$ is singular because it contains a zero on the diagonal. For an invertible diagonal matrix, we find the inverse simply by replacing each diagonal entry with its reciprocal, giving $D^{-1} = \operatorname{diag}(1/2, -1/3, 1/5)$. Multiplying $D$ by $D^{-1}$ confirms that each entry pairs with its reciprocal to produce the $3 \times 3$ identity matrix."

