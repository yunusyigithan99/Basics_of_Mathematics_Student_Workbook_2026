# Exercise 5: Matrix Times Vector

## 1. Original Problem
Let:
$$A = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}, \qquad x = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$$
Compute $Ax$. Then express $Ax$ as a linear combination of the columns of $A$, with coefficients coming from the vector $x$.

---

## 2. What We Are Trying to Find
We need to:
- Compute the matrix-vector product $Ax$ using the standard row-by-column method.
- Re-interpret the exact same calculation as a linear combination where each column of $A$ is scaled by the corresponding coordinate of $x$.
- Show that both perspectives yield the exact same resulting vector.

---

## 3. Key Concepts and Theorems
1. **Row View of Matrix-Vector Multiplication:**
   Each entry of the product $Ax$ is the dot product of a row of $A$ with the vector $x$:
   $$(Ax)_i = \sum_{j=1}^n a_{ij} x_j$$
2. **Column View of Matrix-Vector Multiplication:**
   The product $Ax$ is fundamentally a **linear combination of the columns of $A$**, weighted by the entries of $x$:
   If the columns of $A$ are $\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_n$ and $x = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$, then:
   $$Ax = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \dots + x_n \mathbf{a}_n$$
   This column view is one of the most fundamental ideas in all of linear algebra.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $Ax$ via Row-by-Column Multiplication
Matrix $A$ is $2 \times 2$ and vector $x$ is $2 \times 1$, so the result is a $2 \times 1$ column vector:
$$Ax = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 2 \end{pmatrix}$$

- **First entry (Row 1 $\cdot$ $x$):**
  $$2 \cdot 4 + (-1) \cdot 2 = 8 - 2 = 6$$
- **Second entry (Row 2 $\cdot$ $x$):**
  $$1 \cdot 4 + 3 \cdot 2 = 4 + 6 = 10$$

Thus:
$$Ax = \begin{pmatrix} 6 \\ 10 \end{pmatrix}$$

---

### Step 2: Identify the Columns of $A$ and the Scalars in $x$
- The columns of matrix $A$ are:
  $$\mathbf{a}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \qquad \mathbf{a}_2 = \begin{pmatrix} -1 \\ 3 \end{pmatrix}$$
- The scalar components of vector $x$ are:
  $$x_1 = 4, \qquad x_2 = 2$$

---

### Step 3: Express $Ax$ as a Linear Combination of Columns
Set up the linear combination using the scalar weights from $x$:
$$Ax = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 = 4 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 2 \begin{pmatrix} -1 \\ 3 \end{pmatrix}$$

Perform scalar multiplication on each column vector:
$$4 \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 4 \cdot 2 \\ 4 \cdot 1 \end{pmatrix} = \begin{pmatrix} 8 \\ 4 \end{pmatrix}$$
$$2 \begin{pmatrix} -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 \cdot (-1) \\ 2 \cdot 3 \end{pmatrix} = \begin{pmatrix} -2 \\ 6 \end{pmatrix}$$

Add the two resulting vectors together:
$$\begin{pmatrix} 8 \\ 4 \end{pmatrix} + \begin{pmatrix} -2 \\ 6 \end{pmatrix} = \begin{pmatrix} 8 + (-2) \\ 4 + 6 \end{pmatrix} = \begin{pmatrix} 6 \\ 10 \end{pmatrix}$$

---

## 5. Why Each Step Is Valid
- **Equivalence of Algebraic Formulations:** Expanding $x_1 \begin{pmatrix} a_{11} \\ a_{21} \end{pmatrix} + x_2 \begin{pmatrix} a_{12} \\ a_{22} \end{pmatrix}$ yields $\begin{pmatrix} a_{11}x_1 + a_{12}x_2 \\ a_{21}x_1 + a_{22}x_2 \end{pmatrix}$, which matches the row dot-product definition line for line.
- **Linear Space Axioms:** Vector scaling and vector addition are closed and associative in $\mathbb{R}^2$, guaranteeing that both evaluation orders produce the identical element.

---

## 6. Final Answer in Words
The product $Ax$ is the column vector with entries $6$ and $10$. Expressed as a linear combination of the columns of matrix $A$ using the weights from vector $x$, it is written as $4$ times the column vector $\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ plus $2$ times the column vector $\begin{pmatrix} -1 \\ 3 \end{pmatrix}$, which simplifies to $\begin{pmatrix} 8 \\ 4 \end{pmatrix} + \begin{pmatrix} -2 \\ 6 \end{pmatrix} = \begin{pmatrix} 6 \\ 10 \end{pmatrix}$.

---

## 7. Quick Verification
- **Consistency between methods:**
  - Row method output: $\begin{pmatrix} 6 \\ 10 \end{pmatrix}$.
  - Column method output: $\begin{pmatrix} 6 \\ 10 \end{pmatrix}$.
  - Both outputs match perfectly.
- **Inverse check:**
  Since $\det(A) = 2(3) - (-1)(1) = 7 \neq 0$, the inverse exists:
  $$A^{-1} = \frac{1}{7}\begin{pmatrix} 3 & 1 \\ -1 & 2 \end{pmatrix}$$
  Checking $A^{-1}(Ax)$:
  $$\frac{1}{7}\begin{pmatrix} 3 & 1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 6 \\ 10 \end{pmatrix} = \frac{1}{7} \begin{pmatrix} 3(6) + 1(10) \\ -1(6) + 2(10) \end{pmatrix} = \frac{1}{7} \begin{pmatrix} 28 \\ 14 \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix} = x \quad \checkmark$$

---

## 8. Common Mistakes to Avoid
- **Writing $Ax$ as a Row Vector:** Forgetting that an $m \times n$ matrix times an $n \times 1$ vector produces an $m \times 1$ column vector, not a horizontal row.
- **Swapping Coefficients:** Multiplying the first column by $2$ and the second column by $4$. The first coordinate $x_1$ always scales the first column, and $x_2$ scales the second.
- **Treating $Ax$ as Scalar Multiplication:** Attempting to multiply every entry of $A$ by vector $x$ as if $x$ were a single number.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Multiplying matrix $A$ by vector $x$ can be viewed either by taking the dot product of each row with $x$, or by taking a linear combination of the columns of $A$ weighted by the entries of $x$. Using the column perspective, $Ax$ equals $4$ times the first column plus $2$ times the second column. Both perspectives yield the exact same result: the column vector $\begin{pmatrix}6\\10\end{pmatrix}$."

