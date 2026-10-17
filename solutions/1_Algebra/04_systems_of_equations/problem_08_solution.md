# Exercise 8: Two Systems with the Same Coefficient Matrix

## 1. Original Problem
Solve by elimination the two systems:
$$\text{System 1: } \begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases}$$
$$\text{System 2: } \begin{cases} 2x + y = 1 \\ x - y = 4 \end{cases}$$
Compare the successive elimination steps. Which part of the calculation is the same in both cases, and why?

---

## 2. What We Are Trying to Find
We need to:
- Solve System 1 completely using Gaussian elimination.
- Solve System 2 completely using Gaussian elimination.
- Compare the row operations applied to both systems step by step.
- Identify which portion of the arithmetic is identical in both problems.
- Explain why the elimination steps depend strictly on the coefficient matrix and are independent of the right-hand side values.

---

## 3. Key Concepts and Theorems
1. **Role of the Coefficient Matrix in Gaussian Elimination:**
   Elementary row operations are determined **exclusively** by the entries of the coefficient matrix $A$. Their objective is to create leading zeros in the columns of $A$.
2. **Right-Hand Side as a Passive Passenger:**
   The right-hand side vector $\mathbf{b}$ passively undergoes the row operations dictated by $A$, but its values never influence which row operations are chosen.
3. **Multi-RHS Augmented Matrix $[A \mid b_1 \; b_2]$:**
   Because the elimination steps depend only on $A$, multiple systems $Ax = b_1$ and $Ax = b_2$ can be solved simultaneously in a single combined augmented matrix:
   $$\left[\begin{array}{cc|cc} 2 & 1 & 5 & 1 \\ 1 & -1 & 1 & 4 \end{array}\right]$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Solve System 1 by Elimination
Augmented matrix for System 1:
$$M^{(1)} = \left(\begin{array}{cc|c} 2 & 1 & 5 \\ 1 & -1 & 1 \end{array}\right)$$

1. **Swap rows to get pivot 1 ($R_1 \leftrightarrow R_2$):**
   $$\left(\begin{array}{cc|c} 1 & -1 & 1 \\ 2 & 1 & 5 \end{array}\right)$$
2. **Eliminate entry in Row 2 ($R_2 \leftarrow R_2 - 2R_1$):**
   - Left side: $(2, 1) - 2(1, -1) = (0, 1 - (-2)) = (0, 3)$
   - Right side: $5 - 2(1) = 3$
   $$\left(\begin{array}{cc|c} 1 & -1 & 1 \\ 0 & 3 & 3 \end{array}\right)$$
3. **Back-substitution:**
   - From Row 2: $3y = 3 \implies y = 1$
   - From Row 1: $x - y = 1 \implies x - 1 = 1 \implies x = 2$

**Solution to System 1:** $(x, y) = (2, 1)$.

---

### Step 2: Solve System 2 by Elimination
Augmented matrix for System 2:
$$M^{(2)} = \left(\begin{array}{cc|c} 2 & 1 & 1 \\ 1 & -1 & 4 \end{array}\right)$$

1. **Swap rows to get pivot 1 ($R_1 \leftrightarrow R_2$):**
   $$\left(\begin{array}{cc|c} 1 & -1 & 4 \\ 2 & 1 & 1 \end{array}\right)$$
2. **Eliminate entry in Row 2 ($R_2 \leftarrow R_2 - 2R_1$):**
   - Left side: $(2, 1) - 2(1, -1) = (0, 3)$
   - Right side: $1 - 2(4) = 1 - 8 = -7$
   $$\left(\begin{array}{cc|c} 1 & -1 & 4 \\ 0 & 3 & -7 \end{array}\right)$$
3. **Back-substitution:**
   - From Row 2: $3y = -7 \implies y = -\frac{7}{3}$
   - From Row 1: $x - y = 4 \implies x - \left(-\frac{7}{3}\right) = 4 \implies x + \frac{7}{3} = \frac{12}{3} \implies x = \frac{5}{3}$

