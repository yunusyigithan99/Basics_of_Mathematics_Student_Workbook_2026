# Exercise 2: Gaussian Elimination — One Solution

## 1. Original Problem
Solve using Gaussian elimination:
$$\begin{cases} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 2 \end{cases}$$
After solving, substitute the result into all equations and check consistency.

---

## 2. What We Are Trying to Find
We need to:
- Form the augmented matrix $[A \mid b]$ for the $3 \times 3$ linear system.
- Apply Gaussian elimination to reduce the matrix to upper-triangular row echelon form.
- Use back-substitution to determine the unique numeric values for $x, y, z$.
- Substitute the computed values back into all three original equations to verify that each equality holds true.

---

## 3. Key Concepts and Theorems
1. **The Augmented Matrix:**
   A system $Ax = b$ is represented as $[A \mid b]$, allowing row operations to transform both coefficients and constants simultaneously.
2. **Row Echelon Form (REF):**
   A matrix is in echelon form if leading non-zero entries (pivots) move strictly to the right in successive rows, with all entries below each pivot equal to zero.
3. **Back-Substitution:**
   Once in upper-triangular echelon form, the bottom equation contains only one unknown. Solving it allows back-substituting upward to solve the remaining variables sequentially.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Augmented Matrix
Write down the augmented matrix $[A \mid b]$:
$$M_0 = \left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 2 & -1 & 1 & 3 \\ 1 & 2 & -1 & 2 \end{array}\right)$$

---

### Step 2: Forward Elimination (Column 1)
Using the pivot $a_{11} = 1$, eliminate entries below it:

1. **Eliminate entry $(2, 1)$ ($R_2 \leftarrow R_2 - 2R_1$):**
   $$(2, -1, 1 \mid 3) - 2(1, 1, 1 \mid 6) = (2 - 2, -1 - 2, 1 - 2 \mid 3 - 12) = (0, -3, -1 \mid -9)$$

2. **Eliminate entry $(3, 1)$ ($R_3 \leftarrow R_3 - R_1$):**
   $$(1, 2, -1 \mid 2) - (1, 1, 1 \mid 6) = (1 - 1, 2 - 1, -1 - 1 \mid 2 - 6) = (0, 1, -2 \mid -4)$$

The matrix becomes:
$$M_1 = \left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & -3 & -1 & -9 \\ 0 & 1 & -2 & -4 \end{array}\right)$$

---

### Step 3: Forward Elimination (Column 2)
To keep calculations simple and avoid fractions, swap Row 2 and Row 3 to get a pivot of $+1$:
$$R_2 \leftrightarrow R_3$$
$$M_2 = \left(\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & -2 & -4 \\ 0 & -3 & -1 & -9 \end{array}\right)$$

Now eliminate the entry $-3$ in Row 3 using Row 2:
$$R_3 \leftarrow R_3 + 3R_2$$
- Calculation:
  $$(0, -3, -1 \mid -9) + 3(0, 1, -2 \mid -4) = (0, -3 + 3, -1 - 6 \mid -9 - 12) = (0, 0, -7 \mid -21)$$

The matrix is now in **upper triangular row echelon form**:
$$M_3 = \left(\begin{array}{ccc|c} \mathbf{1} & 1 & 1 & 6 \\ 0 & \mathbf{1} & -2 & -4 \\ 0 & 0 & \mathbf{-7} & -21 \end{array}\right)$$

---

### Step 4: Back-Substitution
Translate the echelon matrix back into equations:
1. **Solve for $z$ from Row 3:**
   $$-7z = -21 \implies z = \frac{-21}{-7} = 3$$

2. **Solve for $y$ from Row 2:**
   $$y - 2z = -4$$
   Substitute $z = 3$:
   $$y - 2(3) = -4 \implies y - 6 = -4 \implies y = 2$$

3. **Solve for $x$ from Row 1:**
   $$x + y + z = 6$$
   Substitute $y = 2$ and $z = 3$:
   $$x + 2 + 3 = 6 \implies x + 5 = 6 \implies x = 1$$

Thus, the unique solution is:
$$(x, y, z) = (1, 2, 3)$$

---

### Step 5: Check Consistency by Substitution into All Equations
Substitute $x = 1, y = 2, z = 3$ into each of the original equations:
1. **Equation 1:**
   $$1 + 2 + 3 = 6 \quad (6 = 6) \quad \checkmark$$
2. **Equation 2:**
   $$2(1) - 2 + 3 = 2 - 2 + 3 = 3 \quad (3 = 3) \quad \checkmark$$
3. **Equation 3:**
   $$1 + 2(2) - 3 = 1 + 4 - 3 = 2 \quad (2 = 2) \quad \checkmark$$

All three equations are satisfied simultaneously.

---

## 5. Why Each Step Is Valid
- **Elementary Row Operations Preserve Equivalence:** Row replacement and row swapping generate an isomorphic system of linear constraints, guaranteeing that the solution set remains strictly invariant.
- **Triangular Decoupling:** In upper triangular form, the bottom equation contains a single independent unknown ($z$), enabling deterministic cascading evaluation.

---

## 6. Final Answer in Words
Using Gaussian elimination, the system is reduced to upper triangular form, yielding the unique solution $x = 1$, $y = 2$, and $z = 3$. Substituting these values back into the three original equations verifies that $1+2+3=6$, $2(1)-2+3=3$, and $1+2(2)-3=2$, confirming complete consistency.

---

## 7. Quick Verification
- **Vector check:**
  $$A\mathbf{x} = \begin{pmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 2 - 2 + 3 \\ 1 + 6 - 6 \\ 3 + 2 + 3 \end{pmatrix} \dots$$
  For our problem matrix $A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 1 & 2 & -1 \end{pmatrix}$:
  $$A\mathbf{x} = \begin{pmatrix} 1(1) + 1(2) + 1(3) \\ 2(1) - 1(2) + 1(3) \\ 1(1) + 2(2) - 1(3) \end{pmatrix} = \begin{pmatrix} 6 \\ 3 \\ 2 \end{pmatrix} = \mathbf{b} \quad \checkmark$$

---

## 8. Common Mistakes to Avoid
- **Arithmetic Slips with Negative Signs:** In $R_2 - 2R_1$, writing $3 - 2(6) = 3 - 12 = -9$, but mistakenly writing $+9$.
- **Stopping Without Back-Substitution:** Stopping after finding $z = 3$ without solving for $x$ and $y$.
- **Checking Only One Equation:** Verifying $x, y, z$ only in Equation 1. A solution must satisfy all equations.

---

## 9. Classroom Presentation (3-Sentence Summary)
"We set up the augmented matrix and apply Gaussian elimination using $R_2 - 2R_1$ and $R_3 - R_1$, then swap rows and eliminate to obtain an upper triangular matrix with $-7z = -21$. Back-substituting $z = 3$ upward through the equations gives $y = 2$ and $x = 1$. Substituting $(1, 2, 3)$ into all three original equations confirms that every equality holds, proving this is the unique solution."

