# Problem 1 Solution: Line Through Two Points

## 1. Original Problem
Find the equation of the line passing through the points
$$A = (1, 2) \quad \text{and} \quad B = (4, -1)$$
in both parametric form and general (implicit) form. Identify a direction vector and an example of a normal vector. Check that both points satisfy the obtained equation.

---

## 2. What We Are Trying to Find
We need to:
1. Construct a direction vector $v = \overrightarrow{AB}$ connecting point $A$ to point $B$.
2. Formulate the parametric vector equations of the line.
3. Determine a normal vector $n$ orthogonal to the direction vector in $\mathbb{R}^2$.
4. Derive the general Cartesian equation $Ax + By + C = 0$.
5. Verify that both original points $A$ and $B$ satisfy the general equation.

---

## 3. Key Concepts and Theorems
1. **Direction Vector of a Line:**
   Given two distinct points $A$ and $B$, the vector $v = \overrightarrow{AB} = B - A$ points along the line and serves as its direction vector.
2. **Parametric Form in $\mathbb{R}^2$:**
   Using base point $A$ and direction vector $v$:
   $$(x, y) = A + t\,v, \quad t \in \mathbb{R} \iff \begin{cases} x = x_A + t\,v_1 \\ y = y_A + t\,v_2 \end{cases}$$
3. **Normal Vector in $\mathbb{R}^2$:**
   A normal vector $n = (A, B)$ is perpendicular to the line's direction $v = (v_1, v_2)$, meaning:
   $$n \cdot v = 0 \iff A v_1 + B v_2 = 0.$$
   A standard choice for $v = (v_1, v_2)$ is $n = (-v_2, v_1)$ or $(v_2, -v_1)$.
4. **General Form of a Line:**
   The set of points $(x, y)$ satisfying the orthogonality condition with the normal vector:
   $$n \cdot \big((x, y) - A\big) = 0 \iff A(x - x_A) + B(y - y_A) = 0 \iff Ax + By + C = 0,$$
   where $C = -(A x_A + B y_A)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Find a Direction Vector $v$
Subtract the coordinates of point $A(1, 2)$ from $B(4, -1)$:
$$v = \overrightarrow{AB} = (4 - 1, \; -1 - 2) = (3, -3).$$
Notice that we can divide by 3 to obtain the simplest collinear direction vector:
$$v = (1, -1).$$
Either $(3, -3)$ or $(1, -1)$ is a valid direction vector for the line.

### Step 2: Write the Parametric Form
Using point $A(1, 2)$ and direction vector $v = (1, -1)$:
$$(x, y) = (1, 2) + t(1, -1), \quad t \in \mathbb{R}.$$
In scalar component form:
$$\begin{cases}
x = 1 + t \\
y = 2 - t
\end{cases} \quad (t \in \mathbb{R}).$$

### Step 3: Find a Normal Vector $n$
Let $n = (a, b)$ be a normal vector perpendicular to $v = (1, -1)$.
The orthogonality condition requires:
$$n \cdot v = 0 \implies a(1) + b(-1) = 0 \implies a - b = 0 \implies a = b.$$
Choosing $a = 1$ gives $b = 1$, so a normal vector is:
$$n = (1, 1).$$

### Step 4: Derive the General Form
With normal vector $n = (1, 1)$, the general form is:
$$1x + 1y + C = 0 \implies x + y + C = 0.$$
Substitute the coordinates of point $A(1, 2)$ to determine constant $C$:
$$1 + 2 + C = 0 \implies 3 + C = 0 \implies C = -3.$$
Thus, the general equation of the line is:
$$x + y - 3 = 0 \quad (\text{or } x + y = 3).$$

### Step 5: Check That Both Points Satisfy the Equation
1. Substitute point $A(1, 2)$:
   $$1 + 2 - 3 = 3 - 3 = 0.$$ (Satisfied)
2. Substitute point $B(4, -1)$:
   $$4 + (-1) - 3 = 4 - 4 = 0.$$ (Satisfied)
Both points lie on the line.

---

## 5. Why Each Step Is Valid
1. **Subtracting coordinates** yields the displacement vector between two points on the line, which by definition is parallel to the line.
2. **Dividing direction vector by a positive scalar** changes only its speed/magnitude of parameterization, leaving the geometric path invariant.
3. **The Cartesian equation $x + y - 3 = 0$** follows from expanding the geometric relation $n \cdot (\mathbf{x} - A) = 0$.

---

## 6. Final Answer in Words
The direction vector is $v = (1, -1)$ (or $(3, -3)$) and a normal vector is $n = (1, 1)$. The parametric form is $(x, y) = (1, 2) + t(1, -1)$ for $t \in \mathbb{R}$. The general equation of the line is $x + y - 3 = 0$. Substituting $A(1, 2)$ gives $1 + 2 - 3 = 0$ and substituting $B(4, -1)$ gives $4 - 1 - 3 = 0$, verifying that both points lie on the line.

---

## 7. Quick Verification
- **Slope-intercept form:**
  From $A(1, 2)$ and $B(4, -1)$, the slope is $m = \frac{-1 - 2}{4 - 1} = \frac{-3}{3} = -1$.
  Point-slope equation: $y - 2 = -1(x - 1) \implies y - 2 = -x + 1 \implies x + y - 3 = 0$.
- **Parameter values check:**
  - Setting $t = 0$ gives $(1 + 0, 2 - 0) = (1, 2) = A$.
  - Setting $t = 3$ gives $(1 + 3, 2 - 3) = (4, -1) = B$.
  Both points are directly recovered.

---

## 8. Common Mistakes to Avoid
- **Confusing direction and normal vectors:** Using the direction vector $(1, -1)$ as the coefficients in the general equation, writing $x - y + C = 0$, which is perpendicular to the true line.
- **Arithmetic sign in $B - A$:** Computing $-1 - 2 = 1$ instead of $-3$.
- **Not checking both points:** Verifying only point $A$ and missing an incorrect slope that misses point $B$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Subtracting point $A(1, 2)$ from $B(4, -1)$ gives the direction vector $(3, -3)$, which simplifies to $v = (1, -1)$, giving the parametric form $(x, y) = (1, 2) + t(1, -1)$. A perpendicular normal vector is $n = (1, 1)$, which yields the general Cartesian equation $x + y - 3 = 0$ after plugging in point $A$. We confirm the result by plugging in both points $A(1, 2)$ and $B(4, -1)$, both of which satisfy $x + y - 3 = 0$ identically.

