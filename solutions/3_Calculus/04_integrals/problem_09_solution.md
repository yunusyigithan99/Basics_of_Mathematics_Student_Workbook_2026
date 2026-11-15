# Problem 09: Definite Integrals and Signed vs. Geometric Area

## 1. Original Problem
Compute
$$\int_{-1}^{2}x\,dx.$$
Then separately compute the areas of the parts of the graph below and above the $x$-axis and explain the difference between the definite integral and geometric area.

---

## 2. What We Are Trying to Find
1. The exact value of the definite integral $\int_{-1}^{2}x\,dx$ using the Fundamental Theorem of Calculus.
2. The separate geometric areas of the regions enclosed between the line $y = x$ and the $x$-axis on $[-1, 0]$ (below the axis) and $[0, 2]$ (above the axis).
3. The total geometric area of the enclosed shapes.
4. A clear explanation of the difference between **signed area (the definite integral)** and **geometric area (physical area)**.

---

## 3. Key Concepts and Theorems
1. **Fundamental Theorem of Calculus (Newton-Leibniz Formula):**
   If $f$ is continuous on $[a, b]$ and $F$ is an antiderivative of $f$, then:
   $$\int_a^b f(x)\,dx = F(b) - F(a) = [F(x)]_a^b.$$
2. **Signed Area of a Definite Integral:**
   The Riemann integral measures net accumulated signed area:
   $$\int_a^b f(x)\,dx = \text{Area above the } x\text{-axis} - \text{Area below the } x\text{-axis}.$$
3. **Geometric (Total) Area:**
   The physical geometric area enclosed between the curve and the $x$-axis is the integral of the absolute value of the function:
   $$\text{Area}_{\text{geom}} = \int_a^b |f(x)|\,dx = A_{\text{above}} + A_{\text{below}}.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the definite integral analytically
An antiderivative of $f(x) = x$ is:
$$F(x) = \frac{x^2}{2}.$$
Applying the Newton-Leibniz formula on $[-1, 2]$:
$$\int_{-1}^{2}x\,dx = \left[\frac{x^2}{2}\right]_{-1}^{2} = \frac{2^2}{2} - \frac{(-1)^2}{2} = \frac{4}{2} - \frac{1}{2} = \frac{3}{2} = 1.5.$$

### Step 2: Analyze the geometry below the $x$-axis (on $[-1, 0]$)
For $x \in [-1, 0]$, $f(x) \le 0$, so the graph lies below the $x$-axis.
- The region is a right-angled triangle with vertices at $(-1, 0)$, $(0, 0)$, and $(-1, -1)$.
- Base length: $b_1 = 0 - (-1) = 1$.
- Height (vertical distance from axis to $y = -1$): $h_1 = | -1 | = 1$.
- Geometric area $A_1$:
  $$A_1 = \frac{1}{2} \cdot b_1 \cdot h_1 = \frac{1}{2} \cdot 1 \cdot 1 = \frac{1}{2} = 0.5.$$

Notice that the definite integral across this sub-interval is:
$$\int_{-1}^{0}x\,dx = \left[\frac{x^2}{2}\right]_{-1}^{0} = 0 - \frac{(-1)^2}{2} = -\frac{1}{2} = -0.5 = -A_1.$$

### Step 3: Analyze the geometry above the $x$-axis (on $[0, 2]$)
For $x \in [0, 2]$, $f(x) \ge 0$, so the graph lies above the $x$-axis.
- The region is a right-angled triangle with vertices at $(0, 0)$, $(2, 0)$, and $(2, 2)$.
- Base length: $b_2 = 2 - 0 = 2$.
- Height: $h_2 = 2$.
- Geometric area $A_2$:
  $$A_2 = \frac{1}{2} \cdot b_2 \cdot h_2 = \frac{1}{2} \cdot 2 \cdot 2 = 2.$$

The definite integral across this sub-interval is:
$$\int_{0}^{2}x\,dx = \left[\frac{x^2}{2}\right]_{0}^{2} = \frac{2^2}{2} - 0 = 2 = A_2.$$

