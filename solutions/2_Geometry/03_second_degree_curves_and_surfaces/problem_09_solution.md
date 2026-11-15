# Problem 9 Solution: Ellipsoid and Its Cross-Sections

## 1. Original Problem
Consider the second-degree surface in $\mathbb{R}^3$ given by the equation:
$$\frac{x^2}{9} + \frac{y^2}{4} + \frac{z^2}{16} = 1.$$
1. State the lengths of the three semiaxes of the surface.
2. Describe the cross-section of the surface with the coordinate plane $z = 0$.
3. Analyze and explain how the horizontal cross-sections $z = c$ change as the parameter $c$ varies within the interval $|c| < 4$.

---

## 2. What We Are Trying to Find
We are asked to:
1. Extract the semiaxes $a, b, c_z$ along the $x, y,$ and $z$ directions from the denominators.
2. Set $z = 0$ to determine the exact 2D curve formed on the $xy$-plane.
3. Fix $z = c$ with $-4 < c < 4$ to obtain the family of horizontal cross-sections, determining their shape, varying semiaxes, and geometric behavior as $|c|$ approaches the boundary value $4$.

---

## 3. Key Concepts and Theorems
1. **Canonical Equation of an Ellipsoid:**
   $$\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c_z^2} = 1,$$
   where $a, b, c_z > 0$ represent the lengths of the principal semiaxes along the $x$, $y$, and $z$ axes respectively.
2. **Method of Cross-Sections (Traces):**
   The intersection of a 3D surface with a plane $z = c$ is obtained by substituting $z = c$ into the surface equation:
   $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 - \frac{c^2}{c_z^2}.$$
   - If $1 - \frac{c^2}{c_z^2} > 0$ (i.e., $|c| < c_z$), the cross-section is an **ellipse** whose size depends on $c$.
   - If $1 - \frac{c^2}{c_z^2} = 0$ (i.e., $c = \pm c_z$), the cross-section degenerates into a **single point** (the poles).
   - If $1 - \frac{c^2}{c_z^2} < 0$ (i.e., $|c| > c_z$), the intersection is **empty** (no real points).

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Semiaxis Lengths
Compare the given equation with the standard canonical form $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c_z^2} = 1$:
$$a^2 = 9 \implies a = 3,$$
$$b^2 = 4 \implies b = 2,$$
$$c_z^2 = 16 \implies c_z = 4.$$
Thus, the three principal semiaxes of the ellipsoid are:
- Semiaxis along the $x$-axis: $a = 3$
- Semiaxis along the $y$-axis: $b = 2$
- Semiaxis along the $z$-axis: $c_z = 4$

### Step 2: Describe the Cross-Section with $z = 0$
Substitute $z = 0$ into the surface equation:
$$\frac{x^2}{9} + \frac{y^2}{4} + \frac{0^2}{16} = 1 \implies \frac{x^2}{9} + \frac{y^2}{4} = 1.$$
This is a standard 2D **ellipse** lying in the $xy$-plane with:
- Center at the origin $(0, 0, 0)$
- Semi-major axis along $x$ of length $a = 3$ (intercepts $(\pm 3, 0, 0)$)
- Semi-minor axis along $y$ of length $b = 2$ (intercepts $(0, \pm 2, 0)$)
This cross-section represents the "equator" of the ellipsoid, which has the maximum cross-sectional area among all horizontal slices parallel to the $xy$-plane.

### Step 3: Analyze the Horizontal Cross-Sections $z = c$ for $|c| < 4$
Substitute an arbitrary constant height $z = c$ (with $-4 < c < 4$) into the equation:
$$\frac{x^2}{9} + \frac{y^2}{4} + \frac{c^2}{16} = 1 \implies \frac{x^2}{9} + \frac{y^2}{4} = 1 - \frac{c^2}{16}.$$
Since $|c| < 4$, the factor $k(c) = 1 - \frac{c^2}{16}$ is strictly positive:
$$0 < 1 - \frac{c^2}{16} \le 1.$$
Divide both sides by $k(c) = 1 - \frac{c^2}{16}$ to write the cross-section in canonical 2D form:
$$\frac{x^2}{9\left(1 - \frac{c^2}{16}\right)} + \frac{y^2}{4\left(1 - \frac{c^2}{16}\right)} = 1.$$
This shows that for every $|c| < 4$, the cross-section is a **similar ellipse** with:
- Semiaxis along $x$: $a(c) = 3\sqrt{1 - \frac{c^2}{16}}$
- Semiaxis along $y$: $b(c) = 2\sqrt{1 - \frac{c^2}{16}}$

