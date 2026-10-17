# Problem 9 Solution: Distances to a Line and a Plane

## 1. Original Problem
Compute:
1. The Euclidean distance from the point $P = (2, 3)$ to the line in $\mathbb{R}^2$:
   $$3x + 4y - 10 = 0.$$
2. The Euclidean distance from the point $Q = (2, -1, 3)$ to the plane in $\mathbb{R}^3$:
   $$2x - 2y + z - 4 = 0.$$

Compare the two formulas and explain their fundamental geometric connection with the normal direction.

---

## 2. What We Are Trying to Find
We need to:
1. Compute the distance from a 2D point to a line using the Cartesian distance formula.
2. Compute the distance from a 3D point to a plane using the Cartesian distance formula.
3. Compare the structural algebraic form of both distance expressions.
4. Explain how both formulas are unified by the concept of orthogonal projection onto the unit normal vector.

---

## 3. Key Concepts and Theorems
1. **Distance from a Point to a Line in $\mathbb{R}^2$:**
   For a point $(x_0, y_0)$ and a line $Ax + By + C = 0$:
   $$d = \frac{|A x_0 + B y_0 + C|}{\sqrt{A^2 + B^2}} = \frac{|n \cdot P + C|}{\|n\|},$$
   where $n = (A, B)$ is the normal vector to the line.
2. **Distance from a Point to a Plane in $\mathbb{R}^3$:**
   For a point $(x_0, y_0, z_0)$ and a plane $Ax + By + Cz + D = 0$:
   $$d = \frac{|A x_0 + B y_0 + C z_0 + D|}{\sqrt{A^2 + B^2 + C^2}} = \frac{|n \cdot Q + D|}{\|n\|},$$
   where $n = (A, B, C)$ is the normal vector to the plane.
3. **Unified Geometric Principle (Hyperplane Distance):**
   In any dimension $\mathbb{R}^n$, an affine subspace of codimension 1 (a line in $\mathbb{R}^2$, a plane in $\mathbb{R}^3$, or a hyperplane in $\mathbb{R}^n$) is defined by $n \cdot X + D = 0$. The shortest distance from any point $P$ to this set is measured along the unique direction perpendicular to it, given by the scalar projection onto the unit normal vector:
   $$d = \left|\operatorname{comp}_n (P - X_0)\right| = \frac{|n \cdot (P - X_0)|}{\|n\|} = \frac{|n \cdot P + D|}{\|n\|}.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute Distance from $P(2, 3)$ to the Line $3x + 4y - 10 = 0$
Identify the parameters:
$$x_0 = 2, \quad y_0 = 3, \quad A = 3, \quad B = 4, \quad C = -10.$$
1. Evaluate the numerator (substitute point into the equation):
   $$|A x_0 + B y_0 + C| = |3(2) + 4(3) - 10| = |6 + 12 - 10| = |8| = 8.$$
