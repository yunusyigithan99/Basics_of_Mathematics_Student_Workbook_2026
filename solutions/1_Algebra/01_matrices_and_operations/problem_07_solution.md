# Exercise 7: Identity Matrix, Zero Matrix, and Powers

## 1. Original Problem
For the matrix:
$$A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$$
compute:
$$AI, \qquad IA, \qquad A + 0, \qquad A^2, \qquad A^3.$$
Explain the roles of the matrices $I$ and $0$, and describe the pattern you observe in successive powers of $A$.

---

## 2. What We Are Trying to Find
We need to:
- Multiply matrix $A$ on the right and on the left by the $2 \times 2$ identity matrix $I$.
- Add the $2 \times 2$ zero matrix $0$ to matrix $A$.
- Compute the square $A^2 = A \cdot A$ and the cube $A^3 = A^2 \cdot A$.
- State the algebraic roles of $I$ and $0$ (neutral elements).
- Identify and formulate the general pattern for the $n$-th power of $A$ ($A^n$).

---

## 3. Key Concepts and Theorems
1. **Identity Matrix ($I$):**
   The identity matrix $I_n$ is a square matrix with $1$s along the main diagonal and $0$s everywhere else:
   $$I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$
   It acts as the **multiplicative identity**: for any compatible matrix $A$, $AI = IA = A$ (analogous to the number $1$ in real arithmetic).
2. **Zero Matrix ($0$):**
   The zero matrix consists entirely of zeros:
   $$0 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$
   It acts as the **additive identity**: $A + 0 = A$ (analogous to the number $0$ in real arithmetic).
3. **Matrix Powers:**
   For a square matrix, $A^1 = A$, $A^2 = A \cdot A$, and $A^{k+1} = A^k \cdot A$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $AI$ and $IA$
Using the $2 \times 2$ identity matrix $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$:

- **Right multiplication $AI$:**
  $$AI = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(0) & 2(0) + 1(1) \\ 0(1) + 2(0) & 0(0) + 2(1) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = A$$

- **Left multiplication $IA$:**
  $$IA = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1(2) + 0(0) & 1(1) + 0(2) \\ 0(2) + 1(0) & 0(1) + 1(2) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = A$$

---

### Step 2: Compute $A + 0$
Using the $2 \times 2$ zero matrix $0 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$:
$$A + 0 = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 2+0 & 1+0 \\ 0+0 & 2+0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = A$$

---

### Step 3: Compute $A^2$
Multiply $A$ by itself:
$$A^2 = A \cdot A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$$
- Top-left: $2(2) + 1(0) = 4 + 0 = 4$
- Top-right: $2(1) + 1(2) = 2 + 2 = 4$
- Bottom-left: $0(2) + 2(0) = 0 + 0 = 0$
- Bottom-right: $0(1) + 2(2) = 0 + 4 = 4$

Thus:
$$A^2 = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix}$$

---

### Step 4: Compute $A^3$
Multiply $A^2$ by $A$:
$$A^3 = A^2 \cdot A = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$$
- Top-left: $4(2) + 4(0) = 8 + 0 = 8$
- Top-right: $4(1) + 4(2) = 4 + 8 = 12$
- Bottom-left: $0(2) + 4(0) = 0 + 0 = 0$
- Bottom-right: $0(1) + 4(2) = 0 + 8 = 8$

Thus:
$$A^3 = \begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix}$$

---

### Step 5: Roles of $I$ and $0$, and the Power Pattern
1. **Roles of $I$ and $0$:**
   - The matrix $I$ is the **multiplicative neutral element**: multiplying any matrix by $I$ (on the left or right) leaves the matrix completely unchanged.
   - The matrix $0$ is the **additive neutral element**: adding $0$ to any matrix leaves every entry unchanged.
2. **Pattern in Powers of $A$:**
   Let us compare the powers:
   - $A^1 = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 2^1 & 1 \cdot 2^0 \\ 0 & 2^1 \end{pmatrix}$
   - $A^2 = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 2^2 & 2 \cdot 2^1 \\ 0 & 2^2 \end{pmatrix}$
   - $A^3 = \begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix} = \begin{pmatrix} 2^3 & 3 \cdot 2^2 \\ 0 & 2^3 \end{pmatrix}$

   We observe that:
   - The diagonal entries are always $2^n$.
   - The bottom-left entry remains $0$ (the matrix stays upper-triangular).
   - The top-right entry grows as $n \cdot 2^{n-1}$.
   Hence, the general formula is:
   $$A^n = \begin{pmatrix} 2^n & n \cdot 2^{n-1} \\ 0 & 2^n \end{pmatrix}$$

