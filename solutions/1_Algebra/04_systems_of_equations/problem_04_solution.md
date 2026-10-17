# Exercise 4: Infinitely Many Solutions

## 1. Original Problem
Solve:
$$\begin{cases} x + y + z = 2 \\ 2x + 2y + 2z = 4 \\ x - y + z = 0 \end{cases}$$
Give the solution in parametric form, identify a free variable, and for one chosen parameter value check that the resulting point really satisfies the system.

---

## 2. What We Are Trying to Find
We need to:
- Apply Gaussian elimination to the augmented matrix $[A \mid b]$.
- Identify redundant equations and free variables in the system.
- Express the infinite solution set in a clean vector parametric form.
- Select a specific numerical value for the free parameter and evaluate a concrete solution point.
- Substitute that concrete point into all three equations to verify that it satisfies the entire system.

---

## 3. Key Concepts and Theorems
1. **Rank and Free Variables:**
   For a consistent system with $n$ variables and matrix rank $r$:
   $$\text{Number of free variables} = n - r$$
   If $r < n$, there is at least one free variable, and the system possesses **infinitely many solutions**.
2. **Parametric Form:**
   Assigning an arbitrary scalar parameter (such as $t \in \mathbb{R}$) to each free variable expresses the solution set as a line, plane, or affine subspace in $\mathbb{R}^n$:
   $$\mathbf{x} = \mathbf{x}_p + t \mathbf{v}_h$$
   where $\mathbf{x}_p$ is a particular solution and $\mathbf{v}_h$ is a basis vector of the homogeneous nullspace.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Augmented Matrix
Write down the augmented matrix:
$$M_0 = \left(\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 2 & 2 & 2 & 4 \\ 1 & -1 & 1 & 0 \end{array}\right)$$

---

### Step 2: Forward Elimination
1. **Eliminate Row 2 ($R_2 \leftarrow R_2 - 2R_1$):**
   $$(2, 2, 2 \mid 4) - 2(1, 1, 1 \mid 2) = (0, 0, 0 \mid 0)$$
   *Inspection:* Row 2 reduces completely to all zeros ($0 = 0$). This proves that Equation 2 was an exact duplicate ($2 \times$ Eq 1) providing no independent information.

2. **Eliminate Row 3 ($R_3 \leftarrow R_3 - R_1$):**
   $$(1, -1, 1 \mid 0) - (1, 1, 1 \mid 2) = (1 - 1, -1 - 1, 1 - 1 \mid 0 - 2) = (0, -2, 0 \mid -2)$$

The matrix becomes:
$$M_1 = \left(\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & 0 & 0 & 0 \\ 0 & -2 & 0 & -2 \end{array}\right)$$

---

