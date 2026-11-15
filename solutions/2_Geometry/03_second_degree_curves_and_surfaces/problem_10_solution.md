# Problem 10 Solution: Paraboloids

## 1. Original Problem
Compare the two second-degree surfaces in $\mathbb{R}^3$:
$$S_1 : z = x^2 + y^2 \quad \text{and} \quad S_2 : z = x^2 - y^2.$$
For each surface:
1. Describe the cross-section with the coordinate plane $x = 0$.
2. Describe the cross-section with the coordinate plane $y = 0$.
3. Describe the horizontal cross-sections with planes $z = c$ for various values of the real constant $c$.
4. Provide a qualitative sketch and geometric interpretation of both surfaces.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the mathematical family of both surfaces (elliptic paraboloid vs. hyperbolic paraboloid).
2. Compute the 2D traces of each surface along the primary coordinate planes $x = 0$ and $y = 0$.
3. Analyze the level curves $z = c$ as $c$ is positive, zero, or negative.
4. Explain the key structural difference between a bowl-shaped surface with a minimum point and a saddle-shaped surface with a minimax point.

---

## 3. Key Concepts and Theorems
1. **Elliptic Paraboloid:**
   An equation of the form $z = \frac{x^2}{a^2} + \frac{y^2}{b^2}$. The vertical cross-sections are parabolas opening in the same direction (upwards), and horizontal cross-sections $z = c > 0$ are ellipses (or circles when $a = b$).
2. **Hyperbolic Paraboloid (Saddle Surface):**
   An equation of the form $z = \frac{x^2}{a^2} - \frac{y^2}{b^2}$. Vertical cross-sections parallel to the axes are parabolas opening in opposite directions (one upwards, one downwards). Horizontal cross-sections $z = c \neq 0$ are hyperbolas, while $z = 0$ is a pair of intersecting lines.
3. **Traces (Cross-Sections):**
   Setting one variable to a constant isolates the 2D curve in which the cutting plane intersects the 3D surface.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze Surface 1 ($S_1 : z = x^2 + y^2$)

1. **Cross-section with $x = 0$ ($yz$-plane):**
   Substitute $x = 0$:
   $$z = 0^2 + y^2 \implies z = y^2.$$
   This is a **parabola** in the $yz$-plane with vertex at the origin $(0, 0, 0)$, opening upwards along the positive $z$-axis.
2. **Cross-section with $y = 0$ ($xz$-plane):**
   Substitute $y = 0$:
   $$z = x^2 + 0^2 \implies z = x^2.$$
   This is a **parabola** in the $xz$-plane with vertex at $(0, 0, 0)$, opening upwards along the positive $z$-axis.
3. **Horizontal cross-sections $z = c$:**
   Substitute $z = c$:
   $$x^2 + y^2 = c.$$
   - **Case $c > 0$:** The equation $x^2 + y^2 = c$ represents a **circle** of radius $R = \sqrt{c}$ centered on the $z$-axis at $(0, 0, c)$. As $c$ increases, the circles widen.
   - **Case $c = 0$:** The equation $x^2 + y^2 = 0$ has only the single real solution $(0, 0, 0)$, representing a **single point** (the vertex/minimum).
   - **Case $c < 0$:** The sum of two real squares cannot be negative ($x^2 + y^2 \ge 0$), so for $c < 0$ there are no real points (the intersection is **empty**).
4. **Classification & Geometry:**
   $S_1$ is a **circular (elliptic) paraboloid**. It forms a symmetric, cup-shaped bowl with its global minimum and vertex at the origin $(0, 0, 0)$, opening upwards to infinity.

---

### Step 2: Analyze Surface 2 ($S_2 : z = x^2 - y^2$)

1. **Cross-section with $x = 0$ ($yz$-plane):**
   Substitute $x = 0$:
   $$z = 0^2 - y^2 \implies z = -y^2.$$
   This is a **parabola** in the $yz$-plane with vertex at $(0, 0, 0)$, opening **downwards** along the negative $z$-axis.
2. **Cross-section with $y = 0$ ($xz$-plane):**
   Substitute $y = 0$:
   $$z = x^2 - 0^2 \implies z = x^2.$$
   This is a **parabola** in the $xz$-plane with vertex at $(0, 0, 0)$, opening **upwards** along the positive $z$-axis.
3. **Horizontal cross-sections $z = c$:**
   Substitute $z = c$:
   $$x^2 - y^2 = c.$$
   - **Case $c > 0$:** $x^2 - y^2 = c \iff \frac{x^2}{(\sqrt{c})^2} - \frac{y^2}{(\sqrt{c})^2} = 1$. This is a **hyperbola** in the plane $z = c$ opening horizontally along the $x$-direction with vertices at $(\pm \sqrt{c}, 0, c)$.
   - **Case $c = 0$:** $x^2 - y^2 = 0 \iff (x - y)(x + y) = 0$. This represents a **pair of intersecting straight lines**: $y = x$ and $y = -x$ intersecting at the origin $(0, 0, 0)$.
   - **Case $c < 0$:** Let $c = -k$ with $k > 0$. Then $x^2 - y^2 = -k \iff y^2 - x^2 = k \iff \frac{y^2}{(\sqrt{k})^2} - \frac{x^2}{(\sqrt{k})^2} = 1$. This is a **hyperbola** in the plane $z = c$ opening vertically along the $y$-direction with vertices at $(0, \pm \sqrt{k}, c)$.
