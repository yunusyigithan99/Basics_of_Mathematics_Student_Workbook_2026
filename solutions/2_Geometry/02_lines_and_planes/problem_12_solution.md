# Problem 12 Solution: Intersection Line of Two Planes

## 1. Original Problem
Find a parametric vector equation of the line formed by the intersection of the two planes:
$$\Pi_1 : x + y + z = 3, \qquad \Pi_2 : x - y + z = 1.$$
Find its direction vector in two distinct ways:
1. Directly from the system of linear equations by introducing a free parameter.
2. From the vector cross product of the normal vectors of the two planes.

Compare the results from both methods.

---

## 2. What We Are Trying to Find
We need to:
1. Extract the normal vectors $n_1$ and $n_2$ and compute their cross product $n_1 \times n_2$.
2. Solve the linear system of two equations in three variables by elimination, expressing $x$ and $y$ in terms of free variable $z$.
3. Extract the direction vector from both representations and compare them (showing they are collinear scalar multiples).
4. Find a base point and write the complete parametric equation of the intersection line.

---

## 3. Key Concepts and Theorems
1. **Geometric Intersection of Two Planes:**
   Two non-parallel planes in $\mathbb{R}^3$ intersect along a unique straight line.
2. **Direction Vector via Cross Product:**
   Since the line of intersection lies in both planes simultaneously, its direction vector $v$ must be perpendicular to both normal vectors $n_1$ and $n_2$. Therefore, the cross product gives a direction vector for the line:
   $$v \parallel (n_1 \times n_2).$$
3. **Algebraic Solution (Underdetermined Linear System):**
   A system of 2 linear equations in 3 variables with rank 2 has 1 degree of freedom (1 free parameter). Setting one coordinate as a parameter $t$ produces the parametric equations of the line directly.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Direction Vector via Cross Product (Method 1)
Extract the normal vectors from the equations of $\Pi_1$ and $\Pi_2$:
$$n_1 = (1, 1, 1), \qquad n_2 = (1, -1, 1).$$
Compute their cross product $v_1 = n_1 \times n_2$:
$$v_1 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 1 \\ 1 & -1 & 1 \end{vmatrix}.$$
Expand along the first row:
$$v_1 = \mathbf{i} \begin{vmatrix} 1 & 1 \\ -1 & 1 \end{vmatrix} - \mathbf{j} \begin{vmatrix} 1 & 1 \\ 1 & 1 \end{vmatrix} + \mathbf{k} \begin{vmatrix} 1 & 1 \\ 1 & -1 \end{vmatrix}.$$
Evaluate the $2 \times 2$ determinants:
- $\mathbf{i}$-term: $(1)(1) - (1)(-1) = 1 - (-1) = 2$
- $\mathbf{j}$-term: $-\big((1)(1) - (1)(1)\big) = -(1 - 1) = 0$
- $\mathbf{k}$-term: $(1)(-1) - (1)(1) = -1 - 1 = -2$

Thus, the cross product yields:
$$v_1 = (2, 0, -2).$$
Dividing by the scalar 2 gives the simplified direction vector:
$$v = (1, 0, -1).$$

### Step 2: Direction Vector from the System of Equations (Method 2)
Consider the linear system:
$$\begin{cases}
x + y + z = 3 & \text{(Equation 1)} \\
x - y + z = 1 & \text{(Equation 2)}
\end{cases}$$

1. Add Equation 1 and Equation 2 to eliminate $y$:
   $$(x + y + z) + (x - y + z) = 3 + 1 \implies 2x + 2z = 4 \implies x + z = 2.$$
   Express $x$ in terms of $z$:
   $$x = 2 - z.$$
2. Subtract Equation 2 from Equation 1 to eliminate $x$ and $z$:
   $$(x + y + z) - (x - y + z) = 3 - 1 \implies 2y = 2 \implies y = 1.$$
3. Choose $z = t$ as the free parameter ($t \in \mathbb{R}$). Then:
   $$\begin{cases}
   x = 2 - t \\
   y = 1 \\
   z = t
   \end{cases}$$
