# Problem 6 Solution: Shifted Ellipse by Completing the Square

## 1. Original Problem
Reduce the general second-degree equation
$$4x^2 + 9y^2 - 16x + 18y - 11 = 0$$
to canonical form. Find the coordinates of the center and the lengths of the semiaxes. Finally, check that substituting the coordinates of the center into the left-hand side of the general equation gives a value consistent with the canonical form obtained.

---

## 2. What We Are Trying to Find
We need to:
1. Group $x$-terms and $y$-terms and factor out the leading quadratic coefficients $4$ and $9$.
2. Complete the squares inside each grouped expression.
3. Balance constants to write the equation in standard form $\frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1$.
4. Identify the center $(x_0, y_0)$ and the semiaxes $a$ and $b$.
5. Evaluate the polynomial at the center point $(x_0, y_0)$ to verify that it equals $-C_{\text{balance}} = -36$.

---

## 3. Key Concepts and Theorems
1. **Canonical Form of a Translated Ellipse:**
   $$\frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1,$$
   where $(x_0, y_0)$ is the shifted center of symmetry, $a$ is the horizontal semiaxis, and $b$ is the vertical semiaxis.
2. **Completing the Square with Leading Coefficients:**
   $$A x^2 + B x = A\left(x^2 + \frac{B}{A}x\right) = A\left[\left(x + \frac{B}{2A}\right)^2 - \left(\frac{B}{2A}\right)^2\right].$$
3. **Value of the Polynomial at the Center:**
   If a quadratic equation reduces to $A(x - x_0)^2 + B(y - y_0)^2 - K = 0$, evaluating at the center $(x_0, y_0)$ causes both squared terms to vanish, leaving:
   $$f(x_0, y_0) = -K.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Group Terms and Factor Leading Coefficients
Move the constant $-11$ to the right-hand side and group terms by variable:
$$(4x^2 - 16x) + (9y^2 + 18y) = 11.$$
Factor the coefficient $4$ from the $x$-terms and $9$ from the $y$-terms:
$$4(x^2 - 4x) + 9(y^2 + 2y) = 11.$$

### Step 2: Complete the Squares Inside the Parentheses
- For $x^2 - 4x$:
  $$x^2 - 4x = (x - 2)^2 - 2^2 = (x - 2)^2 - 4.$$
- For $y^2 + 2y$:
  $$y^2 + 2y = (y + 1)^2 - 1^2 = (y + 1)^2 - 1.$$

### Step 3: Distribute and Combine Constants
Substitute the completed squares back into the factored equation:
$$4\big((x - 2)^2 - 4\big) + 9\big((y + 1)^2 - 1\big) = 11$$
$$4(x - 2)^2 - 16 + 9(y + 1)^2 - 9 = 11.$$
Combine constant numbers on the left:
$$-16 - 9 = -25.$$
Add $25$ to both sides:
$$4(x - 2)^2 + 9(y + 1)^2 = 11 + 25 = 36.$$

### Step 4: Divide by the Right-Hand Constant
Divide both sides by $36$ to achieve $1$ on the right-hand side:
$$\frac{4(x - 2)^2}{36} + \frac{9(y + 1)^2}{36} = \frac{36}{36}$$
$$\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1.$$
In terms of squared semiaxes:
$$\frac{(x - 2)^2}{3^2} + \frac{(y + 1)^2}{2^2} = 1.$$

### Step 5: Identify the Center and Semiaxis Lengths
Comparing with $\frac{(x - x_0)^2}{a^2} + \frac{(y - y_0)^2}{b^2} = 1$:
- **Center:**
  $$S = (x_0, y_0) = (2, -1)$$
- **Horizontal semi-major axis length:**
  $$a = \sqrt{9} = 3$$
- **Vertical semi-minor axis length:**
  $$b = \sqrt{4} = 2$$

