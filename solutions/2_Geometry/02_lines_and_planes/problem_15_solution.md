# Problem 15 Solution: Complete Classification of a Line Relative to a Plane

## 1. Original Problem
Let a line $L$ and a plane $\Pi$ in $\mathbb{R}^3$ be given in general vector form by:
$$L : X(t) = p + t\,v, \quad t \in \mathbb{R},$$
$$\Pi : n \cdot X = d,$$
where $p$ is a base point on the line, $v \neq \mathbf{0}$ is the line's direction vector, $n \neq \mathbf{0}$ is the plane's normal vector, and $d \in \mathbb{R}$ is the plane constant.

1. State the exact mathematical conditions that distinguish the three possible geometric cases:
   - Case 1: The line intersects the plane at exactly one point ($L \cap \Pi = \{I\}$).
   - Case 2: The line is strictly parallel to the plane with no common points ($L \cap \Pi = \emptyset$).
   - Case 3: The line is entirely contained within the plane ($L \subset \Pi$).
2. Illustrate each of the three cases with a clear, self-contained numerical example.

---

## 2. What We Are Trying to Find
We need to:
1. Substitute the general parametric equation $X(t) = p + t\,v$ into the plane equation $n \cdot X = d$.
2. Analyze the resulting linear equation $(n \cdot v)t = d - n \cdot p$ in terms of its coefficients.
3. Formulate the necessary and sufficient criteria for uniqueness, inconsistency, and indeterminacy.
4. Provide simple, concrete numerical examples for all three outcomes, demonstrating the theory in practice.

---

## 3. Key Concepts and Theorems
1. **Linear Equation in One Unknown:**
   Any relationship between an affine line and a hyperplane in $\mathbb{R}^n$ reduces to a scalar equation of the form:
   $$A\,t = B,$$
   where $A = n \cdot v$ and $B = d - n \cdot p$.
2. **Three Fundamental Solution Regimes:**
   - **Unique Solution:** If $A \neq 0$, then $t = \frac{B}{A}$ uniquely.
   - **No Solution (Inconsistent):** If $A = 0$ and $B \neq 0$, the equation $0 \cdot t = B \neq 0$ has no solution.
   - **Infinitely Many Solutions (Identity):** If $A = 0$ and $B = 0$, the equation $0 \cdot t = 0$ is satisfied by all $t \in \mathbb{R}$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Derive the Fundamental Algebraic Equation
Substitute the parametric line $X(t) = p + t\,v$ into the plane equation $n \cdot X = d$:
$$n \cdot (p + t\,v) = d.$$
Apply the linearity of the inner product:
$$n \cdot p + t(n \cdot v) = d \implies (n \cdot v)\,t = d - n \cdot p.$$
Let:
- $A = n \cdot v$ (the rate at which the line penetrates the plane)
- $B = d - n \cdot p$ (the offset distance from the base point $p$ to the plane level set)

The position is entirely classified by the values of $A$ and $B$.

---

### Step 2: Formulate the Three Criteria

#### Case 1: Exactly One Intersection Point ($L \cap \Pi = \{I\}$)
- **Mathematical Condition:**
  $$n \cdot v \neq 0.$$
- **Geometric Meaning:** The direction of the line is not orthogonal to the normal vector; hence, the line is not parallel to the plane. It cuts through the plane transversely at the unique parameter value:
  $$t^* = \frac{d - n \cdot p}{n \cdot v}, \qquad I = p + \left(\frac{d - n \cdot p}{n \cdot v}\right)v.$$

#### Case 2: Strictly Parallel and Disjoint ($L \cap \Pi = \emptyset$)
- **Mathematical Condition:**
  $$n \cdot v = 0 \quad \text{and} \quad n \cdot p \neq d.$$
- **Geometric Meaning:** The direction vector $v$ is perpendicular to the normal vector $n$ (meaning the line runs parallel to the plane), but the base point $p$ does not lie on the plane. The equation becomes $0 \cdot t = B \neq 0$, which is impossible. The line maintains a constant non-zero distance from the plane.

#### Case 3: Line Contained Entirely in the Plane ($L \subset \Pi$)
- **Mathematical Condition:**
  $$n \cdot v = 0 \quad \text{and} \quad n \cdot p = d.$$
- **Geometric Meaning:** The direction vector is parallel to the plane ($n \cdot v = 0$), and the base point $p$ belongs to the plane ($n \cdot p = d$). The equation reduces to $0 \cdot t = 0$, which is true for all $t \in \mathbb{R}$. Every point on the line is also a point on the plane.

---

### Step 3: Numerical Illustrations

#### Numerical Example for Case 1 (One Intersection Point)
- Let the line have base point $p = (1, 0, 0)$ and direction $v = (1, 1, 1)$.
- Let the plane be $\Pi : z = 2$, which has normal $n = (0, 0, 1)$ and $d = 2$.
- Test condition:
  $$n \cdot v = (0)(1) + (0)(1) + (1)(1) = 1 \neq 0.$$