In vector form:
$$(x, y, z) = (2 - t, \; 1, \; t) = (2, 1, 0) + t(-1, 0, 1).$$
From this algebraic solution, the direction vector is:
$$v_2 = (-1, 0, 1).$$

### Step 3: Compare the Results
Comparing the direction vectors obtained from both methods:
$$v_1 = (2, 0, -2), \qquad v_2 = (-1, 0, 1).$$
Notice that:
$$v_1 = -2\,v_2.$$
The two direction vectors are scalar multiples of each other. They point along the exact same line in 3D space, with opposite orientations and a scale factor of 2. Both are completely valid representations of the line's direction.

### Step 4: Write the Final Parametric Equation
Using the base point $P_0 = (2, 1, 0)$ (found at $t = 0$) and direction vector $(1, 0, -1)$ or $(-1, 0, 1)$:
$$L : (x, y, z) = (2, 1, 0) + t(1, 0, -1), \quad t \in \mathbb{R}.$$

---

## 5. Why Each Step Is Valid
1. **The cross product method** is valid because the line of intersection is contained in both planes, requiring its direction to be perpendicular to both normal vectors simultaneously.
2. **Elimination by addition and subtraction** preserves the solution space of the linear system via elementary row operations.
3. **Assigning a free parameter** correctly parameterizes the 1-dimensional null-space kernel of the $2 \times 3$ system.

---

## 6. Final Answer in Words
The cross product of the normal vectors $(1, 1, 1) \times (1, -1, 1)$ gives the direction vector $v_1 = (2, 0, -2)$, which simplifies to $(1, 0, -1)$. Solving the system by elimination fixes $y = 1$ and $x = 2 - z$, yielding the direction vector $v_2 = (-1, 0, 1)$ when setting $z$ as the parameter. Comparing them shows that $v_1 = -2v_2$, proving they are collinear. A parametric equation of the line of intersection is $(x, y, z) = (2, 1, 0) + t(1, 0, -1)$ for $t \in \mathbb{R}$.

---

## 7. Quick Verification
- **Test base point $(2, 1, 0)$ in both planes:**
  - $\Pi_1$: $2 + 1 + 0 = 3$. (Satisfied)
  - $\Pi_2$: $2 - 1 + 0 = 1$. (Satisfied)
- **Test another point on the line (set $t = 1 \implies (3, 1, -1)$):**
  - $\Pi_1$: $3 + 1 + (-1) = 3$. (Satisfied)
  - $\Pi_2$: $3 - 1 + (-1) = 1$. (Satisfied)
- **Check orthogonality of direction vector with normal vectors:**
  $$(1, 0, -1) \cdot (1, 1, 1) = 1(1) + 0(1) + (-1)(1) = 1 - 1 = 0,$$
  $$(1, 0, -1) \cdot (1, -1, 1) = 1(1) + 0(-1) + (-1)(1) = 1 - 1 = 0.$$
  The line lies in both planes simultaneously.

---

## 8. Common Mistakes to Avoid
- **Thinking the two direction vectors must be identical:** Believing $(2, 0, -2)$ and $(-1, 0, 1)$ disagree, forgetting that any non-zero scalar multiple $k\,v$ is a valid direction vector for the same line.
- **Arithmetic sign in cross product:** In the $\mathbf{k}$-component, calculating $1(-1) - 1(1) = 0$ instead of $-2$.
- **Forgetting to find a base point:** Giving only the direction vector without finding an explicit point $(x_0, y_0, z_0)$ on the line.

---

## 9. Classroom Presentation (3-Sentence Summary)
Taking the cross product of the normal vectors $(1, 1, 1)$ and $(1, -1, 1)$ gives the direction vector $(2, 0, -2)$, which simplifies to $(1, 0, -1)$. Solving the linear system algebraically yields $y = 1$ and $x = 2 - z$, which parameterizes the direction as $(-1, 0, 1)$—the exact opposite scalar multiple of our cross product result. Combining the base point $(2, 1, 0)$ with this direction gives the parametric line $(x, y, z) = (2, 1, 0) + t(1, 0, -1)$, which satisfies both plane equations for all real $t$.