---

## 5. Why Each Step Is Valid
- **Neutrality of $I$ and $0$:** By matrix arithmetic definitions, $(AI)_{ij} = \sum a_{ik}\delta_{kj} = a_{ij}$ and $(A+0)_{ij} = a_{ij} + 0 = a_{ij}$.
- **Associativity of Matrix Powers:** Matrix multiplication is associative, so $A^3 = (A \cdot A) \cdot A = A^2 \cdot A$.
- **Decomposition Explanation for the Pattern:** Notice $A = 2I + N$, where $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. Since $I$ and $N$ commute ($2I \cdot N = N \cdot 2I$) and $N^2 = 0$ (a nilpotent matrix), the binomial theorem gives $(2I + N)^n = (2I)^n + n(2I)^{n-1}N + 0 = 2^n I + n 2^{n-1}N$, which produces exactly $\begin{pmatrix} 2^n & n 2^{n-1} \\ 0 & 2^n \end{pmatrix}$.

---

## 6. Final Answer in Words
The products $AI$ and $IA$ both equal the original matrix $A$, confirming that $I$ serves as the multiplicative identity. Adding the zero matrix yields $A + 0 = A$, showing that $0$ is the additive identity. The square of $A$ is $\begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix}$ and the cube is $\begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix}$. The general pattern for the $n$-th power is that the main diagonal entries are $2^n$, the bottom-left entry is $0$, and the top-right entry is $n \cdot 2^{n-1}$.

---

## 7. Quick Verification
- **Testing the formula for $n=1$:**
  $$A^1 = \begin{pmatrix} 2^1 & 1 \cdot 2^0 \\ 0 & 2^1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = A \quad \checkmark$$
- **Testing the formula for $n=2$:**
  $$A^2 = \begin{pmatrix} 2^2 & 2 \cdot 2^1 \\ 0 & 2^2 \end{pmatrix} = \begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix} \quad \checkmark$$
- **Testing the formula for $n=3$:**
  $$A^3 = \begin{pmatrix} 2^3 & 3 \cdot 2^2 \\ 0 & 2^3 \end{pmatrix} = \begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix} \quad \checkmark$$
- **Consistency for $n=4$:**
  $$A^4 = A^3 \cdot A = \begin{pmatrix} 8 & 12 \\ 0 & 8 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 16 & 8 + 24 \\ 0 & 16 \end{pmatrix} = \begin{pmatrix} 16 & 32 \\ 0 & 16 \end{pmatrix}$$
  Formula prediction: $2^4 = 16$ and $4 \cdot 2^3 = 4 \cdot 8 = 32$. Exact match! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Squaring Each Entry Individually:** Computing $A^2$ as $\begin{pmatrix} 2^2 & 1^2 \\ 0^2 & 2^2 \end{pmatrix} = \begin{pmatrix} 4 & 1 \\ 0 & 4 \end{pmatrix}$. Matrix powers MUST be calculated using row-by-column multiplication.
- **Assuming the Top-Right Entry is $1^n$:** Assuming off-diagonal entries simply raise to the power $n$, which would mistakenly keep the top-right entry as $1$.
- **Confusing Matrix $I$ with a Matrix of All Ones:** Writing $I = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ instead of the diagonal identity $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Multiplying by the identity matrix leaves matrix $A$ unchanged as $AI = IA = A$, and adding the zero matrix similarly gives $A + 0 = A$, establishing them as the multiplicative and additive neutral elements. When computing powers of $A$, row-by-column multiplication gives $A^2 = \begin{pmatrix}4&4\\0&4\end{pmatrix}$ and $A^3 = \begin{pmatrix}8&12\\0&8\end{pmatrix}$. This reveals a clear structural pattern where the diagonal entries double as $2^n$ while the upper-right entry accumulates linearly with the derivative-like formula $n \cdot 2^{n-1}$."