### Step 3: Swap Rows into Echelon Form
Swap Row 2 and Row 3 to push the zero row to the bottom ($R_2 \leftrightarrow R_3$):
$$M_2 = \left(\begin{array}{ccc|c} \mathbf{1} & 1 & 1 & 2 \\ 0 & \mathbf{-2} & 0 & -2 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

Divide Row 2 by $-2$ ($R_2 \leftarrow -\frac{1}{2}R_2$):
$$M_3 = \left(\begin{array}{ccc|c} \mathbf{1} & 1 & 1 & 2 \\ 0 & \mathbf{1} & 0 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

---

### Step 4: Identify Pivots and the Free Variable
- **Pivot variables (leading entries):**
  - Column 1 has a pivot: $x$ is a basic/pivot variable.
  - Column 2 has a pivot: $y$ is a basic/pivot variable.
- **Free variable:**
  - Column 3 has **no pivot**: **$z$ is a free variable**.
  Set $z = t$, where $t \in \mathbb{R}$ is any real parameter.

---

### Step 5: Express Basic Variables in Terms of the Parameter
1. **From Row 2:**
   $$y = 1$$
   Notice that $y$ is completely fixed; it does not even depend on $t$!

2. **From Row 1:**
   $$x + y + z = 2$$
   Substitute $y = 1$ and $z = t$:
   $$x + 1 + t = 2 \implies x = 2 - 1 - t = 1 - t$$

---

### Step 6: Write the Solution in Parametric Form
Collecting the variables:
$$\begin{cases} x = 1 - t \\ y = 1 \\ z = t \end{cases} \qquad (t \in \mathbb{R})$$

In vector parametric form:
$$\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 - t \\ 1 \\ t \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}, \qquad t \in \mathbb{R}$$
Geometrically, this represents a straight line in 3D space passing through $(1, 1, 0)$ with direction vector $(-1, 0, 1)$.

---

### Step 7: Check a Specific Parameter Value
Choose a simple parameter value, say **$t = 2$**:
- $x = 1 - 2 = -1$
- $y = 1$
- $z = 2$

Test the point $(-1, 1, 2)$ in all three original equations:
1. **Equation 1:**
   $$x + y + z = -1 + 1 + 2 = 2 \quad (2 = 2) \quad \checkmark$$
2. **Equation 2:**
   $$2x + 2y + 2z = 2(-1) + 2(1) + 2(2) = -2 + 2 + 4 = 4 \quad (4 = 4) \quad \checkmark$$
3. **Equation 3:**
   $$x - y + z = -1 - 1 + 2 = 0 \quad (0 = 0) \quad \checkmark$$

The test point $(-1, 1, 2)$ satisfies all three equations perfectly!

---

## 5. Why Each Step Is Valid
- **Dimension of Affine Solution Space:** The coefficient matrix has rank $r = 2$ in $\mathbb{R}^3$, so by the Rank-Nullity Theorem, the solution space has dimension $3 - 2 = 1$ (a line).
- **Independence of Pivot Variables:** Fixing the free variable $z = t$ leaves a full-rank square subsystem for $x$ and $y$, which is uniquely solvable for every choice of $t$.

---

## 6. Final Answer in Words
The system has infinitely many solutions. The variable $z$ is free, while $y = 1$ is fixed and $x = 1 - t$. In parametric vector form, the solution set is $\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}$ for any $t \in \mathbb{R}$. Testing the parameter value $t = 2$ gives the point $(-1, 1, 2)$, which satisfies all three original equations.

---

## 7. Quick Verification
- **Testing another parameter value ($t = 0$):**
  Point: $(1, 1, 0)$.
  - $1 + 1 + 0 = 2 \checkmark$
  - $2(1) + 2(1) + 0 = 4 \checkmark$
  - $1 - 1 + 0 = 0 \checkmark$
- **Testing $t = -3$:**
  Point: $(4, 1, -3)$.
  - $4 + 1 - 3 = 2 \checkmark$
  - $2(4) + 2(1) + 2(-3) = 8 + 2 - 6 = 4 \checkmark$
  - $4 - 1 - 3 = 0 \checkmark$
Every generated point satisfies the system.

---

## 8. Common Mistakes to Avoid
- **Treating $y$ as a Free Variable:** Assuming any variable with a zero in the row is free. $y$ is a pivot variable with the fixed value $y = 1$.
- **Stopping at $0 = 0$:** Seeing the row of zeros and stopping without writing out the parametric equations for $x$ and $y$.
- **Writing $z = 0$ Instead of $z = t$:** Mistakenly assuming a free variable must be zero rather than recognizing it can take any real value.

---

## 9. Classroom Presentation (3-Sentence Summary)
"During Gaussian elimination, the second row reduces to all zeros because it is an exact duplicate of the first row, leaving us with rank 2 and making $z = t$ a free variable. Solving the remaining equations gives the fixed value $y = 1$ and $x = 1 - t$, producing the parametric line solution $\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}1\\1\\0\end{pmatrix} + t\begin{pmatrix}-1\\0\\1\end{pmatrix}$. Testing the specific parameter value $t = 2$ yields the point $(-1, 1, 2)$, which successfully satisfies all three equations."

