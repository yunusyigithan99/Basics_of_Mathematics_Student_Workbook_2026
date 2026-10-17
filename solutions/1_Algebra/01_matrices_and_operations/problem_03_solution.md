# Exercise 3: When Can Matrices Be Multiplied?

## 1. Original Problem
The matrix sizes are:
$$A_{2\times3}, \qquad B_{3\times4}, \qquad C_{4\times2}, \qquad D_{2\times2}.$$
For the products:
$$AB, \quad BA, \quad BC, \quad CB, \quad AC, \quad CA, \quad AD, \quad DA$$
determine whether they are defined. If so, state the size of the result. Justify each decision using the dimension compatibility condition.

---

## 2. What We Are Trying to Find
We need to test eight specific pairs of matrix multiplications to determine:
- Whether each multiplication is legally allowed based on the dimensions of the matrices.
- The resulting size (number of rows and columns) for every defined product.
- A clear mathematical justification using the inner dimension rule for every case.

---

## 3. Key Concepts and Theorems
1. **Dimension Compatibility Condition (The Inner Dimension Rule):**
   The product of two matrices $M$ and $N$ is defined if and only if the number of **columns** in the first matrix equals the number of **rows** in the second matrix:
   $$\text{columns}(M) = \text{rows}(N)$$
   In symbol form:
   $$M_{m \times k} \cdot N_{k \times n} = P_{m \times n}$$
2. **Resulting Size:**
   - The "inner dimensions" (both equal to $k$) match and collapse.
   - The "outer dimensions" determine the shape of the result: $m$ rows and $n$ columns.
3. **If inner dimensions do not match:** The dot product between a row of the left matrix and a column of the right matrix cannot be computed because the two vectors have different lengths. Hence, the product is **undefined**.

---

## 4. Detailed Step-by-Step Solution

Let us test each product individually by writing the sizes side by side and inspecting the inner pair:

1. **Product $AB$:**
   - Sizes: $(2 \times \mathbf{3})$ and $(\mathbf{3} \times 4)$.
   - Check: The inner dimensions are both $3$ (they match).
   - **Status:** **Defined**.
   - **Result Size:** The outer dimensions are $2$ and $4$, so $AB$ has size **$2 \times 4$**.

2. **Product $BA$:**
   - Sizes: $(3 \times \mathbf{4})$ and $(\mathbf{2} \times 3)$.
   - Check: The inner dimensions are $4$ and $2$. Since $4 \neq 2$, they do not match.
   - **Status:** **Undefined**.

3. **Product $BC$:**
   - Sizes: $(3 \times \mathbf{4})$ and $(\mathbf{4} \times 2)$.
   - Check: The inner dimensions are both $4$ (they match).
   - **Status:** **Defined**.
   - **Result Size:** The outer dimensions are $3$ and $2$, so $BC$ has size **$3 \times 2$**.

4. **Product $CB$:**
   - Sizes: $(4 \times \mathbf{2})$ and $(\mathbf{3} \times 4)$.
   - Check: The inner dimensions are $2$ and $3$. Since $2 \neq 3$, they do not match.
   - **Status:** **Undefined**.

5. **Product $AC$:**
   - Sizes: $(2 \times \mathbf{3})$ and $(\mathbf{4} \times 2)$.
   - Check: The inner dimensions are $3$ and $4$. Since $3 \neq 4$, they do not match.
   - **Status:** **Undefined**.

6. **Product $CA$:**
   - Sizes: $(4 \times \mathbf{2})$ and $(\mathbf{2} \times 3)$.
   - Check: The inner dimensions are both $2$ (they match).
   - **Status:** **Defined**.
   - **Result Size:** The outer dimensions are $4$ and $3$, so $CA$ has size **$4 \times 3$**.

7. **Product $AD$:**
   - Sizes: $(2 \times \mathbf{3})$ and $(\mathbf{2} \times 2)$.
   - Check: The inner dimensions are $3$ and $2$. Since $3 \neq 2$, they do not match.
   - **Status:** **Undefined**.

8. **Product $DA$:**
   - Sizes: $(2 \times \mathbf{2})$ and $(\mathbf{2} \times 3)$.
   - Check: The inner dimensions are both $2$ (they match).
   - **Status:** **Defined**.
   - **Result Size:** The outer dimensions are $2$ and $3$, so $DA$ has size **$2 \times 3$**.

---

## 5. Why Each Step Is Valid
- **Inner Dimension Equality:** Each entry $(MN)_{ij}$ is calculated by taking the $i$-th row of $M$ and computing its dot product with the $j$-th column of $N$. This dot product requires the row and column to contain the exact same number of entries; otherwise, terms cannot be paired and multiplied.
- **Outer Dimension Inheritance:** The number of rows in the resulting matrix equals the number of available rows in the first matrix, and the number of columns equals the number of available columns in the second matrix.

---

## 6. Final Answer in Words
Of the eight proposed products, exactly four are defined and four are undefined:
- $AB$ is defined with size $2 \times 4$.
- $BA$ is undefined because the inner sizes $4$ and $2$ do not match.
- $BC$ is defined with size $3 \times 2$.
- $CB$ is undefined because the inner sizes $2$ and $3$ do not match.
- $AC$ is undefined because the inner sizes $3$ and $4$ do not match.
- $CA$ is defined with size $4 \times 3$.
- $AD$ is undefined because the inner sizes $3$ and $2$ do not match.
- $DA$ is defined with size $2 \times 3$.

---

## 7. Quick Verification
We can summarize the decisions in a clear verification table:

| Product | Size Setup | Inner Pair Equal? | Status | Resulting Size |
| :---: | :---: | :---: | :---: | :---: |
| $AB$ | $(2 \times 3)(3 \times 4)$ | $3 = 3$ (Yes) | Defined | $2 \times 4$ |
| $BA$ | $(3 \times 4)(2 \times 3)$ | $4 \neq 2$ (No) | Undefined | — |
| $BC$ | $(3 \times 4)(4 \times 2)$ | $4 = 4$ (Yes) | Defined | $3 \times 2$ |
| $CB$ | $(4 \times 2)(3 \times 4)$ | $2 \neq 3$ (No) | Undefined | — |
| $AC$ | $(2 \times 3)(4 \times 2)$ | $3 \neq 4$ (No) | Undefined | — |
| $CA$ | $(4 \times 2)(2 \times 3)$ | $2 = 2$ (Yes) | Defined | $4 \times 3$ |
| $AD$ | $(2 \times 3)(2 \times 2)$ | $3 \neq 2$ (No) | Undefined | — |
| $DA$ | $(2 \times 2)(2 \times 3)$ | $2 = 2$ (Yes) | Defined | $2 \times 3$ |

---

## 8. Common Mistakes to Avoid
- **Assuming Multiplication Commutes:** Believing that because $AB$ is defined, $BA$ must also be defined. As seen with $AB$ and $BA$, one can exist while the other does not.
- **Matching Outer Dimensions Instead of Inner:** Checking if row counts match rather than comparing the columns of the first with the rows of the second.
- **Reporting the Inner Size as the Result:** Mistakenly writing that $(2 \times 3)(3 \times 4)$ produces a $3 \times 3$ matrix instead of $2 \times 4$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"To determine if two matrices can be multiplied, we check whether the number of columns in the first matrix matches the number of rows in the second. If this inner pair of numbers matches, multiplication is defined, and the outer numbers give the dimensions of the resulting matrix. In this exercise, $AB$, $BC$, $CA$, and $DA$ satisfy this condition, while the other four products are undefined because their inner dimensions disagree."

