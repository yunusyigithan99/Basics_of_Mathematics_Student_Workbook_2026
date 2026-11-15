# Problem 14: Center of Mass (Centroid) of a Planar Lamina

*(Workbook Note: The core exercise document intentionally sets 12 cross-sectional exercises. This problem serves as the capstone geometric and physical application covering moments, centroids, and mass distribution to complete the full 15-problem workbook review suite).*

## 1. Original Problem
Find the center of mass (centroid) $(\bar{x}, \bar{y})$ of a thin homogeneous planar plate (lamina of constant density $\rho = 1$) bounded by the parabola
$$y = 4 - x^2$$
and the $x$-axis ($y = 0$).

1. State the symmetry argument that determines $\bar{x}$ immediately without integration.
2. Compute the total mass (area) $M$ of the plate.
3. Compute the first moment of mass about the $x$-axis, $M_x = \frac{1}{2} \int_{-2}^2 y^2\,dx$.
4. Determine the vertical coordinate $\bar{y} = \frac{M_x}{M}$, and explain why $\bar{y} < 2$ (strictly below the vertical midpoint).

---

## 2. What We Are Trying to Find
1. The horizontal balance coordinate $\bar{x}$ using geometric symmetry.
2. The total mass (area) $M = \int y\,dx$ of the parabolic region.
3. The moment of mass $M_x$ about the horizontal axis.
4. The exact vertical centroid coordinate $\bar{y} = M_x / M$.
5. A physical explanation of why mass concentration shifts the center of mass downward below the midpoint height.

---

## 3. Key Concepts and Theorems
1. **Centroid Coordinates of a Homogeneous Lamina:**
   For a region bounded by $y = f(x) \ge 0$ above $[a, b]$ on the $x$-axis:
   - Total Mass (Area):
     $$M = \int_a^b f(x)\,dx.$$
   - Moment about the $y$-axis:
     $$M_y = \int_a^b x f(x)\,dx \implies \bar{x} = \frac{M_y}{M}.$$
   - Moment about the $x$-axis:
     $$M_x = \frac{1}{2} \int_a^b [f(x)]^2\,dx \implies \bar{y} = \frac{M_x}{M}.$$
2. **Symmetry Principle for Centroids:**
   If a homogeneous region has a line of geometric symmetry, its centroid must lie on that line.
3. **Physical Balance Point:**
   The centroid $(\bar{x}, \bar{y})$ is the unique point where the lamina can be perfectly balanced horizontally on the tip of a pencil.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Use symmetry to determine $\bar{x}$
The region is bounded by the parabola $y = 4 - x^2$ and the line $y = 0$.
The intersection points with the $x$-axis are:
$$4 - x^2 = 0 \iff x^2 = 4 \implies x = \pm 2.$$
The domain of the plate is $x \in [-2, 2]$.

Notice that:
$$f(-x) = 4 - (-x)^2 = 4 - x^2 = f(x).$$
The curve is an **even function**, meaning the region is completely symmetric across the vertical $y$-axis ($x = 0$).
Because the plate is homogeneous (uniform mass density everywhere), the center of mass must lie on this line of symmetry. 
Therefore, without any calculation:
$$\bar{x} = 0.$$

*(Analytically: $M_y = \int_{-2}^2 x(4 - x^2)\,dx = 0$ because the integrand is odd over a symmetric interval).*

### Step 2: Compute the total mass (area) $M$
Assuming constant density $\rho = 1$, the mass equals the geometric area:
$$M = \int_{-2}^2 (4 - x^2)\,dx.$$
Using symmetry to integrate over $[0, 2]$ and double the result:
$$M = 2 \int_0^2 (4 - x^2)\,dx = 2 \left[4x - \frac{x^3}{3}\right]_0^2$$
$$= 2 \left[\left(4(2) - \frac{2^3}{3}\right) - 0\right] = 2 \left[8 - \frac{8}{3}\right] = 2 \left[\frac{24 - 8}{3}\right] = 2 \left(\frac{16}{3}\right) = \frac{32}{3}.$$

### Step 3: Compute the first moment about the $x$-axis ($M_x$)
Consider a thin vertical strip of width $dx$ at coordinate $x$:
- Its height is $y = 4 - x^2$.
- Its mass is $dm = y\,dx$.
- The center of mass of this vertical strip is located at its midpoint height: $\tilde{y} = \frac{y}{2}$.
- The moment of this strip about the $x$-axis is:
  $$dM_x = \tilde{y} \cdot dm = \left(\frac{y}{2}\right)(y\,dx) = \frac{1}{2}y^2\,dx.$$

Integrating across the entire plate from $x = -2$ to $x = 2$:
$$M_x = \frac{1}{2} \int_{-2}^2 (4 - x^2)^2\,dx.$$
Expand the integrand:
$$(4 - x^2)^2 = 16 - 8x^2 + x^4.$$
Because the integrand is even, we double the integral over $[0, 2]$, canceling the factor of $\frac{1}{2}$:
$$M_x = \int_0^2 (16 - 8x^2 + x^4)\,dx.$$
Evaluate the antiderivative:
$$M_x = \left[16x - \frac{8x^3}{3} + \frac{x^5}{5}\right]_0^2$$
$$= \left(16(2) - \frac{8(8)}{3} + \frac{32}{5}\right) - 0$$
$$= 32 - \frac{64}{3} + \frac{32}{5}.$$
Factor out $32$:
$$M_x = 32 \left(1 - \frac{2}{3} + \frac{1}{5}\right) = 32 \left(\frac{15 - 10 + 3}{15}\right) = 32 \left(\frac{8}{15}\right) = \frac{256}{15}.$$

