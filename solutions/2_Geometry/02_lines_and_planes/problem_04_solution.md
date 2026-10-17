# Problem 4 Solution: Plane Through Three Points

## 1. Original Problem
Find the equation of the plane passing through the three points
$$A = (1, 0, 0), \qquad B = (0, 1, 0), \qquad C = (0, 0, 1).$$
First construct two vectors lying in the plane, and then use their cross product to find a normal vector. Finally, check that the resulting equation is satisfied by all three points.

---

## 2. What We Are Trying to Find
We need to:
1. Construct two in-plane displacement vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
2. Compute the normal vector $n = \overrightarrow{AB} \times \overrightarrow{AC}$ using the vector cross product.
3. Formulate the general Cartesian equation of the plane $Ax + By + Cz + D = 0$.
4. Check that all three vertices $A$, $B$, and $C$ satisfy the plane equation.

---

## 3. Key Concepts and Theorems
1. **Three Non-Collinear Points Determine a Unique Plane:**
   Any three points $A, B, C$ not lying on a single straight line uniquely specify a flat two-dimensional plane in $\mathbb{R}^3$.
2. **In-Plane Displacement Vectors:**
   Vectors formed by subtracting coordinates of points on the plane lie entirely in the plane:
   $$\overrightarrow{AB} = B - A, \qquad \overrightarrow{AC} = C - A.$$
3. **Normal Vector via Cross Product:**
   The cross product of two non-collinear vectors in the plane yields a normal vector $n$ orthogonal to both, and hence orthogonal to the entire plane:
   $$n = \overrightarrow{AB} \times \overrightarrow{AC}.$$
4. **Intercept Form of a Plane:**
   When a plane intercepts the coordinate axes at $(a, 0, 0)$, $(0, b, 0)$, and $(0, 0, c)$, its equation can also be written in intercept form:
   $$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Construct Two Vectors Lying in the Plane
Using point $A(1, 0, 0)$ as the initial vertex:
$$\overrightarrow{AB} = B - A = (0 - 1, \; 1 - 0, \; 0 - 0) = (-1, 1, 0),$$
$$\overrightarrow{AC} = C - A = (0 - 1, \; 0 - 0, \; 1 - 0) = (-1, 0, 1).$$
Both vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ lie within the plane.

### Step 2: Compute the Normal Vector via Cross Product
Evaluate $n = \overrightarrow{AB} \times \overrightarrow{AC}$:
$$n = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{vmatrix}.$$
Expand along the first row:
$$n = \mathbf{i} \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} - \mathbf{j} \begin{vmatrix} -1 & 0 \\ -1 & 1 \end{vmatrix} + \mathbf{k} \begin{vmatrix} -1 & 1 \\ -1 & 0 \end{vmatrix}.$$
Calculate the $2 \times 2$ determinants:
- $\mathbf{i}$-term: $(1)(1) - (0)(0) = 1$
- $\mathbf{j}$-term: $-\big((-1)(1) - (0)(-1)\big) = -(-1 - 0) = -(-1) = 1$
- $\mathbf{k}$-term: $(-1)(0) - (1)(-1) = 0 - (-1) = 1$

Thus, the normal vector is:
$$n = (1, 1, 1).$$

### Step 3: Formulate the Equation of the Plane
Using normal vector $n = (1, 1, 1)$ and base point $A(1, 0, 0)$:
$$1(x - 1) + 1(y - 0) + 1(z - 0) = 0 \implies (x - 1) + y + z = 0.$$
Rearranging into standard form:
$$x + y + z - 1 = 0 \quad (\text{or } x + y + z = 1).$$

### Step 4: Check All Three Points in the Equation
1. **Point $A(1, 0, 0)$:**
   $$x + y + z = 1 + 0 + 0 = 1. \quad \text{(Satisfied)}$$
2. **Point $B(0, 1, 0)$:**
   $$x + y + z = 0 + 1 + 0 = 1. \quad \text{(Satisfied)}$$
3. **Point $C(0, 0, 1)$:**
   $$x + y + z = 0 + 0 + 1 = 1. \quad \text{(Satisfied)}$$
All three points satisfy the equation.

---

## 5. Why Each Step Is Valid
1. **Constructing difference vectors** captures the two spatial degrees of freedom within the plane.
2. **The cross product** guarantees that $n$ is perpendicular to both $\overrightarrow{AB}$ and $\overrightarrow{AC}$ simultaneously, which defines the unique normal line to the plane.
3. **Direct point evaluation** verifies that the constant term $D = -1$ correctly positions the plane on all three given vertices.

---

## 6. Final Answer in Words
Two vectors lying in the plane are $\overrightarrow{AB} = (-1, 1, 0)$ and $\overrightarrow{AC} = (-1, 0, 1)$. Their cross product yields the normal vector $n = (1, 1, 1)$. The Cartesian equation of the plane is $x + y + z = 1$ (or $x + y + z - 1 = 0$). Substituting $A(1, 0, 0)$, $B(0, 1, 0)$, and $C(0, 0, 1)$ yields $1 = 1$ in every case, confirming that all three points lie on the plane.

---

## 7. Quick Verification
- **Intercept Form:**
  The points $A, B, C$ are the unit intercepts along the three coordinate axes ($a = 1, b = 1, c = 1$).
  Using the intercept formula:
  $$\frac{x}{1} + \frac{y}{1} + \frac{z}{1} = 1 \implies x + y + z = 1.$$
  This matches the cross-product derivation instantly.
- **Normal vector check:**
  $$n \cdot \overrightarrow{AB} = 1(-1) + 1(1) + 1(0) = -1 + 1 + 0 = 0,$$
  $$n \cdot \overrightarrow{AC} = 1(-1) + 1(0) + 1(1) = -1 + 0 + 1 = 0.$$
  Perpendicularity is confirmed.

---

## 8. Common Mistakes to Avoid
- **Sign slips in cross product minors:** In the $\mathbf{j}$-minor, forgetting that $(-1)(1) = -1$, and with the outer negative sign, $-(-1) = +1$.
- **Incomplete verification:** Checking only point $A$ and failing to check points $B$ and $C$.
- **Subtracting in mixed orders:** Using $B - A$ and then $A - C$, which changes orientation (though for a plane, any normal vector $\pm n$ yields the equivalent equation).

---

## 9. Classroom Presentation (3-Sentence Summary)
We construct two displacement vectors in the plane, $\overrightarrow{AB} = (-1, 1, 0)$ and $\overrightarrow{AC} = (-1, 0, 1)$, and compute their cross product to find the normal vector $n = (1, 1, 1)$. Using point $A(1, 0, 0)$ with this normal vector produces the elegant Cartesian equation $x + y + z = 1$. We verify this equation by substituting all three vertices $A$, $B$, and $C$, each of which satisfies the equation $x + y + z = 1$ with sum equal to 1.

