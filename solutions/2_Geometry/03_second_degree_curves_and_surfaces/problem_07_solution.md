# Problem 7 Solution: Classifying a Second-Degree Equation

## 1. Original Problem
Determine the type of planar geometric object described by each of the following second-degree equations:
1. $4x^2 + 9y^2 = 36$
2. $x^2 - y^2 = 1$
3. $x^2 - 4y = 0$
4. $x^2 + y^2 + 1 = 0$

In the last case, provide a rigorous mathematical proof explaining why there are no real points satisfying the equation.

---

## 2. What We Are Trying to Find
We need to:
1. Normalize and rewrite each equation into recognizable canonical form.
2. Classify each equation into its proper geometric category (ellipse, hyperbola, parabola, or degenerate/empty locus).
3. Identify the key geometric attributes of each non-degenerate curve.
4. Prove that the fourth equation possesses no real solutions using the properties of real numbers.

---

## 3. Key Concepts and Theorems
1. **General Second-Degree Equation in the Plane:**
   $$A x^2 + B xy + C y^2 + D x + E y + F = 0.$$
   When $B = 0$ (no mixed term), the conic is classified by the signs and degrees of the quadratic terms:
   - $A \cdot C > 0$ with matching sign on constant: **Ellipse** (or circle if $A = C$).
   - $A \cdot C < 0$: **Hyperbola**.
   - Exactly one quadratic term ($A = 0$ or $C = 0$) with linear counterpart: **Parabola**.
   - $A \cdot C > 0$ with opposing sign on constant ($x^2 + y^2 = -R^2$): **Empty locus (no real points)**.
2. **Axiom of Squares for Real Numbers:**
   For any real number $t \in \mathbb{R}$, its square is non-negative:
   $$t^2 \ge 0.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze Equation 1 ($4x^2 + 9y^2 = 36$)
Divide both sides by the constant 36:
$$\frac{4x^2}{36} + \frac{9y^2}{36} = \frac{36}{36} \implies \frac{x^2}{9} + \frac{y^2}{4} = 1 \implies \frac{x^2}{3^2} + \frac{y^2}{2^2} = 1.$$
- **Classification:** **Ellipse**
- **Attributes:**
  - Center: $(0, 0)$
  - Horizontal semi-major axis: $a = 3$
  - Vertical semi-minor axis: $b = 2$
  - Intercepts: $(\pm 3, 0)$ and $(0, \pm 2)$

### Step 2: Analyze Equation 2 ($x^2 - y^2 = 1$)
Compare with the standard hyperbola equation $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$:
$$\frac{x^2}{1^2} - \frac{y^2}{1^2} = 1.$$
- **Classification:** **Equilateral (Rectangular) Hyperbola**
- **Attributes:**
  - Center: $(0, 0)$
  - Transverse and conjugate semiaxes: $a = 1, b = 1$
  - Vertices: $(\pm 1, 0)$ on the $x$-axis
  - Asymptotes: $y = \pm \frac{1}{1} x \implies y = x$ and $y = -x$ (perpendicular to each other, forming a $90^\circ$ angle).

### Step 3: Analyze Equation 3 ($x^2 - 4y = 0$)
Isolate the linear variable $y$:
$$x^2 = 4y \iff y = \frac{1}{4}x^2.$$
- **Classification:** **Parabola**
- **Attributes:**
  - Vertex: $(0, 0)$
  - Axis of symmetry: the vertical $y$-axis ($x = 0$)
  - Opening direction: upwards into the upper half-plane ($y \ge 0$)
  - Focal parameter: $2p = 4 \implies p = 2$, so Focus is $F(0, 1)$ and Directrix is $y = -1$.

### Step 4: Analyze Equation 4 ($x^2 + y^2 + 1 = 0$)
Rearrange the equation by isolating the quadratic terms on the left:
$$x^2 + y^2 = -1.$$
- **Classification:** **Empty set $\emptyset$ (imaginary circle / no real points)**.

### Step 5: Proof of Why There Are No Real Points for Case 4
Let $x$ and $y$ be any arbitrary real numbers ($x, y \in \mathbb{R}$).
1. By the fundamental properties of the real number system, the square of any real number is strictly non-negative:
   $$x^2 \ge 0 \quad \text{for all } x \in \mathbb{R},$$
   $$y^2 \ge 0 \quad \text{for all } y \in \mathbb{R}.$$