### Step 4: Determine the vertical centroid coordinate $\bar{y}$
The vertical coordinate is the ratio of the moment to the total mass:
$$\bar{y} = \frac{M_x}{M} = \frac{\frac{256}{15}}{\frac{32}{3}} = \frac{256}{15} \cdot \frac{3}{32}.$$
Simplifying the fractions:
$$\frac{256}{32} = 8, \qquad \frac{3}{15} = \frac{1}{5}.$$
Therefore:
$$\bar{y} = 8 \cdot \frac{1}{5} = \frac{8}{5} = 1.6.$$

The center of mass of the lamina is:
$$(\bar{x}, \bar{y}) = (0, 1.6) = \left(0, \frac{8}{5}\right).$$

### Step 5: Explain why $\bar{y} < 2$ (below the vertical midpoint)
The maximum height of the parabolic plate occurs at its vertex $(0, 4)$, so the vertical range is $[0, 4]$.
The geometric midpoint of this height is:
$$y_{\text{mid}} = \frac{0 + 4}{2} = 2.$$
However, the calculated centroid height is $\bar{y} = 1.6 < 2$.

**Physical Explanation:**
The shape of the parabola $y = 4 - x^2$ is wide at the base and tapers toward the top:
- At the bottom ($y = 0$), the width is $4$ (from $x = -2$ to $x = 2$).
- At the midpoint ($y = 2$), the width shrinks to $2\sqrt{2} \approx 2.83$.
- Near the top ($y = 4$), the width shrinks to zero.
Because the lower half of the plate ($y \in [0, 2]$) contains much more surface area and mass than the narrow upper half ($y \in [2, 4]$), the distribution of mass is heavily bottom-weighted. The center of mass is gravitationally pulled downward toward the heavier base, positioning the balance point at $y = 1.6$, well below the midpoint height of $2$.

```text
                  y
                4 |           *(0, 4) Vertex
                  |          / \
                2 + - - - - * - * - - - + y = 2 (Geometric Midpoint)
              1.6 |.......( 0, 1.6 )....| Centroid (Balance Point)
                  |       /     \       |
        ----------+------*-------*------+----> x
                 -2      0       2
                     <------4------>
                      Base Width = 4
```

---

## 5. Why Each Step Is Valid
- **Step 1:** The line of symmetry of a homogeneous plate contains the center of mass by definition of balance.
- **Step 2:** The area between a continuous non-negative curve and the $x$-axis is computed via standard definite integration.
- **Step 3:** The moment formula averages the vertical position of each vertical rectangular slice at height $y/2$.
- **Step 4:** The centroid is the center of mass $(\bar{x}, \bar{y}) = (M_y/M, M_x/M)$.
- **Step 5:** Centroids always bias toward regions of greater width/area.

---

## 6. Final Answer in Words
The center of mass (centroid) of the parabolic lamina is:
$$(\bar{x}, \bar{y}) = \left(0, \frac{8}{5}\right) = (0, 1.6).$$
The horizontal coordinate $\bar{x} = 0$ is determined by the even symmetry of $y = 4 - x^2$ about the $y$-axis. 
The total mass of the plate is $M = \frac{32}{3}$, and the moment about the $x$-axis is $M_x = \frac{256}{15}$. 
The vertical balance height is $\bar{y} = 1.6$, which is strictly less than the midpoint height of $2$ because the parabola is widest at its base ($4$ units wide) and tapers to a point at the top, concentrating the majority of the plate's mass in the lower portion.

---

## 7. Quick Verification
- Check area of lower half ($y \in [0, 2]$):
  Lower region area $\approx 7.22$ out of $10.67$ total mass ($\approx 67.7\%$ of mass is below $y = 2$).
  Because over two-thirds of the mass is below $y = 2$, the balance point MUST lie below $y = 2$.
  A balance point at $y = 1.6$ is fully consistent with this distribution.

---

## 8. Common Mistakes to Avoid
- **Forgetting the factor $\frac{1}{2}$ in the moment $M_x$:** Writing $M_x = \int y^2\,dx$, which gives twice the true moment and yields an impossible $\bar{y} = 3.2$.
- **Integrating $x^2$ instead of $y^2$ for $M_x$:** Confusing the moment about the $x$-axis ($M_x \propto y^2$) with the moment about the $y$-axis ($M_y \propto x y$).
- **Calculating $\bar{x}$ unnecessarily:** Wasting time integrating an odd function that vanishes by symmetry.

---

## 9. Classroom Presentation (3-Sentence Summary)
By symmetry across the $y$-axis, the horizontal center of mass of the parabolic plate $y = 4 - x^2$ is immediately $\bar{x} = 0$. Integrating the area gives a total mass of $32/3$, while the moment about the $x$-axis evaluates to $M_x = \frac{1}{2}\int_{-2}^2 (4 - x^2)^2\,dx = 256/15$. Dividing the moment by the mass yields $\bar{y} = 8/5 = 1.6$, which lies strictly below the vertical midpoint of $2$ because the parabola's wide base concentrates most of the plate's mass near the bottom.
