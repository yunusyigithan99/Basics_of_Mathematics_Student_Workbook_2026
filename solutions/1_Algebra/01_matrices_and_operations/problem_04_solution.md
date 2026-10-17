# Exercise 4: Matrix Multiplication and Noncommutativity

## 1. Original Problem
For the matrices:
$$A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & 0 \\ 3 & 1 \end{pmatrix}$$
compute $AB$ and $BA$. Is $AB = BA$? Use this example to explain what noncommutativity of matrix multiplication means.

---

## 2. What We Are Trying to Find
We need to:
- Compute the product $AB$ using standard matrix multiplication.
- Compute the product $BA$ with the order of matrices reversed.
- Compare the two resulting matrices to test if $AB = BA$.
- Explain the concept of noncommutativity in matrix algebra compared to the multiplication of real numbers.

---

## 3. Key Concepts and Theorems
1. **Matrix Multiplication Rule (Row-by-Column):**
   If $A$ is an $m \times k$ matrix and $B$ is a $k \times n$ matrix, the entry in row $i$ and column $j$ of the product $C = AB$ is computed by taking the dot product of row $i$ of $A$ with column $j$ of $B$:
   $$c_{ij} = \sum_{r=1}^k a_{ir} b_{rj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \dots + a_{ik}b_{kj}$$
2. **Noncommutativity:**
   An operation $*$ on a set is commutative if $x * y = y * x$ for all elements. For real numbers, multiplication is commutative ($3 \cdot 5 = 5 \cdot 3 = 15$). In contrast, matrix multiplication is generally **noncommutative**: even when both products $AB$ and $BA$ are well-defined and have the same dimensions, $AB \neq BA$ in general.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Product $AB$
Write the matrices side by side:
$$AB = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 3 & 1 \end{pmatrix}$$

Calculate each entry of the resulting $2 \times 2$ matrix:
- **Top-left entry $(AB)_{11}$** (Row 1 of $A$ $\cdot$ Column 1 of $B$):
  $$(AB)_{11} = 1 \cdot 2 + 2 \cdot 3 = 2 + 6 = 8$$
- **Top-right entry $(AB)_{12}$** (Row 1 of $A$ $\cdot$ Column 2 of $B$):
  $$(AB)_{12} = 1 \cdot 0 + 2 \cdot 1 = 0 + 2 = 2$$
- **Bottom-left entry $(AB)_{21}$** (Row 2 of $A$ $\cdot$ Column 1 of $B$):
  $$(AB)_{21} = 0 \cdot 2 + 1 \cdot 3 = 0 + 3 = 3$$
- **Bottom-right entry $(AB)_{22}$** (Row 2 of $A$ $\cdot$ Column 2 of $B$):
  $$(AB)_{22} = 0 \cdot 0 + 1 \cdot 1 = 0 + 1 = 1$$

Assembling the entries:
$$AB = \begin{pmatrix} 8 & 2 \\ 3 & 1 \end{pmatrix}$$

---

### Step 2: Compute the Product $BA$
Now reverse the order of the factors:
$$BA = \begin{pmatrix} 2 & 0 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$$

Calculate each entry:
- **Top-left entry $(BA)_{11}$** (Row 1 of $B$ $\cdot$ Column 1 of $A$):
  $$(BA)_{11} = 2 \cdot 1 + 0 \cdot 0 = 2 + 0 = 2$$
- **Top-right entry $(BA)_{12}$** (Row 1 of $B$ $\cdot$ Column 2 of $A$):
  $$(BA)_{12} = 2 \cdot 2 + 0 \cdot 1 = 4 + 0 = 4$$
- **Bottom-left entry $(BA)_{21}$** (Row 2 of $B$ $\cdot$ Column 1 of $A$):
  $$(BA)_{21} = 3 \cdot 1 + 1 \cdot 0 = 3 + 0 = 3$$
- **Bottom-right entry $(BA)_{22}$** (Row 2 of $B$ $\cdot$ Column 2 of $A$):
  $$(BA)_{22} = 3 \cdot 2 + 1 \cdot 1 = 6 + 1 = 7$$

Assembling the entries:
$$BA = \begin{pmatrix} 2 & 4 \\ 3 & 7 \end{pmatrix}$$

---

### Step 3: Compare $AB$ and $BA$
$$AB = \begin{pmatrix} 8 & 2 \\ 3 & 1 \end{pmatrix}, \qquad BA = \begin{pmatrix} 2 & 4 \\ 3 & 7 \end{pmatrix}$$
Since three out of the four corresponding entries differ (e.g., $(AB)_{11} = 8 \neq 2 = (BA)_{11}$), we conclude:
$$AB \neq BA$$

---

### Step 4: Explanation of Noncommutativity
In scalar arithmetic, multiplying numbers simply scales an amount, and scaling by $a$ then $b$ is identical to scaling by $b$ then $a$. In contrast, matrices represent linear transformations (such as shears, rotations, and projections) or composite system mappings. Reversing the order of matrices changes which transformation is applied first and pairs different rows with different columns in the dot products. Therefore, matrix multiplication depends fundamentally on the sequence of operations.

---

## 5. Why Each Step Is Valid
- **Computing Row-Column Dot Products:** The product of two matrices represents the composition of their corresponding linear functions; the algebraic dot product formula is the exact algebraic equivalent of function composition.
- **Comparing Entry-by-Entry:** By definition, two matrices are equal if and only if they have the same size and every corresponding entry is equal. Finding even a single mismatched entry is mathematically sufficient to prove inequality.

---

## 6. Final Answer in Words
The product $AB$ equals the matrix with first row $8, 2$ and second row $3, 1$. The reversed product $BA$ equals the matrix with first row $2, 4$ and second row $3, 7$. Because these two result matrices are not equal, $AB \neq BA$. This demonstrates that matrix multiplication is noncommutative: changing the order of the matrices changes the final outcome.

---

## 7. Quick Verification
- **Trace check (sum of diagonal entries):**
  - $\operatorname{tr}(AB) = 8 + 1 = 9$
  - $\operatorname{tr}(BA) = 2 + 7 = 9$
  - *Mathematical theorem:* For any square matrices of matching size, $\operatorname{tr}(AB) = \operatorname{tr}(BA)$. Our results both sum to $9$, verifying an essential algebraic property while confirming that individual entries differ.
- **Determinant check:**
  - $\det(A) = 1 \cdot 1 - 2 \cdot 0 = 1$
  - $\det(B) = 2 \cdot 1 - 0 \cdot 3 = 2$
  - $\det(AB) = 8 \cdot 1 - 2 \cdot 3 = 8 - 6 = 2 = \det(A)\det(B) \quad \checkmark$
  - $\det(BA) = 2 \cdot 7 - 4 \cdot 3 = 14 - 12 = 2 = \det(B)\det(A) \quad \checkmark$

---

## 8. Common Mistakes to Avoid
- **Multiplying Element-by-Element (Hadamard product):** Multiplying $a_{11}$ by $b_{11}$, $a_{12}$ by $b_{12}$, etc., rather than using the row-by-column dot product rule.
- **Assuming Commutativity Automatically Holds:** Treating $AB$ and $BA$ as interchangeable in algebraic simplifications like $(A+B)^2 = A^2 + 2AB + B^2$ (which is false for matrices because $AB + BA \neq 2AB$).
- **Row/Column Inversion in Dot Products:** Multiplying columns of the first matrix by rows of the second matrix.

---

## 9. Classroom Presentation (3-Sentence Summary)
"By calculating the row-by-column products, we find that $AB = \begin{pmatrix}8&2\\3&1\end{pmatrix}$, whereas reversing the order gives $BA = \begin{pmatrix}2&4\\3&7\end{pmatrix}$. Because these two results are completely different, this calculation proves that matrix multiplication does not commute. In geometric terms, this means that the sequence in which two transformations are applied directly changes the final outcome."