2. Adding these two non-negative inequalities yields:
   $$x^2 + y^2 \ge 0 + 0 = 0.$$
3. Now add 1 to both sides:
   $$x^2 + y^2 + 1 \ge 0 + 1 = 1.$$
4. Therefore, for every possible pair of real coordinates $(x, y) \in \mathbb{R}^2$, the left-hand side is at least $1$:
   $$\text{LHS} \ge 1 > 0.$$
5. Because the left-hand side is strictly positive ($\ge 1$), it can never equal $0$:
   $$x^2 + y^2 + 1 \neq 0 \quad \text{for all } (x, y) \in \mathbb{R}^2.$$
Consequently, no real points satisfy the equation, and the solution set in $\mathbb{R}^2$ is the empty set $\emptyset$.

---

## 5. Why Each Step Is Valid
1. **Dividing by 36** casts the quadratic equation into normalized standard form where the right-hand constant equals 1.
2. **The signs of the coefficients** of $x^2$ and $y^2$ determine the signature of the quadratic form.
3. **The proof of non-existence** relies directly on the ordering axioms of the real field $\mathbb{R}$, where sums of squares can never be negative.

---

## 6. Final Answer in Words
1. $4x^2 + 9y^2 = 36$ describes an **ellipse** with center $(0, 0)$ and semiaxes $a = 3$ and $b = 2$.
2. $x^2 - y^2 = 1$ describes a **rectangular hyperbola** with center $(0, 0)$, vertices at $(\pm 1, 0)$, and perpendicular asymptotes $y = \pm x$.
3. $x^2 - 4y = 0$ describes a **parabola** with vertex at $(0, 0)$ opening upwards along the $y$-axis.
4. $x^2 + y^2 + 1 = 0$ represents the **empty set** (no real points). There are no real points because for any real numbers $x$ and $y$, $x^2 \ge 0$ and $y^2 \ge 0$, which guarantees that $x^2 + y^2 + 1 \ge 1 > 0$, making it impossible to sum to zero.

---

## 7. Quick Verification
- **Discriminant $\Delta = B^2 - 4AC$ check:**
  - Case 1: $A = 4, B = 0, C = 9 \implies \Delta = 0 - 4(4)(9) = -144 < 0$ (Elliptic type).
  - Case 2: $A = 1, B = 0, C = -1 \implies \Delta = 0 - 4(1)(-1) = +4 > 0$ (Hyperbolic type).
  - Case 3: $A = 1, B = 0, C = 0 \implies \Delta = 0 - 4(1)(0) = 0$ (Parabolic type).
  - Case 4: $A = 1, B = 0, C = 1 \implies \Delta = -4 < 0$, but constant $F = 1$ has same sign as $A$ and $C$, confirming the locus of real points is empty.

---

## 8. Common Mistakes to Avoid
- **Confusing rectangular hyperbola with intersecting lines:** $x^2 - y^2 = 0$ defines two intersecting lines $y = \pm x$, whereas $x^2 - y^2 = 1$ defines a smooth hyperbola whose asymptotes are those lines.
- **Claiming $x^2 + y^2 + 1 = 0$ is a circle with radius $-1$:** A geometric radius must be a positive real number ($R > 0$); an equation $x^2 + y^2 = -1$ has radius $R = \sqrt{-1} = i$, which has no real geometric locus in $\mathbb{R}^2$.
- **Inverting the parabola orientation:** Thinking $x^2 - 4y = 0$ opens horizontally. The linear variable ($y$) defines the axis of opening.

---

## 9. Classroom Presentation (3-Sentence Summary)
Dividing $4x^2 + 9y^2 = 36$ by 36 yields an ellipse with semiaxes 3 and 2, while $x^2 - y^2 = 1$ is a rectangular hyperbola opening horizontally with asymptotes $y = \pm x$. The equation $x^2 = 4y$ is a parabola opening upwards with vertex at the origin. Finally, $x^2 + y^2 + 1 = 0$ contains no real points because squares of real numbers are always non-negative, forcing the sum $x^2 + y^2 + 1$ to be at least 1 and thus never equal to zero.

