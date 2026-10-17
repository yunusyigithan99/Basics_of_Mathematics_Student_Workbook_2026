# Problem 14 Solution: Contrast: Intersection and Parallelism

## 1. Original Problem
From the point $P = (0, 0, 1)$, two lines are drawn with direction vectors:
$$v_1 = (2, 1, -1) \quad \text{and} \quad v_2 = (2, 1, 0).$$
For each line, analyze its position relative to the coordinate plane
$$\Pi : z = 0 \quad (\text{the } xy\text{-plane}).$$
For the line that intersects the plane, determine the coordinates of the intersection point. For the other line, explain how you can recognize parallelism immediately without setting up or solving an algebraic equation.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the normal vector $n$ of the plane $z = 0$.
2. Compute the dot products $v_1 \cdot n$ and $v_2 \cdot n$ to evaluate transversality versus parallelism.
3. Find the unique intersection point of line $L_1$ with the plane $z = 0$.
4. Explain how visual inspection of the $z$-coordinate of $v_2$ proves parallelism of line $L_2$ to $z = 0$ without calculation.

---

## 3. Key Concepts and Theorems
1. **The Coordinate Plane $z = 0$:**
   The plane $z = 0$ consists of all points in $\mathbb{R}^3$ whose vertical coordinate is zero (the $xy$-plane). Its normal vector points along the positive $z$-axis:
   $$n = (0, 0, 1) = \mathbf{k}.$$
2. **Line-Plane Incidence Condition:**
   - If the direction vector $v$ has a non-zero $z$-component ($v_z \neq 0$, so $v \cdot n \neq 0$), the line moves vertically and must cut through the horizontal plane $z = 0$ at a single unique point.
   - If the direction vector $v$ has a zero $z$-component ($v_z = 0$, so $v \cdot n = 0$), the line never changes its vertical height; it moves entirely horizontally.
3. **Strict Parallelism:**
   If $v_z = 0$ and the base point has $z_0 \neq 0$, the entire line lies in the parallel plane $z = z_0$, so it never intersects the plane $z = 0$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Plane's Normal Vector and Base Point
- Plane $\Pi : z = 0$ can be written as $0x + 0y + 1z = 0$.
  Its normal vector is:
  $$n = (0, 0, 1).$$
- The common base point is $P = (0, 0, 1)$. Note that $z_P = 1 \neq 0$, so $P$ does not lie in the plane $\Pi$.

### Step 2: Analyze Line $L_1$ with Direction $v_1 = (2, 1, -1)$
Parametric equations for $L_1$:
$$\begin{cases}
x(t) = 0 + 2t = 2t \\
y(t) = 0 + t = t \\
z(t) = 1 - t
\end{cases}$$
Compute the dot product with the normal vector:
$$v_1 \cdot n = (2)(0) + (1)(0) + (-1)(1) = -1 \neq 0.$$
Because $v_1 \cdot n \neq 0$, line $L_1$ **intersects the plane $z = 0$ at exactly one point**.

### Step 3: Find the Intersection Point of $L_1$ with $z = 0$
Set the $z$-coordinate equation equal to zero:
$$z(t) = 0 \implies 1 - t = 0 \implies t = 1.$$
Substitute $t = 1$ back into the $x$ and $y$ parametric expressions:
$$x = 2(1) = 2,$$
$$y = 1(1) = 1,$$
$$z = 1 - 1 = 0.$$
Thus, the intersection point of $L_1$ with the plane $z = 0$ is:
$$I = (2, 1, 0).$$

### Step 4: Analyze Line $L_2$ with Direction $v_2 = (2, 1, 0)$
Parametric equations for $L_2$:
$$\begin{cases}
x(s) = 0 + 2s = 2s \\
y(s) = 0 + s = s \\
z(s) = 1 + 0s = 1
\end{cases}$$
Compute the dot product with the normal vector:
$$v_2 \cdot n = (2)(0) + (1)(0) + (0)(1) = 0.$$
Because $v_2 \cdot n = 0$ and the base point $P$ has $z = 1 \neq 0$, line $L_2$ is **strictly parallel** to the plane $z = 0$ and never intersects it ($L_2 \cap \Pi = \emptyset$).

