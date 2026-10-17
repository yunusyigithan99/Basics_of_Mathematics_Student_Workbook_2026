# Problem 11 Solution: Plane Containing a Line and a Point

## 1. Original Problem
Find the Cartesian equation of the plane containing the line
$$L : (x, y, z) = (1, 0, 2) + t(1, 1, -1), \quad t \in \mathbb{R}$$
and the external point
$$P = (0, 2, 1).$$
Check that both the entire line $L$ and the point $P$ lie in the plane you obtain.

---

## 2. What We Are Trying to Find
We need to:
1. Verify that point $P$ does not lie on line $L$ (confirming the problem uniquely determines a single plane).
2. Construct two non-collinear spanning vectors lying inside the plane: the line's direction vector $v$ and the displacement vector connecting the line's base point $P_0$ to $P$.
3. Compute the normal vector $n = v \times \overrightarrow{P_0 P}$.
4. Derive the Cartesian equation of the plane $Ax + By + Cz = D$.
5. Verify that point $P$ satisfies the plane equation.
6. Verify that the line's parametric formula satisfies the plane equation identically for all $t \in \mathbb{R}$.

---

## 3. Key Concepts and Theorems
1. **Geometric Determination of a Plane by a Line and a Point:**
   A line $L$ and a point $P \notin L$ uniquely define a plane in $\mathbb{R}^3$.
2. **Two In-Plane Spanning Vectors:**
   - The direction vector of the line: $v_1 = v$.
   - The displacement vector from any base point $P_0 \in L$ to $P$: $v_2 = P - P_0$.
   Since $P \notin L$, $v_1$ and $v_2$ are linearly independent.
3. **Normal Vector via Cross Product:**
   $$n = v_1 \times v_2.$$
4. **Condition for an Entire Line to Lie in a Plane:**
   A line $L(t) = P_0 + t\,v$ lies entirely within a plane $\Pi : n \cdot X = d$ if and only if:
   - Its direction is parallel to the plane: $v \cdot n = 0$, and
   - At least one point on the line belongs to the plane: $n \cdot P_0 = d$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify Given Elements and Check Point $P$
From the parametric equation of line $L$:
- Base point: $P_0 = (1, 0, 2)$
- Direction vector: $v = (1, 1, -1)$
- External point: $P = (0, 2, 1)$

Check if $P$ is on $L$:
$$0 = 1 + t \implies t = -1.$$
Checking $y$: $y = 0 + (-1)(1) = -1 \neq 2$.
Since $P$ does not satisfy the line equations, $P \notin L$. The plane is uniquely determined.

### Step 2: Construct Two Spanning Vectors in the Plane
1. First vector (along the line):
   $$v_1 = v = (1, 1, -1).$$
2. Second vector (connecting $P_0$ on the line to $P$):
   $$v_2 = \overrightarrow{P_0 P} = P - P_0 = (0 - 1, \; 2 - 0, \; 1 - 2) = (-1, 2, -1).$$

### Step 3: Compute the Normal Vector via Cross Product
Evaluate $n = v_1 \times v_2$:
$$n = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & -1 \\ -1 & 2 & -1 \end{vmatrix}.$$
Expand along the first row:
$$n = \mathbf{i} \begin{vmatrix} 1 & -1 \\ 2 & -1 \end{vmatrix} - \mathbf{j} \begin{vmatrix} 1 & -1 \\ -1 & -1 \end{vmatrix} + \mathbf{k} \begin{vmatrix} 1 & 1 \\ -1 & 2 \end{vmatrix}.$$
Calculate the $2 \times 2$ determinants:
- $\mathbf{i}$-term: $(1)(-1) - (-1)(2) = -1 + 2 = 1$
- $\mathbf{j}$-term: $-\big((1)(-1) - (-1)(-1)\big) = -(-1 - 1) = -(-2) = 2$
- $\mathbf{k}$-term: $(1)(2) - (1)(-1) = 2 - (-1) = 2 + 1 = 3$

Thus, the normal vector is:
$$n = (1, 2, 3).$$

