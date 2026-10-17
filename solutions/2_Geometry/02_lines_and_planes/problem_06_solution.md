# Problem 6 Solution: Angle Between Planes

## 1. Original Problem
Given the equations of two planes in $\mathbb{R}^3$:
$$\Pi_1 : x + y + z = 1, \qquad \Pi_2 : x - y = 2.$$
1. Use the normal vectors of the planes to determine whether the planes are parallel.
2. If they are not parallel, compute the angle between them in radians and degrees.
3. Explain why the normal vectors alone are sufficient to compute the angle between two planes.

---

## 2. What We Are Trying to Find
We need to:
1. Extract the normal vectors $n_1$ and $n_2$ directly from the coefficients of the Cartesian equations.
2. Test for parallelism by checking whether $n_1$ and $n_2$ are scalar multiples of each other.
3. Compute the dot product $n_1 \cdot n_2$ and the vector magnitudes $\|n_1\|$ and $\|n_2\|$.
4. Evaluate $\cos \theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \|n_2\|}$ to determine the dihedral angle $\theta$.
5. Provide the geometric rationale explaining why the angle between the normal lines is identical to the dihedral angle between the planes.

---

## 3. Key Concepts and Theorems
1. **Normal Vectors from General Equations:**
   For a plane $Ax + By + Cz = D$, the vector of coefficients $n = (A, B, C)$ is a normal vector perpendicular to the plane.
2. **Parallelism Criterion for Planes:**
   Two planes $\Pi_1$ and $\Pi_2$ are parallel if and only if their normal vectors are collinear (proportional):
   $$\Pi_1 \parallel \Pi_2 \iff n_1 \parallel n_2 \iff n_1 = k\,n_2 \quad (k \neq 0).$$
3. **Dihedral Angle Between Two Planes:**
   The angle $\theta \in [0, \pi/2]$ between two planes is defined as the acute angle between their normal lines:
   $$\cos \theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \, \|n_2\|}.$$
   (The absolute value ensures that the resulting angle is the conventional acute or right dihedral angle $\theta \in [0^\circ, 90^\circ]$).
4. **Perpendicular Planes:**
   If $n_1 \cdot n_2 = 0$, then $\cos \theta = 0$, which means the planes are orthogonal ($\theta = 90^\circ$).

---

## 4. Detailed Step-by-Step Solution

### Step 1: Extract the Normal Vectors
Read the coefficients of $x, y, z$ from the equations:
- For $\Pi_1 : 1x + 1y + 1z = 1$:
  $$n_1 = (1, 1, 1).$$
- For $\Pi_2 : 1x - 1y + 0z = 2$:
  $$n_2 = (1, -1, 0).$$

### Step 2: Determine Whether the Planes Are Parallel
Test whether $n_1$ is a scalar multiple of $n_2$:
$$(1, 1, 1) = k(1, -1, 0) \implies \begin{cases} 1 = k \\ 1 = -k \\ 1 = 0 \end{cases}$$
The third equation $1 = 0$ is a clear contradiction. Thus, $n_1$ and $n_2$ are not proportional:
$$n_1 \nparallel n_2.$$
Therefore, the planes $\Pi_1$ and $\Pi_2$ are **not parallel**; they intersect along a straight line.

### Step 3: Compute the Dot Product and Lengths
Calculate the dot product of $n_1$ and $n_2$:
$$n_1 \cdot n_2 = (1)(1) + (1)(-1) + (1)(0) = 1 - 1 + 0 = 0.$$
Calculate their Euclidean lengths:
$$\|n_1\| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3},$$
$$\|n_2\| = \sqrt{1^2 + (-1)^2 + 0^2} = \sqrt{1 + 1 + 0} = \sqrt{2}.$$

### Step 4: Compute the Angle $\theta$
Apply the angle formula:
$$\cos \theta = \frac{|n_1 \cdot n_2|}{\|n_1\| \, \|n_2\|} = \frac{|0|}{\sqrt{3} \cdot \sqrt{2}} = \frac{0}{\sqrt{6}} = 0.$$
Inverting the cosine function:
$$\theta = \arccos(0) = \frac{\pi}{2} \text{ radians} = 90^\circ.$$
The two planes are **perpendicular** (orthogonal).

