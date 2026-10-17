# Problem 10 Solution: Triangle Area from Vectors

## 1. Original Problem
The points
$$A = (0, 0, 0), \qquad B = (2, 1, 0), \qquad C = (1, 3, 2)$$
form a triangle in $\mathbb{R}^3$.
1. Construct the displacement vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
2. Compute the area of the parallelogram spanned by these two vectors using the cross product.
3. Find the area of triangle $ABC$.
4. Explain the geometric reason for the factor $\frac{1}{2}$ in the triangle area formula.

---

## 2. What We Are Trying to Find
We need to:
1. Determine the vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ by subtracting point coordinates.
2. Calculate the cross product $\overrightarrow{AB} \times \overrightarrow{AC}$.
3. Calculate the magnitude (length) of this cross product, which gives the parallelogram area.
4. Halve the parallelogram area to obtain the triangle area.
5. Explain geometrically why the triangle's area is exactly half of the parallelogram's area.

---

## 3. Key Concepts and Theorems
1. **Geometric Magnitude of the Cross Product:**
   For any two vectors $u$ and $v$ in $\mathbb{R}^3$, the norm of their cross product equals:
   $$\|u \times v\| = \|u\| \, \|v\| \sin \theta,$$
   where $\theta$ is the angle between $u$ and $v$.
   In elementary geometry, a parallelogram with adjacent side lengths $\|u\|$ and $\|v\|$ and included angle $\theta$ has height $h = \|v\| \sin \theta$, giving:
   $$\text{Area}_{\text{parallelogram}} = \text{base} \times \text{height} = \|u\| \, (\|v\| \sin \theta) = \|u \times v\|.$$
2. **Area of a Triangle Spanned by Two Vectors:**
   A triangle with vertices $A, B, C$ is formed by two adjacent vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$. Its area is given by:
   $$\text{Area}_{\triangle ABC} = \frac{1}{2} \|\overrightarrow{AB} \times \overrightarrow{AC}\|.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Construct the Vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$
Subtract the coordinates of vertex $A(0, 0, 0)$ from $B(2, 1, 0)$ and $C(1, 3, 2)$:
$$\overrightarrow{AB} = B - A = (2 - 0, \; 1 - 0, \; 0 - 0) = (2, 1, 0),$$
$$\overrightarrow{AC} = C - A = (1 - 0, \; 3 - 0, \; 2 - 0) = (1, 3, 2).$$

