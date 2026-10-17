# Exercise 11: A Parameter in a System of Three Equations

## 1. Original Problem
Analyze the number of solutions depending on the parameter $t$:
$$\begin{cases} x + y + z = 1 \\ x + ty + z = 2 \\ x + y + tz = 3 \end{cases}$$
Use elimination and separately analyze the parameter values for which a standard calculation step ceases to be valid.

---

## 2. What We Are Trying to Find
We need to:
- Apply Gaussian elimination to the parameterized $3 \times 3$ system.
- Identify the critical pivot step that depends on the parameter $t$ and determine when division by that expression is undefined.
- Analyze the system at the singular value where standard division ceases to be valid.
- Analyze the system for all remaining general values of $t$.
- Classify the number of solutions across all cases (unique solution, infinite solutions, or no solution).

---

## 3. Key Concepts and Theorems
1. **Division Validity in Elimination:**
   In Gaussian elimination, dividing a row by an algebraic expression $c(t)$ is valid **if and only if** $c(t) \neq 0$.
   Whenever an expression involving a parameter appears as a pivot, you must branch into separate cases:
   - Case 1: The pivot equals zero ($c(t) = 0$), where division is forbidden.
   - Case 2: The pivot is non-zero ($c(t) \neq 0$), where standard reduction proceeds.
2. **Determinant Criterion:**
   $\det A(t) \neq 0 \iff$ unique solution exists.
   $\det A(t) = 0 \iff$ either no solution or infinitely many solutions, determined by the augmented column.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Augmented Matrix
Write the augmented matrix $[A(t) \mid b]$:
$$M_0 = \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 1 & t & 1 & 2 \\ 1 & 1 & t & 3 \end{array}\right)$$

---

### Step 2: Perform Initial Elimination (Using Pivot 1)
Using the constant pivot $a_{11} = 1$, eliminate entries in the first column:
1. **$R_2 \leftarrow R_2 - R_1$:**
   $$(1, t, 1 \mid 2) - (1, 1, 1 \mid 1) = (1 - 1, t - 1, 1 - 1 \mid 2 - 1) = (0, t - 1, 0 \mid 1)$$
2. **$R_3 \leftarrow R_3 - R_1$:**
   $$(1, 1, t \mid 3) - (1, 1, 1 \mid 1) = (1 - 1, 1 - 1, t - 1 \mid 3 - 1) = (0, 0, t - 1 \mid 2)$$

The augmented matrix is now:
$$M_1 = \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & \mathbf{t - 1} & 0 & 1 \\ 0 & 0 & \mathbf{t - 1} & 2 \end{array}\right)$$

Notice that this matrix is already in **upper triangular form**!
The diagonal pivot positions are:
$$a_{11} = 1, \qquad a_{22} = t - 1, \qquad a_{33} = t - 1$$

---

### Step 3: Identify Where Standard Calculation Ceases to Be Valid
To solve for $y$ from Row 2 and for $z$ from Row 3, the standard algebraic step is:
$$y = \frac{1}{t - 1}, \qquad z = \frac{2}{t - 1}$$
This operation requires dividing by $t - 1$, which ceases to be valid when the denominator is zero:
$$t - 1 = 0 \iff t = 1$$
Therefore, we must branch into two mutually exclusive cases: **$t = 1$** and **$t \neq 1$**.

---

### Step 4: Analysis of Case 1 ($t = 1$)
Substitute $t = 1$ directly into matrix $M_1$:
$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 2 \end{array}\right)$$

Look at Row 2 and Row 3:
- Row 2 translates to: $0 \cdot x + 0 \cdot y + 0 \cdot z = 1 \iff 0 = 1$
- Row 3 translates to: $0 \cdot x + 0 \cdot y + 0 \cdot z = 2 \iff 0 = 2$

Both rows represent impossible mathematical contradictions ($0 = 1$ and $0 = 2$).
Therefore, when $t = 1$, the system is **inconsistent** and has **no solution**.

---

### Step 5: Analysis of Case 2 ($t \neq 1$)
When $t \neq 1$, the pivot $t - 1$ is non-zero, so division by $t - 1$ is completely legitimate.

