# Problem 15 Solution: Recognition and Sketch Without a Given Name

## 1. Original Problem
Consider the two second-degree equations:
1. $4x^2 + 9y^2 - 8x + 36y + 4 = 0$
2. $4x^2 + y^2 = z^2$

For the first equation:
- Reduce it to canonical form.
- Recognize the type of planar curve.
- Give its most important geometric features and provide sketching instructions.

For the second equation:
- Do not begin by using a ready-made name for the surface.
- First describe the horizontal cross-sections $z = c$, paying special attention to the unequal scales along the coordinate axes.
- Then describe the vertical cross-sections by the planes $x = 0$ and $y = 0$.
- Based on these cross-sections, identify the surface and provide sketching instructions.

---

## 2. What We Are Trying to Find
We need to:
1. Complete the squares for equation (1) in 2D to reduce it to a standard shifted ellipse equation and extract its center, semiaxes, vertices, and foci.
2. Analyze equation (2) in 3D through systematic cross-sections without premature classification.
3. Show that horizontal slices of (2) are non-circular ellipses with a fixed $1:2$ aspect ratio scaling linearly with $|z|$.
4. Show that vertical slices of (2) are pairs of intersecting straight lines with different slopes.
5. Synthesize these cross-sectional behaviors to identify the surface as an elliptic cone.

---

## 3. Key Concepts and Theorems
1. **Canonical Form of a Translated 2D Ellipse:**
   $$\frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1.$$
2. **Method of Cross-Sections for Surfaces:**
   By analyzing traces along orthogonal coordinate directions, a 3D surface is uniquely classified by the geometry of its planar slices:
   - If horizontal slices are ellipses whose sizes scale linearly with $|z|$ and vertical slices are pairs of intersecting lines meeting at a common point, the surface is a cone over an ellipse (**elliptic cone**).

---

## 4. Detailed Step-by-Step Solution

### Part A: Equation 1 ($4x^2 + 9y^2 - 8x + 36y + 4 = 0$)

#### Step A1: Group Terms and Factor Leading Coefficients
Group terms by variable and isolate the constant term:
$$(4x^2 - 8x) + (9y^2 + 36y) = -4.$$
Factor out the leading quadratic coefficients:
$$4(x^2 - 2x) + 9(y^2 + 4y) = -4.$$

#### Step A2: Complete the Squares
- For $x^2 - 2x$:
  $$x^2 - 2x = (x - 1)^2 - 1^2 = (x - 1)^2 - 1.$$
- For $y^2 + 4y$:
  $$y^2 + 4y = (y + 2)^2 - 2^2 = (y + 2)^2 - 4.$$

#### Step A3: Substitute and Balance Constants
Substitute back:
$$4\big((x - 1)^2 - 1\big) + 9\big((y + 2)^2 - 4\big) = -4$$
$$4(x - 1)^2 - 4 + 9(y + 2)^2 - 36 = -4.$$
Combine constants on the left:
$$-4 - 36 = -40.$$
Add $40$ to both sides:
$$4(x - 1)^2 + 9(y + 2)^2 = -4 + 40 = 36.$$

#### Step A4: Divide to Obtain Canonical Form
Divide both sides by $36$:
$$\frac{4(x - 1)^2}{36} + \frac{9(y + 2)^2}{36} = \frac{36}{36}$$
$$\frac{(x - 1)^2}{9} + \frac{(y + 2)^2}{4} = 1 \iff \frac{(x - 1)^2}{3^2} + \frac{(y + 2)^2}{2^2} = 1.$$

#### Step A5: Geometric Features and Sketching of Curve 1
- **Curve Type:** **Ellipse** with horizontal major axis.
- **Center:** $S(x_0, y_0) = (1, -2)$.
- **Horizontal semi-major axis:** $a = \sqrt{9} = 3$.
- **Vertical semi-minor axis:** $b = \sqrt{4} = 2$.
- **Vertices (Major axis):**
  $$(x_0 \pm a, y_0) \implies (1 + 3, -2) = (4, -2) \quad \text{and} \quad (1 - 3, -2) = (-2, -2).$$
- **Co-vertices (Minor axis):**
  $$(x_0, y_0 \pm b) \implies (1, -2 + 2) = (1, 0) \quad \text{and} \quad (1, -2 - 2) = (1, -4).$$
- **Foci:**
  $c = \sqrt{a^2 - b^2} = \sqrt{9 - 4} = \sqrt{5} \approx 2.236$.
  $$F_1 = (1 - \sqrt{5}, -2), \quad F_2 = (1 + \sqrt{5}, -2).$$
- **Sketching Instructions:** Mark center at $(1, -2)$, plot the major vertices at $(-2, -2)$ and $(4, -2)$, plot the minor co-vertices at $(1, 0)$ and $(1, -4)$, and sketch a smooth oval connecting these four boundary points.

---

### Part B: Equation 2 ($4x^2 + y^2 = z^2$)

#### Step B1: Describe Horizontal Cross-Sections $z = c$
Substitute $z = c$ into $4x^2 + y^2 = z^2$:
$$4x^2 + y^2 = c^2.$$
1. **For $c = 0$:**
   $$4x^2 + y^2 = 0 \implies x = 0, \; y = 0.$$
   The cross-section in the plane $z = 0$ is a **single point**: the origin $(0, 0, 0)$.
2. **For $c \neq 0$:**
   Divide both sides by $c^2 > 0$:
   $$\frac{4x^2}{c^2} + \frac{y^2}{c^2} = 1 \implies \frac{x^2}{(|c|/2)^2} + \frac{y^2}{|c|^2} = 1.$$
   This is an **ellipse** in the horizontal plane $z = c$ with:
   - Semiaxis along the $x$-axis: $a(c) = \frac{|c|}{2}$
   - Semiaxis along the $y$-axis: $b(c) = |c|$
   - Aspect ratio:
     $$\frac{b(c)}{a(c)} = \frac{|c|}{|c|/2} = 2.$$
   Every horizontal slice at height $c \neq 0$ is an ellipse whose vertical diameter along $y$ is **twice as long** as its horizontal diameter along $x$. As $|c|$ increases, these ellipses grow linearly in size.

