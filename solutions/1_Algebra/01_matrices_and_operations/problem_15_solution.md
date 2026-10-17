# Exercise 15: Associativity of Multiplication and Different Calculation Paths

## 1. Original Problem
Given:
$$A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix}, \quad C = \begin{pmatrix} 2 & 1 \\ 0 & -1 \end{pmatrix}$$
Compute $(AB)C$ and $A(BC)$. Compare the results and the number of intermediate operations. Explain what associativity of matrix multiplication means in this example.

---

## 2. What We Are Trying to Find
We need to:
- Compute the three-matrix product along Path 1: first multiply $A$ and $B$, then multiply the resulting matrix by $C$, giving $(AB)C$.
- Compute the same product along Path 2: first multiply $B$ and $C$, then multiply $A$ by the resulting matrix, giving $A(BC)$.
- Compare the final resulting matrices from both calculation paths to confirm they are identical.
- Count and compare the number of scalar multiplications and additions needed in Path 1 versus Path 2.
- Explain the theoretical meaning and practical computational consequences of the associativity of matrix multiplication.

---

## 3. Key Concepts and Theorems
1. **Associativity of Matrix Multiplication:**
   For any matrices $A, B, C$ with compatible sizes $(m \times k)$, $(k \times p)$, and $(p \times n)$, matrix multiplication is associative:
   $$(AB)C = A(BC)$$
   Parentheses dictate which operation is performed first, but the final outcome is guaranteed to be mathematically identical.
2. **Computational Cost of Matrix Multiplication:**
   Multiplying an $m \times k$ matrix by a $k \times n$ matrix produces an $m \times n$ matrix.
   - Total entries to compute: $m \cdot n$.
   - Each entry requires $k$ scalar multiplications and $k - 1$ scalar additions.
   - Total scalar multiplications: $m \cdot k \cdot n$.
   - Total scalar additions: $m \cdot (k - 1) \cdot n$.
   The chosen parenthesization can dramatically alter the computational workload even though the mathematical result is identical.

---

## 4. Detailed Step-by-Step Solution

Let us check the sizes of the matrices:
$$A \text{ is } 2 \times 3, \qquad B \text{ is } 3 \times 2, \qquad C \text{ is } 2 \times 2$$

---

### Step 1: Compute $(AB)C$ (Path 1)
- **First, compute $M_1 = AB$:**
  $$A_{(2 \times 3)} \cdot B_{(3 \times 2)} \implies M_1 \text{ is } 2 \times 2$$
  $$M_1 = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix}$$
  Calculate each entry:
  - $(M_1)_{11} = 1(1) + 2(2) + 0(-1) = 1 + 4 + 0 = 5$
  - $(M_1)_{12} = 1(0) + 2(1) + 0(3) = 0 + 2 + 0 = 2$
  - $(M_1)_{21} = 0(1) + 1(2) + 1(-1) = 0 + 2 - 1 = 1$
  - $(M_1)_{22} = 0(0) + 1(1) + 1(3) = 0 + 1 + 3 = 4$
  $$AB = \begin{pmatrix} 5 & 2 \\ 1 & 4 \end{pmatrix}$$

- **Second, multiply $(AB)$ by $C$:**
  $$(AB)_{(2 \times 2)} \cdot C_{(2 \times 2)} \implies (AB)C \text{ is } 2 \times 2$$
  $$(AB)C = \begin{pmatrix} 5 & 2 \\ 1 & 4 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & -1 \end{pmatrix}$$
  Calculate each entry:
  - Entry $(1, 1): 5(2) + 2(0) = 10 + 0 = 10$
  - Entry $(1, 2): 5(1) + 2(-1) = 5 - 2 = 3$
  - Entry $(2, 1): 1(2) + 4(0) = 2 + 0 = 2$
  - Entry $(2, 2): 1(1) + 4(-1) = 1 - 4 = -3$

  $$(AB)C = \begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix}$$

---

### Step 2: Compute $A(BC)$ (Path 2)
- **First, compute $M_2 = BC$:**
  $$B_{(3 \times 2)} \cdot C_{(2 \times 2)} \implies M_2 \text{ is } 3 \times 2$$
  $$M_2 = \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ -1 & 3 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & -1 \end{pmatrix}$$
  Calculate each entry:
  - Row 1:
    - $(M_2)_{11} = 1(2) + 0(0) = 2 + 0 = 2$
    - $(M_2)_{12} = 1(1) + 0(-1) = 1 + 0 = 1$
  - Row 2:
    - $(M_2)_{21} = 2(2) + 1(0) = 4 + 0 = 4$
    - $(M_2)_{22} = 2(1) + 1(-1) = 2 - 1 = 1$
  - Row 3:
    - $(M_2)_{31} = -1(2) + 3(0) = -2 + 0 = -2$
    - $(M_2)_{32} = -1(1) + 3(-1) = -1 - 3 = -4$
  $$BC = \begin{pmatrix} 2 & 1 \\ 4 & 1 \\ -2 & -4 \end{pmatrix}$$

- **Second, multiply $A$ by $(BC)$:**
  $$A_{(2 \times 3)} \cdot (BC)_{(3 \times 2)} \implies A(BC) \text{ is } 2 \times 2$$
  $$A(BC) = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 4 & 1 \\ -2 & -4 \end{pmatrix}$$
  Calculate each entry:
  - Entry $(1, 1): 1(2) + 2(4) + 0(-2) = 2 + 8 + 0 = 10$
  - Entry $(1, 2): 1(1) + 2(1) + 0(-4) = 1 + 2 + 0 = 3$
  - Entry $(2, 1): 0(2) + 1(4) + 1(-2) = 0 + 4 - 2 = 2$
  - Entry $(2, 2): 0(1) + 1(1) + 1(-4) = 0 + 1 - 4 = -3$

  $$A(BC) = \begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix}$$

