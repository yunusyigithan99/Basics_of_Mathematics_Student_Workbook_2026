# Problem 13 Solution: Closest Point on a Plane

## 1. Original Problem
Find the point $Q$ on the plane
$$\Pi : x + 2y + 2z = 4$$
that is closest to the point
$$P = (3, 0, 0).$$
Compute the minimum distance between $P$ and the plane, and check that the line segment joining $P$ and $Q$ is perpendicular to the plane.

---

## 2. What We Are Trying to Find
We need to:
1. Construct the normal line dropped from $P(3, 0, 0)$ perpendicular to the plane.
2. Intersect the normal line with the plane equation to find the closest point $Q$.
3. Compute the minimum Euclidean distance $d(P, \Pi)$ using both the vector norm $\|P - Q\|$ and the standard point-to-plane distance formula.
4. Verify that the displacement vector $\overrightarrow{PQ}$ is parallel to the normal vector $n$, confirming perpendicularity.

---

## 3. Key Concepts and Theorems
1. **Geometric Principle of Minimum Distance:**
   The point $Q$ on a plane $\Pi$ closest to an external point $P$ is the orthogonal projection of $P$ onto $\Pi$. The vector $\overrightarrow{PQ}$ must be parallel to the normal vector $n$ of the plane.
2. **Normal Line Parametric Equation:**
   Passing through $P$ with direction $n = (A, B, C)$:
   $$\mathbf{r}(t) = P + t\,n.$$
3. **Point-to-Plane Distance Formula:**
   For plane $Ax + By + Cz + D = 0$ and point $(x_0, y_0, z_0)$:
   $$d = \frac{|A x_0 + B y_0 + C z_0 + D|}{\sqrt{A^2 + B^2 + C^2}}.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Normal Vector and Set Up the Normal Line
From the plane equation $x + 2y + 2z - 4 = 0$, the normal vector is:
$$n = (1, 2, 2).$$
The line passing through $P(3, 0, 0)$ parallel to $n$ is:
$$\begin{cases}
x(t) = 3 + t \\
y(t) = 0 + 2t = 2t \\
z(t) = 0 + 2t = 2t
\end{cases}$$

### Step 2: Find the Intersection Parameter $t$
Substitute the parametric coordinates into the plane equation $x + 2y + 2z = 4$:
$$(3 + t) + 2(2t) + 2(2t) = 4.$$
Expand and collect like terms:
$$3 + t + 4t + 4t = 4$$
$$3 + 9t = 4.$$
Subtract 3 from both sides:
$$9t = 1 \implies t = \frac{1}{9}.$$

### Step 3: Compute the Coordinates of the Closest Point $Q$
Substitute $t = \frac{1}{9}$ into the parametric equations:
$$x = 3 + \frac{1}{9} = \frac{27 + 1}{9} = \frac{28}{9},$$
$$y = 2\left(\frac{1}{9}\right) = \frac{2}{9},$$
$$z = 2\left(\frac{1}{9}\right) = \frac{2}{9}.$$
Thus, the closest point on the plane is:
$$Q = \left(\frac{28}{9}, \; \frac{2}{9}, \; \frac{2}{9}\right) \approx (3.111, \; 0.222, \; 0.222).$$

### Step 4: Verify That $Q$ Lies on the Plane
Substitute the coordinates of $Q$ into $x + 2y + 2z$:
$$\text{LHS} = \frac{28}{9} + 2\left(\frac{2}{9}\right) + 2\left(\frac{2}{9}\right) = \frac{28 + 4 + 4}{9} = \frac{36}{9} = 4 = \text{RHS}.$$
The point $Q$ satisfies the plane equation.

