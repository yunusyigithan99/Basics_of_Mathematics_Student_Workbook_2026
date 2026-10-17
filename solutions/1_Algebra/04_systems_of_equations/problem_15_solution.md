# Exercise 15: Classifying Three Systems

## 1. Original Problem
For each of the following systems, perform only as much elimination as necessary to recognize its type:

1. $$\begin{cases} x + y = 2 \\ x - y = 0 \end{cases}$$
2. $$\begin{cases} x + y = 2 \\ 2x + 2y = 4 \end{cases}$$
3. $$\begin{cases} x + y = 2 \\ 2x + 2y = 5 \end{cases}$$

For each, justify the classification: exactly one solution, infinitely many solutions, or no solution.

---

## 2. What We Are Trying to Find
We need to:
- Apply minimal Gaussian elimination to each of the three $2 \times 2$ systems.
- Stop elimination as soon as the structural echelon form reveals the nature of the solution space.
- Classify each system into one of the three fundamental linear algebra categories:
  - Exactly one solution (consistent, full rank),
  - Infinitely many solutions (consistent, rank deficiency),
  - No solution (inconsistent, contradiction).
- Provide a rigorous mathematical justification for each classification.

---

## 3. Key Concepts and Theorems
1. **The Three Fundamental Classifications:**
   Any system of linear equations in echelon form exhibits one of three structural outcomes:
   - **Unique Solution:** Every variable column has a leading pivot ($\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) = n$). No free variables exist.
   - **Infinitely Many Solutions:** The system is consistent, but at least one row becomes all zeros: $[0 \; 0 \dots 0 \mid 0]$, meaning $\operatorname{rank}(A) = \operatorname{rank}([A \mid b]) < n$. At least one free variable exists.
   - **No Solution (Inconsistent):** A row emerges with zeros in the coefficient block and a non-zero constant on the right: $[0 \; 0 \dots 0 \mid c]$ with $c \neq 0$, representing the impossible equation $0 = c$.

---

## 4. Detailed Step-by-Step Solution

### System 1:
$$\begin{cases} x + y = 2 \\ x - y = 0 \end{cases}$$

- **Augmented matrix setup:**
  $$\left(\begin{array}{cc|c} 1 & 1 & 2 \\ 1 & -1 & 0 \end{array}\right)$$
- **Minimal Elimination (1 Step):**
  Subtract Row 1 from Row 2 ($R_2 \leftarrow R_2 - R_1$):
  $$(1, -1 \mid 0) - (1, 1 \mid 2) = (1 - 1, -1 - 1 \mid 0 - 2) = (0, -2 \mid -2)$$
  $$\left(\begin{array}{cc|c} \mathbf{1} & 1 & 2 \\ 0 & \mathbf{-2} & -2 \end{array}\right)$$
- **Classification:** **Exactly One Solution**.
- **Justification:**
  The matrix is in upper triangular form with two non-zero pivots ($a_{11} = 1$ and $a_{22} = -2$).
  Because the number of pivots ($r = 2$) equals the number of variables ($n = 2$), every variable has a unique pivot column and there are no free variables.
  Solving gives $y = \frac{-2}{-2} = 1$ and $x = 2 - 1 = 1$, producing the unique solution $(1, 1)$.

---

### System 2:
$$\begin{cases} x + y = 2 \\ 2x + 2y = 4 \end{cases}$$

- **Augmented matrix setup:**
  $$\left(\begin{array}{cc|c} 1 & 1 & 2 \\ 2 & 2 & 4 \end{array}\right)$$
- **Minimal Elimination (1 Step):**
  Subtract $2$ times Row 1 from Row 2 ($R_2 \leftarrow R_2 - 2R_1$):
  $$(2, 2 \mid 4) - 2(1, 1 \mid 2) = (2 - 2, 2 - 2 \mid 4 - 4) = (0, 0 \mid 0)$$
  $$\left(\begin{array}{cc|c} \mathbf{1} & 1 & 2 \\ 0 & 0 & 0 \end{array}\right)$$
- **Classification:** **Infinitely Many Solutions**.
- **Justification:**
  The second row reduces entirely to zeros ($[0 \; 0 \mid 0]$), which represents the trivially true statement $0 = 0$.
  The system is consistent, but has only $r = 1$ pivot for $n = 2$ variables.
  The number of free variables is $n - r = 2 - 1 = 1$ ($y = t$ is free). The system describes a single line $x + y = 2$, yielding the infinite solution set $(x, y) = (2 - t, t)$.

