# Exercise 15: Two Methods for Solving the Same System

## 1. Original Problem
For the matrix and vector:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}, \qquad b = \begin{pmatrix} 7 \\ 8 \end{pmatrix}$$
solve $Ax = b$ in two ways:
1. using $A^{-1}b$,
2. using Gaussian elimination.

Compare both solutions, the number of essential steps, and state which method was simpler in this example.

---

## 2. What We Are Trying to Find
We need to:
- Solve the linear system $Ax = b$ using the matrix inverse formula $x = A^{-1}b$ (Method 1).
- Solve the exact same system using Gaussian elimination with back-substitution on the augmented matrix $[A \mid b]$ (Method 2).
- Compare the two calculated solution vectors to confirm they are identical.
- Compare the computational effort (number of arithmetic steps, complexity, and overhead) required by each method.
- State which method is simpler and explain the criteria that guide this choice in practical mathematics and computing.

---

## 3. Key Concepts and Theorems
1. **Matrix Inversion Method ($x = A^{-1}b$):**
   Requires computing the full inverse matrix $A^{-1}$ first, then multiplying by $b$.
   - Ideal when the same coefficient matrix $A$ is used to solve systems with many different vectors $b$.
   - Computationally expensive for large matrices ($O(n^3)$ operations with high overhead).
2. **Gaussian Elimination on $[A \mid b]$:**
   Applies elementary row operations to reduce the augmented matrix directly to row echelon form, followed by back-substitution.
   - Ideal for solving a single system with one specific vector $b$.
   - Solves for the vector directly without computing the $n^2$ entries of $A^{-1}$.

---

## 4. Detailed Step-by-Step Solution

### Method 1: Solving via $x = A^{-1}b$
- **Step 1: Compute the determinant of $A$:**
  $$\det A = (2 \cdot 3) - (1 \cdot 1) = 6 - 1 = 5$$

- **Step 2: Find the inverse matrix $A^{-1}$:**
  $$A^{-1} = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$$

- **Step 3: Multiply $A^{-1}$ by $b = \begin{pmatrix} 7 \\ 8 \end{pmatrix}$:**
  $$x = A^{-1}b = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix} \begin{pmatrix} 7 \\ 8 \end{pmatrix}$$
  Calculate each component:
  - First component: $3(7) + (-1)(8) = 21 - 8 = 13$
  - Second component: $-1(7) + 2(8) = -7 + 16 = 9$

  Multiply by $\frac{1}{5}$:
  $$x = \begin{pmatrix} \frac{13}{5} \\ \frac{9}{5} \end{pmatrix}$$

---

### Method 2: Solving via Gaussian Elimination
Set up the augmented matrix $[A \mid b]$:
$$M_0 = \begin{pmatrix} 2 & 1 & \mid & 7 \\ 1 & 3 & \mid & 8 \end{pmatrix}$$

- **Step 1: Swap rows to obtain a pivot of $1$ ($R_1 \leftrightarrow R_2$):**
  $$M_1 = \begin{pmatrix} 1 & 3 & \mid & 8 \\ 2 & 1 & \mid & 7 \end{pmatrix}$$

- **Step 2: Eliminate the entry in Row 2 ($R_2 \leftarrow R_2 - 2R_1$):**
  - Left side: $(2, 1) - 2(1, 3) = (2 - 2, 1 - 6) = (0, -5)$
  - Right side: $7 - 2(8) = 7 - 16 = -9$

  The echelon augmented matrix is:
  $$M_2 = \begin{pmatrix} 1 & 3 & \mid & 8 \\ 0 & -5 & \mid & -9 \end{pmatrix}$$

- **Step 3: Solve by back-substitution:**
  - From Row 2:
    $$-5x_2 = -9 \implies x_2 = \frac{9}{5}$$
  - Substitute $x_2 = \frac{9}{5}$ into Row 1:
    $$x_1 + 3\left(\frac{9}{5}\right) = 8$$
    $$x_1 + \frac{27}{5} = \frac{40}{5} \implies x_1 = \frac{40}{5} - \frac{27}{5} = \frac{13}{5}$$