4. **Classification & Geometry:**
   $S_2$ is a **hyperbolic paraboloid** (commonly known as a **saddle surface**). The origin $(0, 0, 0)$ is a **saddle point**: it is a local minimum along the $x$-direction ($z = x^2$) and simultaneously a local maximum along the $y$-direction ($z = -y^2$).

---

### Step 3: Comparison and Qualitative Sketch Summary
- **$S_1$ (Elliptic Paraboloid):** Both vertical cross-sections $z = x^2$ and $z = y^2$ curve in the same direction (upwards). Slices at $z > 0$ are closed concentric circles. Shape: a smooth 3D bowl.
- **$S_2$ (Hyperbolic Paraboloid):** One vertical cross-section curves upwards ($z = x^2$) while the orthogonal one curves downwards ($z = -y^2$). Slices at $z \neq 0$ are open hyperbolas whose orientation rotates by $90^\circ$ as $z$ crosses $0$. Shape: a horse saddle or mountain pass.

---

## 5. Why Each Step Is Valid
1. **Setting coordinate variables to zero** isolates planar slices that are mathematically equivalent to 2D Cartesian curves.
2. **The signs of quadratic terms** dictate curvature: $x^2 + y^2$ has positive definite Hessian matrix (positive Gaussian curvature $K > 0$), whereas $x^2 - y^2$ has indefinite Hessian with one positive and one negative eigenvalue (negative Gaussian curvature $K < 0$).
3. **The factorization $x^2 - y^2 = (x - y)(x + y)$** at $z = 0$ rigorously confirms that the saddle surface contains two intersecting straight lines (it is a doubly ruled surface).

---

## 6. Final Answer in Words
For $S_1 : z = x^2 + y^2$, the cross-sections are $z = y^2$ (parabola opening up) for $x = 0$, $z = x^2$ (parabola opening up) for $y = 0$, and for $z = c$ they are circles of radius $\sqrt{c}$ when $c > 0$, a single point at $(0,0,0)$ when $c = 0$, and empty when $c < 0$; $S_1$ is an elliptic paraboloid (bowl). For $S_2 : z = x^2 - y^2$, the cross-sections are $z = -y^2$ (parabola opening down) for $x = 0$, $z = x^2$ (parabola opening up) for $y = 0$, and for $z = c$ they are hyperbolas opening along $x$ when $c > 0$, two intersecting lines $y = \pm x$ when $c = 0$, and hyperbolas opening along $y$ when $c < 0$; $S_2$ is a hyperbolic paraboloid (saddle surface).

---

## 7. Quick Verification
- For $S_1$: Point $(1, 1, 2)$ gives $2 = 1^2 + 1^2 = 2$. Cross-section at $z = 2$ is $x^2 + y^2 = 2$, radius $\sqrt{2}$.
- For $S_2$: Point $(2, 1, 3)$ gives $3 = 2^2 - 1^2 = 4 - 1 = 3$. Cross-section at $z = 3$ is $x^2 - y^2 = 3$ (hyperbola opening along $x$).
- Point $(1, 2, -3)$ gives $-3 = 1^2 - 2^2 = 1 - 4 = -3$. Cross-section at $z = -3$ is $y^2 - x^2 = 3$ (hyperbola opening along $y$).
All points and cross-section signs are completely consistent.

---

## 8. Common Mistakes to Avoid
- **Thinking $z = x^2 - y^2$ has no points for $z < 0$:** Unlike $x^2 + y^2$, the difference of squares can take negative values whenever $|y| > |x|$.
- **Misidentifying the opening of $z = -y^2$:** Forgetting the minus sign and assuming all parabolas open upwards.
- **Missing the intersecting lines at $z = 0$:** Overlooking that $x^2 - y^2 = 0$ factors into two lines $y = \pm x$ through the saddle point.

---

## 9. Classroom Presentation (3-Sentence Summary)
For $z = x^2 + y^2$, both axial slices are parabolas opening upwards, and horizontal cuts produce concentric circles of radius $\sqrt{c}$, creating an upward-opening bowl called an elliptic paraboloid. In contrast, for $z = x^2 - y^2$, the slice along $x$ curves upward ($z = x^2$) while the slice along $y$ curves downward ($z = -y^2$), producing a saddle point at the origin. Horizontal slices of this saddle surface form hyperbolas that switch orientation across the two crossing asymptotic lines $y = \pm x$ at $z = 0$.
