# Problem 3 Solution: Ellipse Semiaxes and Stretched Orientation

## 1. Original Problem
For the ellipse given in canonical form:
$$\frac{x^2}{25} + \frac{y^2}{9} = 1,$$
find the lengths of the semiaxes, the coordinates of all intercepts with the coordinate axes, and provide a clear description for sketching. Explain along which axis the ellipse is more stretched and how this geometric property is directly visible in the algebraic structure of the equation.

---

## 2. What We Are Trying to Find
We need to:
1. Extract the values of $a$ and $b$ from the denominators.
2. Determine the four axial intercepts (vertices and co-vertices) by setting $y = 0$ and $x = 0$.
3. Identify the major and minor axes.
4. Explain how comparing the denominators $25$ and $9$ reveals the direction and degree of stretching.
5. Provide precise coordinates and focal points for plotting and sketching.

---

## 3. Key Concepts and Theorems
1. **Canonical Form of an Ellipse:**
   $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1,$$
   where $a > 0$ is the horizontal semiaxis length and $b > 0$ is the vertical semiaxis length.
2. **Major and Minor Axes:**
   - If $a > b$, the major axis lies along the $x$-axis with length $2a$, and the minor axis lies along the $y$-axis with length $2b$.
   - The ellipse is stretched more along whichever variable has the larger denominator.
3. **Focal Distance:**
   The linear eccentricity (distance from the center to each focus) is given by:
   $$c = \sqrt{a^2 - b^2} \quad (\text{for } a > b).$$
   The foci lie on the major axis at $(\pm c, 0)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Semiaxis Lengths
Compare the given equation with $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$:
$$a^2 = 25 \implies a = \sqrt{25} = 5,$$
$$b^2 = 9 \implies b = \sqrt{9} = 3.$$
- **Horizontal semi-major axis length:** $a = 5$
- **Vertical semi-minor axis length:** $b = 3$

### Step 2: Find the Intercepts with the Coordinate Axes
1. **$x$-intercepts:** Set $y = 0$ in the equation:
   $$\frac{x^2}{25} + \frac{0^2}{9} = 1 \implies \frac{x^2}{25} = 1 \implies x^2 = 25 \implies x = \pm 5.$$
   The $x$-intercepts (the major vertices) are:
   $$V_1 = (-5, 0) \quad \text{and} \quad V_2 = (5, 0).$$
2. **$y$-intercepts:** Set $x = 0$ in the equation:
   $$\frac{0^2}{25} + \frac{y^2}{9} = 1 \implies \frac{y^2}{9} = 1 \implies y^2 = 9 \implies y = \pm 3.$$
   The $y$-intercepts (the minor co-vertices) are:
   $$B_1 = (0, -3) \quad \text{and} \quad B_2 = (0, 3).$$

### Step 3: Foci Calculation
Calculate the focal distance $c$:
$$c = \sqrt{a^2 - b^2} = \sqrt{25 - 9} = \sqrt{16} = 4.$$
The two foci are located along the major axis at:
$$F_1 = (-4, 0) \quad \text{and} \quad F_2 = (4, 0).$$

### Step 4: Explain Along Which Axis the Ellipse Is More Stretched
- The ellipse is **more stretched along the $x$-axis** (horizontally).
- **How this is visible in the equation:**
  1. In the equation $\frac{x^2}{25} + \frac{y^2}{9} = 1$, the sum of two non-negative terms equals $1$:
     $$\frac{x^2}{25} \le 1 \implies x^2 \le 25 \implies -5 \le x \le 5,$$
     $$\frac{y^2}{9} \le 1 \implies y^2 \le 9 \implies -3 \le y \le 3.$$
  2. Because the denominator under $x^2$ ($25$) is larger than the denominator under $y^2$ ($9$), the coordinate $x$ can grow to $\pm 5$ before its contribution reaches $1$, whereas $y$ can only grow to $\pm 3$.
  3. Dividing by a larger number ($25$) "compresses" the effect of larger $x$-values, allowing the curve to span a greater physical width ($10$ units wide) compared to its vertical height ($6$ units tall).

