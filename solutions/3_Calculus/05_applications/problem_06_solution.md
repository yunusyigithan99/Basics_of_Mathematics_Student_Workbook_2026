# Problem 06: Average Value of a Function and the Mean Value Theorem for Integrals

## 1. Original Problem
Compute the average value of the function
$$f(x) = x^2$$
on the interval $[0, 3]$.

Find a point $c \in [0, 3]$ for which $f(c)$ is equal to this average value, and interpret the result geometrically.

---

## 2. What We Are Trying to Find
1. The exact average value $f_{\text{avg}}$ of $f(x) = x^2$ on the closed interval $[0, 3]$ using the integral definition of the mean.
2. The specific point $c \in [0, 3]$ guaranteed by the Mean Value Theorem for Integrals such that $f(c) = f_{\text{avg}}$.
3. The geometric interpretation of the average value in terms of equivalent rectangular areas and area compensation.

---

## 3. Key Concepts and Theorems
1. **Average (Mean) Value of a Continuous Function:**
   For a continuous function $f(x)$ on $[a, b]$, its average value is defined by:
   $$f_{\text{avg}} = \frac{1}{b - a} \int_a^b f(x)\,dx.$$
2. **Mean Value Theorem for Integrals:**
   If $f$ is continuous on $[a, b]$, there exists at least one number $c \in [a, b]$ such that:
   $$f(c) = f_{\text{avg}} = \frac{1}{b - a} \int_a^b f(x)\,dx \iff \int_a^b f(x)\,dx = f(c)(b - a).$$
3. **Geometric Meaning:**
   The area under the curve $y = f(x)$ over $[a, b]$ is equal to the area of a rectangle with the same base length $(b - a)$ and constant height $f(c)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the definite integral of $f(x) = x^2$ on $[0, 3]$
We evaluate the total accumulated area under the parabola $y = x^2$:
$$\int_0^3 x^2\,dx = \left[\frac{x^3}{3}\right]_0^3 = \frac{3^3}{3} - \frac{0^3}{3} = \frac{27}{3} - 0 = 9.$$

### Step 2: Compute the average value $f_{\text{avg}}$
The width of the interval is:
$$b - a = 3 - 0 = 3.$$
Using the average value formula:
$$f_{\text{avg}} = \frac{1}{b - a} \int_a^b f(x)\,dx = \frac{1}{3} \cdot 9 = 3.$$
Thus, the average value of $x^2$ on $[0, 3]$ is $3$.

### Step 3: Find the point $c \in [0, 3]$ where $f(c) = f_{\text{avg}}$
We solve the equation:
$$f(c) = 3 \iff c^2 = 3.$$
This quadratic equation has two algebraic solutions:
$$c = \pm\sqrt{3}.$$
Since the interval is $[0, 3]$, we reject the negative root $-\sqrt{3}$.
Therefore:
$$c = \sqrt{3} \approx 1.73205.$$
Notice that $0 \le \sqrt{3} \le 3$, so $c = \sqrt{3} \in [0, 3]$.

### Step 4: Geometric interpretation
The relationship has a profound and intuitive geometric meaning:
1. **Equivalent Area of a Rectangle:**
   The area under the curved parabola from $x = 0$ to $x = 3$ is exactly $9$. 
   If we draw a horizontal line at the average height $y = f_{\text{avg}} = 3$, it forms a rectangle on $[0, 3]$ with:
   - Base width: $3 - 0 = 3$,
   - Constant height: $3$.
   The area of this rectangle is:
   $$\text{Area}_{\text{rectangle}} = \text{base} \times \text{height} = 3 \times 3 = 9.$$
   The curved area and the rectangular area are **identical**.

