# Exercise 6: Transpose

## 1. Original Problem
For the matrices:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix}$$
compute $A^T$, $B^T$, and $AB$. Then verify in this example that:
$$(AB)^T = B^T A^T.$$

---

## 2. What We Are Trying to Find
We need to:
- Find the transpose matrix $A^T$ by turning the rows of $A$ into columns.
- Find the transpose matrix $B^T$ by turning the rows of $B$ into columns.
- Compute the matrix product $AB$ and then take its transpose $(AB)^T$.
- Compute the reversed product of the transposes $B^T A^T$.
- Confirm that $(AB)^T$ and $B^T A^T$ produce the exact same matrix.

---

## 3. Key Concepts and Theorems
1. **Matrix Transpose ($M^T$):**
   The transpose of an $m \times n$ matrix $M$ is the $n \times m$ matrix $M^T$ obtained by reflecting $M$ over its main diagonal. Equivalently, the rows of $M$ become the columns of $M^T$:
   $$(M^T)_{ij} = M_{ji}$$
2. **Transpose of a Product Theorem (Order Reversal):**
   For any matrices $M$ and $N$ where the product $MN$ is defined, the transpose of the product equals the product of the transposes in **reverse order**:
   $$(MN)^T = N^T M^T$$
   *Why the order must reverse:* If $M$ is $m \times k$ and $N$ is $k \times n$, then $MN$ is $m \times n$, so $(MN)^T$ is $n \times m$. Looking at transposes, $M^T$ is $k \times m$ and $N^T$ is $n \times k$. The product $M^T N^T$ is undefined whenever $m \neq n$, whereas $N^T M^T$ has size $(n \times k)(k \times m) = n \times m$, perfectly matching $(MN)^T$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $A^T$
Matrix $A$ has size $2 \times 3$:
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$$
Convert Row 1 into Column 1, and Row 2 into Column 2. The resulting size is $3 \times 2$:
$$A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$

---

### Step 2: Compute $B^T$
Matrix $B$ has size $3 \times 2$:
$$B = \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix}$$
Convert the three rows into three columns. The resulting size is $2 \times 3$:
$$B^T = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{pmatrix}$$

---

### Step 3: Compute $AB$
$A$ is $2 \times 3$ and $B$ is $3 \times 2$, so $AB$ is a $2 \times 2$ matrix:
$$AB = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix}$$

Compute each entry by taking row-by-column dot products:
- **Entry $(AB)_{11}$** (Row 1 of $A$ $\cdot$ Column 1 of $B$):
  $$1(1) + 2(2) + 3(-1) = 1 + 4 - 3 = 2$$
- **Entry $(AB)_{12}$** (Row 1 of $A$ $\cdot$ Column 2 of $B$):
  $$1(0) + 2(1) + 3(3) = 0 + 2 + 9 = 11$$
- **Entry $(AB)_{21}$** (Row 2 of $A$ $\cdot$ Column 1 of $B$):
  $$4(1) + 5(2) + 6(-1) = 4 + 10 - 6 = 8$$
- **Entry $(AB)_{22}$** (Row 2 of $A$ $\cdot$ Column 2 of $B$):
  $$4(0) + 5(1) + 6(3) = 0 + 5 + 18 = 23$$

Thus:
$$AB = \begin{pmatrix} 2 & 11 \\ 8 & 23 \end{pmatrix}$$

---

### Step 4: Compute $(AB)^T$
Transpose the $2 \times 2$ matrix $AB$ by swapping its off-diagonal entries:
$$(AB)^T = \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix}$$

---

### Step 5: Compute $B^T A^T$
Now multiply $B^T$ ($2 \times 3$) by $A^T$ ($3 \times 2$):
$$B^T A^T = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$

Calculate each entry:
- **Entry $(B^T A^T)_{11}$:**
  $$1(1) + 2(2) + (-1)(3) = 1 + 4 - 3 = 2$$
- **Entry $(B^T A^T)_{12}$:**
  $$1(4) + 2(5) + (-1)(6) = 4 + 10 - 6 = 8$$
- **Entry $(B^T A^T)_{21}$:**
  $$0(1) + 1(2) + 3(3) = 0 + 2 + 9 = 11$$
- **Entry $(B^T A^T)_{22}$:**
  $$0(4) + 1(5) + 3(6) = 0 + 5 + 18 = 23$$

Thus:
$$B^T A^T = \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix}$$

---

### Step 6: Verify the Identity
Comparing the two matrices:
$$(AB)^T = \begin{pmatrix} 2 & 8 \\ 11 & 23 \end{pmatrix} = B^T A^T$$
The identity $(AB)^T = B^T A^T$ holds exactly.

---

## 5. Why Each Step Is Valid
- **Swapping Indices for Transposition:** Replacing entry $(i, j)$ with entry $(j, i)$ is the direct definition of matrix transposition.
- **Order Reversal in Multiplication:** In $(AB)^T$, the entry at position $(i, j)$ is $(AB)_{ji}$, which is the dot product of Row $j$ of $A$ and Column $i$ of $B$. Since Row $j$ of $A$ is Column $j$ of $A^T$ and Column $i$ of $B$ is Row $i$ of $B^T$, this dot product equals (Row $i$ of $B^T$) $\cdot$ (Column $j$ of $A^T$), which is by definition $(B^T A^T)_{ij}$.

---

## 6. Final Answer in Words
The transpose $A^T$ is the $3 \times 2$ matrix with rows $(1, 4)$, $(2, 5)$, and $(3, 6)$. The transpose $B^T$ is the $2 \times 3$ matrix with rows $(1, 2, -1)$ and $(0, 1, 3)$. The product $AB$ is the $2 \times 2$ matrix with top row $2, 11$ and bottom row $8, 23$. Its transpose $(AB)^T$ has top row $2, 8$ and bottom row $11, 23$. Computing $B^T A^T$ yields the identical matrix, confirming that $(AB)^T = B^T A^T$.

---

## 7. Quick Verification
- **Size compatibility:**
  - $A$ is $2 \times 3 \implies A^T$ is $3 \times 2$.
  - $B$ is $3 \times 2 \implies B^T$ is $2 \times 3$.
  - $B^T A^T$ is $(2 \times 3)(3 \times 2) = 2 \times 2$, which matches $(AB)^T$.
- **Attempting $A^T B^T$ to see the contradiction:**
  $A^T$ is $3 \times 2$ and $B^T$ is $2 \times 3$. The product $A^T B^T$ would have size $3 \times 3$, which cannot possibly equal $(AB)^T$ (which is $2 \times 2$). This confirms that reversing the order is mathematically necessary.

---

## 8. Common Mistakes to Avoid
- **Forgetting to Reverse Order:** Writing $(AB)^T = A^T B^T$. As shown by the size check, this is generally not even the same size.
- **Transposing Entries but Not Matrix Dimensions:** Keeping the original matrix shape when taking a transpose. A $2 \times 3$ matrix must always become a $3 \times 2$ matrix.
- **Sign Errors:** Dropping the minus sign on $-1$ when transposing or multiplying.

---

## 9. Classroom Presentation (3-Sentence Summary)
"To transpose a matrix, we swap its rows and columns, turning $A$ into a $3 \times 2$ matrix and $B$ into a $2 \times 3$ matrix. When multiplying $A$ and $B$, we obtain a $2 \times 2$ matrix whose transpose has rows $(2, 8)$ and $(11, 23)$. By calculating $B^T A^T$, we get the exact same matrix, illustrating the fundamental algebraic property that transposing a product always reverses the order of the matrices."