### Step 5: Description for Sketching
- Center the drawing at the origin $(0, 0)$.
- Mark the major vertices at $(-5, 0)$ and $(5, 0)$ on the $x$-axis.
- Mark the minor co-vertices at $(0, -3)$ and $(0, 3)$ on the $y$-axis.
- Mark the foci at $(-4, 0)$ and $(4, 0)$.
- Connect the four vertices with a smooth, continuous convex oval that has horizontal tangents at $(0, \pm 3)$ and vertical tangents at $(\pm 5, 0)$.

---

## 5. Why Each Step Is Valid
1. **Setting a variable to zero** isolates the intersection of the conic section with the orthogonal coordinate axis.
2. **Taking square roots of denominators** extracts the true Euclidean half-lengths of the boundary box.
3. **The bounding inequalities** $|x| \le 5$ and $|y| \le 3$ hold because squares of real numbers are non-negative ($y^2/9 \ge 0 \implies x^2/25 = 1 - y^2/9 \le 1$).

---

## 6. Final Answer in Words
The horizontal semi-major axis has length $a = 5$ and the vertical semi-minor axis has length $b = 3$. The intercepts with the coordinate axes are $(\pm 5, 0)$ on the $x$-axis and $(0, \pm 3)$ on the $y$-axis. The ellipse is more stretched along the $x$-axis because the denominator under $x^2$ is $25 = 5^2$, which is strictly greater than the denominator under $y^2$ ($9 = 3^2$), allowing $x$ to extend over the wider interval $[-5, 5]$ while $y$ is constrained to $[-3, 3]$.

---

## 7. Quick Verification
- **Test arbitrary point on the ellipse:**
  Let $x = 4$.
  $$\frac{4^2}{25} + \frac{y^2}{9} = 1 \implies \frac{16}{25} + \frac{y^2}{9} = 1 \implies \frac{y^2}{9} = 1 - \frac{16}{25} = \frac{9}{25} \implies y^2 = \frac{81}{25} \implies y = \pm \frac{9}{5} = \pm 1.8.$$
  Check sum: $\frac{16}{25} + \frac{81/25}{9} = \frac{16}{25} + \frac{9}{25} = \frac{25}{25} = 1$.
  The point $(4, 1.8)$ lies precisely on the ellipse.
- **Focal property verification:**
  Sum of distances from any point on the ellipse to both foci must equal $2a = 10$.
  For co-vertex $B_2(0, 3)$:
  $$d(B_2, F_1) = \sqrt{(-4 - 0)^2 + (0 - 3)^2} = \sqrt{16 + 9} = 5.$$
  $$d(B_2, F_2) = \sqrt{(4 - 0)^2 + (0 - 3)^2} = \sqrt{16 + 9} = 5.$$
  $$d(B_2, F_1) + d(B_2, F_2) = 5 + 5 = 10 = 2a.$$
  The constant focal sum identity is verified.

---

## 8. Common Mistakes to Avoid
- **Confusing semiaxes with full axes:** Stating that the axes are 5 and 3 (which are the *semi*-axes); the full axis lengths are $2a = 10$ and $2b = 6$.
- **Confusing denominators with semiaxes:** Writing $a = 25$ and $b = 9$ without taking square roots.
- **Wrong focal distance formula:** Using $c = \sqrt{a^2 + b^2}$ (which is the formula for a hyperbola) instead of $c = \sqrt{a^2 - b^2}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
From the denominators of $x^2/25 + y^2/9 = 1$, we take square roots to find the horizontal semi-major axis $a = 5$ and vertical semi-minor axis $b = 3$, giving axial intercepts at $(\pm 5, 0)$ and $(0, \pm 3)$. The ellipse is visibly more stretched along the $x$-axis because the denominator under $x^2$ is larger ($25 > 9$), allowing $x$ to reach $\pm 5$ before the sum exceeds 1. We sketch the ellipse as a horizontal oval spanning from $-5$ to $5$ across the $x$-axis and from $-3$ to $3$ along the $y$-axis, with foci at $(\pm 4, 0)$.