### Step 5: Why Normal Vectors Alone Are Sufficient
- A plane is a flat two-dimensional surface. In three-dimensional space, the orientation of a plane is entirely determined by the unique normal line perpendicular to it.
- If we slice both planes with a perpendicular cross-sectional plane orthogonal to their line of intersection, the dihedral angle between the planes is visible as the angle between the two intersecting lines of the cross-section.
- Because each normal vector is rotated by exactly $90^\circ$ relative to its respective plane within this cross-sectional slice, the angle between the two normal vectors is geometrically identical to the angle between the planes:
  $$\angle(\Pi_1, \Pi_2) = \angle(n_1, n_2).$$
- The position coordinates or constant terms (1 and 2) only describe parallel shifts of the planes in space, which have no effect on their relative angles. Thus, the normal vectors contain all the directional information needed.

---

## 5. Why Each Step Is Valid
1. **Reading coefficients** is valid because $Ax + By + Cz = D$ algebraically encodes $n \cdot X = D$.
2. **The dot product evaluating to 0** strictly implies orthogonality of the two normal vectors.
3. **Rigid rotational invariance** guarantees that rotating two intersecting geometric sheets by $90^\circ$ preserves their relative angle of intersection.

---

## 6. Final Answer in Words
The normal vectors are $n_1 = (1, 1, 1)$ and $n_2 = (1, -1, 0)$. They are not parallel because their coordinates are not proportional. The dot product is $n_1 \cdot n_2 = 1 - 1 + 0 = 0$, giving $\cos \theta = 0$, which means the angle between the planes is $\theta = \frac{\pi}{2}$ radians ($90^\circ$). The planes are perpendicular. Normal vectors alone are sufficient because they uniquely lock in the spatial tilt of each plane, and rotating each plane to its normal line preserves the dihedral angle.

---

## 7. Quick Verification
- **Cross product (direction of line of intersection):**
  $$v_L = n_1 \times n_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 1 \\ 1 & -1 & 0 \end{vmatrix} = \mathbf{i}(1) - \mathbf{j}(-1) + \mathbf{k}(-2) = (1, 1, -2).$$
- Construct in-plane vectors perpendicular to $v_L$:
  - In $\Pi_1$, vector $u_1 = v_L \times n_1 = (1, 1, -2) \times (1, 1, 1) = (3, -3, 0) \sim (1, -1, 0)$.
  - In $\Pi_2$, vector $u_2 = v_L \times n_2 = (1, 1, -2) \times (1, -1, 0) = (-2, -2, -2) \sim (1, 1, 1)$.
  - Check their dot product: $(1, -1, 0) \cdot (1, 1, 1) = 1 - 1 + 0 = 0$.
  The transverse lines inside the two planes are perpendicular, confirming $\theta = 90^\circ$.

---

## 8. Common Mistakes to Avoid
- **Missing the zero $z$-coefficient in $\Pi_2$:** Writing $n_2 = (1, -1, 1)$ or $(1, -1)$ instead of $(1, -1, 0)$.
- **Using the constant terms in the angle formula:** Confusing the right-hand constants (1 and 2) with normal vector components.
- **Forgetting absolute value:** If $n_1 \cdot n_2$ were negative, one must take $|n_1 \cdot n_2|$ to report the acute dihedral angle $\theta \le 90^\circ$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The normal vectors extracted from the plane equations are $n_1 = (1, 1, 1)$ and $n_2 = (1, -1, 0)$, which are clearly not scalar multiples, showing that the planes are not parallel. Taking their dot product gives $(1)(1) + (1)(-1) + (1)(0) = 0$, which immediately proves that the normal vectors—and therefore the planes themselves—are perpendicular at an angle of $90^\circ$. Normal vectors are sufficient on their own because rotating two planes into their respective normal lines preserves the dihedral angle between them while filtering out irrelevant translational shifts.