**Solution to System 2:** $(x, y) = \left(\frac{5}{3}, -\frac{7}{3}\right)$.

---

### Step 3: Compare Elimination Steps and Explain Why They Match
1. **Which part of the calculation is identical:**
   - The choice of row operations is **100% identical**: first $R_1 \leftrightarrow R_2$, then $R_2 \leftarrow R_2 - 2R_1$.
   - The transformation of the left-hand side coefficient matrix is **identical at every single stage**:
     $$\begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix} \xrightarrow{R_1 \leftrightarrow R_2} \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix} \xrightarrow{R_2 - 2R_1} \begin{pmatrix} 1 & -1 \\ 0 & 3 \end{pmatrix}$$
   - The final reduced coefficient matrix $\begin{pmatrix} 1 & -1 \\ 0 & 3 \end{pmatrix}$ is the exact same upper triangular matrix in both cases.

2. **Why this happens:**
   The entire sequence of elementary row operations in Gaussian elimination is designed to eliminate entries *below the diagonal of the coefficient matrix $A$*.
   Because both systems share the **exact same coefficient matrix** $A = \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$, the row multipliers and pivot decisions are determined solely by the entries of $A$. The right-hand side vectors ($b_1 = \begin{pmatrix} 5 \\ 1 \end{pmatrix}$ and $b_2 = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$) merely receive the arithmetic operations without ever influencing which operations are selected.

---

## 5. Why Each Step Is Valid
- **Linearity of Row Operators:** The row operation transformation $E: \mathbb{R}^{m \times (n+1)} \to \mathbb{R}^{m \times (n+1)}$ acts as $E[A \mid b] = [EA \mid Eb]$. The left block $EA$ depends strictly on $A$.
- **LU Factorization Foundation:** This structural property is the exact mathematical foundation of LU decomposition, where $A = LU$ is factored once and can subsequently solve $Ax = b$ for any number of right-hand vectors via simple forward and backward substitution.

---

## 6. Final Answer in Words
The solution to System 1 is $(x, y) = (2, 1)$, and the solution to System 2 is $(x, y) = (5/3, -7/3)$. The entire left-hand side calculation—swapping Row 1 with Row 2 and subtracting $2R_1$ from $R_2$ to reach the echelon matrix with first row $1, -1$ and second row $0, 3$—is completely identical in both systems. This happens because the choice of row operations in Gaussian elimination is governed entirely by the entries of the coefficient matrix $A$, which is identical in both problems.

---

## 7. Quick Verification
- **System 1 check:**
  $2(2) + 1 = 5 \checkmark$
  $2 - 1 = 1 \checkmark$
- **System 2 check:**
  $2(5/3) + (-7/3) = 10/3 - 7/3 = 3/3 = 1 \checkmark$
  $5/3 - (-7/3) = 5/3 + 7/3 = 12/3 = 4 \checkmark$

---

## 8. Common Mistakes to Avoid
- **Repeating Left-Hand Side Arithmetic:** Treating each system as an entirely unrelated problem and recalculating the coefficient entries from scratch.
- **Arithmetic Sign Error in System 2:** Calculating $1 - 2(4) = 1 - 8 = -7$, but mistakenly dropping the negative sign.
- **Back-Substitution Error:** Writing $x = 4 - 7/3$ instead of $x = 4 + (-7/3)$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"We solve both systems by swapping rows and subtracting $2R_1$ from $R_2$, yielding the unique solutions $(2, 1)$ for the first system and $(5/3, -7/3)$ for the second. The entire sequence of row operations and the resulting upper triangular matrix $\begin{pmatrix}1&-1\\0&3\end{pmatrix}$ are identical in both cases. This demonstrates that the elimination path is dictated entirely by the coefficient matrix $A$, with the right-hand sides merely following along passively."

