# Problem 02: Geometric Optimization — Maximizing Rectangular Area

## 1. Original Problem
A rectangle has perimeter $40$.

1. Write its area as a function of the length of one side.
2. Determine the domain of this function resulting from the geometry of the problem.
3. Find the dimensions that give the maximum area.
4. Justify that the point found actually gives a maximum.

---

## 2. What We Are Trying to Find
1. The mathematical objective function $A(x)$ expressing the rectangle's area in terms of a single side length $x$.
2. The physically meaningful domain for $x$ dictated by Euclidean geometry.
3. The critical points of the area function and corresponding side lengths.
4. A rigorous justification (using the first/second derivative test and algebra) confirming that this critical point is a global maximum.

---

## 3. Key Concepts and Theorems
1. **Geometric Optimization Scheme:**
   - Define variables and identify the objective function ($A = x \cdot y$).
   - Identify constraints (Perimeter $P = 2x + 2y = 40$) and eliminate one variable.
   - Establish the geometric domain.
   - Find critical points ($A'(x) = 0$).
   - Verify the character of the optimum using derivative tests.
2. **Second Derivative Test:**
   If $A'(x_0) = 0$ and $A''(x_0) < 0$, then $x_0$ is a strict local maximum.
3. **Isoperimetric Theorem for Quadrilaterals:**
   Among all rectangles with a fixed perimeter, the square encloses the greatest area.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Write the area as a function of one side
Let $x$ and $y$ denote the lengths of the two adjacent sides of the rectangle.
The perimeter of the rectangle is:
$$2x + 2y = 40.$$
Dividing both sides by $2$:
$$x + y = 20 \iff y = 20 - x.$$
The area of a rectangle is the product of its adjacent sides:
$$A = x \cdot y.$$
Substituting $y = 20 - x$ into the area expression gives the objective function in terms of $x$ alone:
$$A(x) = x(20 - x) = 20x - x^2.$$

### Step 2: Determine the geometric domain
For a non-degenerate physical rectangle:
- The side length $x$ must be strictly positive: $x > 0$.
- The other side length $y$ must also be strictly positive:
  $$y > 0 \iff 20 - x > 0 \iff x < 20.$$

Combining both conditions yields the open interval:
$$D_A = (0, 20).$$
*(If degenerate rectangles with zero width or length and zero area are allowed at the boundaries, the domain is the compact interval $[0, 20]$.)*

### Step 3: Find the dimensions that maximize area
Differentiate $A(x) = 20x - x^2$ with respect to $x$:
$$A'(x) = \frac{d}{dx}(20x - x^2) = 20 - 2x.$$
Set the first derivative to zero to find stationary points:
$$20 - 2x = 0 \iff 2x = 20 \iff x = 10.$$
Since $10 \in (0, 20)$, this is a valid interior critical point.

Now, calculate the other dimension $y$:
$$y = 20 - x = 20 - 10 = 10.$$
Thus, the dimensions are:
$$x = 10, \qquad y = 10.$$
The optimal rectangle is a **square** of side length $10$.
The resulting maximum area is:
$$A(10) = 10 \cdot 10 = 100.$$

### Step 4: Justify that the point is indeed a maximum
We confirm the maximum using three independent mathematical justifications:

1. **Second Derivative Test:**
   Differentiating $A'(x) = 20 - 2x$:
   $$A''(x) = -2.$$
   Because $A''(x) = -2 < 0$ for all $x \in (0, 20)$, the curve is concave everywhere (downward-opening parabola). Therefore, $x = 10$ is a strict global maximum on $(0, 20)$.

2. **First Derivative Sign Analysis:**
   - For $0 < x < 10$: $A'(x) = 2(10 - x) > 0 \implies A(x)$ is strictly increasing.
   - For $10 < x < 20$: $A'(x) = 2(10 - x) < 0 \implies A(x)$ is strictly decreasing.
   Since the derivative transitions from positive to negative, $x = 10$ is a unique global peak.

3. **Algebraic Completion of the Square:**
   $$A(x) = -(x^2 - 20x) = -(x^2 - 20x + 100 - 100) = -(x - 10)^2 + 100.$$
   Because $(x - 10)^2 \ge 0$ for all real $x$, $-(x - 10)^2 \le 0$, which implies:
   $$A(x) \le 100 \quad \text{for all } x \in \mathbb{R},$$
   with equality holding if and only if $x - 10 = 0 \iff x = 10$.

---

## 5. Why Each Step Is Valid
- **Step 1:** The perimeter formula establishes a linear constraint that reduces a multivariable problem to a single-variable function.
- **Step 2:** Physical lengths cannot be negative or zero.
- **Step 3:** The extremum of a smooth differentiable function on an open interval must occur at a point where the derivative vanishes (Fermat's Theorem).
- **Step 4:** A strictly negative second derivative guarantees downward concavity, making any critical point an absolute maximum.

---

## 6. Final Answer in Words
1. The area function is $A(x) = 20x - x^2$.
2. The domain resulting from physical geometry is $D_A = (0, 20)$.
3. The dimensions that maximize the area are $x = 10$ and $y = 10$ (a square), producing a maximum area of $100$.
4. The maximum is justified because $A''(x) = -2 < 0$ everywhere, proving that the objective function is strictly concave and attains its unique global maximum at $x = 10$.

---

## 7. Quick Verification
- Check nearby dimensions with perimeter $40$:
  - $x = 9 \implies y = 11 \implies \text{Area} = 9 \times 11 = 99 < 100$.
  - $x = 11 \implies y = 9 \implies \text{Area} = 11 \times 9 = 99 < 100$.
  - $x = 5 \implies y = 15 \implies \text{Area} = 5 \times 15 = 75 < 100$.
Every deviation from $10 \times 10$ reduces the area.

---

## 8. Common Mistakes to Avoid
- **Omitting the domain:** Forgetting that side lengths must be positive, which could allow meaningless solutions like $x = -5, y = 25$.
- **Not proving it is a maximum:** Stopping after finding $x = 10$ without applying the second derivative test or sign chart.
- **Algebraic error in perimeter:** Writing $x + y = 40$ instead of $2x + 2y = 40$.

---

## 9. Classroom Presentation (3-Sentence Summary)
From the perimeter constraint $2x + 2y = 40$, we express the adjacent side as $y = 20 - x$, which gives the area function $A(x) = 20x - x^2$ on the domain $(0, 20)$. Setting the derivative $A'(x) = 20 - 2x = 0$ yields $x = 10$, which implies $y = 10$, meaning the optimal rectangle is a square. Because the second derivative $A''(x) = -2$ is strictly negative everywhere, this square configuration mathematically guarantees the maximum possible area of $100$.
