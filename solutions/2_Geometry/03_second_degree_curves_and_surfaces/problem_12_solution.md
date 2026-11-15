# Problem 12 Solution: Recognizing a Surface from Cross-Sections

## 1. Original Problem
A certain second-degree surface in $\mathbb{R}^3$ satisfies the following geometric properties:
1. The horizontal cross-section with the plane $z = 0$ is a single point.
2. For $z > 0$, the horizontal cross-sections $z = \text{const}$ are circles whose radii increase monotonically as $z$ increases.
3. Every vertical cross-section containing the vertical coordinate axis $Oz$ is a parabola.

Propose a simple second-degree equation for such a surface and provide a rigorous justification for your choice by verifying each of the three geometric conditions.

---

## 2. What We Are Trying to Find
We need to:
1. Reverse the standard analysis by constructing a mathematical equation from geometric clues.
2. Formulate a quadratic equation in $x, y, z$ embodying rotational symmetry about the $z$-axis.
3. Verify that the trace at $z = 0$ collapses to a single point (the vertex).
4. Verify that horizontal planes $z = c > 0$ produce circles of radius $R(c)$ that strictly increase with $c$.
5. Verify that every vertical plane containing the $z$-axis slices the surface along a parabola.

---

## 3. Key Concepts and Theorems
1. **Surfaces of Revolution Around the $z$-Axis:**
   Any surface with rotational symmetry about the $z$-axis depends on $x$ and $y$ only through the radial distance squared:
   $$r^2 = x^2 + y^2.$$
   An equation $F(x^2 + y^2, z) = 0$ automatically produces circular horizontal cross-sections.
2. **Vertical Planes Containing the $z$-Axis:**
   Any plane containing the $z$-axis ($Oz$) passes through the origin and can be parameterized by angle $\theta \in [0, \pi)$ as:
   $$y = (\tan \theta) x \quad (\text{or } x = 0 \text{ for } \theta = \pi/2).$$
   Along any such plane, the radial distance is $r = \sqrt{x^2 + y^2}$, and points are given by $(r \cos \theta, r \sin \theta, z)$.
3. **Parabolic Vertical Profile:**
   If the vertical slice is a parabola with vertex at the origin opening upwards, the height $z$ must be proportional to the square of the distance from the axis of symmetry:
   $$z = k\,r^2 = k(x^2 + y^2), \quad \text{where } k > 0.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Propose the Equation
The simplest second-degree equation that satisfies all given criteria is:
$$z = x^2 + y^2 \quad (\text{or with an arbitrary scaling constant } z = k(x^2 + y^2) \text{ with } k > 0).$$
Let us choose the canonical normalization $k = 1$:
$$z = x^2 + y^2.$$

### Step 2: Verify Condition 1 (Cross-Section $z = 0$ Is a Single Point)
Substitute $z = 0$ into the proposed equation:
$$0 = x^2 + y^2 \iff x^2 + y^2 = 0.$$
In the real numbers $\mathbb{R}$, $x^2 \ge 0$ and $y^2 \ge 0$. The sum of two non-negative real numbers can equal zero if and only if both numbers are individually zero:
$$x^2 = 0 \implies x = 0 \quad \text{and} \quad y^2 = 0 \implies y = 0.$$
Therefore, the only real solution in the plane $z = 0$ is the origin $(0, 0, 0)$.
The cross-section is indeed a **single point**. Condition 1 is satisfied.

### Step 3: Verify Condition 2 (Circles of Increasing Radius for $z > 0$)
Substitute an arbitrary constant height $z = c$ where $c > 0$:
$$x^2 + y^2 = c.$$
Since $c > 0$, this is the standard Cartesian equation of a **circle** lying in the horizontal plane $z = c$ with:
- Center on the $z$-axis at $(0, 0, c)$
- Radius: $R(c) = \sqrt{c}$

Now examine how the radius changes as $c$ increases:
$$\frac{dR}{dc} = \frac{1}{2\sqrt{c}} > 0 \quad \text{for all } c > 0.$$
Because the derivative is strictly positive, the radius $R(c) = \sqrt{c}$ is a **strictly increasing function** of the height $c$.
For example:
- At $z = 1$: circle of radius $R = 1$
- At $z = 4$: circle of radius $R = 2$
- At $z = 9$: circle of radius $R = 3$
Condition 2 is satisfied.

