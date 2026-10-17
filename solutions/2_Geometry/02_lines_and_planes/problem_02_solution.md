# Problem 2 Solution: A Line in Space

## 1. Original Problem
A line $L$ in 3-dimensional space $\mathbb{R}^3$ is given in parametric vector form by:
$$L : (x, y, z) = (2, -1, 3) + t(1, 2, -2), \quad t \in \mathbb{R}.$$
1. State a known base point lying on the line and its direction vector.
2. Check whether the point $P = (4, 3, -1)$ lies on $L$.
3. Find the coordinates of the point on $L$ corresponding to parameter value $t = -1$.

---

## 2. What We Are Trying to Find
We need to:
1. Extract the base position vector $P_0$ and direction vector $v$ from the parametric vector expression.
2. Test point membership by checking if a single consistent real parameter $t$ produces all three coordinates of $P = (4, 3, -1)$.
3. Substitute $t = -1$ into the parametric equation to compute the corresponding spatial coordinates.

---

## 3. Key Concepts and Theorems
1. **Parametric Form of a 3D Line:**
   A line in $\mathbb{R}^3$ cannot be described by a single linear equation; it requires two linear equations (an intersection of two planes) or a parametric vector form:
   $$\mathbf{r}(t) = P_0 + t\,v,$$
   where $P_0 = (x_0, y_0, z_0)$ is any point on the line (the base point at $t = 0$) and $v = (v_1, v_2, v_3) \neq \mathbf{0}$ is a direction vector parallel to the line.
2. **Point Incidence Criterion:**
   A point $P = (x_P, y_P, z_P)$ lies on the line $L$ if and only if the three coordinate equations:
   $$x_P = x_0 + t\,v_1, \qquad y_P = y_0 + t\,v_2, \qquad z_P = z_0 + t\,v_3$$
   share a single, common, simultaneous real solution $t \in \mathbb{R}$. If the equations yield conflicting values of $t$, the point does not lie on the line.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify Base Point and Direction Vector
From the given expression $(x, y, z) = (2, -1, 3) + t(1, 2, -2)$:
- Setting $t = 0$ gives the base point:
  $$P_0 = (2, -1, 3).$$
- The vector multiplied by the parameter $t$ is the direction vector:
  $$v = (1, 2, -2).$$

### Step 2: Check Whether $P = (4, 3, -1)$ Lies on $L$
Set the parametric components equal to the coordinates of $P(4, 3, -1)$:
$$\begin{cases}
2 + t = 4 & \text{(Equation for } x\text{)} \\
-1 + 2t = 3 & \text{(Equation for } y\text{)} \\
3 - 2t = -1 & \text{(Equation for } z\text{)}
\end{cases}$$
Solve for $t$ from the first equation:
$$2 + t = 4 \implies t = 2.$$
Now check whether this value $t = 2$ satisfies the remaining two equations:
- For $y$:
  $$-1 + 2(2) = -1 + 4 = 3.$$
  This matches the $y$-coordinate of $P$.
- For $z$:
  $$3 - 2(2) = 3 - 4 = -1.$$
  This matches the $z$-coordinate of $P$.
Since $t = 2$ satisfies all three coordinate equations simultaneously, the point $P = (4, 3, -1)$ **lies on the line $L$**.

### Step 3: Find the Point Corresponding to $t = -1$
Substitute $t = -1$ into the parametric equation of the line:
$$(x, y, z) = (2, -1, 3) + (-1)(1, 2, -2) = (2 - 1, \; -1 - 2, \; 3 - (-2)) = (1, -3, 5).$$
The point corresponding to $t = -1$ is $(1, -3, 5)$.

---

## 5. Why Each Step Is Valid
1. **Reading off $P_0$ and $v$** directly matches the definition of affine lines $\mathbf{r}(t) = P_0 + t\,v$.
2. **Checking all three coordinates** is essential because a line is a 1-dimensional manifold in 3-dimensional space; matching two coordinates while failing the third would mean the point misses the line in space.
3. **Plugging $t = -1$** is a direct vector addition and scalar multiplication in $\mathbb{R}^3$.

---

## 6. Final Answer in Words
A base point on the line is $P_0 = (2, -1, 3)$ and the direction vector is $v = (1, 2, -2)$. The point $P = (4, 3, -1)$ lies on the line because the parameter value $t = 2$ consistently produces all three coordinates. The point on the line corresponding to $t = -1$ is $(1, -3, 5)$.

---

## 7. Quick Verification
- **Vector collinearity test for point $P$:**
  Construct $\overrightarrow{P_0 P} = P - P_0 = (4 - 2, 3 - (-1), -1 - 3) = (2, 4, -4)$.
  Notice that $(2, 4, -4) = 2(1, 2, -2) = 2v$.
  Because $\overrightarrow{P_0 P}$ is a direct scalar multiple of $v$ (with factor $2$), $P$ must lie on the line.
- **Verification of point at $t = -1$:**
  Let $Q = (1, -3, 5)$.
  $\overrightarrow{Q P_0} = P_0 - Q = (2 - 1, -1 - (-3), 3 - 5) = (1, 2, -2) = v$.
  Moving 1 unit along $v$ from $Q$ returns to $P_0$, which corresponds precisely to $\Delta t = +1$.

---

## 8. Common Mistakes to Avoid
- **Checking only two coordinates:** Verifying $x$ and $y$ and forgetting to check $z$. If $P$ were $(4, 3, 0)$, $t$ would be 2 for $x$ and $y$, but $z$ would fail.
- **Double-negative mistake at $t = -1$:** Calculating $3 - (-1)(-2)$ or $3 - (-2)$ incorrectly.
- **Mistaking $P_0$ for a unique point:** Thinking $(2, -1, 3)$ is the only point on the line; any value of $t$ provides an equally valid base point.

---

## 9. Classroom Presentation (3-Sentence Summary)
From the parametric equation $(x, y, z) = (2, -1, 3) + t(1, 2, -2)$, we immediately identify the base point $(2, -1, 3)$ and direction vector $(1, 2, -2)$. Point $P(4, 3, -1)$ lies on the line because setting $t = 2$ simultaneously satisfies all three coordinate equations without contradiction. Finally, plugging $t = -1$ into the equation yields the point $(1, -3, 5)$, which lies one unit of direction vector backwards from the base point.