2. Evaluate the denominator (length of normal vector $n = (3, 4)$):
   $$\|n\| = \sqrt{A^2 + B^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5.$$
3. Compute the distance:
   $$d(P, \text{Line}) = \frac{8}{5} = 1.6.$$

### Step 2: Compute Distance from $Q(2, -1, 3)$ to the Plane $2x - 2y + z - 4 = 0$
Identify the parameters:
$$x_0 = 2, \quad y_0 = -1, \quad z_0 = 3, \quad A = 2, \quad B = -2, \quad C = 1, \quad D = -4.$$
1. Evaluate the numerator (substitute point into the equation):
   $$|A x_0 + B y_0 + C z_0 + D| = |2(2) - 2(-1) + 1(3) - 4| = |4 + 2 + 3 - 4| = |5| = 5.$$
2. Evaluate the denominator (length of normal vector $n = (2, -2, 1)$):
   $$\|n\| = \sqrt{A^2 + B^2 + C^2} = \sqrt{2^2 + (-2)^2 + 1^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3.$$
3. Compute the distance:
   $$d(Q, \text{Plane}) = \frac{5}{3} \approx 1.667.$$

### Step 3: Compare Formulas and Explain Connection to Normal Direction
- **Structural Similarity:**
  Both formulas have the identical structure:
  $$d = \frac{|\text{Equation evaluated at the point}|}{\|\text{Normal vector}\|}.$$
- **Geometric Role of the Normal Vector:**
  1. The shortest distance from any point to a flat surface (a line in $\mathbb{R}^2$ or a plane in $\mathbb{R}^3$) is measured along a line that is strictly perpendicular to the surface.
  2. The direction of this shortest path is precisely the direction of the normal vector $n$.
  3. If we pick any base point $X_0$ on the line or plane (so that $n \cdot X_0 + D = 0$), the displacement vector from $X_0$ to the test point $P$ is $P - X_0$.
  4. The perpendicular distance is the scalar projection of $P - X_0$ onto the unit normal vector $e_n = \frac{n}{\|n\|}$:
     $$d = \left|(P - X_0) \cdot \frac{n}{\|n\|}\right| = \frac{|n \cdot P - n \cdot X_0|}{\|n\|} = \frac{|n \cdot P + D|}{\|n\|}.$$
  5. The numerator measures the algebraic "gap" or offset from the level set zero, and dividing by the magnitude $\|n\|$ normalizes away the arbitrary scaling of the coefficients, yielding the true physical Euclidean distance.

---

## 5. Why Each Step Is Valid
1. **The numerator evaluation** measures the value of the affine linear functional at the target point.
2. **Dividing by the Euclidean norm** converts the linear functional into an orthonormal coordinate measurement along the normal axis.
3. **The absolute value** ensures that physical distance is non-negative, independent of which side of the hyperplane the point lies on.

---

## 6. Final Answer in Words
The distance from point $P(2, 3)$ to the line $3x + 4y - 10 = 0$ is $\frac{8}{5} = 1.6$. The distance from point $Q(2, -1, 3)$ to the plane $2x - 2y + z - 4 = 0$ is $\frac{5}{3} \approx 1.67$. Both formulas share the exact same mathematical form: the absolute value of the Cartesian equation evaluated at the given point divided by the Euclidean norm of the normal vector. This common structure arises because the shortest path to any hyperplane is always parallel to its normal vector.

---

## 7. Quick Verification
- **Parametric normal line check for line distance:**
  Line from $P(2, 3)$ in direction $n(3, 4)$: $(x, y) = (2 + 3t, 3 + 4t)$.
  Substitute into $3x + 4y - 10 = 0$:
  $$3(2 + 3t) + 4(3 + 4t) - 10 = 0 \implies 6 + 9t + 12 + 16t - 10 = 0 \implies 25t + 8 = 0 \implies t = -\frac{8}{25}.$$
  Distance: $\|t\,n\| = |t| \|n\| = \frac{8}{25} \times 5 = \frac{8}{5} = 1.6$.
- **Parametric normal line check for plane distance:**
  Line from $Q(2, -1, 3)$ in direction $n(2, -2, 1)$: $(x, y, z) = (2 + 2t, -1 - 2t, 3 + t)$.
  Substitute into $2x - 2y + z - 4 = 0$:
  $$2(2 + 2t) - 2(-1 - 2t) + (3 + t) - 4 = 0 \implies 4 + 4t + 2 + 4t + 3 + t - 4 = 0 \implies 9t + 5 = 0 \implies t = -\frac{5}{9}.$$
  Distance: $\|t\,n\| = |t| \|n\| = \frac{5}{9} \times 3 = \frac{5}{3}$.
  Both results are verified via independent normal parameterizations.

---

## 8. Common Mistakes to Avoid
- **Omitting the absolute value:** If the point yields a negative value inside the equation, writing a negative distance.
- **Forgetting the constant term in the numerator:** Evaluating only $A x_0 + B y_0$ without including $C$ or $D$.
- **Dividing by the wrong norm:** Dividing by $\sqrt{x_0^2 + y_0^2}$ (the point's coordinates) instead of $\sqrt{A^2 + B^2}$ (the normal vector components).

---

## 9. Classroom Presentation (3-Sentence Summary)
Plugging the points into the line and plane equations gives numerators $|3(2)+4(3)-10| = 8$ and $|2(2)-2(-1)+3-4| = 5$. Dividing by the lengths of their respective normal vectors, which are $\sqrt{3^2+4^2} = 5$ and $\sqrt{2^2+(-2)^2+1^2} = 3$, yields distances of $8/5$ and $5/3$. Both formulas are identical in nature because the shortest path from a point to any hyperplane is directed along the normal vector, whose unit norm serves as the required scaling denominator.

