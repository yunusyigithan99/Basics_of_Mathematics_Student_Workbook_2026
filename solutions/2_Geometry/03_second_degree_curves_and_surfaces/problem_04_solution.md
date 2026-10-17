# Problem 4 Solution: Parabola Features and Sketching

## 1. Original Problem
For the parabola given by the equation:
$$y^2 = 12x,$$
identify the vertex, the axis of symmetry, and the opening direction. Compute the exact coordinates of the points on the parabola corresponding to $x = 3$, and use them to provide a complete guide for making an accurate sketch.

---

## 2. What We Are Trying to Find
We need to:
1. Match the given equation to the standard canonical form $y^2 = 2px$.
2. State the vertex coordinates and the linear equation of the axis of symmetry.
3. Determine the opening orientation (up, down, left, or right) from algebraic sign constraints.
4. Calculate the focal parameter $p$, the focus $F$, and the directrix line.
5. Solve for the $y$-values when $x = 3$, identifying the endpoints of the latus rectum (focal chord).
6. Provide geometric instructions for sketching the parabola.

---

## 3. Key Concepts and Theorems
1. **Canonical Form of a Horizontal Parabola:**
   $$y^2 = 2px,$$
   where $p > 0$ is the distance between the focus and the directrix.
2. **Geometric Properties:**
   - **Vertex:** $(0, 0)$
   - **Axis of Symmetry:** The line $y = 0$ (the $x$-axis), because substituting $-y$ for $y$ leaves the equation invariant: $(-y)^2 = y^2 = 2px$.
   - **Focus:** $F = \left(\frac{p}{2}, 0\right)$
   - **Directrix:** The vertical line $x = -\frac{p}{2}$
   - **Opening Direction:** Since $y^2 \ge 0$ for all $y \in \mathbb{R}$, we must have $2px \ge 0 \implies x \ge 0$. The curve exists only in the right half-plane and opens to the right.
3. **Latus Rectum (Focal Chord):**
   The chord passing through the focus perpendicular to the axis of symmetry corresponds to $x = \frac{p}{2}$. Its endpoints have $y = \pm p$, giving a total focal width of $2p$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Match to Canonical Form and Extract Parameters
Compare $y^2 = 12x$ with $y^2 = 2px$:
$$2p = 12 \implies p = 6.$$
- The focal distance from the vertex is:
  $$\frac{p}{2} = \frac{6}{2} = 3.$$

### Step 2: Identify Vertex, Axis of Symmetry, and Opening Direction
- **Vertex:**
  Setting $x = 0$ gives $y^2 = 0 \implies y = 0$. The vertex is at the origin:
  $$V = (0, 0).$$
- **Axis of Symmetry:**
  The equation contains $y^2$ and no linear $y$-term. Thus, if $(x, y)$ is on the curve, $(x, -y)$ is also on the curve. The curve is symmetric across the $x$-axis:
  $$\text{Axis of symmetry: } y = 0.$$
- **Opening Direction:**
  Because the square of any real number is non-negative ($y^2 \ge 0$), we have:
  $$12x \ge 0 \implies x \ge 0.$$
  The curve contains no points with negative $x$-coordinates. As $x \to +\infty$, $|y| = \sqrt{12x} \to +\infty$.
  Therefore, the parabola **opens horizontally to the right** (along the positive $x$-axis).

### Step 3: Compute Points for $x = 3$
Substitute $x = 3$ into the equation:
$$y^2 = 12(3) = 36.$$
Taking the square root:
$$y = \pm \sqrt{36} = \pm 6.$$
The two corresponding points on the parabola are:
$$P_1 = (3, 6) \quad \text{and} \quad P_2 = (3, -6).$$
*Geometric Note:* Since $\frac{p}{2} = 3$, $x = 3$ is precisely the line through the focus. Thus, $P_1$ and $P_2$ are the endpoints of the latus rectum, and the distance between them is $|6 - (-6)| = 12 = 2p$.

### Step 4: Summary of Associated Focal Geometry
- **Focus:** $F = (3, 0)$
- **Directrix:** $x = -3$

### Step 5: Instructions for Making a Sketch
1. Draw Cartesian axes with equal scaling.
2. Mark the vertex at the origin $V(0, 0)$.
3. Plot the focus at $F(3, 0)$ and draw the vertical dashed directrix line at $x = -3$.
4. Plot the two symmetric points $P_1(3, 6)$ and $P_2(3, -6)$ directly above and below the focus.
5. Draw a smooth, opening curve starting at $(0, 0)$ with a vertical tangent at the origin, passing smoothly through $(3, 6)$ in the first quadrant and $(3, -6)$ in the fourth quadrant, widening continuously as $x$ increases.

---

## 5. Why Each Step Is Valid
1. **The non-negativity of $y^2$** restricts the domain to $x \in [0, \infty)$, mathematically fixing the rightward orientation.
2. **Invariance under $y \mapsto -y$** proves bilateral reflectional symmetry across the horizontal $x$-axis.
3. **Evaluating at $x = 3$** tests the defining parabolic property: distance from $(3, 6)$ to focus $(3, 0)$ is $|6 - 0| = 6$, and distance to directrix $x = -3$ is $|3 - (-3)| = 6$. Both distances are equal.

---

## 6. Final Answer in Words
The parabola $y^2 = 12x$ has its vertex at the origin $V = (0, 0)$, its axis of symmetry is the $x$-axis ($y = 0$), and it opens to the right into the positive $x$ half-plane. Substituting $x = 3$ yields $y^2 = 36$, giving the symmetric points $(3, 6)$ and $(3, -6)$, which represent the endpoints of the focal chord directly above and below the focus $(3, 0)$.

---

## 7. Quick Verification
- **Equidistance definition of a parabola:**
  Every point $P(x, y)$ on the parabola must satisfy $d(P, F) = d(P, \text{directrix})$.
  Let $P = (3, 6)$, Focus $F = (3, 0)$, Directrix $x = -3$:
  $$d(P, F) = \sqrt{(3 - 3)^2 + (6 - 0)^2} = \sqrt{0 + 36} = 6.$$
  $$d(P, \text{directrix}) = |3 - (-3)| = |3 + 3| = 6.$$
  Since $6 = 6$, the point $(3, 6)$ strictly satisfies the geometric definition of the parabola.
- **Additional check at $x = 12$:**
  $$y^2 = 12(12) = 144 \implies y = \pm 12.$$
  Points $(12, 12)$ and $(12, -12)$ lie on the curve.

---

## 8. Common Mistakes to Avoid
- **Confusing horizontal and vertical parabolas:** Sketching $y^2 = 12x$ as opening upwards like $y = 12x^2$. The squared variable dictates the direction of opening ($y^2$ opens horizontally).
- **Opening in the wrong direction:** Opening to the left ($x \le 0$), forgetting that a positive coefficient $+12$ requires $x \ge 0$.
- **Missing the negative root:** Finding only $y = +6$ and omitting the symmetric point $(3, -6)$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The equation $y^2 = 12x$ has its vertex at the origin $(0, 0)$ and is symmetric across the $x$-axis because replacing $y$ with $-y$ leaves the equation unchanged. Because $y^2$ is always non-negative, $x$ must be non-negative, meaning the parabola opens horizontally to the right. Setting $x = 3$ gives $y^2 = 36$, producing the symmetric points $(3, 6)$ and $(3, -6)$, which lie directly above and below the focus $(3, 0)$ and confirm the curve's focal width of 12.

