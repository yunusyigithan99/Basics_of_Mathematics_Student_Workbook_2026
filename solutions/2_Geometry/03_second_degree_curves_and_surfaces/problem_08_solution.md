# Problem 8 Solution: Sphere by Completing the Square

## 1. Original Problem
Reduce the general second-degree equation in $\mathbb{R}^3$:
$$x^2 + y^2 + z^2 - 4x + 2y - 6z - 2 = 0$$
to canonical form. Find the center $S$ and the radius $R$ of the sphere. Provide the coordinates of two simple points lying on the sphere, and verify both points by substituting them into the equation.

---

## 2. What We Are Trying to Find
We need to:
1. Complete the square independently for each of the three spatial variables $x, y,$ and $z$.
2. Formulate the canonical equation of the sphere $(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = R^2$.
3. Identify the center coordinates $(x_0, y_0, z_0)$ and the radius $R$.
4. Select two points lying on the sphere (such as along an axis passing through the center).
5. Verify both points by direct substitution into both the canonical and general forms.

---

## 3. Key Concepts and Theorems
1. **General Equation of a Sphere:**
   In three-dimensional space, an equation with equal coefficients on $x^2, y^2, z^2$ and no cross terms $xy, yz, zx$:
   $$x^2 + y^2 + z^2 + D x + E y + F z + G = 0$$
   represents a sphere, a single point, or the empty set, depending on the value of $R^2$.
2. **Completing the Square in 3D:**
   $$x^2 - 4x = (x - 2)^2 - 4,$$
   $$y^2 + 2y = (y + 1)^2 - 1,$$
   $$z^2 - 6z = (z - 3)^2 - 9.$$
3. **Canonical Form of a Sphere:**
   $$(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = R^2,$$
   where $(x_0, y_0, z_0)$ is the center in $\mathbb{R}^3$ and $R > 0$ is the geometric radius.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Group Terms by Coordinate Variable
Rearrange the equation and move the constant term $-2$ to the right side:
$$(x^2 - 4x) + (y^2 + 2y) + (z^2 - 6z) = 2.$$

### Step 2: Complete the Squares
Complete the square for each variable:
- For $x$: $x^2 - 4x = (x - 2)^2 - 2^2 = (x - 2)^2 - 4$
- For $y$: $y^2 + 2y = (y + 1)^2 - 1^2 = (y + 1)^2 - 1$
- For $z$: $z^2 - 6z = (z - 3)^2 - 3^2 = (z - 3)^2 - 9$

### Step 3: Substitute and Balance the Equation
Substitute these expressions back into the grouped equation:
$$\big((x - 2)^2 - 4\big) + \big((y + 1)^2 - 1\big) + \big((z - 3)^2 - 9\big) = 2.$$
Combine the negative constants:
$$-4 - 1 - 9 = -14.$$
Add $14$ to both sides of the equation:
$$(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 2 + 14 = 16.$$
Since $16 = 4^2$, the canonical form of the sphere is:
$$(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 4^2.$$

### Step 4: Extract Center and Radius
Comparing with $(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = R^2$:
- **Center:**
  $$S = (x_0, y_0, z_0) = (2, -1, 3)$$
- **Radius:**
  $$R = \sqrt{16} = 4$$

### Step 5: Select Two Points on the Sphere
The simplest points are found by keeping two coordinates equal to the center and varying the third coordinate by $\pm R$:
Let $y = -1$ and $z = 3$:
$$(x - 2)^2 + (-1 + 1)^2 + (3 - 3)^2 = 16 \implies (x - 2)^2 + 0 + 0 = 16 \implies x - 2 = \pm 4.$$
- For $x - 2 = 4 \implies x = 6$, giving point $P_1 = (6, -1, 3)$.
- For $x - 2 = -4 \implies x = -2$, giving point $P_2 = (-2, -1, 3)$.

### Step 6: Verify Both Points in Both Forms
1. **Verification of Point $P_1(6, -1, 3)$:**
   - *Canonical form:*
     $$(6 - 2)^2 + (-1 + 1)^2 + (3 - 3)^2 = 4^2 + 0 + 0 = 16. \quad \text{(Satisfied)}$$
   - *General form:*
     $$6^2 + (-1)^2 + 3^2 - 4(6) + 2(-1) - 6(3) - 2$$
     $$= 36 + 1 + 9 - 24 - 2 - 18 - 2 = 46 - 46 = 0. \quad \text{(Satisfied)}$$

2. **Verification of Point $P_2(-2, -1, 3)$:**
   - *Canonical form:*
     $$(-2 - 2)^2 + (-1 + 1)^2 + (3 - 3)^2 = (-4)^2 + 0 + 0 = 16. \quad \text{(Satisfied)}$$
   - *General form:*
     $$(-2)^2 + (-1)^2 + 3^2 - 4(-2) + 2(-1) - 6(3) - 2$$
     $$= 4 + 1 + 9 + 8 - 2 - 18 - 2 = 22 - 22 = 0. \quad \text{(Satisfied)}$$

Both points satisfy both the canonical form and the original general equation.

---

## 5. Why Each Step Is Valid
1. **Separation of variables** is valid because there are no mixed products ($xy, yz, xz$), allowing independent completion of the square for each coordinate axis.
2. **Balancing the equation** adds the sum of squares $4 + 1 + 9 = 14$ to both sides, maintaining identity.
3. **The 3D Pythagorean distance theorem** proves that the locus of points equidistant ($R = 4$) from $(2, -1, 3)$ forms a sphere.

---

## 6. Final Answer in Words
The canonical form of the sphere is $(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16$. The center of the sphere is $S = (2, -1, 3)$ and its radius is $R = 4$. Two points on the sphere are $P_1 = (6, -1, 3)$ and $P_2 = (-2, -1, 3)$. Substituting these points into the canonical form yields $16 = 16$, and substituting into the original general equation yields $0 = 0$, confirming the solution.

---

## 7. Quick Verification
- **Test vertical poles of the sphere:**
  Keep $x = 2$ and $y = -1$, vary $z = 3 \pm 4$:
  - North Pole: $N = (2, -1, 7)$
    $$2^2 + (-1)^2 + 7^2 - 4(2) + 2(-1) - 6(7) - 2 = 4 + 1 + 49 - 8 - 2 - 42 - 2 = 54 - 54 = 0.$$
  - South Pole: $S_{\text{pole}} = (2, -1, -1)$
    $$2^2 + (-1)^2 + (-1)^2 - 4(2) + 2(-1) - 6(-1) - 2 = 4 + 1 + 1 - 8 - 2 + 6 - 2 = 12 - 12 = 0.$$
  Both vertical poles satisfy the general equation.

---

## 8. Common Mistakes to Avoid
- **Sign errors in center coordinates:** Reading $(x - 2)^2, (y + 1)^2, (z - 3)^2$ as center $(-2, 1, -3)$ instead of $(+2, -1, +3)$.
- **Neglecting to add to the right side:** Forgetting that completing squares adds $4 + 1 + 9 = 14$ to the right side, which would leave $R^2 = 2$ instead of $16$.
- **Arithmetic sign in $(-1)^2$:** Computing $(-1)^2 = -1$ instead of $+1$.

---

## 9. Classroom Presentation (3-Sentence Summary)
We complete the square on all three variables by rewriting $x^2 - 4x$ as $(x - 2)^2 - 4$, $y^2 + 2y$ as $(y + 1)^2 - 1$, and $z^2 - 6z$ as $(z - 3)^2 - 9$. Moving the subtracted numbers to the right side gives the canonical sphere equation $(x - 2)^2 + (y + 1)^2 + (z - 3)^2 = 16$, revealing a center at $(2, -1, 3)$ and a radius of $4$. We verify this result by testing the points $(6, -1, 3)$ and $(-2, -1, 3)$, which lie directly on the sphere's horizontal equator and satisfy both equations.