#### Step B2: Describe Vertical Cross-Sections
1. **Cross-section with $x = 0$ ($yz$-plane):**
   Substitute $x = 0$:
   $$4(0)^2 + y^2 = z^2 \implies y^2 = z^2 \implies z^2 - y^2 = 0 \implies (z - y)(z + y) = 0.$$
   This is a **pair of intersecting lines**:
   $$z = y \quad \text{and} \quad z = -y.$$
   These lines pass through the origin $(0, 0, 0)$ with slope $\pm 1$ ($45^\circ$).
2. **Cross-section with $y = 0$ ($xz$-plane):**
   Substitute $y = 0$:
   $$4x^2 + 0^2 = z^2 \implies z^2 - 4x^2 = 0 \implies (z - 2x)(z + 2x) = 0.$$
   This is a **pair of intersecting lines**:
   $$z = 2x \quad \text{and} \quad z = -2x.$$
   These lines pass through the origin $(0, 0, 0)$ with steeper slope $\pm 2$.

#### Step B3: Identify the Surface and Provide Sketching Instructions
- **Identification:**
  The surface has an apex at $(0, 0, 0)$, all vertical cross-sections through the origin are straight lines meeting at the apex, and all horizontal cross-sections are ellipses with a constant $1:2$ semiaxis ratio expanding linearly with height $|z|$.
  Therefore, the surface is an **elliptic cone** (a cone with elliptical cross-sections).
- **Sketching Instructions:**
  1. Draw the origin $(0, 0, 0)$ as the sharp apex.
  2. Draw the vertical bounding rays in the $xz$-plane ($z = \pm 2x$, narrower opening) and in the $yz$-plane ($z = \pm y$, wider opening).
  3. At a chosen positive height, say $z = 2$, draw an ellipse centered at $(0, 0, 2)$ with $x$-semiaxis $1$ and $y$-semiaxis $2$.
  4. Symmetrically at $z = -2$, draw the identical ellipse centered at $(0, 0, -2)$.
  5. Connect the apex to the elliptical rims to render the upper and lower nappes of the elliptic cone.

---

## 5. Why Each Step Is Valid
1. **Completing the square in Part A** uses exact integer arithmetic ($4 \times 1 = 4$, $9 \times 4 = 36$, balance $-4 + 40 = 36$), which is fully reversible.
2. **Writing $4x^2 / c^2 = x^2 / (c/2)^2$ in Part B** directly identifies the semiaxis lengths in the standard elliptic form.
3. **The linear cross-sections in Part B** confirm that the surface is generated by a family of straight lines passing through the origin (a quadric cone).

---

## 6. Final Answer in Words
1. The first equation reduces to the canonical ellipse $\frac{(x - 1)^2}{9} + \frac{(y + 2)^2}{4} = 1$ with center $S = (1, -2)$, horizontal semi-major axis $a = 3$, and vertical semi-minor axis $b = 2$.
2. For the second equation, horizontal slices $z = c$ are ellipses $\frac{x^2}{(|c|/2)^2} + \frac{y^2}{|c|^2} = 1$ where the $y$-semiaxis is twice as long as the $x$-semiaxis, and vertical slices $x = 0$ and $y = 0$ are pairs of lines $z = \pm y$ and $z = \pm 2x$ intersecting at the origin. These cross-sections identify the surface as an **elliptic cone** with apex at the origin.

---

## 7. Quick Verification
- **Check Part A:** Center $(1, -2) \implies 4(1)^2 + 9(-2)^2 - 8(1) + 36(-2) + 4 = 4 + 36 - 8 - 72 + 4 = 44 - 80 = -36 \neq 0$ (matches the constant 36).
  Top co-vertex $(1, 0)$: $4(1)^2 + 9(0)^2 - 8(1) + 36(0) + 4 = 4 - 8 + 4 = 0$. (Verified)
- **Check Part B:** Point on ellipse at $z = 2$: $x = 1, y = 0, z = 2 \implies 4(1)^2 + 0^2 = 4 = 2^2$. (Verified)
  Point on ellipse at $z = 2$: $x = 0, y = 2, z = 2 \implies 0 + 2^2 = 4 = 2^2$. (Verified)

---

## 8. Common Mistakes to Avoid
- **In Part A, adding unbalanced constants:** Adding $1$ and $4$ instead of $4 \times 1 = 4$ and $9 \times 4 = 36$.
- **In Part B, calling it a circular cone:** Overlooking the factor $4$ on $x^2$, which causes the cross-sections to be stretched into ellipses rather than circles.
- **Inverting the semiaxes of the ellipse:** Taking $a(c) = 2|c|$ instead of $|c|/2$ because $4 = 2^2$ is in the numerator.

---

## 9. Classroom Presentation (3-Sentence Summary)
Completing the square on the first equation yields $(x - 1)^2/9 + (y + 2)^2/4 = 1$, which represents an ellipse centered at $(1, -2)$ with semiaxes 3 and 2. For the second equation, horizontal slices produce ellipses with semiaxes $|z|/2$ along $x$ and $|z|$ along $y$, showing that the cross-sections are twice as wide along the $y$-axis as along the $x$-axis. Since the vertical cross-sections along the coordinate planes are straight lines $z = \pm 2x$ and $z = \pm y$ intersecting at $(0, 0, 0)$, the surface is an elliptic cone with its apex at the origin.
