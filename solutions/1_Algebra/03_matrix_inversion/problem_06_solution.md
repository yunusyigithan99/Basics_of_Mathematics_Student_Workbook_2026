# Exercise 6: Solving a System Using the Inverse

## 1. Original Problem
Solve:
$$Ax = b$$
where:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}, \qquad b = \begin{pmatrix} 5 \\ 7 \end{pmatrix}$$
using $x = A^{-1}b$. Then substitute the resulting vector back into the equation and check the result.

---

## 2. What We Are Trying to Find
We need to:
- Find the inverse matrix $A^{-1}$ for the coefficient matrix $A$.
- Multiply $A^{-1}$ by the right-hand side constant vector $b$ on the left to compute the solution vector $x = A^{-1}b$.
- Substitute the computed solution vector $x$ back into the original matrix equation $Ax = b$ to verify that both equations are satisfied.

---

## 3. Key Concepts and Theorems
1. **Matrix Inversion Method for Linear Systems:**
   If a system of $n$ linear equations with $n$ unknowns is written in matrix form $Ax = b$, and if the coefficient matrix $A$ is invertible ($\det A \neq 0$), then multiplying both sides on the left by $A^{-1}$ isolates $x$:
   $$A^{-1}(Ax) = A^{-1}b \implies (A^{-1}A)x = A^{-1}b \implies Ix = A^{-1}b \implies x = A^{-1}b$$
   This yields the unique solution directly as a matrix-vector product.
2. **Formula for $2 \times 2$ Inverse:**
   $$A^{-1} = \frac{1}{\det A}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Determinant and Inverse of $A$
For $A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$:
$$\det A = (2 \cdot 3) - (1 \cdot 1) = 6 - 1 = 5$$
Since $\det A = 5 \neq 0$, the inverse exists.

Apply the $2 \times 2$ inverse formula (swap main diagonal entries, negate off-diagonal entries, divide by 5):
$$A^{-1} = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$$

---

### Step 2: Compute the Solution Vector $x = A^{-1}b$
Multiply $A^{-1}$ by vector $b = \begin{pmatrix} 5 \\ 7 \end{pmatrix}$:
$$x = A^{-1}b = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 5 \\ 7 \end{pmatrix}$$

Perform the row-by-vector dot products:
- First component: $3(5) + (-1)(7) = 15 - 7 = 8$
- Second component: $-1(5) + 2(7) = -5 + 14 = 9$

Multiply by the scalar $\frac{1}{5}$:
$$x = \frac{1}{5} \begin{pmatrix} 8 \\ 9 \end{pmatrix} = \begin{pmatrix} \frac{8}{5} \\ \frac{9}{5} \end{pmatrix}$$

Thus, $x_1 = \frac{8}{5} = 1.6$ and $x_2 = \frac{9}{5} = 1.8$.

---

### Step 3: Substitute $x$ Back into $Ax = b$ to Verify
Multiply matrix $A$ by our solution vector $x$:
$$Ax = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} \frac{8}{5} \\ \frac{9}{5} \end{pmatrix}$$

Evaluate each row:
- **First equation:**
  $$2\left(\frac{8}{5}\right) + 1\left(\frac{9}{5}\right) = \frac{16}{5} + \frac{9}{5} = \frac{25}{5} = 5$$
- **Second equation:**
  $$1\left(\frac{8}{5}\right) + 3\left(\frac{9}{5}\right) = \frac{8}{5} + \frac{27}{5} = \frac{35}{5} = 7$$

Assembling the result:
$$Ax = \begin{pmatrix} 5 \\ 7 \end{pmatrix} = b$$
Both equations match the right-hand side vector $b$ exactly!

---

## 5. Why Each Step Is Valid
- **Left Multiplication Associativity:** We must multiply by $A^{-1}$ from the left because matrix multiplication is noncommutative ($x A^{-1}$ is undefined). Associativity $(A^{-1}A)x = I x = x$ rigorously isolates the variable vector.
- **Substitution Consistency:** A vector is a true solution to a linear system if and only if replacing the variables with their numeric values yields true equalities in all constituent equations simultaneously.

---

## 6. Final Answer in Words
The inverse of the coefficient matrix is $A^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$. Multiplying this inverse by the constant vector $b = \begin{pmatrix} 5 \\ 7 \end{pmatrix}$ yields the unique solution vector $x = \begin{pmatrix} 8/5 \\ 9/5 \end{pmatrix}$. Substituting this vector back into $Ax$ produces $\begin{pmatrix} 5 \\ 7 \end{pmatrix}$, confirming that the system is completely satisfied.

---

## 7. Quick Verification
- **Cramer's Rule check:**
  - $D = \det A = 5$.
  - $D_1 = \det\begin{pmatrix} 5 & 1 \\ 7 & 3 \end{pmatrix} = 15 - 7 = 8 \implies x_1 = \frac{D_1}{D} = \frac{8}{5} \quad \checkmark$
  - $D_2 = \det\begin{pmatrix} 2 & 5 \\ 1 & 7 \end{pmatrix} = 14 - 5 = 9 \implies x_2 = \frac{D_2}{D} = \frac{9}{5} \quad \checkmark$
Cramer's rule gives identical coordinates!

---

## 8. Common Mistakes to Avoid
- **Multiplying on the Wrong Side:** Writing $b A^{-1}$ instead of $A^{-1}b$. An $n \times 1$ vector cannot be multiplied on the right by an $n \times n$ matrix.
- **Sign Slips in $A^{-1}$:** Forgetting that the off-diagonal entries change signs to $-1$ and $-1$.
- **Losing the Determinant Factor:** Dropping the $\frac{1}{5}$ factor, which would lead to the unscaled answer $\begin{pmatrix} 8 \\ 9 \end{pmatrix}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"To solve $Ax = b$ using matrix inversion, we first find $A^{-1} = \frac{1}{5}\begin{pmatrix}3&-1\\-1&2\end{pmatrix}$ using the $2 \times 2$ determinant formula. Multiplying $A^{-1}$ on the left by $b = \begin{pmatrix}5\\7\end{pmatrix}$ isolates the solution vector as $x = \begin{pmatrix}8/5\\9/5\end{pmatrix}$. Substituting these coordinates back into the original equations yields $\begin{pmatrix}5\\7\end{pmatrix}$, verifying that our solution is correct."

