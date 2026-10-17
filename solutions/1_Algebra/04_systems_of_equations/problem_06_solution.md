# Exercise 6: A System with a Parameter — Which Cases Actually Occur?

## 1. Original Problem
Analyze, depending on the parameter $a$, the system:
$$\begin{cases} x + y = 2 \\ ax + ay = 4 \end{cases}$$
Among the three possibilities — exactly one solution, infinitely many solutions, no solution — determine which actually occur and for which values of $a$. If one type cannot occur, explain why.

---

## 2. What We Are Trying to Find
We need to:
- Perform Gaussian elimination on the parameterized $2 \times 2$ system.
- Classify the behavior of the system across all real values of $a \in \mathbb{R}$.
- Identify which of the three standard linear system outcomes (unique solution, infinite solutions, no solution) actually occur, and for which values of $a$.
- Identify which case NEVER occurs, and provide a rigorous theoretical and geometric explanation of why it is impossible.

---

## 3. Key Concepts and Theorems
1. **The Three Theoretical Possibilities for a Linear System:**
   For any linear system over $\mathbb{R}$, exactly one of the following holds:
   - **Case 1:** Exactly one solution ($\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) = n$).
   - **Case 2:** Infinitely many solutions ($\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) < n$).
   - **Case 3:** No solution ($\operatorname{rank}(A) < \operatorname{rank}([A \mid b])$).
2. **Determinant and Unique Solutions:**
   A square $n \times n$ system can have a unique solution if and only if its coefficient determinant is non-zero:
   $$\text{Unique solution} \iff \det A \neq 0$$
   If $\det A = 0$ identically for all values of a parameter, a unique solution can **never** occur under any circumstances.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Augmented Matrix
Write the system as an augmented matrix:
$$M_0 = \left(\begin{array}{cc|c} 1 & 1 & 2 \\ a & a & 4 \end{array}\right)$$

---

### Step 2: Apply Gaussian Elimination
Eliminate the variable $x$ in Row 2 by subtracting $a$ times Row 1 from Row 2:
$$R_2 \leftarrow R_2 - a R_1$$

Compute each entry of the new Row 2:
- First entry: $a - a(1) = 0$
- Second entry: $a - a(1) = 0$
- Right-hand side entry: $4 - a(2) = 4 - 2a$

The resulting augmented matrix is:
$$M_1 = \left(\begin{array}{cc|c} 1 & 1 & 2 \\ \mathbf{0} & \mathbf{0} & \mathbf{4 - 2a} \end{array}\right)$$

The second row represents the equation:
$$0 \cdot x + 0 \cdot y = 4 - 2a \iff 0 = 4 - 2a$$

---

### Step 3: Analyze the Cases Depending on $a$

1. **Subcase 1: When $4 - 2a = 0 \iff 2a = 4 \iff a = 2$:**
   Substitute $a = 2$ into the matrix:
   $$\left(\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & 0 & 0 \end{array}\right)$$
   The second row becomes $0 = 0$, which is always true and provides no constraint.
   The system reduces to the single equation:
   $$x + y = 2 \implies x = 2 - y$$
   Setting $y = t \in \mathbb{R}$, we get:
   $$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2 - t \\ t \end{pmatrix} = \begin{pmatrix} 2 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 1 \end{pmatrix}$$
   **Outcome:** **Infinitely many solutions** occur when **$a = 2$**.

2. **Subcase 2: When $4 - 2a \neq 0 \iff a \neq 2$:**
   If $a \neq 2$, the right-hand side $4 - 2a$ is a non-zero number (for example, if $a = 0$, $4 - 2(0) = 4$, giving $0 = 4$).
   The second equation becomes:
   $$0 = \text{non-zero number}$$
   This is a complete contradiction. No values of $x$ and $y$ can satisfy this equation.
   **Outcome:** **No solution (inconsistent)** occurs for all **$a \neq 2$**.

---

### Step 4: Explain Why "Exactly One Solution" Can NEVER Occur
The case of **exactly one solution cannot occur for any value of $a$**.

**Algebraic Proof:**
Look at the coefficient matrix $A = \begin{pmatrix} 1 & 1 \\ a & a \end{pmatrix}$.
Compute its determinant:
$$\det A = (1 \cdot a) - (1 \cdot a) = a - a = 0$$
Notice that $\det A = 0$ for **every single real number $a$**.
Because a unique solution requires $\det A \neq 0$, and here the determinant is identically zero regardless of $a$, the matrix is permanently singular. The rank of $A$ is at most $1$, which is strictly less than the number of variables ($n = 2$).

**Geometric Proof:**
- The left-hand side of Equation 1 is $x + y$.
- The left-hand side of Equation 2 is $a(x + y)$.
Both equations describe lines with normal vector $(1, 1)$, meaning their slope is always $m = -1$. Because the two lines are always parallel, they either completely coincide (when $a = 2$, giving infinitely many solutions) or are parallel and distinct (when $a \neq 2$, giving no solutions). They can never cross at a single point.

---

## 5. Why Each Step Is Valid
- **Equivalence of Linear Systems:** $R_2 - aR_1$ is valid for all $a \in \mathbb{R}$ because it adds a multiple of Row 1 to Row 2 without scaling Row 2 itself.
- **Rouché-Capelli Theorem:** $\operatorname{rank}(A) = 1$ for all $a$. For $a = 2$, $\operatorname{rank}([A|b]) = 1 = \operatorname{rank}(A) < 2$ (infinite solutions). For $a \neq 2$, $\operatorname{rank}([A|b]) = 2 > \operatorname{rank}(A)$ (inconsistent).

---

## 6. Final Answer in Words
Of the three theoretical possibilities:
- **Infinitely many solutions** occurs when $a = 2$.
- **No solution** occurs for all $a \neq 2$.
- **Exactly one solution** can **never occur** for any value of $a$, because the determinant of the coefficient matrix is identically zero ($\det A = a - a = 0$) for all $a$, meaning the two lines are always parallel and can never cross at a single point.

---

## 7. Quick Verification
- **Test $a = 2$:** System is $\begin{cases} x+y=2 \\ 2x+2y=4 \end{cases}$. Dividing the second equation by 2 gives $x+y=2$. The equations are identical, confirming infinitely many solutions. $\checkmark$
- **Test $a = 0$:** System is $\begin{cases} x+y=2 \\ 0 = 4 \end{cases}$. The second equation is $0 = 4$, confirming no solution. $\checkmark$
- **Test $a = 1$:** System is $\begin{cases} x+y=2 \\ x+y=4 \end{cases}$. Subtracting gives $0 = -2$, confirming no solution. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Assuming All Three Cases Must Occur:** Blindly writing down parameter intervals for "unique solution" without checking $\det A$.
- **Dividing by $a$ Early:** Dividing Equation 2 by $a$ without considering that $a = 0$ requires a separate case. Performing $R_2 - aR_1$ avoids division by $a$ completely.
- **Confusing $a = 2$ with $a = 4$:** Solving $4 - 2a = 0$ as $a = 4$ instead of $a = 2$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Eliminating $x$ from the second row gives $0 = 4 - 2a$, which produces infinitely many solutions when $a = 2$ and no solution for all other values $a \neq 2$. The case of exactly one solution can never occur because the coefficient determinant is $a - a = 0$ for every value of $a$. Geometrically, the two equations have identical left-hand side ratios, so the lines are always parallel and can never intersect at a unique point."

