# Problem 14 Solution: Closest Point on a Line

## 1. Original Problem
Given the point $P = (4, 1)$ and a line $L$ passing through the origin with direction vector $v = (1, 2)$.
Using orthogonal vector projection:
1. Find the coordinates of the closest point $Q$ on the line $L$ to point $P$.
2. Compute the minimum distance from $P$ to the line.
3. Verify that the displacement vector connecting $Q$ to $P$ is perpendicular to the direction vector $v$ of the line.

---

## 2. What We Are Trying to Find
We need to:
1. Treat the coordinates of point $P$ as the position vector $u = \overrightarrow{OP} = (4, 1)$.
2. Calculate the projection of $u$ onto direction vector $v$ to locate the point of orthogonal incidence $Q$.
3. Compute the error/residual vector $\overrightarrow{QP} = u - Q$.
4. Calculate the Euclidean norm $\|\overrightarrow{QP}\|$, which represents the minimum distance.
5. Show that $\overrightarrow{QP} \cdot v = 0$ to confirm that the shortest distance is achieved along the perpendicular line.

---

## 3. Key Concepts and Theorems
1. **Parametric Equation of a Line Through the Origin:**
   The line $L$ consisting of all scalar multiples of direction vector $v$:
   $$L = \{ t\,v \mid t \in \mathbb{R} \}.$$
2. **Orthogonal Projection as Minimum Distance:**
   The point $Q \in L$ that minimizes the Euclidean distance $\|P - Q\|$ to an external point $P$ is given precisely by the orthogonal projection of the position vector $u = \overrightarrow{OP}$ onto $v$:
   $$Q = \operatorname{proj}_v u = \left(\frac{u \cdot v}{v \cdot v}\right) v.$$
3. **Distance from a Point to a Line:**
   The geometric distance is the length of the perpendicular residual vector:
   $$d(P, L) = \|\overrightarrow{QP}\| = \|u - \operatorname{proj}_v u\|.$$
4. **Geometric Optimality Condition:**
   The shortest distance from a point to a line is measured along the perpendicular line segment, meaning $\overrightarrow{QP} \perp v \iff \overrightarrow{QP} \cdot v = 0$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Vectors and Compute Dot Products
Let $u = \overrightarrow{OP} = (4, 1)$ and $v = (1, 2)$.
Compute the dot products:
$$u \cdot v = (4)(1) + (1)(2) = 4 + 2 = 6,$$
$$v \cdot v = \|v\|^2 = 1^2 + 2^2 = 1 + 4 = 5.$$

### Step 2: Find the Closest Point $Q$ on the Line
Calculate the projection of $u$ onto $v$:
$$Q = \operatorname{proj}_v u = \left(\frac{u \cdot v}{v \cdot v}\right) v = \frac{6}{5}(1, 2) = \left(\frac{6}{5}, \; \frac{12}{5}\right) = (1.2, \; 2.4).$$
This point $Q$ lies on the line $L$ and is the closest point to $P$.

### Step 3: Compute the Displacement Vector $\overrightarrow{QP}$
Construct the vector connecting $Q$ to $P$:
$$\overrightarrow{QP} = P - Q = (4, 1) - \left(\frac{6}{5}, \; \frac{12}{5}\right) = \left(\frac{20}{5} - \frac{6}{5}, \; \frac{5}{5} - \frac{12}{5}\right) = \left(\frac{14}{5}, \; -\frac{7}{5}\right) = (2.8, \; -1.4).$$

### Step 4: Compute the Distance from $P$ to the Line
Calculate the magnitude of $\overrightarrow{QP}$:
$$d(P, L) = \|\overrightarrow{QP}\| = \sqrt{\left(\frac{14}{5}\right)^2 + \left(-\frac{7}{5}\right)^2} = \sqrt{\frac{196}{25} + \frac{49}{25}} = \sqrt{\frac{245}{25}}.$$
Simplify the square root:
$$\sqrt{\frac{245}{25}} = \frac{\sqrt{49 \times 5}}{5} = \frac{7\sqrt{5}}{5} \approx 3.1305.$$

### Step 5: Verify Perpendicularity to the Line
Take the dot product of $\overrightarrow{QP} = \left(\frac{14}{5}, -\frac{7}{5}\right)$ with the line's direction vector $v = (1, 2)$:
$$\overrightarrow{QP} \cdot v = \left(\frac{14}{5}\right)(1) + \left(-\frac{7}{5}\right)(2) = \frac{14}{5} - \frac{14}{5} = 0.$$
Because the dot product is $0$, the displacement vector $\overrightarrow{QP}$ is strictly perpendicular to the direction vector $v$.

---

## 5. Why Each Step Is Valid
1. **Orthogonal projection minimizes distance:** The squared distance function $f(t) = \|u - t\,v\|^2$ is a strictly convex parabola in $t$. Differentiating with respect to $t$ and setting to zero yields $t = \frac{u \cdot v}{v \cdot v}$, proving that projection yields the unique global minimum.
2. **Exact fractional arithmetic** guarantees that no precision is lost when taking differences and norms.
3. **The vanishing scalar product** confirms that the connection between the point and the line forms a right angle.

---

## 6. Final Answer in Words
The closest point on the line to $P = (4, 1)$ is $Q = \left(\frac{6}{5}, \frac{12}{5}\right) = (1.2, 2.4)$. The distance from $P$ to the line is $d(P, L) = \frac{7\sqrt{5}}{5}$ (approximately $3.13$). The displacement vector connecting them is $\overrightarrow{QP} = \left(\frac{14}{5}, -\frac{7}{5}\right)$, whose dot product with $v = (1, 2)$ is $\frac{14}{5} - \frac{14}{5} = 0$, confirming that the shortest path meets the line perpendicularly.

---

## 7. Quick Verification
- **Cartesian Line Equation Check:**
  The line passes through $(0, 0)$ with direction $(1, 2)$, so its slope is $m = 2/1 = 2$.
  Equation of line: $y = 2x \iff 2x - y = 0$.
  Standard distance formula from point $(x_0, y_0) = (4, 1)$ to line $Ax + By + C = 0$:
  $$d = \frac{|A x_0 + B y_0 + C|}{\sqrt{A^2 + B^2}} = \frac{|2(4) - 1(1) + 0|}{\sqrt{2^2 + (-1)^2}} = \frac{|8 - 1|}{\sqrt{5}} = \frac{7}{\sqrt{5}} = \frac{7\sqrt{5}}{5}.$$
  This matches our vector projection distance formula identically!

---

## 8. Common Mistakes to Avoid
- **Inverting the slope:** Treating $v = (1, 2)$ as slope $1/2$ instead of $\Delta y / \Delta x = 2/1 = 2$.
- **Subtracting in the wrong order:** Computing $Q - P$ instead of $P - Q$ (this flips the vector direction, though the length and perpendicularity remain unchanged).
- **Arithmetic slips with fractions:** Calculating $\frac{5}{5} - \frac{12}{5} = \frac{7}{5}$ instead of $-\frac{7}{5}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
By projecting the position vector $P = (4, 1)$ onto the line's direction $v = (1, 2)$, we find the closest point $Q = (6/5, 12/5)$. The distance between $P$ and $Q$ is calculated using the Euclidean norm of the residual vector $(14/5, -7/5)$, giving $7\sqrt{5}/5$. We verify this minimum-distance property by showing that the dot product of this residual vector with the direction vector $v$ equals zero, confirming that the shortest path to a line is always perpendicular to it.

