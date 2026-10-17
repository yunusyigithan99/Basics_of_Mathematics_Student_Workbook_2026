# Exercise 12: Formula for a Matrix Power

## 1. Original Problem
Let:
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
Compute $A^2$, $A^3$, and $A^4$, and use them to formulate a conjecture for $A^n$. Then do not stop after checking one more case: assume the formula is true for $n$, multiply by $A$, and explain why you obtain exactly the formula for $n+1$.

---

## 2. What We Are Trying to Find
We need to:
- Compute the explicit powers $A^2$, $A^3$, and $A^4$ via matrix multiplication.
- Detect the mathematical pattern that emerges across these powers and state a conjecture for $A^n$ for any positive integer $n$.
- Formally prove the conjecture using the principle of mathematical induction: assuming $A^n$ holds, multiply by $A$ on the right, and demonstrate that the product yields the exact formula with $n$ replaced by $n+1$.

---

## 3. Key Concepts and Theorems
1. **Matrix Powers:**
   Powers of a square matrix are defined recursively by $A^1 = A$ and $A^{k+1} = A^k \cdot A$.
2. **Shear Matrices:**
   The matrix $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ represents a standard horizontal shear mapping $(x, y) \mapsto (x + y, y)$. Applying the shear $n$ times intuitively shifts the $x$-coordinate by $n \cdot y$.
3. **Principle of Mathematical Induction:**
   To prove a statement $P(n)$ for all integers $n \ge 1$:
   - **Base Case:** Prove $P(1)$ is true.
   - **Inductive Step:** Prove that if $P(n)$ is true (the induction hypothesis), then $P(n+1)$ must also be true.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $A^2$, $A^3$, and $A^4$
- **Compute $A^2 = A \cdot A$:**
  $$A^2 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(1) + 1(0) & 1(1) + 1(1) \\ 0(1) + 1(0) & 0(1) + 1(1) \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$$

- **Compute $A^3 = A^2 \cdot A$:**
  $$A^3 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(1) + 2(0) & 1(1) + 2(1) \\ 0(1) + 1(0) & 0(1) + 1(1) \end{pmatrix} = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$$

- **Compute $A^4 = A^3 \cdot A$:**
  $$A^4 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(1) + 3(0) & 1(1) + 3(1) \\ 0(1) + 1(0) & 0(1) + 1(1) \end{pmatrix} = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$$

---

### Step 2: Formulate the Conjecture for $A^n$
Observing the calculated powers:
$$A^1 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \quad A^3 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}, \quad A^4 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$$
In every power:
- The diagonal entries remain constantly equal to $1$.
- The bottom-left entry remains constantly equal to $0$.
- The top-right entry matches the exponent $n$ exactly.

**Conjecture:**
For every positive integer $n \ge 1$:
$$A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$$

---

### Step 3: Inductive Step (Proof for $n+1$)
- **Induction Hypothesis:**
  Assume that the formula holds for an arbitrary positive integer $n$, namely:
  $$A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$$

- **Multiply by $A$ to obtain $A^{n+1}$:**
  By the definition of matrix powers, $A^{n+1} = A^n \cdot A$. Using our hypothesis:
  $$A^{n+1} = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$

- **Perform the multiplication:**
  - Top-left entry: $1(1) + n(0) = 1 + 0 = 1$
  - Top-right entry: $1(1) + n(1) = 1 + n = n + 1$
  - Bottom-left entry: $0(1) + 1(0) = 0 + 0 = 0$
  - Bottom-right entry: $0(1) + 1(1) = 0 + 1 = 1$

  Assembling the resulting matrix:
  $$A^{n+1} = \begin{pmatrix} 1 & n + 1 \\ 0 & 1 \end{pmatrix}$$

- **Conclusion:**
  The resulting matrix has the exact same structural form as $A^n$, with $n$ replaced by $n+1$. Because the formula is true for $n=1$, it is proven for all positive integers $n \in \mathbb{N}$ by mathematical induction.

---

## 5. Why Each Step Is Valid
- **Power Recursion Rule:** The definition of matrix exponentiation satisfies $A^{n+1} = A^n \cdot A$ due to the associativity of matrix multiplication.
- **Row-by-Column Evaluation:** The top-right entry $(1 \cdot 1 + n \cdot 1)$ adds the existing shear value $n$ to the new shear value $1$, producing $n+1$.
- **Induction Principle:** Demonstrating that the truth of the statement for $n$ logically forces the truth for $n+1$ creates an unbroken chain of truth starting from the verified base case $n=1$.

---

## 6. Final Answer in Words
The powers of $A$ are $A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $A^3 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$, and $A^4 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$. The general formula for the $n$-th power is $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$. Multiplying this hypothetical $A^n$ by $A$ produces the matrix with top row $1, n+1$ and bottom row $0, 1$, which proves by induction that the formula holds for every positive integer $n$.

---

## 7. Quick Verification
- **Base case check ($n=1$):**
  $$A^1 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = A \quad \checkmark$$
- **Checking $n=5$ directly:**
  $$A^5 = A^4 \cdot A = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 + 4 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 5 \\ 0 & 1 \end{pmatrix}$$
  Formula gives $\begin{pmatrix} 1 & 5 \\ 0 & 1 \end{pmatrix}$, which matches perfectly. $\checkmark$
- **Binomial theorem perspective:**
  $A = I + N$, where $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. Since $N^2 = 0$ and $IN = NI$:
  $$(I + N)^n = I^n + n I^{n-1} N + \frac{n(n-1)}{2} I^{n-2} N^2 + \dots = I + nN = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix} \quad \checkmark$$

---

## 8. Common Mistakes to Avoid
- **Guessing without Proving:** Stopping after computing $A^4$ and guessing $A^n$ without performing the inductive step multiplication ($A^n \cdot A$).
- **Treating Induction as Checking More Examples:** Calculating $A^5$ and $A^6$ and believing that constitutes a proof. A mathematical proof must show that the transition from $n$ to $n+1$ holds for an arbitrary variable $n$.
- **Assuming Diagonal Entries Change:** Mistakenly writing $1^n = n$ on the diagonal; $1^n$ is always $1$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"By computing the first several powers of $A$, we observe that the diagonal entries remain $1$ while the top-right entry increases by $1$ at each step, leading to the conjecture $A^n = \begin{pmatrix}1&n\\0&1\end{pmatrix}$. To formally prove this for all $n$, we assume the formula holds for $n$ and multiply on the right by $A$, where the row-column product yields $\begin{pmatrix}1&n+1\\0&1\end{pmatrix}$. This completes the inductive step, rigorously proving that applying this shear transformation $n$ times simply scales the off-diagonal shear factor by $n$."

