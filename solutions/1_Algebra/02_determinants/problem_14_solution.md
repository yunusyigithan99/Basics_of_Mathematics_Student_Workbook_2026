# Exercise 14: A System of Equations and the Determinant

## 1. Original Problem
Consider the system $Ax = b$, where:
$$A = \begin{pmatrix} 1 & 2 \\ k & 4 \end{pmatrix}$$
For which values of $k$ does the system have exactly one solution for every $b$? For the remaining value, give an example of a right-hand side $b$ for which the system has infinitely many solutions, and an example for which it has no solution.

---

## 2. What We Are Trying to Find
We need to:
- Compute the determinant of the coefficient matrix $A$ in terms of the parameter $k$.
- Determine the condition on $k$ that guarantees the linear system $Ax = b$ has a unique solution for any arbitrary vector $b$.
- For the critical value where uniqueness fails, construct a concrete right-hand side vector $b_{\text{inf}}$ that yields infinitely many solutions (a consistent dependent system).
- For the same critical value, construct a concrete right-hand side vector $b_{\text{none}}$ that yields no solution (an inconsistent system).

---

## 3. Key Concepts and Theorems
1. **Cramer's Rule and Uniqueness Theorem:**
   For a square linear system $Ax = b$:
   - The system has **exactly one solution for every $b$** if and only if the coefficient matrix $A$ is invertible, which means:
     $$\det A \neq 0$$
   - If $\det A = 0$, the system cannot have a unique solution: it either has **infinitely many solutions** (if $b$ lies in the column space of $A$) or **no solution** (if $b$ lies outside the column space of $A$).
2. **Rank and Consistency (Rouché-Capelli Theorem):**
   - Consistent with infinitely many solutions: $\operatorname{rank}(A) = \operatorname{rank}(A|b) < n$.
   - Inconsistent with no solution: $\operatorname{rank}(A) < \operatorname{rank}(A|b)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Determinant of $A$
The coefficient matrix is $A = \begin{pmatrix} 1 & 2 \\ k & 4 \end{pmatrix}$.
Using the $2 \times 2$ formula:
$$\det A = (1 \cdot 4) - (2 \cdot k) = 4 - 2k$$

---

### Step 2: Determine Values of $k$ for Exactly One Solution
The system has a unique solution for every right-hand side vector $b$ if and only if $\det A \neq 0$:
$$4 - 2k \neq 0 \iff 2k \neq 4 \iff k \neq 2$$

**Conclusion for Part 1:**
The system has exactly one solution for every $b$ whenever **$k \neq 2$**. In this case, the unique solution is given by $x = A^{-1}b$.

---

### Step 3: Analyze the Remaining Case ($k = 2$)
When $k = 2$, the determinant is zero ($\det A = 4 - 2(2) = 0$).
Substitute $k = 2$ into the system of equations:
$$\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}$$

Written out as individual linear equations:
$$\begin{cases} x_1 + 2x_2 = b_1 & \text{(Equation 1)} \\ 2x_1 + 4x_2 = b_2 & \text{(Equation 2)} \end{cases}$$

Notice that the left-hand side of Equation 2 is exactly twice the left-hand side of Equation 1:
$$2(x_1 + 2x_2) = 2x_1 + 4x_2$$
Therefore, consistency requires:
$$b_2 = 2b_1$$

---

### Step 4: Construct Examples for $k = 2$

1. **Example with Infinitely Many Solutions:**
   We need $b_2 = 2b_1$. Let $b_1 = 1$, then $b_2 = 2$:
   $$b_{\text{inf}} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
   The system becomes:
   $$\begin{cases} x_1 + 2x_2 = 1 \\ 2x_1 + 4x_2 = 2 \end{cases}$$
   Dividing the second equation by $2$ gives $x_1 + 2x_2 = 1$, which is completely redundant with the first equation. Setting $x_2 = t$ (a free parameter), we obtain infinitely many solutions:
   $$x_1 = 1 - 2t, \quad x_2 = t \quad (t \in \mathbb{R})$$

2. **Example with No Solution (Inconsistent):**
   We need $b_2 \neq 2b_1$. Let $b_1 = 1$, but choose $b_2 = 0$:
   $$b_{\text{none}} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$
   The system becomes:
   $$\begin{cases} x_1 + 2x_2 = 1 \\ 2x_1 + 4x_2 = 0 \end{cases}$$
   Multiply the first equation by $2$: $2x_1 + 4x_2 = 2$.
   Subtracting this from the second equation yields:
   $$0 = -2$$
   This is a blatant mathematical contradiction. Therefore, no solution exists.

---

## 5. Why Each Step Is Valid
- **Determinant Invertibility Theorem:** If $\det A \neq 0$, the columns of $A$ span all of $\mathbb{R}^2$, guaranteeing that any vector $b$ can be reached uniquely by $x = A^{-1}b$.
- **Linear Dependence of Equations:** When $k=2$, the row space has dimension $1$. The system is consistent if and only if the right-hand vector satisfies the identical linear constraint as the rows ($b_2 = 2b_1$).

---

## 6. Final Answer in Words
The system has exactly one solution for every right-hand side $b$ if and only if $k \neq 2$. For the remaining value $k = 2$, the determinant is zero. Choosing $b = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ makes the second equation an exact duplicate of the first, yielding infinitely many solutions of the form $x_1 = 1 - 2t, x_2 = t$. Choosing $b = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ creates the impossible contradiction $0 = -2$, meaning there are no solutions.

---

## 7. Quick Verification
- For $k = 3 \neq 2$: $\det A = 4 - 2(3) = -2 \neq 0$. The inverse $A^{-1}$ exists, confirming a unique solution for every $b$. $\checkmark$
- For $k = 2$ and $b = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$: $x = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ gives $A x = \begin{pmatrix} 1(1) + 2(0) \\ 2(1) + 4(0) \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} = b$; and $x = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$ gives $\begin{pmatrix} -1 + 2 \\ -2 + 4 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} = b$. Multiple distinct solutions confirm infinitely many solutions. $\checkmark$
- For $k = 2$ and $b = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$: Augmented matrix $\begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 0 \end{pmatrix} \xrightarrow{R_2 - 2R_1} \begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & -2 \end{pmatrix}$, confirming inconsistency. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Stating $k = 2$ Has "No Solutions" Generally:** Assuming $\det A = 0$ always means no solutions. $\det A = 0$ allows either infinitely many solutions OR no solutions, strictly depending on $b$.
- **Choosing an Invalid Right-Hand Side for Infinite Solutions:** Picking arbitrary numbers for $b$ without verifying the proportionality constraint $b_2 = 2b_1$.
- **Sign Error in Determinant:** Writing $4 + 2k = 0$, giving $k = -2$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"The determinant of the system is $\det A = 4 - 2k$, which is non-zero whenever $k \neq 2$, guaranteeing a unique solution for any vector $b$. When $k = 2$, the determinant is zero because the left-hand sides of the equations become parallel multiples of each other. In that case, choosing $b = \begin{pmatrix}1\\2\end{pmatrix}$ matches this ratio and produces infinitely many solutions, whereas choosing $b = \begin{pmatrix}1\\0\end{pmatrix}$ violates the ratio and leads to an impossible contradiction with no solutions."

