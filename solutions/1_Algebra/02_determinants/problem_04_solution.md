# Exercise 4: Triangular Matrix

## 1. Original Problem
Without expanding the determinant, compute:
$$\det\begin{pmatrix} 2 & 4 & 1 \\ 0 & -3 & 5 \\ 0 & 0 & 7 \end{pmatrix}$$
State the rule for an arbitrary triangular matrix and explain it using this example.

---

## 2. What We Are Trying to Find
We need to:
- Compute the determinant of the given $3 \times 3$ upper-triangular matrix without performing a long Sarrus or full expansion calculation.
- State the general mathematical theorem for the determinant of any triangular matrix (upper or lower).
- Explain why this rule holds true using the structure of the provided matrix.

---

## 3. Key Concepts and Theorems
1. **Triangular Matrix Definition:**
   - An **upper triangular matrix** has all entries strictly below the main diagonal equal to zero ($a_{ij} = 0$ for $i > j$).
   - A **lower triangular matrix** has all entries strictly above the main diagonal equal to zero ($a_{ij} = 0$ for $i < j$).
2. **Determinant of a Triangular Matrix Theorem:**
   The determinant of any upper triangular, lower triangular, or diagonal matrix of size $n \times n$ is simply the **product of its main diagonal entries**:
   $$\det T = a_{11} \cdot a_{22} \cdots a_{nn} = \prod_{i=1}^n a_{ii}$$
3. **Why this works:**
   If you expand along the first column of an upper triangular matrix, every entry except the first is zero. Repeating this process on the remaining submatrices recursively isolates only the diagonal elements.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Matrix Structure
Look at the matrix:
$$T = \begin{pmatrix} \mathbf{2} & 4 & 1 \\ 0 & \mathbf{-3} & 5 \\ 0 & 0 & \mathbf{7} \end{pmatrix}$$
- The entries below the main diagonal are $t_{21} = 0$, $t_{31} = 0$, and $t_{32} = 0$.
- Because all entries below the main diagonal are zero, the matrix is **upper triangular**.

---

### Step 2: Apply the Diagonal Product Rule
By the triangular matrix determinant theorem:
$$\det T = t_{11} \cdot t_{22} \cdot t_{33}$$
Substitute the numbers sitting on the main diagonal:
- $t_{11} = 2$
- $t_{22} = -3$
- $t_{33} = 7$

Multiply them directly:
$$\det T = 2 \cdot (-3) \cdot 7 = -6 \cdot 7 = -42$$

---

### Step 3: Explanation of the Rule Using this Example
To see why the rule holds without relying on a black box, consider what happens if we apply Laplace expansion along the first column:
$$T = \begin{pmatrix} 2 & 4 & 1 \\ 0 & -3 & 5 \\ 0 & 0 & 7 \end{pmatrix}$$
- The first column has entries $2$, $0$, $0$.
- Expanding along this column:
  $$\det T = 2 \cdot \det\begin{pmatrix} -3 & 5 \\ 0 & 7 \end{pmatrix} - 0 \cdot \det(\dots) + 0 \cdot \det(\dots)$$
- Now look at the remaining $2 \times 2$ minor: it is also triangular! Its determinant is:
  $$\det\begin{pmatrix} -3 & 5 \\ 0 & 7 \end{pmatrix} = (-3)(7) - (5)(0) = (-3)(7)$$
- Multiplying this by the leading factor $2$:
  $$\det T = 2 \cdot [(-3) \cdot 7] = -42$$
Because all the off-diagonal entries paired with zeros vanish completely, only the product of the diagonal elements survives.

---

## 5. Why Each Step Is Valid
- **Zero Suppression in Permutations:** In the Leibniz formula $\det A = \sum_{\sigma} \operatorname{sgn}(\sigma) \prod a_{i, \sigma(i)}$, every permutation that selects an entry below the diagonal encounters a zero factor, leaving the identity permutation $\sigma = \text{id}$ as the only non-zero term.
- **Recursive Laplace Expansion:** Expanding along the first column (or last row) successively strips away the outer rows and columns, leaving a single chain of multiplied diagonal pivots.

---

## 6. Final Answer in Words
The determinant of the given triangular matrix is $-42$. The general rule states that the determinant of any triangular matrix is the product of the entries on its main diagonal. In this example, the diagonal entries are $2$, $-3$, and $7$, giving $\det = 2 \cdot (-3) \cdot 7 = -42$.

---

## 7. Quick Verification
- **Sarrus' rule check:**
  - Downward diagonals: $(2)(-3)(7) + (4)(5)(0) + (1)(0)(0) = -42 + 0 + 0 = -42$.
  - Upward diagonals: $(0)(-3)(1) + (0)(5)(2) + (7)(0)(4) = 0 + 0 + 0 = 0$.
  - $\det = -42 - 0 = -42$. Exactly matches! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Adding Instead of Multiplying:** Adding the diagonal numbers ($2 + (-3) + 7 = 6$) instead of multiplying them.
- **Applying the Rule to Non-Triangular Matrices:** Attempting to multiply the main diagonal on matrices that have non-zero entries on BOTH sides of the diagonal. The matrix MUST have all zeros either below or above the diagonal.
- **Dropping Negative Signs:** Forgetting the minus sign on $-3$, resulting in $+42$ instead of $-42$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Because all entries below the main diagonal are zero, this is an upper triangular matrix. The determinant of any triangular matrix is simply the product of its diagonal entries, because any expansion along the columns eliminates all off-diagonal products. Multiplying the diagonal entries directly gives $\det = 2 \cdot (-3) \cdot 7 = -42$."

