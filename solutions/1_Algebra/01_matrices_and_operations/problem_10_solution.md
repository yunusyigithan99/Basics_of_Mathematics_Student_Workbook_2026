# Exercise 10: Columns of a Matrix Product

## 1. Original Problem
Given:
$$A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 2 \\ -1 & 0 \\ 3 & 1 \end{pmatrix}$$
Denote the columns of $B$ by $\mathbf{b}_1, \mathbf{b}_2$.

1. Compute $A\mathbf{b}_1$ and $A\mathbf{b}_2$.
2. Compute the matrix $AB$.
3. Compare the results and explain why the columns of $AB$ are exactly the vectors $A\mathbf{b}_1$ and $A\mathbf{b}_2$.

---

## 2. What We Are Trying to Find
We need to:
- Partition matrix $B$ into its two individual column vectors, $\mathbf{b}_1$ and $\mathbf{b}_2$.
- Multiply matrix $A$ separately by each column vector to obtain $A\mathbf{b}_1$ and $A\mathbf{b}_2$.
- Compute the full matrix product $AB$.
- Compare the two computed vectors with the columns of the matrix product $AB$ and explain the algebraic theorem connecting matrix multiplication to column-by-column transformation.

---

## 3. Key Concepts and Theorems
1. **Column Partition of a Matrix:**
   Any $k \times n$ matrix $B$ can be written in partitioned column form:
   $$B = \begin{pmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \dots & \mathbf{b}_n \end{pmatrix}$$
   where each $\mathbf{b}_j$ is a $k \times 1$ column vector.
2. **Column Principle of Matrix Multiplication:**
   When multiplying matrix $A$ by matrix $B$, the $j$-th column of the product matrix $AB$ is precisely equal to matrix $A$ multiplied by the $j$-th column of $B$:
   $$\operatorname{col}_j(AB) = A \cdot \mathbf{b}_j$$
   Therefore:
   $$AB = A \begin{pmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \dots & \mathbf{b}_n \end{pmatrix} = \begin{pmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & \dots & A\mathbf{b}_n \end{pmatrix}$$
   This principle reveals that full matrix multiplication is simply several matrix-vector multiplications executed side by side in parallel.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Columns of $B$
Matrix $B$ has size $3 \times 2$:
$$B = \begin{pmatrix} 1 & 2 \\ -1 & 0 \\ 3 & 1 \end{pmatrix}$$
Its two columns are:
$$\mathbf{b}_1 = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}, \qquad \mathbf{b}_2 = \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}$$

---

### Step 2: Compute $A\mathbf{b}_1$ and $A\mathbf{b}_2$
Matrix $A$ has size $2 \times 3$, and each column vector is $3 \times 1$, resulting in a $2 \times 1$ vector.

- **Multiply $A$ by $\mathbf{b}_1$:**
  $$A\mathbf{b}_1 = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}$$
  - Top entry: $1(1) + 2(-1) + 0(3) = 1 - 2 + 0 = -1$
  - Bottom entry: $0(1) + 1(-1) + 1(3) = 0 - 1 + 3 = 2$
  $$A\mathbf{b}_1 = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$$

- **Multiply $A$ by $\mathbf{b}_2$:**
  $$A\mathbf{b}_2 = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}$$
  - Top entry: $1(2) + 2(0) + 0(1) = 2 + 0 + 0 = 2$
  - Bottom entry: $0(2) + 1(0) + 1(1) = 0 + 0 + 1 = 1$
  $$A\mathbf{b}_2 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$

---

### Step 3: Compute the Matrix Product $AB$
Matrix $A$ ($2 \times 3$) and $B$ ($3 \times 2$) produce a $2 \times 2$ matrix:
$$AB = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ -1 & 0 \\ 3 & 1 \end{pmatrix}$$

Evaluate each entry $(AB)_{ij}$ as Row $i$ of $A$ $\cdot$ Column $j$ of $B$:
- **Top-left $(AB)_{11}$:** $1(1) + 2(-1) + 0(3) = -1$
- **Top-right $(AB)_{12}$:** $1(2) + 2(0) + 0(1) = 2$
- **Bottom-left $(AB)_{21}$:** $0(1) + 1(-1) + 1(3) = 2$
- **Bottom-right $(AB)_{22}$:** $0(2) + 1(0) + 1(1) = 1$

Assembling the matrix:
$$AB = \begin{pmatrix} -1 & 2 \\ 2 & 1 \end{pmatrix}$$

---