**Geometric Evolution as $c$ varies:**
1. At the center $c = 0$, the semiaxes reach their maximum values $a(0) = 3$ and $b(0) = 2$.
2. As $|c|$ increases away from $0$ towards $4$, the scaling factor $\sqrt{1 - c^2/16}$ monotonically decreases from $1$ towards $0$.
3. The ratio of the semiaxes remains constant at all heights:
   $$\frac{a(c)}{b(c)} = \frac{3\sqrt{1 - c^2/16}}{2\sqrt{1 - c^2/16}} = \frac{3}{2}.$$
   Therefore, every horizontal slice is geometrically similar in aspect ratio, but smoothly shrinks in area as the cutting plane moves upward or downward.
4. When $|c| \to 4$, the semiaxes shrink to zero, and at $c = \pm 4$ the ellipse collapses into a single point: $(0, 0, 4)$ at the top pole and $(0, 0, -4)$ at the bottom pole.

---

## 5. Why Each Step Is Valid
1. **Extracting denominators** is valid because the equation is already normalized to $+1$ on the right side.
2. **Setting $z = 0$** directly corresponds to finding the intersection of the surface with the subspace defined by $z = 0$.
3. **Dividing by $1 - c^2/16$** is valid because $|c| < 4$ guarantees that $1 - c^2/16 > 0$, ensuring the divisor is strictly non-zero.

---

## 6. Final Answer in Words
The surface is an ellipsoid with semiaxes of lengths $a = 3$ along the $x$-axis, $b = 2$ along the $y$-axis, and $c_z = 4$ along the $z$-axis. The cross-section with the coordinate plane $z = 0$ is an ellipse $\frac{x^2}{9} + \frac{y^2}{4} = 1$ with semiaxes $3$ and $2$. For any height $z = c$ with $|c| < 4$, the cross-section is an ellipse $\frac{x^2}{9(1 - c^2/16)} + \frac{y^2}{4(1 - c^2/16)} = 1$; as $|c|$ increases from $0$ toward $4$, these ellipses maintain a constant aspect ratio of $3:2$ but monotonically shrink in size until collapsing into single points $(0, 0, \pm 4)$ at the poles.

---

## 7. Quick Verification
- At $c = 0$: $a(0) = 3\sqrt{1} = 3$, $b(0) = 2\sqrt{1} = 2$. Semiaxes match the equator.
- At $c = 2$: $1 - 2^2/16 = 1 - 1/4 = 3/4$.
  $a(2) = 3\sqrt{3/4} = \frac{3\sqrt{3}}{2} \approx 2.598$, $b(2) = 2\sqrt{3/4} = \sqrt{3} \approx 1.732$.
  Check a point: $x = a(2), y = 0, z = 2$:
  $$\frac{(3\sqrt{3}/2)^2}{9} + 0 + \frac{2^2}{16} = \frac{27/4}{9} + \frac{4}{16} = \frac{3}{4} + \frac{1}{4} = 1.$$
  The point lies exactly on the ellipsoid.

---

## 8. Common Mistakes to Avoid
- **Confusing denominators with semiaxes:** Taking $9, 4, 16$ as semiaxes instead of $\sqrt{9} = 3, \sqrt{4} = 2, \sqrt{16} = 4$.
- **Ignoring the restriction $|c| < 4$:** Trying to compute real cross-sections for $c = 5$, where $1 - 25/16 = -9/16 < 0$ yields no real points.
- **Thinking cross-sections are circles:** Overlooking that the denominators under $x^2$ and $y^2$ are unequal ($9 \neq 4$), which makes every horizontal cross-section an ellipse rather than a circle.

---

## 9. Classroom Presentation (3-Sentence Summary)
The denominators immediately reveal the three principal semiaxes of the ellipsoid: 3 along $x$, 2 along $y$, and 4 along $z$. Setting $z = 0$ isolates the central equatorial cross-section, which is the ellipse $x^2/9 + y^2/4 = 1$ with semiaxes 3 and 2. Slicing with horizontal planes $z = c$ for $|c| < 4$ produces ellipses with semiaxes scaled by $\sqrt{1 - c^2/16}$, which smoothly shrink while preserving their $3:2$ aspect ratio until they terminate at the poles $(0, 0, \pm 4)$.