### Step 2: Compute the Cross Product $\overrightarrow{AB} \times \overrightarrow{AC}$
Set up the $3 \times 3$ determinant:
$$\overrightarrow{AB} \times \overrightarrow{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & 1 & 0 \\ 1 & 3 & 2 \end{vmatrix}.$$
Expand by minors along the first row:
$$\overrightarrow{AB} \times \overrightarrow{AC} = \mathbf{i} \begin{vmatrix} 1 & 0 \\ 3 & 2 \end{vmatrix} - \mathbf{j} \begin{vmatrix} 2 & 0 \\ 1 & 2 \end{vmatrix} + \mathbf{k} \begin{vmatrix} 2 & 1 \\ 1 & 3 \end{vmatrix}.$$
Calculate the $2 \times 2$ determinants:
- $\mathbf{i}$-term: $(1)(2) - (0)(3) = 2 - 0 = 2$
- $\mathbf{j}$-term: $-\big((2)(2) - (0)(1)\big) = -(4 - 0) = -4$
- $\mathbf{k}$-term: $(2)(3) - (1)(1) = 6 - 1 = 5$

Thus, the cross product vector is:
$$\overrightarrow{AB} \times \overrightarrow{AC} = (2, -4, 5).$$

### Step 3: Compute the Parallelogram Area
The area of the parallelogram spanned by $\overrightarrow{AB}$ and $\overrightarrow{AC}$ is the Euclidean length of the cross product:
$$\text{Area}_{\text{parallelogram}} = \|\overrightarrow{AB} \times \overrightarrow{AC}\| = \sqrt{2^2 + (-4)^2 + 5^2} = \sqrt{4 + 16 + 25} = \sqrt{45}.$$
Simplifying the radical:
$$\sqrt{45} = \sqrt{9 \times 5} = 3\sqrt{5} \approx 6.708.$$

### Step 4: Compute the Triangle Area
The area of triangle $ABC$ is half the parallelogram area:
$$\text{Area}_{\triangle ABC} = \frac{1}{2} \|\overrightarrow{AB} \times \overrightarrow{AC}\| = \frac{3\sqrt{5}}{2} = \frac{\sqrt{45}}{2} \approx 3.354.$$

### Step 5: Explain the Factor $\frac{1}{2}$
- The vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ define two adjacent sides of a parallelogram with fourth vertex $D = A + \overrightarrow{AB} + \overrightarrow{AC} = B + \overrightarrow{AC}$.
- The line segment $BC$ is a diagonal connecting opposite vertices of this parallelogram.
- Any diagonal of a parallelogram divides it into two congruent triangles ($\triangle ABC \cong \triangle DCB$) having the identical base length and the identical perpendicular height.
- Because the total area of the parallelogram is shared equally between these two non-overlapping congruent triangles, the area of triangle $ABC$ must be precisely $\frac{1}{2}$ of the parallelogram's area.

---

## 5. Why Each Step Is Valid
1. **Constructing vectors relative to the origin** preserves the geometric distances and angles of the points in 3D Cartesian coordinates.
2. **The cross product length identity** $\|u \times v\| = \|u\|\|v\|\sin\theta$ is a geometric theorem equivalent to the standard base $\times$ height formula.
3. **Halving the area** is valid by Euclidean congruence of the two triangles formed by the diagonal.

---

## 6. Final Answer in Words
The displacement vectors are $\overrightarrow{AB} = (2, 1, 0)$ and $\overrightarrow{AC} = (1, 3, 2)$. Their cross product is $\overrightarrow{AB} \times \overrightarrow{AC} = (2, -4, 5)$. The area of the parallelogram spanned by these vectors is $\|\overrightarrow{AB} \times \overrightarrow{AC}\| = \sqrt{45} = 3\sqrt{5}$. The area of triangle $ABC$ is $\frac{3\sqrt{5}}{2}$ (or approximately $3.354$). The factor of $\frac{1}{2}$ appears because the diagonal of the parallelogram splits it into two congruent triangles of equal area.

---

## 7. Quick Verification
- Check orthogonality of normal vector $n = (2, -4, 5)$:
  $$n \cdot \overrightarrow{AB} = 2(2) + (-4)(1) + 5(0) = 4 - 4 + 0 = 0,$$
  $$n \cdot \overrightarrow{AC} = 2(1) + (-4)(3) + 5(2) = 2 - 12 + 10 = 0.$$
- Check via side lengths and Heron's formula / cosine rule:
  $$\|\overrightarrow{AB}\| = \sqrt{4 + 1 + 0} = \sqrt{5}, \quad \|\overrightarrow{AC}\| = \sqrt{1 + 9 + 4} = \sqrt{14}.$$
  $$\overrightarrow{AB} \cdot \overrightarrow{AC} = 2(1) + 1(3) + 0(2) = 5.$$
  By Lagrange's identity:
  $$\|\overrightarrow{AB} \times \overrightarrow{AC}\|^2 = \|\overrightarrow{AB}\|^2 \|\overrightarrow{AC}\|^2 - (\overrightarrow{AB} \cdot \overrightarrow{AC})^2 = 5 \times 14 - 5^2 = 70 - 25 = 45.$$
  Thus $\|\overrightarrow{AB} \times \overrightarrow{AC}\| = \sqrt{45}$, perfectly verifying the calculation!

---

## 8. Common Mistakes to Avoid
- **Forgetting to halve the parallelogram area:** Giving $\sqrt{45}$ as the triangle area instead of $\frac{\sqrt{45}}{2}$.
- **Minor sign error in the $\mathbf{j}$ cofactor:** Computing $-(4 - 0) = -4$ incorrectly as $+4$.
- **Using point coordinates instead of displacement vectors:** Attempting to cross $B \times C$ without subtracting vertex $A$ (though in this case $A$ is $(0,0,0)$, for any other point $A$ this would cause severe errors).

---

## 9. Classroom Presentation (3-Sentence Summary)
We construct vectors $\overrightarrow{AB} = (2, 1, 0)$ and $\overrightarrow{AC} = (1, 3, 2)$ from vertex $A$ and compute their cross product, which equals $(2, -4, 5)$. The magnitude of this cross product is $\sqrt{2^2 + (-4)^2 + 5^2} = \sqrt{45} = 3\sqrt{5}$, representing the area of the full parallelogram spanned by the two vectors. Halving this result gives the triangle's area as $3\sqrt{5}/2$, because the diagonal of any parallelogram divides it into two congruent triangles.