2. **Area Compensation / Leveling:**
   The horizontal line $y = 3$ intersects the curve at $x = \sqrt{3}$:
   - On the left interval $[0, \sqrt{3}]$, the curve is below the average line ($x^2 < 3$). There is an "empty deficit area" between the curve and the line $y = 3$.
   - On the right interval $[\sqrt{3}, 3]$, the curve rises above the average line ($x^2 > 3$). There is an "excess area" sticking out above $y = 3$.
   The Mean Value Theorem proves that the excess area on the right **exactly fills** the deficit area on the left. Imagine the region under the curve made of soft clay: leveling out the curved mound until it becomes a flat tabletop produces a uniform height of exactly $3$.

```text
                  y
                9 |                         * (3, 9)
                  |                        /|
                  |     Excess Area       / |
                3 + - - - - - - * - - - -+ -| y = 3 (Average Height)
                  |            /|: : : : : :|
                  |  Deficit  / |: : : : : :| (Rectangle Area = 3 x 3 = 9)
                  |   Area   /  |: : : : : :|
        ----------+---------*---+-----------+----> x
                  0        √3   |           3
                           c ≈ 1.732
```

---

## 5. Why Each Step Is Valid
- **Step 1:** The polynomial $x^2$ is continuous on $[0, 3]$, satisfying the Fundamental Theorem of Calculus.
- **Step 2:** The definition of continuous average is the limit of arithmetic means of Riemann samples as the partition mesh goes to zero.
- **Step 3:** The Intermediate Value Theorem guarantees that a continuous function attains every value between its minimum ($0$) and maximum ($9$); since $3 \in [0, 9]$, a real solution $c$ is guaranteed.
- **Step 4:** Splitting integrals shows $\int_0^{\sqrt{3}} (3 - x^2)\,dx = \int_{\sqrt{3}}^3 (x^2 - 3)\,dx$, proving exact area balance.

---

## 6. Final Answer in Words
The average value of $f(x) = x^2$ on the interval $[0, 3]$ is $f_{\text{avg}} = 3$. 
The point where the function equals its average value is $c = \sqrt{3} \approx 1.732$. 
Geometrically, this means that the area under the parabolic curve $y = x^2$ over $[0, 3]$ (which equals $9$) is exactly equal to the area of a rectangle with the same base width of $3$ and height $3$. The horizontal line $y = 3$ levels the curve: the excess area above $y = 3$ on $[\sqrt{3}, 3]$ perfectly balances the deficit area below $y = 3$ on $[0, \sqrt{3}]$.

---

## 7. Quick Verification
Verify area compensation:
- Deficit area on $[0, \sqrt{3}]$:
  $$\int_0^{\sqrt{3}} (3 - x^2)\,dx = \left[3x - \frac{x^3}{3}\right]_0^{\sqrt{3}} = 3\sqrt{3} - \frac{3\sqrt{3}}{3} = 2\sqrt{3}.$$
- Excess area on $[\sqrt{3}, 3]$:
  $$\int_{\sqrt{3}}^3 (x^2 - 3)\,dx = \left[\frac{x^3}{3} - 3x\right]_{\sqrt{3}}^3 = (9 - 9) - (\sqrt{3} - 3\sqrt{3}) = 0 - (-2\sqrt{3}) = 2\sqrt{3}.$$
Both areas equal $2\sqrt{3} \approx 3.464$. The cancellation is exact.

---

## 8. Common Mistakes to Avoid
- **Averaging the endpoint values:** Computing $\frac{f(0) + f(3)}{2} = \frac{0 + 9}{2} = 4.5$. This is valid only for linear functions, but completely false for non-linear curves like parabolas.
- **Forgetting to divide by the interval length $(b - a)$:** Giving the total integral $9$ as the average value.
- **Including the negative root $-\sqrt{3}$:** Failing to restrict $c$ to the specified interval $[0, 3]$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The average value of $f(x) = x^2$ on $[0, 3]$ is found by dividing the total integral of $9$ by the interval length of $3$, which gives an average height of $3$. Setting $c^2 = 3$ gives $c = \sqrt{3} \approx 1.732$ as the exact location where the curve reaches this average value. Geometrically, this means the area under the parabolic curve is identical to the area of a $3 \times 3$ rectangle, effectively flattening the curve into a uniform horizontal slab.