1. **From Row 3:**
   $$(t - 1)z = 2 \implies z = \frac{2}{t - 1}$$

2. **From Row 2:**
   $$(t - 1)y = 1 \implies y = \frac{1}{t - 1}$$

3. **From Row 1 (back-substitution):**
   $$x + y + z = 1$$
   $$x + \frac{1}{t - 1} + \frac{2}{t - 1} = 1$$
   $$x + \frac{3}{t - 1} = 1 \implies x = 1 - \frac{3}{t - 1} = \frac{(t - 1) - 3}{t - 1} = \frac{t - 4}{t - 1}$$

Because $x, y, z$ are uniquely determined for any chosen $t \neq 1$, the system has **exactly one solution**.

---

### Step 6: Summary of the Analysis
- For **$t = 1$**: **No solution** (inconsistent).
- For **$t \neq 1$**: **Exactly one solution**, given explicitly by:
  $$\mathbf{x} = \begin{pmatrix} \frac{t - 4}{t - 1} \\ \frac{1}{t - 1} \\ \frac{2}{t - 1} \end{pmatrix}$$
- The case of **infinitely many solutions never occurs** for any value of $t$.

---

## 5. Why Each Step Is Valid
- **Equivalence of Linear Systems:** $R_2 - R_1$ and $R_3 - R_1$ involve only integer additions that do not scale the target rows, remaining universally valid for all $t \in \mathbb{R}$.
- **Determinant Product Formula:** $\det A(t) = 1 \cdot (t - 1) \cdot (t - 1) = (t - 1)^2$. The matrix is non-singular if and only if $(t - 1)^2 \neq 0 \iff t \neq 1$.

---

## 6. Final Answer in Words
The system has two possible behaviors depending on $t$:
- If $t = 1$, the standard step of dividing by $t - 1$ ceases to be valid because it produces division by zero; substituting $t = 1$ yields the contradiction $0 = 1$, meaning there is **no solution**.
- If $t \neq 1$, the pivot $t - 1 \neq 0$ is valid, and the system has **exactly one solution** given by $x = \frac{t - 4}{t - 1}$, $y = \frac{1}{t - 1}$, and $z = \frac{2}{t - 1}$. Infinitely many solutions can never occur.

---

## 7. Quick Verification
- **Test with $t = 2 \neq 1$:**
  Formula prediction: $x = \frac{2 - 4}{2 - 1} = -2$, $y = \frac{1}{1} = 1$, $z = \frac{2}{1} = 2$.
  Check original equations:
  - Eq 1: $-2 + 1 + 2 = 1 \checkmark$
  - Eq 2: $-2 + 2(1) + 2 = 2 \checkmark$
  - Eq 3: $-2 + 1 + 2(2) = 3 \checkmark$
- **Test with $t = 4$:**
  Formula: $x = 0, y = 1/3, z = 2/3$.
  - Eq 1: $0 + 1/3 + 2/3 = 1 \checkmark$
  - Eq 2: $0 + 4(1/3) + 2/3 = 6/3 = 2 \checkmark$
  - Eq 3: $0 + 1/3 + 4(2/3) = 9/3 = 3 \checkmark$
The solution holds across all $t \neq 1$.

---

## 8. Common Mistakes to Avoid
- **Dividing by $t - 1$ Without Specifying $t \neq 1$:** Performing division blindly, missing the critical breakdown point $t = 1$.
- **Assuming $t = 1$ Has Infinite Solutions:** Seeing identical coefficients on the left and assuming infinite solutions, while missing that the right-hand sides are different ($1 \neq 2 \neq 3$), creating a contradiction.
- **Algebraic Slip in $x$:** Writing $1 - \frac{3}{t-1} = \frac{t-2}{t-1}$ instead of $\frac{t-4}{t-1}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Subtracting the first row from the second and third rows simplifies the system into an upper triangular matrix with $t - 1$ as the second and third diagonal pivots. For $t = 1$, standard division is invalid and the equations produce the contradiction $0 = 1$, meaning the system has no solution. For any $t \neq 1$, the pivots are non-zero, yielding a unique solution where $y = \frac{1}{t-1}$, $z = \frac{2}{t-1}$, and $x = \frac{t-4}{t-1}$."

