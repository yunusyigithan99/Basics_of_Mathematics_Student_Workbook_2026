# Problem 11: Volume of a Solid of Revolution via the Disk Method

## 1. Original Problem
The region under the graph
$$y = \sqrt{x}, \qquad x \in [0, 4],$$
is rotated about the $x$-axis.

1. Construct the integral describing the volume using the disk method.
2. Compute the volume.
3. Explain where the factor $\pi y^2$ in the integral comes from.

---

## 2. What We Are Trying to Find
1. The mathematical formulation of the volume integral for a solid of revolution using the disk method (Cavalieri's principle).
2. The exact analytical calculation of the volume.
3. A clear geometric explanation of the origin of the term $\pi y^2$ in the integrand.

---

## 3. Key Concepts and Theorems
1. **The Disk Method (Rotation about the $x$-axis):**
   When the region under a non-negative continuous curve $y = f(x)$ on $[a, b]$ is rotated $360^\circ$ (full revolution) about the $x$-axis, the volume of the resulting solid is:
   $$V = \int_a^b \pi [f(x)]^2\,dx = \pi \int_a^b y^2\,dx.$$
2. **Infinitesimal Cylindrical Slice (Disk):**
   Each cross-section perpendicular to the $x$-axis is a circular disk with radius $R(x) = y = f(x)$ and infinitesimal thickness $dx$.
   $$\text{Volume of disk: } dV = \text{Area} \times \text{Thickness} = \pi R^2 dx = \pi y^2 dx.$$
3. **Power Rule for Integration:**
   $$\int x\,dx = \frac{x^2}{2} + C.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Explain where the factor $\pi y^2$ in the integral comes from
To understand the origin of the integral formula, consider what happens when a thin vertical strip of width $dx$ at coordinate $x$ is spun around the $x$-axis:
1. **Axis of revolution:** The rotation occurs around the horizontal line $y = 0$ ($x$-axis).
2. **Radius of the slice:** The vertical distance from the rotation axis up to the curve $y = \sqrt{x}$ is the radius of rotation:
   $$R(x) = y - 0 = y.$$
3. **Circular cross-section:** Rotating this vertical line segment of length $y$ through $360^\circ$ sweeps out a full flat circle in the $yz$-plane perpendicular to the $x$-axis.
4. **Area of the circle:** By elementary Euclidean geometry, the area of a circle with radius $r$ is:
   $$\text{Area} = \pi r^2.$$
   Substituting the radius $r = y$ gives the cross-sectional area at position $x$:
   $$A(x) = \pi y^2.$$
5. **Infinitesimal volume element ($dV$):**
   Giving this circular cross-section an infinitesimal thickness $dx$ forms a thin circular cylinder (a "disk" or coin). The volume of a cylinder is base area times height:
   $$dV = A(x) \cdot dx = \pi y^2\,dx.$$

Summing all these infinite parallel disks from $x = a$ to $x = b$ produces the continuous volume integral:
$$V = \int_a^b dV = \int_a^b \pi y^2\,dx.$$

```text
                  y
                2 |                * (4, 2)
                  |              / |
                  |    y = √x   /  |
                  |            /   | Radius = y
        ----------+-----------+----+----> x
                  0           x    4
                  |           |
                  |          ( ) Disk of thickness dx, Radius y, Area = π y^2
                  |           |
```

### Step 2: Construct the integral describing the volume
We are given the curve $y = \sqrt{x}$ on the interval $[0, 4]$.
Substitute $y = \sqrt{x}$ into the disk formula:
$$y^2 = (\sqrt{x})^2 = x.$$
The limits of integration are $x = 0$ to $x = 4$.
Factoring out the constant $\pi$ by linearity:
$$V = \int_0^4 \pi y^2\,dx = \pi \int_0^4 (\sqrt{x})^2\,dx = \pi \int_0^4 x\,dx.$$

### Step 3: Compute the volume
Evaluate the definite integral using the power rule:
$$\int x\,dx = \frac{x^2}{2}.$$
Apply the limits from $x = 0$ to $x = 4$ via the Newton-Leibniz formula:
$$V = \pi \left[\frac{x^2}{2}\right]_0^4 = \pi \left(\frac{4^2}{2} - \frac{0^2}{2}\right) = \pi \left(\frac{16}{2} - 0\right) = 8\pi.$$

Using the numerical approximation $\pi \approx 3.14159$:
$$V = 8\pi \approx 25.1327 \quad \text{cubic units}.$$

---

## 5. Why Each Step Is Valid
- **Step 1:** Cavalieri's principle states that integrating the parallel cross-sectional areas perpendicular to an axis calculates the total 3D volume.
- **Step 2:** The square of the positive square root function $(\sqrt{x})^2$ is $x$ for all $x \ge 0$.
- **Step 3:** The polynomial $x$ is continuous on $[0, 4]$, allowing direct evaluation via standard antiderivatives.

---

## 6. Final Answer in Words
1. The integral describing the volume using the disk method is:
   $$V = \pi \int_0^4 x\,dx.$$
2. The exact volume of the resulting paraboloid of revolution is:
   $$V = 8\pi \approx 25.13\text{ cubic units}.$$
3. The factor $\pi y^2$ represents the geometric surface area of each circular disk cross-section perpendicular to the $x$-axis, where $y = \sqrt{x}$ serves as the radius of the circle ($A = \pi r^2 = \pi y^2$).

---

## 7. Quick Verification
- Paraboloid volume formula:
  The solid of revolution formed by rotating $y = \sqrt{x} \iff x = y^2$ from $y = 0$ to $y = 2$ is a circular paraboloid of base radius $R = 2$ and height $H = 4$.
  The geometric volume of a circular paraboloid is exactly half of its circumscribed cylinder:
  $$V_{\text{paraboloid}} = \frac{1}{2} \pi R^2 H = \frac{1}{2} \pi (2^2) (4) = \frac{1}{2} \pi (4)(4) = 8\pi.$$
This classical geometric theorem confirms our calculus result of $8\pi$ with zero margin of error.

---

## 8. Common Mistakes to Avoid
- **Forgetting to square $y$:** Computing $\pi \int \sqrt{x}\,dx = \pi [\frac{2}{3}x^{3/2}]_0^4 = \frac{16\pi}{3}$, which fails to use the circular area formula $A = \pi r^2$.
- **Omitting the factor $\pi$:** Calculating $\int_0^4 x\,dx = 8$ without multiplying by $\pi$.
- **Confusing with the cylindrical shells method:** The disk method slices perpendicular to the axis of rotation, requiring $dx$ for rotation about the $x$-axis.

---

## 9. Classroom Presentation (3-Sentence Summary)
Rotating the region under $y = \sqrt{x}$ about the $x$-axis creates circular cross-sections whose area is given by $\pi y^2 = \pi (\sqrt{x})^2 = \pi x$. Integrating these circular disks of thickness $dx$ from $x = 0$ to $x = 4$ sets up the volume integral $V = \pi \int_0^4 x\,dx$. Evaluating this integral gives $8\pi$, which perfectly matches the classical geometric formula for a circular paraboloid of height $4$ and radius $2$.
