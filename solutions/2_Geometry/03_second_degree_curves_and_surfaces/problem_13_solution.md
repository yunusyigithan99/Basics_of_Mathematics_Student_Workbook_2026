# Problem 13 Solution: Intersection of a Sphere and a Plane

## 1. Original Problem
Given the sphere in $\mathbb{R}^3$:
$$S : x^2 + y^2 + z^2 = 25$$
and the horizontal plane $\Pi : z = 3$:
1. Find the equation of the intersection curve and compute its radius.
2. Analyze and describe what happens to the intersection curve for a general plane $z = c$, categorizing the geometric outcome depending on the value of the parameter $c \in \mathbb{R}$.

---

## 2. What We Are Trying to Find
We need to:
1. Substitute $z = 3$ into the sphere equation to determine the exact 2D algebraic equation of the curve in the plane $z = 3$.
2. Calculate the radius $r$ of this intersection circle.
3. Solve the general case $x^2 + y^2 = 25 - c^2$ for any real height $c$.
4. Establish the three distinct geometric regimes based on the sign of $25 - c^2$: a real circle, a single point of tangency, or no intersection (empty set).

---

## 3. Key Concepts and Theorems
1. **Intersection of a Sphere with a Plane:**
   The intersection of a sphere of radius $R$ and a plane at distance $d$ from the center of the sphere is:
   - A **circle** of radius $r = \sqrt{R^2 - d^2}$ if $d < R$.
   - A **single point** (point of tangency) if $d = R$.
   - **Empty** ($\emptyset$) if $d > R$.
2. **Sphere of Radius $R$ Centered at the Origin:**
   $$x^2 + y^2 + z^2 = R^2.$$
   Here $R^2 = 25 \implies R = 5$, and the center is $O = (0, 0, 0)$.
3. **Distance from Center to the Plane $z = c$:**
   Since the plane $z = c$ is horizontal and the center of the sphere is at $(0, 0, 0)$, the perpendicular distance from the center to the plane is simply:
   $$d = |c|.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Find the Intersection with $z = 3$
Substitute $z = 3$ directly into the sphere equation $x^2 + y^2 + z^2 = 25$:
$$x^2 + y^2 + 3^2 = 25$$
$$x^2 + y^2 + 9 = 25.$$
Subtract $9$ from both sides:
$$x^2 + y^2 = 25 - 9 = 16.$$
In the cutting plane $z = 3$, the coordinates $x$ and $y$ satisfy:
$$x^2 + y^2 = 4^2.$$
- **Equation of the curve:** The intersection is a 3D circle given by the simultaneous system:
  $$\begin{cases} x^2 + y^2 = 16 \\ z = 3 \end{cases}$$
- **Radius of the intersection circle:**
  $$r = \sqrt{16} = 4.$$
- **Center of the circle:** The point $(0, 0, 3)$ on the $z$-axis.

### Step 2: Geometric Interpretation via the Pythagorean Theorem
Consider the right triangle formed by:
1. The sphere center $O(0, 0, 0)$,
2. The center of the slice $C(0, 0, 3)$,
3. Any point $P(x, y, 3)$ on the intersection circle.
- The hypotenuse is the radius of the sphere: $OP = R = 5$.
- The vertical leg is the distance along the $z$-axis: $OC = d = 3$.
- The horizontal leg is the radius of the slice: $CP = r$.
By the Pythagorean theorem:
$$r^2 + d^2 = R^2 \implies r = \sqrt{R^2 - d^2} = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = \sqrt{16} = 4.$$
This confirms the algebraic result through purely Euclidean geometry.

### Step 3: Complete Classification for $z = c$
Substitute the general plane equation $z = c$ into the sphere equation:
$$x^2 + y^2 + c^2 = 25 \implies x^2 + y^2 = 25 - c^2.$$
The geometric nature of the solution set depends strictly on the value of $25 - c^2$:

1. **Case 1: $|c| < 5$ (i.e., $-5 < c < 5$):**
   Here $c^2 < 25$, so $25 - c^2 > 0$.
   The intersection is a **circle** lying in the plane $z = c$, centered at $(0, 0, c)$ with radius:
   $$r(c) = \sqrt{25 - c^2}.$$
   - At $c = 0$ (equatorial plane), the circle is largest with maximum radius $r(0) = \sqrt{25} = 5$ (a great circle).
   - As $|c|$ increases toward $5$, the radius $r(c)$ strictly decreases toward $0$.