### Step 5: Compute the Distance
- **Using the displacement vector $\overrightarrow{PQ}$:**
  $$\overrightarrow{PQ} = Q - P = \left(\frac{28}{9} - 3, \; \frac{2}{9} - 0, \; \frac{2}{9} - 0\right) = \left(\frac{1}{9}, \; \frac{2}{9}, \; \frac{2}{9}\right) = \frac{1}{9}(1, 2, 2) = \frac{1}{9}n.$$
  The distance is the length of this vector:
  $$d = \|\overrightarrow{PQ}\| = \left\|\frac{1}{9} n\right\| = \frac{1}{9} \sqrt{1^2 + 2^2 + 2^2} = \frac{1}{9} \sqrt{1 + 4 + 4} = \frac{1}{9} \sqrt{9} = \frac{3}{9} = \frac{1}{3}.$$

- **Using the standard distance formula:**
  $$d = \frac{|1(3) + 2(0) + 2(0) - 4|}{\sqrt{1^2 + 2^2 + 2^2}} = \frac{|3 - 4|}{\sqrt{9}} = \frac{|-1|}{3} = \frac{1}{3}.$$
  Both calculations yield $d = \frac{1}{3}$.

### Step 6: Verify Perpendicularity of the Connecting Segment
The connecting displacement vector is:
$$\overrightarrow{PQ} = \left(\frac{1}{9}, \; \frac{2}{9}, \; \frac{2}{9}\right) = \frac{1}{9}(1, 2, 2) = \frac{1}{9}n.$$
Because $\overrightarrow{PQ}$ is an exact scalar multiple of the normal vector $n = (1, 2, 2)$, the segment $PQ$ is oriented strictly in the normal direction. Hence, the segment joining $P$ and $Q$ is perpendicular to the plane.

---

## 5. Why Each Step Is Valid
1. **The normal line parameterization** ensures that the connecting segment is orthogonal to every vector lying in the plane.
2. **Solving the linear equation in $t$** finds the unique intersection point of this orthogonal line with the plane.
3. **The norm calculation** measures the physical Euclidean distance between the given point and its orthogonal projection.

---

## 6. Final Answer in Words
The point on the plane $x + 2y + 2z = 4$ closest to $P(3, 0, 0)$ is $Q = \left(\frac{28}{9}, \frac{2}{9}, \frac{2}{9}\right)$. The minimum distance between $P$ and the plane is $\frac{1}{3}$. The connecting vector is $\overrightarrow{PQ} = \frac{1}{9}(1, 2, 2)$, which is a positive scalar multiple of the plane's normal vector $n = (1, 2, 2)$, confirming that the segment is strictly perpendicular to the plane.

---

## 7. Quick Verification
- **Orthogonality with in-plane vectors:**
  Pick two points on the plane:
  $A(4, 0, 0)$ and $B(0, 2, 0)$.
  In-plane vector: $\overrightarrow{AB} = (-4, 2, 0)$.
  Dot product with $\overrightarrow{PQ} = \frac{1}{9}(1, 2, 2)$:
  $$\overrightarrow{PQ} \cdot \overrightarrow{AB} = \frac{1}{9}\big(1(-4) + 2(2) + 2(0)\big) = \frac{1}{9}(-4 + 4 + 0) = 0.$$
  The segment is perpendicular to $\overrightarrow{AB}$, confirming true geometric orthogonality.

---

## 8. Common Mistakes to Avoid
- **Confusing direction signs:** Writing $P - Q$ versus $Q - P$; both have the same length and line of action, but one must be consistent when moving from $P$ to the plane.
- **Arithmetic in fraction addition:** Writing $3 + 1/9 = 4/9$ instead of $(27+1)/9 = 28/9$.
- **Omitting the absolute value:** Writing $(3 - 4)/3 = -1/3$ as a negative distance; geometric distance must always be non-negative.

---

## 9. Classroom Presentation (3-Sentence Summary)
Tracing a line from $P(3, 0, 0)$ along the plane's normal vector $(1, 2, 2)$ gives the parameter equation $3 + 9t = 4$, which solves to $t = 1/9$. This parameter locates the closest point on the plane as $Q = (28/9, 2/9, 2/9)$ and yields a minimal distance of $1/3$. The displacement vector connecting $P$ to $Q$ is $(1/9, 2/9, 2/9) = (1/9)n$, which is directly proportional to the normal vector, verifying that the shortest path meets the plane at a right angle.

