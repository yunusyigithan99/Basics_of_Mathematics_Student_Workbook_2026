# Problem 10 Solution: The Tangent Line as an Application of the Derivative

## 1. Original Problem
For the quadratic function:
$$f(x) = x^2 - 3x + 1$$
1. Find the coordinates of the point of tangency $P$ corresponding to $x = 2$.
2. Compute the value of the derivative $f'(2)$ to determine the slope of the tangent line.
3. Derive the Cartesian equation of the tangent line in slope-intercept and general form.
4. Verify by direct substitution that the point of tangency $P$ lies on the obtained tangent line.

---

## 2. What We Are Trying to Find
We need to:
1. Evaluate $f(2)$ to find the $y$-coordinate of the contact point $P(x_0, y_0)$.
2. Differentiate $f(x)$ to get $f'(x)$, then evaluate $m = f'(2)$.
3. Use the point-slope formula $y - y_0 = m(x - x_0)$ to write the tangent line equation.
4. Substitute $(x_0, y_0)$ into the tangent equation to confirm that the line and the parabola intersect at that exact point.

---

## 3. Key Concepts and Theorems
1. **Geometric Definition of the Tangent Line:**
   The tangent line to the differentiable curve $y = f(x)$ at the point $P(x_0, f(x_0))$ is the unique straight line passing through $P$ whose slope equals the instantaneous derivative:
   $$m = f'(x_0).$$
2. **Point-Slope Form of a Line:**
   $$y - y_0 = m(x - x_0) \iff y = f'(x_0)(x - x_0) + f(x_0).$$
3. **Local Linear Approximation:**
   The tangent line represents the best first-order linear approximation of $f(x)$ near $x_0$:
   $$f(x) \approx T(x) = f(x_0) + f'(x_0)(x - x_0).$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Find the Coordinates of the Point of Tangency $P$
Given $x_0 = 2$, evaluate the function $f(x) = x^2 - 3x + 1$:
$$y_0 = f(2) = 2^2 - 3(2) + 1 = 4 - 6 + 1 = -1.$$
Thus, the point of tangency on the parabola is:
$$P = (x_0, y_0) = (2, -1).$$

---

### Step 2: Compute the General Derivative and Tangent Slope
1. Differentiate $f(x) = x^2 - 3x + 1$ using the power rule:
   $$f'(x) = \frac{d}{dx}[x^2] - \frac{d}{dx}[3x] + \frac{d}{dx}[1] = 2x - 3.$$
2. Evaluate the derivative at the point $x_0 = 2$:
   $$m = f'(2) = 2(2) - 3 = 4 - 3 = 1.$$
The slope of the tangent line is $m = 1$.
Because $m = 1 > 0$, the tangent line rises at an angle of $\alpha = \arctan(1) = 45^\circ$ to the positive $x$-axis.

---

### Step 3: Derive the Equation of the Tangent Line
Use the point-slope equation with point $P(2, -1)$ and slope $m = 1$:
$$y - y_0 = m(x - x_0)$$
$$y - (-1) = 1 \cdot (x - 2)$$
$$y + 1 = x - 2.$$
Subtract $1$ from both sides:
$$y = x - 3 \quad \text{(Slope-Intercept Form)}.$$
In general implicit form:
$$x - y - 3 = 0 \quad \text{(General Form)}.$$

---

### Step 4: Verify That Point $P(2, -1)$ Lies on the Tangent Line
1. **Substitute into the slope-intercept form $y = x - 3$:**
   $$\text{LHS} = y = -1.$$
   $$\text{RHS} = x - 3 = 2 - 3 = -1.$$
   Since $\text{LHS} = \text{RHS} = -1$, the point $P(2, -1)$ satisfies the equation.
2. **Substitute into the general form $x - y - 3 = 0$:**
   $$2 - (-1) - 3 = 2 + 1 - 3 = 3 - 3 = 0.$$
The point of tangency lies squarely on the tangent line.

---

## 5. Why Each Step Is Valid
1. **Finding $f(2) = -1$** locates the unique point on the graph at coordinate $x = 2$.
2. **The power rule** $\frac{d}{dx}[x^2 - 3x + 1] = 2x - 3$ is universally valid for polynomial functions.
3. **The point-slope formula** is the exact geometric equation for a straight line with known point and slope.

---

## 6. Final Answer in Words
The point of tangency is $P = (2, -1)$. The slope of the tangent line is given by the derivative value $f'(2) = 1$. The equation of the tangent line is $y = x - 3$ (or $x - y - 3 = 0$). Substituting the point $P(2, -1)$ into the tangent equation gives $-1 = 2 - 3 = -1$, verifying that the line passes through the point of tangency.

---

## 7. Quick Verification
- **Tangency Condition (Double Root of Intersection):**
  A line is tangent to a parabola if and only if their intersection equation has a single repeated root (discriminant $\Delta = 0$).
  Set the parabola equal to the line:
  $$x^2 - 3x + 1 = x - 3.$$
  Subtract $(x - 3)$ from both sides:
  $$x^2 - 4x + 4 = 0.$$
  Factor:
  $$(x - 2)^2 = 0.$$
  The root is $x = 2$ with multiplicity 2 (a double root), and the discriminant is:
  $$\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0.$$
  This proves algebraically that the line touches the parabola at exactly one point ($x = 2$) without crossing it, confirming true geometric tangency!

---

## 8. Common Mistakes to Avoid
- **Sign slip when subtracting a negative coordinate:** Writing $y - 1$ instead of $y - (-1) = y + 1$, leading to $y = x - 1$.
- **Confusing function value with slope:** Using $m = -1$ (the value of $f(2)$) as the slope instead of $m = f'(2) = 1$.
- **Arithmetic error in $f(2)$:** Computing $2^2 - 3(2) + 1 = 4 - 6 + 1 = -1$ incorrectly.

---

## 9. Classroom Presentation (3-Sentence Summary)
Plugging $x = 2$ into the parabola $f(x) = x^2 - 3x + 1$ gives the point of tangency $(2, -1)$. Differentiating the parabola yields $f'(x) = 2x - 3$, which evaluates to $f'(2) = 1$, establishing that the tangent line has a slope of 1. Using the point-slope formula produces the tangent equation $y = x - 3$, which we verify by noting that $(2, -1)$ satisfies the equation and that setting the parabola equal to the line produces the perfect square $(x - 2)^2 = 0$.