### Step 4: Write the Equation of the Plane
Using normal vector $n = (1, 2, 3)$ and base point $P_0(1, 0, 2)$:
$$1(x - 1) + 2(y - 0) + 3(z - 2) = 0$$
$$(x - 1) + 2y + (3z - 6) = 0$$
$$x + 2y + 3z - 7 = 0 \quad (\text{or } x + 2y + 3z = 7).$$

### Step 5: Check That Point $P$ Lies in the Plane
Substitute $P(0, 2, 1)$ into $x + 2y + 3z = 7$:
$$\text{LHS} = 0 + 2(2) + 3(1) = 0 + 4 + 3 = 7 = \text{RHS}.$$
Point $P$ satisfies the plane equation.

### Step 6: Check That the Entire Line Lies in the Plane
Substitute the parametric coordinates $x(t) = 1 + t, y(t) = t, z(t) = 2 - t$ into $x + 2y + 3z = 7$:
$$\text{LHS} = (1 + t) + 2(t) + 3(2 - t) = 1 + t + 2t + 6 - 3t.$$
Group constant terms and $t$ terms:
$$\text{LHS} = (1 + 6) + (1 + 2 - 3)t = 7 + 0t = 7 = \text{RHS}.$$
The expression simplifies to the identity $7 = 7$ for all $t \in \mathbb{R}$.
Therefore, every point of line $L$ lies in the plane.

---

## 5. Why Each Step Is Valid
1. **The vector $\overrightarrow{P_0 P}$** lies in the plane because both of its endpoints belong to the plane.
2. **The cross product $v \times \overrightarrow{P_0 P}$** produces a vector perpendicular to all linear combinations of the two spanning vectors, defining the unique normal direction.
3. **The cancellation of parameter $t$** demonstrates that the line's direction vector is orthogonal to the normal vector ($v \cdot n = 0$), ensuring the line never leaves the plane.

---

## 6. Final Answer in Words
The Cartesian equation of the plane is $x + 2y + 3z = 7$ (or $x + 2y + 3z - 7 = 0$). Substituting $P(0, 2, 1)$ gives $0 + 4 + 3 = 7$, verifying that $P$ lies in the plane. Substituting the line's parametric equations $(1+t, t, 2-t)$ yields $(1+t) + 2(t) + 3(2-t) = 7 + 0t = 7$, which holds identically for every real number $t$, proving that the entire line lies in the plane.

---

## 7. Quick Verification
- **Orthogonality checks:**
  $$n \cdot v = (1)(1) + (2)(1) + (3)(-1) = 1 + 2 - 3 = 0,$$
  $$n \cdot \overrightarrow{P_0 P} = (1)(-1) + (2)(2) + (3)(-1) = -1 + 4 - 3 = 0.$$
  Both dot products equal zero, verifying that $n$ is truly perpendicular to both generators of the plane.

---

## 8. Common Mistakes to Avoid
- **Sign slips in cross product:** In the $\mathbf{j}$-minor, getting $-(-1 - 1) = -(-2) = +2$; accidentally writing $-2$ flips the plane.
- **Using $P$ as direction vector:** Crossing $v$ with $P$ directly instead of using the displacement vector $\overrightarrow{P_0 P} = P - P_0$.
- **Only checking one point of the line:** Checking $P_0(1, 0, 2)$ without checking that $v \cdot n = 0$ (which ensures the whole line lies in the plane).

---

## 9. Classroom Presentation (3-Sentence Summary)
We take the line's direction vector $(1, 1, -1)$ and the vector connecting the line's base point $(1, 0, 2)$ to $P(0, 2, 1)$, which is $(-1, 2, -1)$, and compute their cross product to find the normal vector $n = (1, 2, 3)$. Using this normal vector with base point $(1, 0, 2)$ gives the plane equation $x + 2y + 3z = 7$. We verify our result by showing that point $P$ satisfies $0 + 4 + 3 = 7$ and that substituting the line's coordinates $(1+t, t, 2-t)$ produces $7 = 7$ for all values of $t$.

