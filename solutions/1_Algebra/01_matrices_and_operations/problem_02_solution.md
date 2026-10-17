# Exercise 2: Addition and Scalar Multiplication

## 1. Original Problem
For the matrices:
$$A = \begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix}, \qquad B = \begin{pmatrix} 4 & -2 \\ 0 & 5 \end{pmatrix}$$
compute:
$$A + B, \qquad A - B, \qquad 3A - 2B.$$
Explain why matrix addition is possible only for matrices of the same size.

---

## 2. What We Are Trying to Find
We need to:
- Add matrices $A$ and $B$ together.
- Subtract matrix $B$ from matrix $A$.
- Scale matrix $A$ by $3$ and matrix $B$ by $2$, then compute their difference ($3A - 2B$).
- Provide a clear mathematical reason why two matrices must share the exact same dimensions to be added.

---

## 3. Key Concepts and Theorems
1. **Entry-by-Entry Addition and Subtraction:** If matrices $A = (a_{ij})$ and $B = (b_{ij})$ have the same size $m \times n$, their sum $A + B$ and difference $A - B$ are formed by adding or subtracting corresponding entries:
   $$(A + B)_{ij} = a_{ij} + b_{ij}, \qquad (A - B)_{ij} = a_{ij} - b_{ij}$$
2. **Scalar Multiplication:** Multiplying a matrix by a scalar $c \in \mathbb{R}$ scales every individual entry by that scalar:
   $$(cA)_{ij} = c \cdot a_{ij}$$
3. **Compatibility for Addition:** Addition requires a one-to-one pairing of entries. If two matrices have different dimensions, at least one entry will lack a partner, leaving the operation undefined.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Check Dimensions
Both $A$ and $B$ have $2$ rows and $2$ columns (size $2 \times 2$). Because their dimensions match, addition, subtraction, and linear combinations are well-defined.

### Step 2: Compute $A + B$
Add the numbers sitting at matching positions:
$$A + B = \begin{pmatrix} 1 + 4 & 2 + (-2) \\ -1 + 0 & 3 + 5 \end{pmatrix} = \begin{pmatrix} 5 & 0 \\ -1 & 8 \end{pmatrix}$$

### Step 3: Compute $A - B$
Subtract each entry of $B$ from the matching entry of $A$:
$$A - B = \begin{pmatrix} 1 - 4 & 2 - (-2) \\ -1 - 0 & 3 - 5 \end{pmatrix} = \begin{pmatrix} -3 & 2 + 2 \\ -1 & -2 \end{pmatrix} = \begin{pmatrix} -3 & 4 \\ -1 & -2 \end{pmatrix}$$

### Step 4: Compute $3A - 2B$
- First, scale matrix $A$ by $3$:
  $$3A = 3 \begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 3 \cdot 1 & 3 \cdot 2 \\ 3 \cdot (-1) & 3 \cdot 3 \end{pmatrix} = \begin{pmatrix} 3 & 6 \\ -3 & 9 \end{pmatrix}$$
- Second, scale matrix $B$ by $2$:
  $$2B = 2 \begin{pmatrix} 4 & -2 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 2 \cdot 4 & 2 \cdot (-2) \\ 2 \cdot 0 & 2 \cdot 5 \end{pmatrix} = \begin{pmatrix} 8 & -4 \\ 0 & 10 \end{pmatrix}$$
- Now subtract $2B$ from $3A$:
  $$3A - 2B = \begin{pmatrix} 3 - 8 & 6 - (-4) \\ -3 - 0 & 9 - 10 \end{pmatrix} = \begin{pmatrix} -5 & 6 + 4 \\ -3 & -1 \end{pmatrix} = \begin{pmatrix} -5 & 10 \\ -3 & -1 \end{pmatrix}$$

### Step 5: Explanation of Dimension Compatibility
Matrix addition is defined as an entry-by-entry operation where $(A+B)_{ij} = a_{ij} + b_{ij}$. For this rule to make sense, every single entry in the first matrix must have exactly one corresponding entry in the second matrix with identical row and column coordinates. If the matrices have different dimensions (for example, a $2 \times 3$ and a $2 \times 2$), certain positions would have nothing to add to, so the operation cannot exist.

---

## 5. Why Each Step Is Valid
- **Matching entries:** Adding and subtracting corresponding entries preserves the algebraic vector space structure of $\mathbb{R}^{m \times n}$.
- **Distributing the scalar:** Scalar multiplication is distributive over entry-level arithmetic: each component is multiplied independently by the constant.
- **Order of operations:** Scaling before subtracting follows the standard algebraic rule that scalar multiplication takes precedence over matrix subtraction.

---

## 6. Final Answer in Words
The sum $A + B$ is the $2 \times 2$ matrix with top row $5, 0$ and bottom row $-1, 8$. The difference $A - B$ is the $2 \times 2$ matrix with top row $-3, 4$ and bottom row $-1, -2$. The linear combination $3A - 2B$ is the $2 \times 2$ matrix with top row $-5, 10$ and bottom row $-3, -1$. Matrix addition is only possible for matrices of equal size because addition is performed entry-by-entry, requiring each element in one matrix to pair with an element in the other.

---

## 7. Quick Verification
- **Verification of $A + B$:** Check whether $(A + B) - B = A$:
  $$\begin{pmatrix} 5 & 0 \\ -1 & 8 \end{pmatrix} - \begin{pmatrix} 4 & -2 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 5 - 4 & 0 - (-2) \\ -1 - 0 & 8 - 5 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix} = A \quad \checkmark$$
- **Verification of $3A - 2B$ entry $(1, 2)$:**
  $3 \cdot a_{12} - 2 \cdot b_{12} = 3(2) - 2(-2) = 6 + 4 = 10 \quad \checkmark$
- **Verification of $3A - 2B$ entry $(2, 2)$:**
  $3 \cdot a_{22} - 2 \cdot b_{22} = 3(3) - 2(5) = 9 - 10 = -1 \quad \checkmark$

---

## 8. Common Mistakes to Avoid
- **Sign Errors with Negatives:** When computing $2 - (-2)$ in $A - B$, mistakenly writing $0$ instead of $2 + 2 = 4$.
- **Incomplete Scalar Multiplication:** Multiplying only the first row or diagonal elements by the scalar, rather than multiplying all 4 entries.
- **Attempting Addition Across Different Shapes:** Assuming missing entries can automatically be treated as zeros without an explicit rule.

---

## 9. Classroom Presentation (3-Sentence Summary)
"To add or subtract matrices, we simply add or subtract the numbers that sit in the exact same positions, which is why both matrices must have identical dimensions. For scalar multiplication, every single entry is multiplied by that number before we combine the matrices. Following these rules, we find $A+B = \begin{pmatrix}5&0\\-1&8\end{pmatrix}$, $A-B = \begin{pmatrix}-3&4\\-1&-2\end{pmatrix}$, and $3A-2B = \begin{pmatrix}-5&10\\-3&-1\end{pmatrix}$."

