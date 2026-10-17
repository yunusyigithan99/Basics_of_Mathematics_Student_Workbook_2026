# Exercise 7: Choosing a Method Deliberately

## 1. Original Problem
Do not solve all of the following systems completely. For each situation, choose the method that best uses its structure and justify your choice:

1. One system with a triangular coefficient matrix:
   $$\begin{cases} 2x - y = 3 \\ 4y = 8 \end{cases}$$
2. Three systems $Ax = b_i$ ($i = 1, 2, 3$) with the same invertible matrix $A$, when $A^{-1}$ is already known.
3. One $3\times3$ system for which the inverse matrix is not given and the goal is only to find one solution vector.

For case 1, carry out the chosen method completely. For cases 2 and 3, describe the plan and indicate which part of the computation would be reusable or unnecessary. Do not judge a method by its name alone — refer to the number of right-hand sides and the structure of the matrix.

---

## 2. What We Are Trying to Find
We need to:
- Select the mathematically optimal solution method for three distinct computational scenarios based on matrix structure and problem parameters.
- Justify each selection in terms of computational efficiency (avoiding wasted operations).
- Completely execute the chosen method for Case 1.
- Detail the solution plan for Case 2, explaining how precomputed data ($A^{-1}$) is reused across multiple right-hand sides.
- Detail the solution plan for Case 3, explaining why computing a full inverse matrix is wasteful when only a single solution vector is desired.

---

## 3. Key Concepts and Theorems
1. **Computational Complexity in Linear Algebra:**
   - **Back-substitution on an upper triangular system:** Requires only $O(n^2)$ scalar operations.
   - **Gaussian elimination on $[A \mid b]$:** Requires $\approx \frac{2}{3}n^3$ operations for forward elimination and $O(n^2)$ for back-substitution.
   - **Matrix Inversion ($A^{-1}$):** Requires $\approx 2n^3$ operations (approximately 3 times more work than Gaussian elimination) to compute all $n^2$ entries of $A^{-1}$.
   - **Matrix-vector product $A^{-1}b$:** Requires $n^2$ scalar multiplications once $A^{-1}$ is in hand.
2. **Structural Decision Criteria:**
   - If the matrix is already triangular $\implies$ **Direct Back-Substitution**.
   - If solving for multiple right-hand sides with $A^{-1}$ already known $\implies$ **Matrix Multiplication ($x_i = A^{-1}b_i$)**.
   - If solving for a single right-hand side with no precomputed inverse $\implies$ **Gaussian Elimination**.

---

## 4. Detailed Step-by-Step Solution

### Case 1: Triangular Coefficient Matrix
$$\begin{cases} 2x - y = 3 \\ 4y = 8 \end{cases}$$

- **Chosen Method:** **Direct Back-Substitution**.
- **Justification:**
  The coefficient matrix is $A = \begin{pmatrix} 2 & -1 \\ 0 & 4 \end{pmatrix}$, which is already upper triangular (echelon form).
  Forward elimination has already been done for us! Applying Gaussian elimination from scratch would perform redundant checks, while computing an inverse would require calculating four entries unnecessarily. We can solve from the bottom up immediately.
- **Complete Execution:**
  1. Solve Equation 2 directly for $y$:
     $$4y = 8 \implies y = \frac{8}{4} = 2$$
  2. Substitute $y = 2$ upward into Equation 1:
     $$2x - 2 = 3 \implies 2x = 5 \implies x = \frac{5}{2} = 2.5$$
- **Solution:** $(x, y) = \left(\frac{5}{2}, 2\right)$.

---

### Case 2: Three Systems $Ax = b_i$ with the Same Matrix $A$, and $A^{-1}$ Already Known
- **Chosen Method:** **Matrix-Vector Multiplication ($x_i = A^{-1}b_i$)**.
- **Justification:**
  Because the inverse matrix $A^{-1}$ is **already provided**, the expensive inversion cost ($2n^3$ operations) has already been paid in advance.
  - **What is reusable:** The matrix $A^{-1}$ is reusable for all three systems.
  - **Cost per system:** Multiplying $A^{-1}$ by a vector $b_i$ takes only $n^2$ operations. For 3 systems, this requires only $3n^2$ operations in total.
  - **Why not Gaussian elimination:** Running Gaussian elimination on three separate systems would repeat the row reductions three times, performing $3 \times \frac{2}{3}n^3 = 2n^3$ operations, ignoring the valuable precomputed asset $A^{-1}$.