---

### System 3:
$$\begin{cases} x + y = 2 \\ 2x + 2y = 5 \end{cases}$$

- **Augmented matrix setup:**
  $$\left(\begin{array}{cc|c} 1 & 1 & 2 \\ 2 & 2 & 5 \end{array}\right)$$
- **Minimal Elimination (1 Step):**
  Subtract $2$ times Row 1 from Row 2 ($R_2 \leftarrow R_2 - 2R_1$):
  $$(2, 2 \mid 5) - 2(1, 1 \mid 2) = (2 - 2, 2 - 2 \mid 5 - 4) = (0, 0 \mid 1)$$
  $$\left(\begin{array}{cc|c} 1 & 1 & 2 \\ \mathbf{0} & \mathbf{0} & \mathbf{1} \end{array}\right)$$
- **Classification:** **No Solution (Inconsistent)**.
- **Justification:**
  The second row has zeros in all variable columns but a non-zero number on the right ($[0 \; 0 \mid 1]$).
  This corresponds to the equation:
  $$0x + 0y = 1 \iff 0 = 1$$
  Because $0 = 1$ is an impossible mathematical contradiction, no pair $(x, y)$ can ever satisfy the system.
  Here, $\operatorname{rank}(A) = 1$, but $\operatorname{rank}([A \mid b]) = 2$. By the Rouché-Capelli Theorem, the system is strictly inconsistent.

---

## 5. Why Each Step Is Valid
- **Rouché-Capelli Theorem Rigor:**
  1. System 1: $\operatorname{rank}(A) = 2 = \operatorname{rank}([A \mid b]) = n \implies$ unique solution.
  2. System 2: $\operatorname{rank}(A) = 1 = \operatorname{rank}([A \mid b]) < n \implies$ infinitely many solutions.
  3. System 3: $\operatorname{rank}(A) = 1 < 2 = \operatorname{rank}([A \mid b]) \implies$ no solution.
- **Geometric Invariance:** In $\mathbb{R}^2$, System 1 represents two perpendicular crossing lines (intersecting at $(1, 1)$), System 2 represents two completely coincident identical lines, and System 3 represents two distinct parallel lines that never intersect.

---

## 6. Final Answer in Words
1. **System 1 has exactly one solution** because one elimination step yields pivots in both columns ($\operatorname{rank} = 2$), giving the unique point $(1, 1)$.
2. **System 2 has infinitely many solutions** because one elimination step produces the row $[0 \; 0 \mid 0]$, meaning the equations are identical multiples of each other ($\operatorname{rank} = 1$) with one free variable.
3. **System 3 has no solution** because one elimination step produces the contradiction row $[0 \; 0 \mid 1]$, meaning $0 = 1$, which represents two parallel non-intersecting lines.

---

## 7. Quick Verification
- **Determinant checks on the coefficient matrices:**
  - System 1: $\det\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = -1 - 1 = -2 \neq 0 \implies$ Unique solution. $\checkmark$
  - System 2: $\det\begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix} = 2 - 2 = 0$; constants satisfy $4 = 2(2) \implies$ Infinitely many solutions. $\checkmark$
  - System 3: $\det\begin{pmatrix} 1 & 1 \\ 2 & 2 \end{pmatrix} = 2 - 2 = 0$; constants satisfy $5 \neq 2(2) \implies$ No solution. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Carrying Out Unnecessary Steps:** Continuing elimination to Jordan form when the prompt says *"perform only as much elimination as necessary to recognize its type"*. A single row operation suffices for all three.
- **Confusing $[0 \; 0 \mid 0]$ with $[0 \; 0 \mid 1]$:** Misreading the zero row of infinite solutions as no solution, or vice versa.
- **Classifying without Justification:** Merely stating "one solution" without citing rank, pivots, or contradiction rows.

---

## 9. Classroom Presentation (3-Sentence Summary)
"With a single elimination step on each system, System 1 produces two non-zero pivots with no free variables, which guarantees exactly one unique solution at $(1, 1)$. System 2 produces the row $[0 \; 0 \mid 0]$, showing the second equation is an exact duplicate that leaves one free variable and infinitely many solutions. System 3 produces the contradiction row $[0 \; 0 \mid 1]$, which translates to the impossible equation $0 = 1$ and proves the system has no solution."