### Step 4: Comparison and Explanation
Observe the columns of $AB$:
- The first column of $AB$ is $\begin{pmatrix} -1 \\ 2 \end{pmatrix}$, which is identical to $A\mathbf{b}_1$.
- The second column of $AB$ is $\begin{pmatrix} 2 \\ 1 \end{pmatrix}$, which is identical to $A\mathbf{b}_2$.
Therefore:
$$AB = \begin{pmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 \end{pmatrix}$$

**Why this holds:**
By the entry-wise definition of matrix multiplication, the element in row $i$ and column $j$ of $AB$ is:
$$(AB)_{ij} = \sum_{k=1}^3 a_{ik} b_{kj}$$
Notice that for a fixed column index $j$, the numbers $b_{1j}, b_{2j}, b_{3j}$ are precisely the entries of the vector $\mathbf{b}_j$. Thus, as $i$ varies across the rows, $(AB)_{ij}$ traces out the exact row-by-vector dot products that define the vector $A\mathbf{b}_j$. In essence, matrix multiplication applies the transformation $A$ to each column vector of $B$ independently.

---

## 5. Why Each Step Is Valid
- **Linear Transformation on Basis/Column Sets:** Matrix $A$ represents a linear map $T(\mathbf{x}) = A\mathbf{x}$. Applying $T$ to a collection of vectors $[\mathbf{b}_1, \mathbf{b}_2]$ maps them to $[T(\mathbf{b}_1), T(\mathbf{b}_2)]$, which matches the block matrix definition.
- **Entry Equivalence:** The summation $\sum_{k} a_{ik} b_{kj}$ is identical whether evaluated as part of a single vector product $A\mathbf{b}_j$ or within the full matrix $AB$.

---

## 6. Final Answer in Words
The product $A\mathbf{b}_1$ is the vector $\begin{pmatrix} -1 \\ 2 \end{pmatrix}$ and $A\mathbf{b}_2$ is the vector $\begin{pmatrix} 2 \\ 1 \end{pmatrix}$. The full matrix product $AB$ is the $2 \times 2$ matrix with first row $-1, 2$ and second row $2, 1$. The columns of $AB$ match $A\mathbf{b}_1$ and $A\mathbf{b}_2$ exactly because multiplying a matrix $A$ by a matrix $B$ is algebraically equivalent to multiplying $A$ by each column of $B$ individually and placing the resulting column vectors side by side.

---

## 7. Quick Verification
- **Reconstruction check:**
  Writing the columns side by side:
  $$\begin{pmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 \end{pmatrix} = \begin{pmatrix} -1 & 2 \\ 2 & 1 \end{pmatrix} = AB \quad \checkmark$$
- **Linear combination check for column 1:**
  $$1 \begin{pmatrix} 1 \\ 0 \end{pmatrix} - 1 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 3 \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 - 2 + 0 \\ 0 - 1 + 3 \end{pmatrix} = \begin{pmatrix} -1 \\ 2 \end{pmatrix} = A\mathbf{b}_1 \quad \checkmark$$
- **Linear combination check for column 2:**
  $$2 \begin{pmatrix} 1 \\ 0 \end{pmatrix} + 0 \begin{pmatrix} 2 \\ 1 \end{pmatrix} + 1 \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 + 0 + 0 \\ 0 + 0 + 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} = A\mathbf{b}_2 \quad \checkmark$$

---

## 8. Common Mistakes to Avoid
- **Treating Columns as Rows:** Packing $A\mathbf{b}_1$ and $A\mathbf{b}_2$ into horizontal rows of the product matrix instead of vertical columns.
- **Thinking Matrix-Vector and Matrix-Matrix Multiplication are Different Rules:** Failing to see that full matrix multiplication is just parallel matrix-vector multiplication.
- **Dimension Confusion:** Expecting $A\mathbf{b}_1$ to produce a $3 \times 1$ vector because $B$ has $3$ rows, rather than a $2 \times 1$ vector dictated by the $2$ rows of $A$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"When we multiply matrix $A$ by the individual columns of $B$, we obtain the vectors $\begin{pmatrix}-1\\2\end{pmatrix}$ and $\begin{pmatrix}2\\1\end{pmatrix}$. Computing the full matrix product $AB$ directly gives the matrix $\begin{pmatrix}-1&2\\2&1\end{pmatrix}$, whose columns are identical to these two vectors. This confirms the fundamental column principle of linear algebra: multiplying two matrices simply means transforming every column of the second matrix by the first matrix in parallel."

