# Problem 12 Solution: A Normal Vector to a Plane

## 1. Original Problem
Given the three non-collinear points in $\mathbb{R}^3$:
$$A = (1, 0, 2), \qquad B = (2, 1, 0), \qquad C = (0, 3, 1).$$
1. Construct two vectors lying in the plane containing these three points.
2. Find a non-zero vector perpendicular to both of these vectors.
3. Check the perpendicularity using dot products.

---

## 2. What We Are Trying to Find
We need to:
1. Find two direction vectors spanning the plane by subtracting point coordinates (e.g., $\overrightarrow{AB}$ and $\overrightarrow{AC}$).
2. Compute their vector cross product to generate a normal vector $n$ that is orthogonal to the plane.
3. Verify that $n$ is orthogonal to both direction vectors by calculating their dot products and showing they equal zero.

---

## 3. Key Concepts and Theorems
1. **Vectors Lying in a Plane:**
   Any two non-parallel displacement vectors formed by three distinct points in a plane, such as $\overrightarrow{AB} = B - A$ and $\overrightarrow{AC} = C - A$, lie entirely within that plane.
2. **Normal Vector via Cross Product:**
   In three-dimensional space, the cross product of two non-parallel vectors in a plane produces a vector $n = u \times v$ that is simultaneously perpendicular to both vectors, and therefore perpendicular to the entire plane:
   $$n \perp u \quad \text{and} \quad n \perp v.$$
3. **Orthogonality Check:**
   Two vectors $n$ and $v$ are perpendicular if and only if their scalar product is zero:
   $$n \cdot v = 0.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Construct Two Vectors Lying in the Plane
Choose $A$ as the reference base point and construct displacement vectors to $B$ and $C$:
$$\overrightarrow{AB} = B - A = (2 - 1, \; 1 - 0, \; 0 - 2) = (1, 1, -2),$$
$$\overrightarrow{AC} = C - A = (0 - 1, \; 3 - 0, \; 1 - 2) = (-1, 3, -1).$$
Both vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ lie in the plane determined by $A, B,$ and $C$.

### Step 2: Find a Vector Perpendicular to Both (Normal Vector $n$)
Compute the cross product $n = \overrightarrow{AB} \times \overrightarrow{AC}$ using the determinant formulation:
$$n = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & -2 \\ -1 & 3 & -1 \end{vmatrix}.$$
Expand along the first row:
$$n = \mathbf{i} \begin{vmatrix} 1 & -2 \\ 3 & -1 \end{vmatrix} - \mathbf{j} \begin{vmatrix} 1 & -2 \\ -1 & -1 \end{vmatrix} + \mathbf{k} \begin{vmatrix} 1 & 1 \\ -1 & 3 \end{vmatrix}.$$
Compute the $2 \times 2$ determinants:
- $\mathbf{i}$-component: $(1)(-1) - (-2)(3) = -1 - (-6) = -1 + 6 = 5$
- $\mathbf{j}$-component: $-\big((1)(-1) - (-2)(-1)\big) = -(-1 - 2) = -(-3) = 3$
- $\mathbf{k}$-component: $(1)(3) - (1)(-1) = 3 - (-1) = 3 + 1 = 4$

Thus, a perpendicular vector is:
$$n = (5, 3, 4).$$

### Step 3: Check Perpendicularity Using Dot Products
Check orthogonality with $\overrightarrow{AB} = (1, 1, -2)$:
$$n \cdot \overrightarrow{AB} = (5)(1) + (3)(1) + (4)(-2) = 5 + 3 - 8 = 0.$$
Check orthogonality with $\overrightarrow{AC} = (-1, 3, -1)$:
$$n \cdot \overrightarrow{AC} = (5)(-1) + (3)(3) + (4)(-1) = -5 + 9 - 4 = 0.$$
Both dot products are zero, which confirms that $n = (5, 3, 4)$ is perpendicular to both spanning vectors.

---

## 5. Why Each Step Is Valid
1. **Subtracting point coordinates** yields valid displacement vectors whose line segments join the vertices within the plane.
2. **The cross product** is guaranteed by vector algebra to produce an orthogonal vector to its inputs whenever the inputs are non-collinear (which they are, since their components are not proportional: $1/(-1) \neq 1/3$).
3. **Checking $n \cdot \overrightarrow{AB} = 0$ and $n \cdot \overrightarrow{AC} = 0$** directly proves perpendicularity by the definition of the inner product in $\mathbb{R}^3$.

---

## 6. Final Answer in Words
Two vectors lying in the plane are $\overrightarrow{AB} = (1, 1, -2)$ and $\overrightarrow{AC} = (-1, 3, -1)$. A vector perpendicular to both is the cross product $n = (5, 3, 4)$ (or any non-zero scalar multiple thereof). The perpendicularity checks give $n \cdot \overrightarrow{AB} = 5 + 3 - 8 = 0$ and $n \cdot \overrightarrow{AC} = -5 + 9 - 4 = 0$, confirming that $n$ is a normal vector to the plane.

---

## 7. Quick Verification
- **Third in-plane vector check:**
  Construct $\overrightarrow{BC} = C - B = (0 - 2, 3 - 1, 1 - 0) = (-2, 2, 1)$.
  Since $\overrightarrow{BC} = \overrightarrow{AC} - \overrightarrow{AB}$, $n$ must also be perpendicular to $\overrightarrow{BC}$:
  $$n \cdot \overrightarrow{BC} = (5)(-2) + (3)(2) + (4)(1) = -10 + 6 + 4 = 0.$$
  The normal vector is perpendicular to every vector in the plane.

---

## 8. Common Mistakes to Avoid
- **Sign confusion in determinants:** Double negatives in $(1)(-1) - (-2)(3) = -1 + 6 = 5$.
- **Middle minor sign:** The $\mathbf{j}$ cofactor has a built-in negative sign: $-(-1 - 2) = -(-3) = +3$. Forgetting this produces $-3$ instead of $+3$.
- **Believing the normal vector is unique:** Any non-zero scalar multiple $k\,n = (5k, 3k, 4k)$ for $k \neq 0$ is also a valid normal vector.

---

## 9. Classroom Presentation (3-Sentence Summary)
By subtracting point coordinates from base point $A$, we obtain two vectors lying in the plane: $\overrightarrow{AB} = (1, 1, -2)$ and $\overrightarrow{AC} = (-1, 3, -1)$. Taking their cross product gives the normal vector $n = (5, 3, 4)$, which is perpendicular to the plane. We verify this by computing the dot products with both spanning vectors, each of which evaluates to zero, confirming true orthogonality.