---

### Step 3: Compare Results
$$(AB)C = \begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix} = A(BC)$$
Both paths yield the exact same $2 \times 2$ matrix.

---

### Step 4: Comparison of Operation Counts
Let us count the number of scalar multiplications and additions for each path:

1. **Path 1: $(AB)C$**
   - **Step 1 ($AB$):** Size $(2 \times 3) \times (3 \times 2) \to 2 \times 2$.
     - Multiplications: $2 \cdot 3 \cdot 2 = 12$
     - Additions: $2 \cdot (3 - 1) \cdot 2 = 8$
   - **Step 2 ($(AB)C$):** Size $(2 \times 2) \times (2 \times 2) \to 2 \times 2$.
     - Multiplications: $2 \cdot 2 \cdot 2 = 8$
     - Additions: $2 \cdot (2 - 1) \cdot 2 = 4$
   - **Total Path 1:** $12 + 8 = \mathbf{20}$ multiplications, $8 + 4 = \mathbf{12}$ additions (total: $32$ operations).

2. **Path 2: $A(BC)$**
   - **Step 1 ($BC$):** Size $(3 \times 2) \times (2 \times 2) \to 3 \times 2$.
     - Multiplications: $3 \cdot 2 \cdot 2 = 12$
     - Additions: $3 \cdot (2 - 1) \cdot 2 = 6$
   - **Step 2 ($A(BC)$):** Size $(2 \times 3) \times (3 \times 2) \to 2 \times 2$.
     - Multiplications: $2 \cdot 3 \cdot 2 = 12$
     - Additions: $2 \cdot (3 - 1) \cdot 2 = 8$
   - **Total Path 2:** $12 + 12 = \mathbf{24}$ multiplications, $6 + 8 = \mathbf{14}$ additions (total: $38$ operations).

**Comparison:** Path 1 requires $20$ multiplications, whereas Path 2 requires $24$ multiplications. Path 1 is computationally cheaper by $4$ multiplications and $2$ additions.

---

### Step 5: Meaning of Associativity in this Example
- **Mathematical Equivalence:** Associativity means that grouping does not change the algebraic outcome: $[(AB)C]\mathbf{x} = [A(BC)]\mathbf{x}$. The composite transformation is identical regardless of whether we consider $A$ and $B$ grouped first or $B$ and $C$ grouped first.
- **Computational Impact (Matrix Chain Multiplication):** Even though the final mathematical matrix is identical, the intermediate matrices have different shapes:
  - In Path 1, the intermediate matrix $AB$ is $2 \times 2$ (only $4$ entries).
  - In Path 2, the intermediate matrix $BC$ is $3 \times 2$ (containing $6$ entries).
  Because $AB$ creates a smaller intermediate matrix, Path 1 does less work. In computer science and scientific computing, finding the cheapest parenthesization is the classic *Matrix Chain Multiplication* problem.

---

## 5. Why Each Step Is Valid
- **Formal Associativity Theorem:** In entry-level algebra, $[(AB)C]_{ij} = \sum_{l} (\sum_{k} a_{ik}b_{kl}) c_{lj} = \sum_{k} a_{ik} (\sum_{l} b_{kl}c_{lj}) = [A(BC)]_{ij}$, which is valid by the distributivity and associativity of real number arithmetic.
- **Complexity Formula Validity:** Computing an inner dot product between a length-$k$ row and a length-$k$ column strictly requires $k$ scalar products and $k-1$ additions.

---

## 6. Final Answer in Words
Both $(AB)C$ and $A(BC)$ evaluate to the same $2 \times 2$ matrix with top row $10, 3$ and bottom row $2, -3$, confirming that matrix multiplication is associative. However, computing $(AB)C$ requires $20$ scalar multiplications and $12$ additions, whereas $A(BC)$ requires $24$ scalar multiplications and $14$ additions. Thus, while associativity guarantees identical mathematical results, the order of parenthesization directly affects computational efficiency.

---

## 7. Quick Verification
- **Comparing outputs entry by entry:**
  $$(AB)C = \begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix}, \qquad A(BC) = \begin{pmatrix} 10 & 3 \\ 2 & -3 \end{pmatrix}$$
  The difference matrix is:
  $$(AB)C - A(BC) = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \quad \checkmark$$
- **Trace check:**
  $\operatorname{tr}((AB)C) = 10 + (-3) = 7$.
  $\operatorname{tr}(A(BC)) = 10 + (-3) = 7$. Matches! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Confusing Associativity with Commutativity:** Changing the order of the matrices instead of changing parentheses (e.g., writing $C(AB)$ instead of $(AB)C$). Associativity allows regrouping parentheses, but the left-to-right order of the matrix symbols ($A$, then $B$, then $C$) must never be altered.
- **Miscalculating Intermediate Shapes:** Believing $BC$ has size $2 \times 3$ instead of $3 \times 2$.
- **Operation Counting Errors:** Counting the additions as equal to the number of multiplications, forgetting that summing $k$ numbers requires only $k - 1$ plus signs.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Computing the matrix product along both paths yields the exact same matrix $\begin{pmatrix}10&3\\2&-3\end{pmatrix}$, confirming that matrix multiplication is strictly associative: $(AB)C = A(BC)$. However, counting the arithmetic operations shows that Path 1 requires only $20$ multiplications compared to $24$ for Path 2, because Path 1 forms a smaller $2 \times 2$ intermediate matrix rather than a $3 \times 2$ matrix. This proves that while parenthesization never alters the mathematical result, choosing the right calculation path can significantly improve computational efficiency."