Thus, the solution vector is:
$$x = \begin{pmatrix} \frac{13}{5} \\ \frac{9}{5} \end{pmatrix}$$

---

### Step 3: Comparison of the Two Methods
1. **Consistency of Results:**
   Both methods yield the exact same solution: $x_1 = \frac{13}{5}$ and $x_2 = \frac{9}{5}$.
2. **Comparison of Steps and Computational Effort:**
   - **Method 1 ($A^{-1}b$):**
     Required: (1) computing the determinant, (2) computing all 4 entries of $A^{-1}$, and (3) performing matrix-vector multiplication with dot products.
     Total scalar operations: $\approx 10$ multiplications and $5$ additions.
   - **Method 2 (Gaussian Elimination):**
     Required: (1) one row swap, (2) one row elimination ($R_2 - 2R_1$), and (3) one back-substitution.
     Total scalar operations: $\approx 4$ multiplications and $3$ additions.
3. **Which method is simpler in this example:**
   **Gaussian elimination is simpler.**
   It works directly toward the solution of the vector $x$ without taking the detour of computing the full matrix inverse $A^{-1}$. Finding $A^{-1}$ computes extra unneeded information (an entire matrix) just to solve for two numbers.

---

## 5. Why Each Step Is Valid
- **Equivalence of Solution Spaces:** Row operations preserve the solution set of linear systems, ensuring that triangular reduction does not alter the values of $x_1$ and $x_2$.
- **Bijectivity of Invertible Maps:** Because $\det A = 5 \neq 0$, the inverse exists and is unique, guaranteeing that both analytical paths must converge to the identical mathematical point.

---

## 6. Final Answer in Words
Both methods produce the identical solution vector $x = \begin{pmatrix} 13/5 \\ 9/5 \end{pmatrix}$. Method 1 computes the inverse $A^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$ and multiplies it by $b$. Method 2 uses Gaussian elimination on the augmented matrix to obtain Row 2 as $-5x_2 = -9$, followed by back-substitution. Gaussian elimination was simpler in this example because it solves for $x$ in fewer steps without the overhead of computing all four entries of the inverse matrix.

---

## 7. Quick Verification
- **Substitute $x$ directly into Equation 1:**
  $$2\left(\frac{13}{5}\right) + 1\left(\frac{9}{5}\right) = \frac{26 + 9}{5} = \frac{35}{5} = 7 \quad \checkmark$$
- **Substitute $x$ directly into Equation 2:**
  $$1\left(\frac{13}{5}\right) + 3\left(\frac{9}{5}\right) = \frac{13 + 27}{5} = \frac{40}{5} = 8 \quad \checkmark$$
Both equations are verified simultaneously.

---

## 8. Common Mistakes to Avoid
- **Arithmetic Fraction Error:** When solving $x_1 = 8 - \frac{27}{5}$, converting $8$ incorrectly (e.g., $8 = \frac{48}{5}$ instead of $\frac{40}{5}$).
- **Sign Error in $R_2 - 2R_1$:** Calculating $1 - 2(3) = -5$ correctly, but writing $7 - 2(8) = +9$ instead of $-9$.
- **Assuming $A^{-1}b$ is Always Preferable:** Believing matrix inversion is faster because it looks like a single formula. In actual numerical mathematics, Gaussian elimination (LU decomposition) is almost always preferred over computing explicit inverses.

---

## 9. Classroom Presentation (3-Sentence Summary)
"We solve the system using $x = A^{-1}b$ by finding the inverse $A^{-1} = \frac{1}{5}\begin{pmatrix}3&-1\\-1&2\end{pmatrix}$ and multiplying by $b$, and then independently via Gaussian elimination on the augmented matrix with back-substitution. Both methods yield the exact same solution vector $x = \begin{pmatrix}13/5\\9/5\end{pmatrix}$. Gaussian elimination is the simpler and more efficient method here because it directly computes the two unknown coordinates without the unnecessary overhead of calculating the entire inverse matrix."

