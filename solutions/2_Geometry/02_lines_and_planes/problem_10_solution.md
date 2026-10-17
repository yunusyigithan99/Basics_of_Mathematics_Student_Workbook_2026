# Problem 10 Solution: Projection of a Point onto a Plane and Reflection

## 1. Original Problem
Find the orthogonal projection of the point
$$P = (2, 1, 3)$$
onto the plane
$$\Pi : x + y + z = 3.$$
Then find the reflection $P'$ of point $P$ across this plane. Finally, verify that the midpoint of the line segment joining $P$ and its reflection $P'$ lies on the plane.

---

## 2. What We Are Trying to Find
We need to:
1. Construct the parametric line passing through $P$ perpendicular to the plane (along normal vector $n$).
2. Intersect this normal line with the plane to determine the projection point $P_0$.
3. Compute the reflection point $P'$ by traversing twice the displacement from $P$ to $P_0$.
4. Calculate the midpoint $M = \frac{P + P'}{2}$ and verify that it equals $P_0$ and satisfies the plane equation.

---

## 3. Key Concepts and Theorems
1. **Normal Line to a Plane Through a Given Point:**
   The perpendicular line dropped from point $P$ onto plane $\Pi$ has direction equal to the plane's normal vector $n = (A, B, C)$:
   $$\mathbf{r}(t) = P + t\,n = (x_P + t A, \; y_P + t B, \; z_P + t C).$$
2. **Orthogonal Projection of a Point:**
   The orthogonal projection $P_0$ is the unique point of intersection between the normal line and the plane $\Pi$. Substituting $\mathbf{r}(t)$ into the plane equation yields the parameter value $t_0$, giving:
   $$P_0 = P + t_0\,n.$$
3. **Reflection Across a Plane:**
   The reflection $P'$ across the plane lies on the same normal line at exactly twice the distance from $P$:
   $$P' = P + 2t_0\,n = 2P_0 - P.$$
4. **Midpoint Property of Reflection:**
   By geometric definition of reflection across a flat mirror, the reflecting plane is the perpendicular bisector of the line segment $PP'$. Hence, the midpoint $M = \frac{P + P'}{2}$ must coincide with the projection $P_0$ and lie on the plane.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Normal Line Through $P$
From the plane equation $x + y + z = 3$, the normal vector is:
$$n = (1, 1, 1).$$
The parametric line passing through $P(2, 1, 3)$ parallel to $n$ is:
$$\begin{cases}
x(t) = 2 + t \\
y(t) = 1 + t \\
z(t) = 3 + t
\end{cases}$$

### Step 2: Find the Intersection Parameter $t_0$
Substitute the parametric coordinates into the plane equation $x + y + z = 3$:
$$(2 + t) + (1 + t) + (3 + t) = 3.$$
Combine like terms:
$$(2 + 1 + 3) + (t + t + t) = 3$$
$$6 + 3t = 3.$$
Subtract 6 and divide by 3:
$$3t = -3 \implies t_0 = -1.$$

### Step 3: Compute the Orthogonal Projection $P_0$
Substitute $t_0 = -1$ into the parametric line equations:
$$x_0 = 2 + (-1) = 1,$$
$$y_0 = 1 + (-1) = 0,$$
$$z_0 = 3 + (-1) = 2.$$
Thus, the orthogonal projection of $P$ onto the plane is:
$$P_0 = (1, 0, 2).$$
Check: $1 + 0 + 2 = 3$, so $P_0$ lies on $\Pi$.

### Step 4: Compute the Reflection Point $P'$
The reflection corresponds to taking twice the parameter step along the normal line, $t = 2t_0 = 2(-1) = -2$:
$$P' = P + 2t_0\,n = (2, 1, 3) + (-2)(1, 1, 1) = (2 - 2, \; 1 - 2, \; 3 - 2) = (0, -1, 1).$$
Alternatively, using the vector midpoint relationship $P' = 2P_0 - P$:
$$P' = 2(1, 0, 2) - (2, 1, 3) = (2, 0, 4) - (2, 1, 3) = (0, -1, 1).$$
The reflection of $P$ across the plane is $P' = (0, -1, 1)$.