### Step 6: Check Substituting the Center into the Left-Hand Side
Define the left-hand side function of the original general equation:
$$f(x, y) = 4x^2 + 9y^2 - 16x + 18y - 11.$$
Substitute the coordinates of the center $x = 2$ and $y = -1$:
$$f(2, -1) = 4(2)^2 + 9(-1)^2 - 16(2) + 18(-1) - 11$$
$$= 4(4) + 9(1) - 32 - 18 - 11$$
$$= 16 + 9 - 32 - 18 - 11 = 25 - 61 = -36.$$

**Consistency Explanation:**
From our reduction, the general equation can be written identically as:
$$4(x - 2)^2 + 9(y + 1)^2 - 36 = 0.$$
At the center $(x, y) = (2, -1)$, the two translated displacement terms vanish:
$$4(2 - 2)^2 + 9(-1 + 1)^2 - 36 = 4(0) + 9(0) - 36 = -36.$$
The direct substitution $f(2, -1) = -36$ matches the balance constant $-36$ from the completed square formulation, proving that the algebra is fully consistent.

---

## 5. Why Each Step Is Valid
1. **Factoring the quadratic coefficients $4$ and $9$** is required so that the terms inside parentheses are monic ($1 \cdot x^2$ and $1 \cdot y^2$).
2. **Balancing the equation** adds $4 \times 4 = 16$ and $9 \times 1 = 9$ to the right side, strictly preserving algebraic equality.
3. **The evaluation $f(x_0, y_0) = -36$** is valid because the center is the stationary point of the quadratic form where all linear gradients $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ vanish.

---

## 6. Final Answer in Words
The canonical form of the ellipse is $\frac{(x - 2)^2}{9} + \frac{(y + 1)^2}{4} = 1$. The center of the ellipse is $S = (2, -1)$. The horizontal semi-major axis has length $a = 3$, and the vertical semi-minor axis has length $b = 2$. Substituting the center coordinates $(2, -1)$ into the left-hand side of the original equation yields $-36$, which precisely matches the constant $-36$ from the completed square identity $4(x - 2)^2 + 9(y + 1)^2 - 36 = 0$.

---

## 7. Quick Verification
- **Test vertices of the ellipse:**
  - Right vertex: $(x_0 + a, y_0) = (2 + 3, -1) = (5, -1)$.
    Substitute into original equation:
    $$4(5)^2 + 9(-1)^2 - 16(5) + 18(-1) - 11 = 4(25) + 9(1) - 80 - 18 - 11 = 109 - 109 = 0.$$
  - Top co-vertex: $(x_0, y_0 + b) = (2, -1 + 2) = (2, 1)$.
    Substitute into original equation:
    $$4(2)^2 + 9(1)^2 - 16(2) + 18(1) - 11 = 4(4) + 9(1) - 32 + 18 - 11 = (16 + 9 + 18) - (32 + 11) = 43 - 43 = 0.$$
  Both vertices lie exactly on the original curve.

---

## 8. Common Mistakes to Avoid
- **Forgetting to multiply the squared constant by the leading coefficient:** Adding $4$ and $1$ to the right side instead of $4 \times 4 = 16$ and $9 \times 1 = 9$.
- **Sign slips in center coordinates:** Reading $(x - 2)$ and $(y + 1)$ as center $(-2, 1)$ instead of $(+2, -1)$.
- **Division error:** Dividing 36 by 4 and getting 8 instead of 9.

---

## 9. Classroom Presentation (3-Sentence Summary)
We group the $x$ and $y$ terms and factor out the coefficients 4 and 9, allowing us to complete the squares as $4(x - 2)^2 - 16$ and $9(y + 1)^2 - 9$. Moving the constants gives $4(x - 2)^2 + 9(y + 1)^2 = 36$, which upon dividing by 36 yields the canonical ellipse equation $(x - 2)^2/9 + (y + 1)^2/4 = 1$, identifying center $(2, -1)$ and semiaxes 3 and 2. Substituting the center $(2, -1)$ into the original equation evaluates to $-36$, which perfectly matches the vanishing of the two squared terms and verifies the calculation.

