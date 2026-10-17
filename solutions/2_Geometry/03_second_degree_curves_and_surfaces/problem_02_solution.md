# Problem 2 Solution: Circle by Completing the Square

## 1. Original Problem
Reduce the general second-degree equation
$$x^2 + y^2 - 6x + 4y - 3 = 0$$
to canonical form. Find the center $S$ and the radius $R$ of the circle, then select two simple points lying on the circle and substitute them into both the canonical and general forms of the equation to verify the result.

---

## 2. What We Are Trying to Find
We need to:
1. Group the $x$-terms and $y$-terms and complete the square for each variable.
2. Formulate the canonical circle equation $(x - x_0)^2 + (y - y_0)^2 = R^2$.
3. Identify the center coordinates $(x_0, y_0)$ and the radius $R$.
4. Determine the coordinates of at least two easily identifiable points on the circumference.
5. Check both points in both the canonical equation and the original general equation.

---

## 3. Key Concepts and Theorems
1. **General Equation of a Circle:**
   $$x^2 + y^2 + D x + E y + F = 0.$$
   Because the coefficients of $x^2$ and $y^2$ are both equal to $+1$ and there is no mixed $xy$-term, the equation describes a circle (provided $R^2 > 0$).
2. **Completing the Square Identity:**
   $$x^2 - 2ax = (x - a)^2 - a^2, \qquad y^2 + 2by = (y + b)^2 - b^2.$$
3. **Canonical (Standard) Form of a Circle:**
   $$(x - x_0)^2 + (y - y_0)^2 = R^2,$$
   where $(x_0, y_0)$ is the center and $R > 0$ is the geometric radius.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Group the Terms by Variable
Rearrange the general equation to place the $x$-terms together, the $y$-terms together, and move the constant term to the right-hand side:
$$(x^2 - 6x) + (y^2 + 4y) = 3.$$

### Step 2: Complete the Square for $x$ and $y$
- For the $x$-expression, halve the linear coefficient $-6$ to get $-3$, and square it:
  $$x^2 - 6x = (x - 3)^2 - 3^2 = (x - 3)^2 - 9.$$
- For the $y$-expression, halve the linear coefficient $+4$ to get $+2$, and square it:
  $$y^2 + 4y = (y + 2)^2 - 2^2 = (y + 2)^2 - 4.$$

### Step 3: Assemble the Canonical Form
Substitute these completed squares back into the equation:
$$\big((x - 3)^2 - 9\big) + \big((y + 2)^2 - 4\big) = 3.$$
Add $9 + 4 = 13$ to both sides:
$$(x - 3)^2 + (y + 2)^2 = 3 + 9 + 4$$
$$(x - 3)^2 + (y + 2)^2 = 16.$$
Since $16 = 4^2$, the canonical form of the circle is:
$$(x - 3)^2 + (y + 2)^2 = 4^2.$$

### Step 4: Identify Center and Radius
Comparing with $(x - x_0)^2 + (y - y_0)^2 = R^2$:
- **Center:**
  $$S = (x_0, y_0) = (3, -2)$$
- **Radius:**
  $$R = \sqrt{16} = 4$$

### Step 5: Choose Two Simple Points on the Circle
The simplest points are located at the highest, lowest, leftmost, and rightmost extremes:
- Setting $x = 3$:
  $$(3 - 3)^2 + (y + 2)^2 = 16 \implies (y + 2)^2 = 16 \implies y + 2 = \pm 4.$$
  - For $y + 2 = 4 \implies y = 2$, giving point $P_1 = (3, 2)$.
  - For $y + 2 = -4 \implies y = -6$, giving point $P_2 = (3, -6)$.

### Step 6: Verify the Points in Both Equations
1. **Verification of Point $P_1(3, 2)$:**
   - *Canonical form:*
     $$(3 - 3)^2 + (2 + 2)^2 = 0^2 + 4^2 = 16. \quad \text{(Satisfied)}$$
   - *General form:*
     $$3^2 + 2^2 - 6(3) + 4(2) - 3 = 9 + 4 - 18 + 8 - 3 = (9 + 4 + 8) - (18 + 3) = 21 - 21 = 0. \quad \text{(Satisfied)}$$

2. **Verification of Point $P_2(3, -6)$:**
   - *Canonical form:*
     $$(3 - 3)^2 + (-6 + 2)^2 = 0^2 + (-4)^2 = 16. \quad \text{(Satisfied)}$$
   - *General form:*
     $$3^2 + (-6)^2 - 6(3) + 4(-6) - 3 = 9 + 36 - 18 - 24 - 3 = 45 - 45 = 0. \quad \text{(Satisfied)}$$

Both points satisfy both representations identically.

---

## 5. Why Each Step Is Valid
1. **Adding and subtracting $(b/2)^2$** does not change the value of the algebraic expression, creating a perfect square trinomial.
2. **Transferring constants to the right side** calculates the net squared Euclidean distance $R^2$ from the center.
3. **Plugging points into both forms** confirms that no sign slips or arithmetic errors occurred during the reduction.

---

## 6. Final Answer in Words
The canonical form of the circle is $(x - 3)^2 + (y + 2)^2 = 16$. The center of the circle is $S = (3, -2)$ and its radius is $R = 4$. Two points on the circle are $P_1 = (3, 2)$ and $P_2 = (3, -6)$. Both points satisfy the canonical form $(0 + 16 = 16)$ and the original general form $(21 - 21 = 0$ and $45 - 45 = 0)$, proving equivalence.

---

## 7. Quick Verification
- **Leftmost and rightmost points check:**
  Set $y = -2 \implies (x - 3)^2 = 16 \implies x - 3 = \pm 4 \implies P_3 = (7, -2), P_4 = (-1, -2)$.
  Test $P_3(7, -2)$ in general equation:
  $$7^2 + (-2)^2 - 6(7) + 4(-2) - 3 = 49 + 4 - 42 - 8 - 3 = 53 - 53 = 0.$$
  Test $P_4(-1, -2)$ in general equation:
  $$(-1)^2 + (-2)^2 - 6(-1) + 4(-2) - 3 = 1 + 4 + 6 - 8 - 3 = 11 - 11 = 0.$$
  All four cardinal points satisfy both forms.

---

## 8. Common Mistakes to Avoid
- **Sign confusion in center coordinates:** Reading $(x - 3)^2 + (y + 2)^2$ as center $(-3, 2)$ instead of $(+3, -2)$.
- **Adding instead of subtracting when completing square:** Writing $x^2 - 6x = (x - 3)^2 + 9$, which leads to $R^2 = 3 - 9 - 4 = -10$ (a non-existent circle).
- **Forgetting to take the square root of 16:** Stating that the radius is $16$ rather than $\sqrt{16} = 4$.

---

## 9. Classroom Presentation (3-Sentence Summary)
By completing the square on the $x$ and $y$ terms, we rewrite $x^2 - 6x$ as $(x - 3)^2 - 9$ and $y^2 + 4y$ as $(y + 2)^2 - 4$. Moving the subtracted constants to the right side produces the canonical circle equation $(x - 3)^2 + (y + 2)^2 = 16$, revealing a center at $(3, -2)$ and a radius of $4$. We verify this transformation by testing the top and bottom points $(3, 2)$ and $(3, -6)$, both of which satisfy the canonical equation and zero out the original general polynomial.