### Step 4: Verify Condition 3 (Vertical Cross-Sections Through $Oz$ Are Parabolas)
A vertical plane containing the $Oz$ axis passes through the line $x = 0, y = 0$.
Any such plane can be represented by the equation:
$$\Pi_\theta : y = (\tan \theta) x \quad (\text{or } x = 0).$$
Let us check both cases:
1. **Case $x = 0$ (the $yz$-plane):**
   Substitute $x = 0$ into $z = x^2 + y^2$:
   $$z = 0^2 + y^2 \implies z = y^2.$$
   This is a parabola in the plane $x = 0$ with vertex at $(0, 0, 0)$, opening upwards.
2. **Case $y = 0$ (the $xz$-plane):**
   Substitute $y = 0$ into $z = x^2 + y^2$:
   $$z = x^2 + 0^2 \implies z = x^2.$$
   This is a parabola in the plane $y = 0$ with vertex at $(0, 0, 0)$, opening upwards.
3. **General vertical plane $y = m\,x$ (where $m = \tan \theta \in \mathbb{R}$):**
   Substitute $y = mx$ into $z = x^2 + y^2$:
   $$z = x^2 + (mx)^2 = (1 + m^2)x^2.$$
   Let $u$ be the horizontal coordinate measuring distance along the direction vector $(1, m, 0)$ in the cutting plane, so that $u^2 = x^2 + y^2 = (1 + m^2)x^2$.
   Then the equation in the cutting plane $(u, z)$ is:
   $$z = u^2.$$
   This is a standard **parabola** in the $(u, z)$ coordinate system with vertex at $(0, 0, 0)$ opening upwards along the positive $z$-axis.
Condition 3 is satisfied for every vertical plane through the $z$-axis.

### Step 5: Name and Classification
The constructed surface is a **circular paraboloid** (or elliptic paraboloid of revolution).

---

## 5. Why Each Step Is Valid
1. **Rotational invariance** about the $z$-axis is algebraically guaranteed by the dependency solely on $r^2 = x^2 + y^2$.
2. **The positive definiteness of $x^2 + y^2$** guarantees uniqueness of the point solution $(0, 0, 0)$ at $z = 0$.
3. **The linear appearance of $z$** with quadratic terms $x^2 + y^2$ ensures the degree of the algebraic surface is exactly 2 (a second-degree quadric) and that the vertical profile is quadratic (a parabola).

---

## 6. Final Answer in Words
A simple and elegant equation for this surface is $z = x^2 + y^2$ (a circular paraboloid).
- At $z = 0$, $x^2 + y^2 = 0$ has only $(0, 0, 0)$ as a real solution, which is a single point.
- For any $z = c > 0$, the equation $x^2 + y^2 = c$ describes a circle with radius $R = \sqrt{c}$, which increases monotonically as $c$ grows.
- For any vertical plane passing through the $z$-axis (given by $y = mx$), the equation reduces to $z = (1 + m^2)x^2$, which is a parabola opening upwards with vertex at the origin.

---

## 7. Quick Verification
- Why not a cone $z^2 = x^2 + y^2$?
  For a cone, vertical cross-sections through $Oz$ are pairs of straight lines $z = \pm u$, not parabolas.
- Why not a sphere $x^2 + y^2 + z^2 = R^2$?
  For a sphere, vertical cross-sections are circles $u^2 + z^2 = R^2$, not parabolas, and the radius shrinks to 0 at the top rather than increasing indefinitely.
- The equation $z = x^2 + y^2$ is the unique minimal second-degree model satisfying all three requirements simultaneously.

---

## 8. Common Mistakes to Avoid
- **Proposing a cone ($z = \sqrt{x^2 + y^2}$):** Forgetting that a cone has linear vertical cross-sections ($z = |x|$), not parabolic ones.
- **Squaring $z$ ($z^2 = x^2 + y^2$):** This yields a double cone where $z < 0$ also produces circles, violating condition 1 and condition 2.
- **Using an elliptic paraboloid with unequal coefficients ($z = 2x^2 + y^2$):** This would produce ellipses rather than circles for horizontal slices, violating condition 2.

---

## 9. Classroom Presentation (3-Sentence Summary)
Because the horizontal slices are circles centered on the vertical axis, the equation must depend on the radial distance squared through $x^2 + y^2$. Because vertical cross-sections through the axis are parabolas opening upwards from the origin, the height $z$ must be directly proportional to this squared distance, giving the simple equation $z = x^2 + y^2$. This circular paraboloid has a single point vertex at $(0, 0, 0)$, circular horizontal cross-sections of expanding radius $\sqrt{z}$ for all $z > 0$, and parabolic vertical traces in every radial direction.
