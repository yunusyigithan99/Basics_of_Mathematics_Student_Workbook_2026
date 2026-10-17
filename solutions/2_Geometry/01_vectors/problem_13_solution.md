# Problem 13 Solution: Do Four Points Lie in One Plane?

## 1. Original Problem
Given the four points in $\mathbb{R}^3$:
$$A = (0, 0, 0), \qquad B = (1, 2, 0), \qquad C = (0, 1, 1), \qquad D = (2, 5, 1).$$

1. Construct the displacement vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
2. Find the normal vector $n = \overrightarrow{AB} \times \overrightarrow{AC}$.
3. Construct $\overrightarrow{AD}$ and check whether the dot product $\overrightarrow{AD} \cdot n = 0$.
4. Based on this result, decide whether point $D$ lies in the plane determined by $A, B,$ and $C$, and justify the criterion.

---

## 2. What We Are Trying to Find
We need to:
1. Determine the vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ defining the plane $ABC$.
2. Compute the cross product $n = \overrightarrow{AB} \times \overrightarrow{AC}$ to find a vector perpendicular to the plane.
3. Construct the vector $\overrightarrow{AD}$ connecting base point $A$ to the fourth point $D$.
4. Calculate the scalar triple product $\overrightarrow{AD} \cdot n$.
5. Conclude whether $D$ is coplanar with $A, B, C$, and explain the underlying geometric theory.

---

## 3. Key Concepts and Theorems
1. **Normal Vector to a Plane:**
   Any plane in $\mathbb{R}^3$ passing through a point $A$ is uniquely characterized by an orthogonal normal vector $n$. A point $P$ lies on the plane if and only if the displacement vector $\overrightarrow{AP}$ is perpendicular to $n$:
   $$P \in \text{Plane}(A, n) \iff \overrightarrow{AP} \cdot n = 0.$$
2. **Coplanarity Criterion (Scalar Triple Product):**
   Three vectors $u, v, w$ are coplanar (lie in the same plane) if and only if their scalar triple product is zero:
   $$(u \times v) \cdot w = 0.$$
   Geometrically, the absolute value of the scalar triple product $|(u \times v) \cdot w|$ represents the volume of the 3D parallelepiped spanned by the three vectors. If this volume is $0$, the parallelepiped is completely flat, meaning all three vectors—and therefore the four points defining them—lie in a single common plane.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$
Subtract the coordinates of origin $A(0, 0, 0)$ from $B$ and $C$:
$$\overrightarrow{AB} = B - A = (1 - 0, \; 2 - 0, \; 0 - 0) = (1, 2, 0),$$
$$\overrightarrow{AC} = C - A = (0 - 0, \; 1 - 0, \; 1 - 0) = (0, 1, 1).$$

### Step 2: Compute $n = \overrightarrow{AB} \times \overrightarrow{AC}$
Evaluate the determinant cross product:
$$n = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 0 \\ 0 & 1 & 1 \end{vmatrix}.$$
Expand along the first row:
$$n = \mathbf{i} \begin{vmatrix} 2 & 0 \\ 1 & 1 \end{vmatrix} - \mathbf{j} \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} + \mathbf{k} \begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix}.$$
Compute the $2 \times 2$ determinants:
- $\mathbf{i}$-term: $(2)(1) - (0)(1) = 2$
- $\mathbf{j}$-term: $-\big((1)(1) - (0)(0)\big) = -1$
- $\mathbf{k}$-term: $(1)(1) - (2)(0) = 1$

Thus, the normal vector to the plane is:
$$n = (2, -1, 1).$$

### Step 3: Construct $\overrightarrow{AD}$ and Check $\overrightarrow{AD} \cdot n = 0$
Construct the displacement vector to point $D(2, 5, 1)$:
$$\overrightarrow{AD} = D - A = (2 - 0, \; 5 - 0, \; 1 - 0) = (2, 5, 1).$$
Now evaluate the dot product of $\overrightarrow{AD}$ with the normal vector $n = (2, -1, 1)$:
$$\overrightarrow{AD} \cdot n = (2)(2) + (5)(-1) + (1)(1) = 4 - 5 + 1 = 0.$$
The dot product is exactly zero.