### Step 5: Check That the Midpoint Lies on the Plane
Calculate the midpoint $M$ of segment $PP'$:
$$M = \frac{P + P'}{2} = \frac{(2, 1, 3) + (0, -1, 1)}{2} = \frac{(2 + 0, \; 1 - 1, \; 3 + 1)}{2} = \frac{(2, 0, 4)}{2} = (1, 0, 2).$$
Notice that $M = P_0 = (1, 0, 2)$.
Now substitute the coordinates of $M(1, 0, 2)$ into the plane equation $x + y + z = 3$:
$$\text{LHS} = 1 + 0 + 2 = 3 = \text{RHS}.$$
The midpoint lies directly on the plane, confirming the reflection.

---

## 5. Why Each Step Is Valid
1. **Using the normal vector as line direction** ensures the path from $P$ to the plane meets the plane at right angles ($90^\circ$), which is the definition of orthogonal projection.
2. **Solving the linear equation in $t$** uniquely determines the point on the plane nearest to $P$.
3. **Doubling the parameter step ($2t_0$)** moves from $P$ through the mirror plane to the exact symmetrical position on the opposite side.

---

## 6. Final Answer in Words
The orthogonal projection of $P(2, 1, 3)$ onto the plane $x + y + z = 3$ is $P_0 = (1, 0, 2)$. The reflection of $P$ across the plane is $P' = (0, -1, 1)$. The midpoint of the line segment joining $P$ and $P'$ is $M = (1, 0, 2)$, which matches $P_0$ and satisfies $1 + 0 + 2 = 3$, verifying that the plane perpendicularly bisects the segment.

---

## 7. Quick Verification
- **Distance check:**
  $$d(P, \Pi) = \frac{|2 + 1 + 3 - 3|}{\sqrt{1^2 + 1^2 + 1^2}} = \frac{3}{\sqrt{3}} = \sqrt{3}.$$
  Direct vector distance $\|P - P_0\| = \|(2 - 1, 1 - 0, 3 - 2)\| = \|(1, 1, 1)\| = \sqrt{1 + 1 + 1} = \sqrt{3}$.
  Direct vector distance $\|P' - P_0\| = \|(0 - 1, -1 - 0, 1 - 2)\| = \|(-1, -1, -1)\| = \sqrt{3}$.
  Both $P$ and $P'$ are equidistant from the plane with distance $\sqrt{3}$.
- **Perpendicularity of $\overrightarrow{PP'}$ to the plane:**
  $$\overrightarrow{PP'} = P' - P = (0 - 2, -1 - 1, 1 - 3) = (-2, -2, -2) = -2(1, 1, 1) = -2n.$$
  The segment is strictly parallel to the normal vector $n$.

---

## 8. Common Mistakes to Avoid
- **Using $t_0$ for reflection instead of $2t_0$:** Confusing the projection point $P_0$ with the reflection point $P'$.
- **Arithmetic sign in $t_0$:** Getting $3t = 3 \implies t = +1$, which moves *away* from the plane in the wrong direction to $(3, 2, 4)$.
- **Assuming reflection preserves all coordinates:** Guessing coordinates instead of systematically moving along the normal vector.

---

## 9. Classroom Presentation (3-Sentence Summary)
We construct the line perpendicular to the plane passing through $P(2, 1, 3)$ along normal vector $(1, 1, 1)$ and intersect it with $x+y+z=3$, giving parameter $t = -1$ and projection point $P_0 = (1, 0, 2)$. Doubling the parameter step to $t = -2$ yields the reflected point $P' = (0, -1, 1)$ on the opposite side of the plane. We verify the construction by checking that the midpoint of segment $PP'$ is $(1, 0, 2)$, which satisfies $1+0+2=3$ and therefore lies squarely on the plane.