### Step 5: How to Recognize Parallelism Without Solving an Equation
- The plane in question is $z = 0$, which is the set of all points at constant vertical elevation $0$.
- Any line moving in space has direction vector $v = (v_x, v_y, v_z)$, where $v_z$ represents the rate of change of height per unit of parameter:
  $$\frac{dz}{ds} = v_z.$$
- Inspecting $v_2 = (2, 1, 0)$ reveals immediately that its third component is $v_z = 0$.
- This means that as parameter $s$ varies, the $z$-coordinate of every point on line $L_2$ is completely constant: $z(s) \equiv 1$ for all $s \in \mathbb{R}$.
- Since the line remains at a constant height of $z = 1$, it is confined to the horizontal plane $z = 1$.
- Because the plane $z = 1$ is parallel to and disjoint from $z = 0$, the line $L_2$ is parallel to the plane $z = 0$ by direct geometric observation, requiring no equation solving.

---

## 5. Why Each Step Is Valid
1. **The $z$-component directly governs vertical motion** in Cartesian coordinates; setting $z(t) = 0$ is the defining algebraic condition for intersecting the $xy$-plane.
2. **The dot product $v_2 \cdot n = 0$** rigorously confirms that the velocity vector is tangent to any horizontal plane.
3. **The constant height $z(s) = 1$** guarantees the distance between $L_2$ and $\Pi$ is identically 1 for all points on the line.

---

## 6. Final Answer in Words
Line $L_1$ with direction $v_1 = (2, 1, -1)$ has a non-zero vertical velocity component ($v_z = -1$), cutting through the plane $z = 0$ at parameter $t = 1$, which gives the unique intersection point $I = (2, 1, 0)$. Line $L_2$ with direction $v_2 = (2, 1, 0)$ has $v_z = 0$, meaning its vertical height is constant at $z = 1$ for all points; therefore, $L_2$ is strictly parallel to the plane $z = 0$ and never meets it. Parallelism is recognized without solving equations simply by noticing that the $z$-component of $v_2$ is zero while the starting point is at $z = 1$.

---

## 7. Quick Verification
- **Check intersection point $I(2, 1, 0)$:**
  - On line $L_1$: $(2, 1, 0) = (0, 0, 1) + 1(2, 1, -1) = (2, 1, 0)$. (Verified)
  - On plane $\Pi$: $z = 0$. (Verified)
- **Check distance of $L_2$ from plane:**
  The distance from any point $(2s, s, 1)$ on $L_2$ to the plane $z = 0$ is:
  $$d = \frac{|0(2s) + 0(s) + 1(1) - 0|}{\sqrt{0^2 + 0^2 + 1^2}} = \frac{1}{1} = 1.$$
  The distance is constant and equal to $1$ for all $s \in \mathbb{R}$, proving the line is parallel to the plane.

---

## 8. Common Mistakes to Avoid
- **Confusing plane $z = 0$ with the origin:** Thinking $z = 0$ means the point $(0, 0, 0)$; $z = 0$ is the entire infinite 2D $xy$-plane.
- **Missing the constant height:** Setting up an equation $1 + 0s = 0$ and being confused by $1 = 0$, instead of recognizing that inconsistency means no intersection and constant distance.
- **Overlooking the starting point height:** Assuming that $v_z = 0$ automatically means the line lies *in* the plane, forgetting to check whether the starting point is at $z = 0$ or $z \neq 0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Line $L_1$ has direction $(2, 1, -1)$ with vertical component $-1$, which allows us to set $1 - t = 0$ and find the intersection point $(2, 1, 0)$ at $t = 1$. In contrast, line $L_2$ has direction $(2, 1, 0)$ with a $z$-component of zero, meaning every point along the line maintains the constant elevation $z = 1$. Because it starts at height 1 and never moves vertically, line $L_2$ is parallel to the plane $z = 0$ by direct inspection, with no algebraic solving required.

