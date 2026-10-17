# Exercise 5: Row Echelon Form and Number of Solutions

## 1. Original Problem
For the augmented matrix:
$$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right]$$
determine the number of solutions and write them in parametric form. Explain how you know how many variables may be chosen freely.

---

## 2. What We Are Trying to Find
We need to:
- Analyze the given augmented matrix already in row echelon form.
- Identify the number of variables, pivots, and ranks of the coefficient and augmented matrices.
- Determine whether the system is consistent and state the total number of solutions.
- Mathematically explain how to determine the exact number of free variables.
- Write out the complete solution set in clean vector parametric form.

---

## 3. Key Concepts and Theorems
1. **Reading Echelon Forms:**
   Let $n$ be the number of unknowns (columns of the coefficient matrix) and let $r$ be the number of non-zero rows (pivots):
   - **Consistency Check:** If there is no row of the form $[0 \; 0 \dots 0 \mid c]$ with $c \neq 0$, the system is consistent.
   - **Unique Solution:** Occurs if and only if $r = n$ (every column has a pivot).
   - **Infinitely Many Solutions:** Occurs if the system is consistent and $r < n$.
2. **Formula for the Number of Free Variables:**
   $$\text{Number of free variables} = n - r$$
   where $n$ is the total number of variables and $r = \operatorname{rank}(A)$ is the number of pivot columns.
   Variables corresponding to columns without pivots can be chosen completely freely.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze the Augmented Matrix
Look at the matrix:
$$M = \left[\begin{array}{ccc|c} \mathbf{1} & 2 & -1 & 3 \\ 0 & \mathbf{1} & 2 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right]$$

- Total number of variables: $n = 3$ (denote them $x_1, x_2, x_3$).
- The pivots (leading non-zero entries of each row) are:
  - Row 1 pivot is in Column 1 ($a_{11} = 1$).
  - Row 2 pivot is in Column 2 ($a_{22} = 1$).
  - Row 3 has no pivot (it is entirely zeros: $[0 \; 0 \; 0 \mid 0]$).
- Number of pivots: $r = 2$.
- The bottom row represents the valid equation $0x_1 + 0x_2 + 0x_3 = 0$ ($0 = 0$), so the system is **consistent**.

---

### Step 2: Determine How Many Variables Are Free
Using the fundamental rank formula:
$$\text{Free variables} = n - r = 3 - 2 = 1$$
- Columns 1 and 2 contain pivots: $x_1$ and $x_2$ are **basic (pivot) variables**.
- Column 3 has **no pivot**: **$x_3$ is the single free variable**.

We assign the free variable an arbitrary real parameter $t$:
$$x_3 = t, \qquad t \in \mathbb{R}$$

Because there is at least one free variable and the system is consistent, the system has **infinitely many solutions**.

---

### Step 3: Express Basic Variables in Terms of Parameter $t$
Solve the equations from bottom to top using back-substitution:

1. **From Row 2:**
   $$x_2 + 2x_3 = 1$$
   Substitute $x_3 = t$:
   $$x_2 + 2t = 1 \implies x_2 = 1 - 2t$$

2. **From Row 1:**
   $$x_1 + 2x_2 - x_3 = 3$$
   Substitute $x_2 = 1 - 2t$ and $x_3 = t$:
   $$x_1 + 2(1 - 2t) - t = 3$$
   Expand the parentheses:
   $$x_1 + 2 - 4t - t = 3$$
   $$x_1 + 2 - 5t = 3 \implies x_1 = 3 - 2 + 5t = 1 + 5t$$

---

### Step 4: Write the Solution in Parametric Form
We collect the three coordinate formulas:
$$\begin{cases} x_1 = 1 + 5t \\ x_2 = 1 - 2t \\ x_3 = t \end{cases} \qquad (t \in \mathbb{R})$$

In vector notation, decompose into a particular solution vector plus the parameterized direction vector:
$$\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 + 5t \\ 1 - 2t \\ t \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} 5 \\ -2 \\ 1 \end{pmatrix}, \qquad t \in \mathbb{R}$$

---

## 5. Why Each Step Is Valid
- **Rank-Nullity Theorem:** In a linear system, the dimension of the affine solution space equals the nullity of the coefficient matrix ($\operatorname{nullity} = n - \operatorname{rank} = 3 - 2 = 1$). A 1-dimensional affine space in $\mathbb{R}^3$ is geometrically a line with infinitely many points.
- **Back-Substitution Triangularity:** With $x_3$ fixed to parameter $t$, the remaining $2 \times 2$ block for $x_1, x_2$ is upper triangular with non-zero diagonal entries $1, 1$, ensuring a unique solution for $x_1$ and $x_2$ for every chosen value of $t$.

---

## 6. Final Answer in Words
The system is consistent and possesses infinitely many solutions. We know exactly one variable may be chosen freely because there are $3$ variables and only $2$ pivots ($3 - 2 = 1$ free variable, which is $x_3 = t$). In parametric vector form, the solution set is $\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} 5 \\ -2 \\ 1 \end{pmatrix}$ for all $t \in \mathbb{R}$.

---

## 7. Quick Verification
- **Test with parameter $t = 0$:**
  $\mathbf{x} = (1, 1, 0)^T$.
  - Row 1: $1(1) + 2(1) - 1(0) = 1 + 2 - 0 = 3 \checkmark$
  - Row 2: $0(1) + 1(1) + 2(0) = 1 \checkmark$
- **Test with parameter $t = 1$:**
  $\mathbf{x} = (6, -1, 1)^T$.
  - Row 1: $1(6) + 2(-1) - 1(1) = 6 - 2 - 1 = 3 \checkmark$
  - Row 2: $0(6) + 1(-1) + 2(1) = -1 + 2 = 1 \checkmark$
Both test points satisfy the system perfectly.

---

## 8. Common Mistakes to Avoid
- **Arithmetic Sign Error in Back-Substitution:** When simplifying $x_1 + 2(1 - 2t) - t = 3$, writing $+4t$ instead of $-4t$, which yields $-3t$ instead of $+5t$.
- **Believing Row 3 Implies No Solution:** Confusing $[0 \; 0 \; 0 \mid 0]$ (consistent, $0=0$) with $[0 \; 0 \; 0 \mid 1]$ (inconsistent, $0=1$).
- **Claiming 2 Free Variables:** Counting non-zero rows instead of subtracting pivots from total variables.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Looking at the row echelon form, we have $3$ variables and $2$ pivot columns, which by the formula $n - r = 3 - 2 = 1$ means exactly one variable ($x_3 = t$) can be chosen freely. Because the system is consistent with a free variable, there are infinitely many solutions. Back-substituting in terms of $t$ gives $x_2 = 1 - 2t$ and $x_1 = 1 + 5t$, defining a 1-dimensional line of solutions $\begin{pmatrix}1\\1\\0\end{pmatrix} + t\begin{pmatrix}5\\-2\\1\end{pmatrix}$."