- **Plan:**
  Compute $x_1 = A^{-1}b_1$, $x_2 = A^{-1}b_2$, and $x_3 = A^{-1}b_3$ independently through direct matrix-vector multiplication.

---

### Case 3: One $3 \times 3$ System with No Inverse Given, Finding One Solution
- **Chosen Method:** **Gaussian Elimination on the Augmented Matrix $[A \mid b]$**.
- **Justification:**
  We only need to find a single vector $x$ for a single right-hand side $b$.
  - **What would be unnecessary (wasteful):** Computing the full matrix inverse $A^{-1}$. Inverting a $3 \times 3$ matrix requires solving $A X = I$ for all 3 columns of the identity, computing 9 separate entries. We do not need the matrix $A^{-1}$; we only need the vector $x$.
  - **Efficiency comparison:** Gaussian elimination directly on $[A \mid b]$ takes only $\approx \frac{2}{3}(3)^3 + (3)^2 \approx 27$ operations. Finding $A^{-1}$ first and then multiplying by $b$ would take $\approx 2(3)^3 + 3^2 \approx 63$ operations—more than double the work!
- **Plan:**
  Set up the $3 \times 4$ augmented matrix $[A \mid b]$, perform row operations to reach upper triangular form, and find the solution vector $x$ via back-substitution.

---

## 5. Why Each Step Is Valid
- **Computational Complexity Rigor:** Algorithmic complexity measures exact arithmetic operation counts; selecting the method with lowest operation count minimizes numerical rounding errors and runtime.
- **Information Parity:** In Case 3, solving for $n$ numbers (vector $x$) requires less information than solving for $n^2$ numbers (matrix $A^{-1}$). Computing unused parameters is mathematically inefficient.

---

## 6. Final Answer in Words
For Case 1, direct back-substitution is optimal because the matrix is already triangular; solving gives $y = 2$ and $x = 5/2$. For Case 2, matrix-vector multiplication $x_i = A^{-1}b_i$ is optimal because $A^{-1}$ is already known and can be reused three times, avoiding repeated row reductions. For Case 3, Gaussian elimination on $[A \mid b]$ is optimal because computing the 9 entries of an unused matrix inverse $A^{-1}$ takes more than double the operations needed to find the single solution vector directly.

---

## 7. Quick Verification
- **Verification of Case 1:**
  - Eq 1: $2(5/2) - 2 = 5 - 2 = 3 \checkmark$
  - Eq 2: $4(2) = 8 \checkmark$
- **Theoretical complexity verification:**
  - Case 2 ops: $3 \times 2^2 = 12$ mults (for $2 \times 2$) vs elimination $2 \times \frac{2}{3}(8) \approx 11$ mults + repeats. For $n \ge 3$, $A^{-1}b$ is vastly faster when $A^{-1}$ is given. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Using a Single Preferred Method Everywhere:** Applying Gaussian elimination to an already-triangular matrix, or computing $A^{-1}$ when only one vector is needed.
- **Ignoring the Number of Right-Hand Sides:** Failing to distinguish between solving 1 system versus solving multiple systems with the same coefficient matrix.
- **Inverting $A$ in Case 3:** Spending time computing a full inverse matrix for a single calculation.

---

## 9. Classroom Presentation (3-Sentence Summary)
"For the first system, the matrix is already upper triangular, so direct back-substitution immediately yields $y = 2$ and $x = 5/2$ without any forward elimination. For the second scenario, since $A^{-1}$ is already known, computing $x_i = A^{-1}b_i$ reuses the inverse across all three right-hand sides with minimal effort. For the third scenario, Gaussian elimination is superior because calculating an unneeded matrix inverse requires more than double the operations necessary to find a single solution vector."