```text
                  y
                  |            (2, 2)
                  |           /|
                  |          / |
                  |         /  |
                  |   A2   /   | (Height = 2)
                  |       /    |
        ----------+------*-----+----> x
               -1 |     0       2
                 \|      (Base = 2)
      (Height=1)  \
      (-1, -1)     * (Base = 1)
                   | A1
```

### Step 4: Compare the definite integral with the geometric area
We now compare the two concepts directly:

1. **Definite Integral (Net Signed Area):**
   The definite integral weights regions by the sign of the function:
   $$\int_{-1}^{2}x\,dx = \int_{-1}^{0}x\,dx + \int_{0}^{2}x\,dx = -A_1 + A_2 = -\frac{1}{2} + 2 = \frac{3}{2} = 1.5.$$
   The negative area below the axis cancels out part of the positive area above the axis.

2. **Total Geometric Area:**
   Physical area cannot be negative. The total surface area of the two triangular regions combined is:
   $$\text{Total Geometric Area} = A_1 + A_2 = \frac{1}{2} + 2 = \frac{5}{2} = 2.5.$$
   This corresponds to the integral of the absolute value:
   $$\int_{-1}^{2}|x|\,dx = \int_{-1}^{0}(-x)\,dx + \int_{0}^{2}x\,dx = \frac{1}{2} + 2 = 2.5.$$

**Core distinction:**
The definite integral computes the **algebraic balance (signed sum)** of accumulation, allowing opposing signs to cancel. Geometric area measures the **magnitude of space** enclosed, where every piece contributes positively regardless of its position relative to the axis.

---

## 5. Why Each Step Is Valid
- **Step 1:** The polynomial $x$ is continuous on $[-1, 2]$, making the Newton-Leibniz formula applicable.
- **Step 2:** The standard Euclidean formula for the area of a right triangle is $\frac{1}{2} \cdot \text{base} \cdot \text{height}$.
- **Step 3:** The integral is additive over adjacent intervals: $\int_{-1}^2 = \int_{-1}^0 + \int_0^2$.
- **Step 4:** The definition of the Riemann integral includes function signs; geometric area requires the absolute value $|f(x)|$.

---

## 6. Final Answer in Words
The value of the definite integral is $\int_{-1}^{2}x\,dx = \frac{3}{2} = 1.5$. 
The geometric area of the triangle below the $x$-axis on $[-1, 0]$ is $A_1 = \frac{1}{2} = 0.5$. 
The geometric area of the triangle above the $x$-axis on $[0, 2]$ is $A_2 = 2$. 
The difference is that the definite integral computes **signed area**, where the portion below the axis is counted negatively, yielding $A_2 - A_1 = 2 - 0.5 = 1.5$. In contrast, the **geometric area** represents physical space, summing both magnitudes without cancellation: $A_1 + A_2 = 0.5 + 2 = 2.5$.

---

## 7. Quick Verification
- Riemann sum interpretation:
  Splitting into $A_2 - A_1 = 2 - 0.5 = 1.5$.
  Antiderivative calculation: $\frac{2^2 - (-1)^2}{2} = \frac{4 - 1}{2} = \frac{3}{2} = 1.5$.
Both analytical and geometric calculations produce identical results.

---

## 8. Common Mistakes to Avoid
- **Confusing definite integral with geometric area:** Answering $2.5$ for the definite integral, failing to account for the negative sign below the $x$-axis.
- **Sign error when evaluating $(-1)^2$:** Computing $-(-1)^2 = -1$, but carelessly writing $\frac{4}{2} - \frac{-1}{2} = \frac{5}{2}$. The lower limit subtraction gives $-\frac{(-1)^2}{2} = -\frac{1}{2}$.
- **Assuming area can be negative:** Writing $A_1 = -0.5$; geometric area is strictly non-negative ($A_1 = +0.5$), but its contribution to the integral is $-0.5$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Evaluating $\int_{-1}^2 x\,dx$ gives $1.5$ using the antiderivative $x^2/2$ between $-1$ and $2$. Geometrically, this breaks into a triangle of area $0.5$ below the $x$-axis and a triangle of area $2$ above it. The definite integral yields the net signed area $2 - 0.5 = 1.5$, whereas the total geometric area sums both magnitudes to give $2 + 0.5 = 2.5$.
