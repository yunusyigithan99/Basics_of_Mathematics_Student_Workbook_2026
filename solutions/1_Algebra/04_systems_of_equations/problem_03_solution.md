# Exercise 3: Inconsistent System

## 1. Original Problem
Solve or show that the system is inconsistent:
$$\begin{cases} x + 2y = 3 \\ 2x + 4y = 7 \end{cases}$$
Show how the contradiction appears in the matrix after elimination and interpret it in terms of equations.

---

## 2. What We Are Trying to Find
We need to:
- Set up the augmented matrix $[A \mid b]$ for the $2 \times 2$ linear system.
- Apply Gaussian elimination to simplify the system.
- Identify the exact algebraic contradiction that emerges in the matrix during elimination.
- Interpret this contradiction both in terms of algebraic equations and in terms of the geometry of lines in the Cartesian plane.

---

## 3. Key Concepts and Theorems
1. **Inconsistent Linear System:**
   A system of linear equations is called **inconsistent** if it possesses no solutions ($S = \emptyset$).
2. **The Contradiction Row Criterion:**
   In Gaussian elimination, a system is inconsistent if and only if a row of the augmented matrix takes the form:
   $$\left[\begin{array}{cc|c} 0 & 0 & c \end{array}\right] \quad \text{with } c \neq 0$$
   This row represents the equation:
   $$0x + 0y = c \iff 0 = c$$
   Since $0$ cannot equal a non-zero number, no values of the variables can satisfy this equation.
3. **Geometric Interpretation of Inconsistency:**
   In $\mathbb{R}^2$, each linear equation represents a straight line.
   - If the lines have the same slope but different $y$-intercepts, they are **parallel and distinct**.
   - Distinct parallel lines never intersect, meaning there is no point $(x, y)$ common to both lines.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Augmented Matrix
Write down the augmented matrix:
$$M_0 = \left(\begin{array}{cc|c} 1 & 2 & 3 \\ 2 & 4 & 7 \end{array}\right)$$

---

### Step 2: Apply Gaussian Elimination
To eliminate the $x$-term in Row 2, subtract $2$ times Row 1 from Row 2:
$$R_2 \leftarrow R_2 - 2R_1$$

Calculate the row entries:
- First entry: $2 - 2(1) = 2 - 2 = 0$
- Second entry: $4 - 2(2) = 4 - 4 = 0$
- Right-hand side entry: $7 - 2(3) = 7 - 6 = 1$

The resulting augmented matrix is:
$$M_1 = \left(\begin{array}{cc|c} 1 & 2 & 3 \\ \mathbf{0} & \mathbf{0} & \mathbf{1} \end{array}\right)$$

---

### Step 3: Interpret the Contradiction in the Matrix and Equations
- **Matrix representation:**
  Row 2 is $\left[\begin{array}{cc|c} 0 & 0 & 1 \end{array}\right]$.
- **Equation interpretation:**
  Translating this row back into algebraic variables yields:
  $$0 \cdot x + 0 \cdot y = 1$$
  Simplifying the left-hand side:
  $$0 = 1$$
- **Conclusion:**
  The statement $0 = 1$ is universally false for all real numbers $x$ and $y$. No pair of numbers $(x, y)$, no matter how large, small, or complex, can ever make $0$ equal to $1$.
  Therefore, the system has **no solution** (it is inconsistent).

---

### Step 4: Geometric Interpretation
Let us write both equations in slope-intercept form ($y = mx + b$):
1. **Line 1 ($x + 2y = 3$):**
   $$2y = -x + 3 \implies y = -\frac{1}{2}x + \frac{3}{2}$$
   - Slope $m_1 = -\frac{1}{2}$
   - $y$-intercept $b_1 = \frac{3}{2} = 1.5$

2. **Line 2 ($2x + 4y = 7$):**
   $$4y = -2x + 7 \implies y = -\frac{2}{4}x + \frac{7}{4} \implies y = -\frac{1}{2}x + \frac{7}{4}$$
   - Slope $m_2 = -\frac{1}{2}$
   - $y$-intercept $b_2 = \frac{7}{4} = 1.75$

**Geometric deduction:**
Both lines have the exact same slope ($m_1 = m_2 = -1/2$), meaning they are parallel. However, their $y$-intercepts are different ($1.5 \neq 1.75$), meaning they are two distinct, non-overlapping lines. Because parallel lines never intersect, there is no point of intersection in the plane, which geometrically explains why the system has no solution.

---

## 5. Why Each Step Is Valid
- **Equivalence of Linear Systems:** Elementary row operations preserve the solution set. If the simplified system contains the false statement $0 = 1$, the original system must have had an empty solution set from the beginning.
- **Rouché-Capelli Theorem:** $\operatorname{rank}(A) = 1$, but $\operatorname{rank}([A \mid b]) = 2$. Since $\operatorname{rank}(A) < \operatorname{rank}([A \mid b])$, the system is strictly inconsistent.

---

## 6. Final Answer in Words
The system is inconsistent and has no solution. Performing the row operation $R_2 - 2R_1$ produces the row $\left[\begin{array}{cc|c} 0 & 0 & 1 \end{array}\right]$, which corresponds to the impossible equation $0 = 1$. Geometrically, the two equations describe two parallel lines with identical slopes of $-1/2$ but different $y$-intercepts ($1.5$ versus $1.75$), which never intersect.

---

## 7. Quick Verification
- **Determinant and proportionality check:**
  $$\det A = 1(4) - 2(2) = 0$$
  Since $\det A = 0$, the lines are parallel.
  Comparing the constant ratio with the coefficient ratio:
  $$\frac{a_{21}}{a_{11}} = \frac{2}{1} = 2, \quad \frac{a_{22}}{a_{12}} = \frac{4}{2} = 2, \quad \text{but} \quad \frac{b_2}{b_1} = \frac{7}{3} \neq 2$$
  Because the left-hand sides double while the right-hand sides do not double, the system is strictly inconsistent. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Claiming the Solution is $(0, 1)$:** Misreading $\left[\begin{array}{cc|c} 0 & 0 & 1 \end{array}\right]$ as $y = 1$. The coefficient of $y$ is $0$, not $1$.
- **Stopping at $\det A = 0$:** Concluding "no solution" solely from $\det A = 0$ without checking the right-hand side. (A zero determinant can also mean infinitely many solutions if $b$ is proportional).
- **Saying $x = 0, y = 0$ is a Solution:** Testing $(0, 0)$ gives $0 = 3$ and $0 = 7$, which fails both equations.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Applying Gaussian elimination with the operation $R_2 \leftarrow R_2 - 2R_1$ yields the row $\left[\begin{array}{cc|c}0&0&1\end{array}\right]$, which represents the mathematical impossibility $0 = 1$. This contradiction proves algebraically that the system is inconsistent and has no solution. Geometrically, both equations represent lines with identical slopes of $-1/2$ but different $y$-intercepts, meaning they are parallel lines that never intersect in the plane."

