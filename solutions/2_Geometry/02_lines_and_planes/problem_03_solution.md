# Problem 3 Solution: Plane Through a Point with a Given Normal Vector

## 1. Original Problem
Find the Cartesian equation of the plane passing through the point
$$P = (1, -2, 3)$$
and perpendicular to the normal vector
$$n = (2, 1, -1).$$
Check the result by substituting the coordinates of point $P$, and explain the geometric role of the normal vector in defining a plane in $\mathbb{R}^3$.

---

## 2. What We Are Trying to Find
We need to:
1. Apply the point-normal equation of a plane in $\mathbb{R}^3$.
2. Expand and simplify the expression into the standard general form $Ax + By + Cz + D = 0$.
3. Substitute the coordinates of $P$ into the resulting equation to verify algebraic correctness.
4. Explain why a single normal vector is sufficient to define the entire 2D orientation of a plane in 3D space.

---

## 3. Key Concepts and Theorems
1. **Geometric Definition of a Plane via a Normal Vector:**
   A plane $\Pi$ in $\mathbb{R}^3$ through point $P$ with normal vector $n \neq \mathbf{0}$ is the set of all points $X = (x, y, z)$ such that the displacement vector $\overrightarrow{PX} = X - P$ is orthogonal to $n$:
   $$X \in \Pi \iff n \cdot (X - P) = 0.$$
2. **Point-Normal Cartesian Equation:**
   Letting $n = (A, B, C)$ and $P = (x_0, y_0, z_0)$:
   $$A(x - x_0) + B(y - y_0) + C(z - z_0) = 0.$$
3. **General Linear Equation of a Plane:**
   Expanding gives:
   $$Ax + By + Cz + D = 0, \quad \text{where } D = -(A x_0 + B y_0 + C z_0).$$
   The coefficients of $x, y, z$ in the general equation are precisely the components of the normal vector $n = (A, B, C)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Point-Normal Equation
Given point $P = (1, -2, 3)$ and normal vector $n = (2, 1, -1)$, write the dot product equation:
$$n \cdot (X - P) = 0 \implies 2(x - 1) + 1\big(y - (-2)\big) + (-1)(z - 3) = 0.$$

### Step 2: Expand and Simplify
Carefully expand each product:
$$2(x - 1) + 1(y + 2) - 1(z - 3) = 0$$
$$2x - 2 + y + 2 - z + 3 = 0.$$
Combine the constant terms:
$$(-2) + 2 + 3 = 3.$$
Thus, the equation of the plane in general form is:
$$2x + y - z + 3 = 0 \quad (\text{or } 2x + y - z = -3).$$

### Step 3: Check by Substituting Point $P$
Substitute $x = 1, y = -2, z = 3$ into the left-hand side of the derived equation:
$$\text{LHS} = 2(1) + (-2) - (3) + 3 = 2 - 2 - 3 + 3 = 0.$$
Since $\text{LHS} = 0 = \text{RHS}$, point $P$ satisfies the equation.

### Step 4: The Geometric Role of the Normal Vector
- In three dimensions, a plane is a two-dimensional flat surface with infinitely many directions lying within it.
- Describing a plane using direction vectors requires choosing two non-parallel vectors spanning it, which can be done in infinitely many different ways.
- However, there is only **one unique direction** in 3D space that is perpendicular to the entire plane (up to scalar multiplication): the normal line.
- Specifying the normal vector $n$ completely locks down the tilt, attitude, and spatial orientation of the plane in space.
- Adding the base point $P$ fixes the plane's exact physical position, anchoring it in $\mathbb{R}^3$.
- Thus, the pair $(P, n)$ provides the most concise, robust, and geometrically intuitive specification of a plane.

---

## 5. Why Each Step Is Valid
1. **The dot product formula $n \cdot (X - P) = 0$** directly encapsulates the geometric definition of perpendicularity between the normal and every vector lying inside the plane.
2. **Distributing coefficients** is valid by the distributive property of multiplication over addition in real numbers.
3. **Plugging $P$ into the equation** verifies that the constant term $D = 3$ was calculated correctly.

---

## 6. Final Answer in Words
The equation of the plane is $2x + y - z + 3 = 0$ (or $2x + y - z = -3$). Substituting $P(1, -2, 3)$ yields $2(1) + (-2) - 3 + 3 = 0$, confirming that $P$ lies on the plane. The normal vector $n = (2, 1, -1)$ fixes the orientation of the plane because any displacement vector within the plane must be perpendicular to $n$, while point $P$ anchors its position in space.

---

## 7. Quick Verification
- **Alternative calculation for constant $D$:**
  $$D = - n \cdot P = - \big(2(1) + 1(-2) + (-1)(3)\big) = - (2 - 2 - 3) = -(-3) = +3.$$
  This directly yields $2x + y - z + 3 = 0$.
- **Pick another point in the plane:**
  Let $x = 0, y = 0 \implies -z + 3 = 0 \implies z = 3$, so point $Q(0, 0, 3)$ is on the plane.
  Construct $\overrightarrow{PQ} = Q - P = (0 - 1, 0 - (-2), 3 - 3) = (-1, 2, 0)$.
  Check $n \cdot \overrightarrow{PQ} = 2(-1) + 1(2) + (-1)(0) = -2 + 2 + 0 = 0$.
  The vector $\overrightarrow{PQ}$ is indeed orthogonal to $n$.

---

## 8. Common Mistakes to Avoid
- **Sign error with negative coordinates:** Writing $y - 2$ instead of $y - (-2) = y + 2$.
- **Dropping the constant term:** Writing $2x + y - z = 0$, which defines a parallel plane passing through the origin $(0, 0, 0)$ instead of through $P$.
- **Flipping the normal vector coefficients:** Swapping coordinates of $n$ with coordinates of $P$.

---

## 9. Classroom Presentation (3-Sentence Summary)
We use the point-normal form $A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$ with normal vector $(2, 1, -1)$ and point $(1, -2, 3)$ to obtain $2(x - 1) + 1(y + 2) - 1(z - 3) = 0$. Expanding and simplifying the constant terms yields the general plane equation $2x + y - z + 3 = 0$, which point $P$ satisfies identically. The normal vector is essential because its perpendicular direction completely determines the spatial tilt of the plane, while point $P$ fixes its exact location in space.

