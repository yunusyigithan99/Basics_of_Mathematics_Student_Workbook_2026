# Problem 5 Solution: Relative Position of Two Lines

## 1. Original Problem
Analyze the relative position of the two lines in $\mathbb{R}^3$:
$$L_1 : (x, y, z) = (1, 1, 0) + t(1, 2, 1), \quad t \in \mathbb{R},$$
$$L_2 : (x, y, z) = (2, 0, 1) + s(0, 1, -1), \quad s \in \mathbb{R}.$$
If they intersect, determine the coordinates of the intersection point. If not, determine whether they are parallel or skew, and rigorously justify the classification.

---

## 2. What We Are Trying to Find
We need to:
1. Extract the direction vectors $v_1$ and $v_2$ and check whether they are proportional (parallel).
2. Set up the system of three linear equations in parameters $t$ and $s$ to search for a common intersection point.
3. Solve the system or demonstrate that it is inconsistent.
4. Classify the geometric relationship (intersecting, parallel, identical, or skew) based on direction proportionality and consistency.
5. Provide a rigorous geometric justification using the scalar triple product.

---

## 3. Key Concepts and Theorems
1. **Classification of Pairs of Lines in $\mathbb{R}^3$:**
   Two lines $L_1$ and $L_2$ with direction vectors $v_1, v_2$ and base points $P_1, P_2$ fall into exactly one of four mutually exclusive geometric categories:
   - **Identical (coincident):** $v_1 \parallel v_2$ and $P_1 \in L_2$.
   - **Parallel (strictly parallel):** $v_1 \parallel v_2$ and $P_1 \notin L_2$.
   - **Intersecting:** $v_1 \nparallel v_2$ and there exists a unique pair $(t, s)$ satisfying the coordinate system.
   - **Skew:** $v_1 \nparallel v_2$ and the coordinate system has no solution (they do not lie in the same plane).
2. **Scalar Triple Product Criterion for Coplanarity:**
   Two lines in $\mathbb{R}^3$ lie in a common plane (are coplanar, meaning they intersect or are parallel) if and only if the scalar triple product of their direction vectors and the displacement vector between their base points is zero:
   $$(v_1 \times v_2) \cdot \overrightarrow{P_1 P_2} = 0.$$
   If this determinant is non-zero, the lines are **skew**.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Check Whether the Direction Vectors Are Parallel
The direction vectors are:
$$v_1 = (1, 2, 1), \qquad v_2 = (0, 1, -1).$$
For $v_1$ and $v_2$ to be parallel, there must exist a scalar $k \in \mathbb{R}$ such that $v_1 = k\,v_2$:
$$(1, 2, 1) = k(0, 1, -1) \implies \begin{cases} 1 = 0 \cdot k = 0 \\ 2 = k \\ 1 = -k \end{cases}$$
The first equation $1 = 0$ is impossible. Therefore, no such scalar $k$ exists, which means:
$$v_1 \nparallel v_2.$$
The lines are **not parallel**. They are either intersecting or skew.

### Step 2: Attempt to Find an Intersection Point
Equate the coordinates of $L_1$ and $L_2$:
$$\begin{cases}
1 + t = 2 + 0s & \text{(Equation 1 for } x\text{)} \\
1 + 2t = 0 + s & \text{(Equation 2 for } y\text{)} \\
0 + t = 1 - s & \text{(Equation 3 for } z\text{)}
\end{cases}$$

From Equation 1:
$$1 + t = 2 \implies t = 1.$$
Substitute $t = 1$ into Equation 2:
$$s = 1 + 2(1) = 3.$$
Now test whether the pair $(t, s) = (1, 3)$ satisfies Equation 3 for the $z$-coordinate:
- Left-hand side: $z_1 = 0 + t = 1$.
- Right-hand side: $z_2 = 1 - s = 1 - 3 = -2$.

Since $1 \neq -2$, Equation 3 is violated. The system of linear equations is inconsistent and has **no solution**.

### Step 3: Classify the Geometric Position
Since:
1. The direction vectors $v_1$ and $v_2$ are not parallel ($v_1 \nparallel v_2$), and
2. The lines have no point in common ($L_1 \cap L_2 = \emptyset$),

the two lines $L_1$ and $L_2$ are **skew** (they lie in different, non-intersecting planes in space).

---

## 5. Why Each Step Is Valid
1. **Direction proportionality check** tests whether the two lines travel in the same or opposite directions in 3D space.
2. **Equating coordinates** translates the geometric search for an intersection point into a linear system of 3 equations in 2 unknowns.
3. **The inconsistency $1 \neq -2$** rigorously proves the lines never meet, and since they are not parallel, they must be skew by definition.

---

## 6. Final Answer in Words
The direction vectors $v_1 = (1, 2, 1)$ and $v_2 = (0, 1, -1)$ are not parallel because their components are not proportional. Equating the parametric coordinates yields $t = 1$ and $s = 3$ from the $x$ and $y$ equations, but these values produce $z = 1$ on the first line and $z = -2$ on the second line. Because the system is inconsistent, the lines have no intersection point. Non-parallel lines with no common point in $\mathbb{R}^3$ are skew.

---

## 7. Quick Verification
- **Scalar Triple Product Test:**
  Base points are $P_1 = (1, 1, 0)$ and $P_2 = (2, 0, 1)$.
  Displacement vector between base points:
  $$\overrightarrow{P_1 P_2} = P_2 - P_1 = (2 - 1, \; 0 - 1, \; 1 - 0) = (1, -1, 1).$$
  Evaluate the $3 \times 3$ determinant:
  $$\det \begin{pmatrix} v_1 \\ v_2 \\ \overrightarrow{P_1 P_2} \end{pmatrix} = \begin{vmatrix} 1 & 2 & 1 \\ 0 & 1 & -1 \\ 1 & -1 & 1 \end{vmatrix} = 1\big(1(1) - (-1)(-1)\big) - 2\big(0(1) - (-1)(1)\big) + 1\big(0(-1) - 1(1)\big).$$
  $$= 1(1 - 1) - 2(0 + 1) + 1(0 - 1) = 0 - 2 - 1 = -3.$$
  Since the determinant is $-3 \neq 0$, the volume of the parallelepiped spanned by the two directions and the connecting vector is non-zero, confirming conclusively that the two lines cannot lie in the same plane and are skew.

---

## 8. Common Mistakes to Avoid
- **Concluding the lines intersect after solving only two equations:** Solving $x$ and $y$ gives $t = 1, s = 3$, and declaring the intersection is $(2, 3, \dots)$ without checking the third coordinate $z$.
- **Confusing skew with parallel:** Forgetting that in $\mathbb{R}^3$, non-intersecting lines can be either parallel or skew.
- **Arithmetic sign in $z = 1 - s$:** Writing $1 - 3 = 2$ instead of $-2$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The direction vectors $(1, 2, 1)$ and $(0, 1, -1)$ are not proportional, which immediately rules out the possibility that the lines are parallel. Equating the parametric equations for the $x$ and $y$ coordinates yields candidate parameters $t = 1$ and $s = 3$, but substituting these into the $z$ equation produces a contradiction, $1 = -2$. Because the lines are non-parallel and have no common intersection point, they are skew lines in space.