- Solve for $t$:
  $$n \cdot p = (0)(1) + (0)(0) + (1)(0) = 0 \implies t = \frac{2 - 0}{1} = 2.$$
- Intersection point:
  $$I = (1, 0, 0) + 2(1, 1, 1) = (3, 2, 2).$$
  Check: $z = 2$, which satisfies the plane equation.

#### Numerical Example for Case 2 (Strictly Parallel, Disjoint)
- Let the line have base point $p = (0, 0, 3)$ and direction $v = (1, 2, 0)$.
- Let the plane be $\Pi : z = 0$ (the $xy$-plane), with normal $n = (0, 0, 1)$ and $d = 0$.
- Test conditions:
  $$n \cdot v = (0)(1) + (0)(2) + (1)(0) = 0,$$
  $$n \cdot p = (0)(0) + (0)(0) + (1)(3) = 3 \neq 0 = d.$$
- Algebraic equation:
  $$0 \cdot t = 0 - 3 = -3 \quad (\text{impossible!})$$
  The line lies entirely in the parallel plane $z = 3$ and never touches $z = 0$.

#### Numerical Example for Case 3 (Contained in the Plane)
- Let the line have base point $p = (1, 1, 0)$ and direction $v = (1, -1, 0)$.
- Let the plane be $\Pi : x + y = 2$, with normal $n = (1, 1, 0)$ and $d = 2$.
- Test conditions:
  $$n \cdot v = (1)(1) + (1)(-1) + (0)(0) = 1 - 1 = 0,$$
  $$n \cdot p = (1)(1) + (1)(1) + (0)(0) = 1 + 1 = 2 = d.$$
- Algebraic equation:
  $$0 \cdot t = 2 - 2 = 0 \quad (\text{identity for all } t \in \mathbb{R}).$$
  Every point $(1 + t, 1 - t, 0)$ satisfies $(1 + t) + (1 - t) = 2$, so $L \subset \Pi$.

---

## 5. Why Each Step Is Valid
1. **The inner product substitution** strictly enforces the requirement that a point must simultaneously satisfy both geometric descriptions.
2. **The linear classification** maps the three geometric possibilities directly onto the three standard algebraic states of linear equations: unique solution, no solution, or infinitely many solutions.
3. **The numerical examples** are constructed with minimal integer coordinates, allowing direct mental verification of each property.

---

## 6. Final Answer in Words
The relationship between a line $p + tv$ and a plane $n \cdot X = d$ reduces to $(n \cdot v)t = d - n \cdot p$.
1. Exactly one intersection point occurs if and only if $n \cdot v \neq 0$.
2. Strict parallelism (no intersection) occurs if and only if $n \cdot v = 0$ and $n \cdot p \neq d$.
3. Containment within the plane occurs if and only if $n \cdot v = 0$ and $n \cdot p = d$.
The three numerical examples illustrate transverse crossing at $(3, 2, 2)$, parallel separation at constant elevation $z = 3$, and full embedding inside the plane $x + y = 2$.

---

## 7. Quick Verification
- **Summary Matrix / Table:**

| Case | Condition on $n \cdot v$ | Condition on $n \cdot p$ | Algebraic Equation | Number of Solutions | Geometric Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | $n \cdot v \neq 0$ | Any value | $A t = B$ ($A \neq 0$) | Exactly 1 | Line cuts through plane |
| **2** | $n \cdot v = 0$ | $n \cdot p \neq d$ | $0 t = B$ ($B \neq 0$) | 0 (Inconsistent) | Line is strictly parallel |
| **3** | $n \cdot v = 0$ | $n \cdot p = d$ | $0 t = 0$ | $\infty$ (Identity) | Line lies in plane |

The table is complete, exhaustive, and mutually exclusive.

---

## 8. Common Mistakes to Avoid
- **Confusing normal vector with tangent vector:** Thinking $n \cdot v = 0$ means the line is perpendicular to the plane. $n$ is perpendicular to the plane, so $v \perp n$ means $v$ is parallel to the plane.
- **Forgetting the second condition:** Evaluating only $n \cdot v = 0$ and guessing whether the line is parallel or contained, without evaluating $n \cdot p = d$.
- **Assuming $d$ is always 0:** Planes that do not pass through the origin have $d \neq 0$, which must be included in the offset calculation.

---

## 9. Classroom Presentation (3-Sentence Summary)
Substituting the line into the plane equation produces the scalar relation $(n \cdot v)t = d - n \cdot p$, whose coefficient $n \cdot v$ determines the geometric behavior. If $n \cdot v \neq 0$, the line penetrates the plane at a single unique intersection point. If $n \cdot v = 0$, the line is parallel to the planar surface, and testing whether the base point satisfies $n \cdot p = d$ immediately distinguishes between a line running parallel at a distance and one lying entirely inside the plane.