### Step 4: Decision and Justification of the Criterion
- **Decision:** Yes, point $D$ lies in the plane determined by $A, B,$ and $C$. All four points $A, B, C, D$ are **coplanar**.
- **Justification:**
  1. The normal vector $n = \overrightarrow{AB} \times \overrightarrow{AC}$ is, by construction, perpendicular to the plane formed by $A, B,$ and $C$.
  2. Any displacement vector starting at $A$ and ending at a point in the plane must lie flat in the plane, and therefore must be perpendicular to the plane's normal vector $n$.
  3. Since $\overrightarrow{AD} \cdot n = 0$, the vector $\overrightarrow{AD}$ has zero projection along the normal direction, meaning point $D$ does not deviate out of the plane.
  4. Alternatively, the scalar triple product $(\overrightarrow{AB} \times \overrightarrow{AC}) \cdot \overrightarrow{AD} = 0$ proves that the volume of the parallelepiped formed by these three vectors is $0$, which only occurs when all three vectors lie in the same 2D plane.

---

## 5. Why Each Step Is Valid
1. **The vector $n$** is perpendicular to every linear combination of $\overrightarrow{AB}$ and $\overrightarrow{AC}$ by the distributive property of dot and cross products.
2. **Evaluating $\overrightarrow{AD} \cdot n = 0$** directly tests whether $\overrightarrow{AD}$ can be represented as a linear combination of $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
3. **The geometric criterion** is exact and avoids needing to write out full parametric coordinate equations.

---

## 6. Final Answer in Words
The displacement vectors are $\overrightarrow{AB} = (1, 2, 0)$ and $\overrightarrow{AC} = (0, 1, 1)$. Their cross product yields the normal vector $n = (2, -1, 1)$. The displacement vector to the fourth point is $\overrightarrow{AD} = (2, 5, 1)$. The dot product evaluates to $\overrightarrow{AD} \cdot n = 4 - 5 + 1 = 0$. Therefore, point $D$ lies entirely within the plane determined by $A, B,$ and $C$, proving that all four points are coplanar.

---

## 7. Quick Verification
- **Express $\overrightarrow{AD}$ directly as a linear combination:**
  We check if $\overrightarrow{AD} = c_1 \overrightarrow{AB} + c_2 \overrightarrow{AC}$:
  $$(2, 5, 1) = c_1 (1, 2, 0) + c_2 (0, 1, 1).$$
  From the $x$-component: $c_1 = 2$.
  From the $z$-component: $c_2 = 1$.
  Check the $y$-component: $2(2) + 1(1) = 4 + 1 = 5$.
  This matches the $y$-coordinate of $\overrightarrow{AD}$ perfectly!
  Since $\overrightarrow{AD} = 2\overrightarrow{AB} + \overrightarrow{AC}$, $\overrightarrow{AD}$ lies strictly in the plane of $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
- **Determinant Check:**
  $$\det \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 2 & 5 & 1 \end{pmatrix} = 1(1 - 5) - 2(0 - 2) + 0 = -4 + 4 = 0.$$
  The volume is strictly zero.

---

## 8. Common Mistakes to Avoid
- **Confusing $\overrightarrow{AD}$ with point coordinates:** In this problem $A = (0, 0, 0)$, so point coordinates match vector components. But if $A \neq (0, 0, 0)$, failing to subtract $A$ would give the wrong vector.
- **Arithmetic sign in dot product:** Computing $5 \times (-1) = +5$ instead of $-5$, which would give $4 + 5 + 1 = 10 \neq 0$ and lead to the false conclusion that the points are not coplanar.
- **Thinking four random points are usually coplanar:** Four points in general 3D space span a non-zero volume; coplanarity is a special geometric condition requiring the scalar triple product to be zero.

---

## 9. Classroom Presentation (3-Sentence Summary)
We find the normal vector to the plane formed by $A$, $B$, and $C$ by computing the cross product $\overrightarrow{AB} \times \overrightarrow{AC} = (2, -1, 1)$. Next, we take the dot product of this normal vector with the displacement vector $\overrightarrow{AD} = (2, 5, 1)$, which evaluates to $4 - 5 + 1 = 0$. Because the dot product is zero, $\overrightarrow{AD}$ has no component perpendicular to the plane, rigorously proving that all four points lie in the exact same plane.