2. **Case 2: $|c| = 5$ (i.e., $c = 5$ or $c = -5$):**
   Here $c^2 = 25$, so $25 - c^2 = 0$.
   The equation becomes:
   $$x^2 + y^2 = 0 \implies x = 0, \; y = 0.$$
   The intersection is a **single point**:
   - For $c = 5$: the North Pole $N(0, 0, 5)$.
   - For $c = -5$: the South Pole $S(0, 0, -5)$.
   The horizontal plane is **tangent** to the sphere at these points.

3. **Case 3: $|c| > 5$ (i.e., $c > 5$ or $c < -5$):**
   Here $c^2 > 25$, so $25 - c^2 < 0$.
   The sum of squares of real numbers cannot be negative:
   $$x^2 + y^2 \ge 0 > 25 - c^2.$$
   There are no real solutions $(x, y) \in \mathbb{R}^2$.
   The intersection is **empty** ($\emptyset$); the plane lies entirely outside the sphere and does not meet it.

---

## 5. Why Each Step Is Valid
1. **Substituting $z = 3$** enforces the geometric condition that the point must belong to both the sphere and the plane simultaneously.
2. **The Pythagorean identity $r^2 = R^2 - d^2$** is valid because the normal vector to the cutting plane $(0, 0, 1)$ is perpendicular to the cutting plane itself.
3. **The tripartite sign analysis** of $25 - c^2$ rigorously partitions the real number line into all possible topological configurations.

---

## 6. Final Answer in Words
The intersection of the sphere $x^2 + y^2 + z^2 = 25$ with the plane $z = 3$ is a circle described by $x^2 + y^2 = 16$ lying in the plane $z = 3$, with center $(0, 0, 3)$ and radius $r = 4$. For a general horizontal plane $z = c$:
- If $|c| < 5$, the intersection is a circle of radius $r = \sqrt{25 - c^2}$ centered at $(0, 0, c)$.
- If $|c| = 5$, the plane is tangent to the sphere, intersecting at the single point $(0, 0, 5)$ or $(0, 0, -5)$.
- If $|c| > 5$, the intersection is empty (no real points), because the plane lies outside the sphere.

---

## 7. Quick Verification
- Point $(4, 0, 3)$: $4^2 + 0^2 + 3^2 = 16 + 0 + 9 = 25$. Point lies on both the circle and the sphere.
- Point $(0, 4, 3)$: $0^2 + 4^2 + 3^2 = 16 + 9 = 25$. Point lies on both.
- Point $(2\sqrt{2}, 2\sqrt{2}, 3)$: $(2\sqrt{2})^2 + (2\sqrt{2})^2 + 3^2 = 8 + 8 + 9 = 25$. Point lies on both.
- Great circle at $c = 0$: $r = \sqrt{25 - 0} = 5 = R$. Correct.
- Pole at $c = 5$: $0^2 + 0^2 + 5^2 = 25$. Correct.

---

## 8. Common Mistakes to Avoid
- **Omitting the plane specification:** Stating that the intersection is just $x^2 + y^2 = 16$, which in 3D space defines an infinite circular cylinder rather than a 1D circle in space. The specification $z = 3$ must be included.
- **Forgetting the square root:** Stating that the radius is 16 instead of $\sqrt{16} = 4$.
- **Ignoring negative values of $c$:** Formulating the conditions only for $c > 0$ and missing the lower hemisphere for $c < 0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Plugging the plane $z = 3$ into the sphere equation $x^2 + y^2 + z^2 = 25$ gives $x^2 + y^2 = 25 - 9 = 16$, which defines a circle of radius 4 in the plane $z = 3$. This result matches the Pythagorean theorem on the cross-sectional triangle with hypotenuse 5 and vertical leg 3, yielding horizontal radius $\sqrt{5^2 - 3^2} = 4$. For an arbitrary plane $z = c$, the intersection is a circle of radius $\sqrt{25 - c^2}$ whenever $|c| < 5$, shrinks to a single tangent pole when $|c| = 5$, and is empty when $|c| > 5$.
