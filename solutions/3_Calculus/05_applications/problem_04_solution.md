# Problem 04: Area Between Intersecting Curves

## 1. Original Problem
Find the area of the region bounded by the graphs
$$y = x$$
and
$$y = x^2.$$
First find the intersection points and justify which function is greater on the relevant interval.

---

## 2. What We Are Trying to Find
1. The exact coordinates of the intersection points of the line $y = x$ and the parabola $y = x^2$.
2. An algebraic and geometric justification of which curve lies on top ($y_{\text{upper}}$ vs. $y_{\text{lower}}$) on the interval between the intersection points.
3. The definite integral representing the area of the bounded region.
4. The exact numerical and fractional value of the enclosed area.

---

## 3. Key Concepts and Theorems
1. **Intersection of Curves:**
   The horizontal boundaries of an enclosed region between two curves $y = f(x)$ and $y = g(x)$ are the solutions to $f(x) = g(x)$.
2. **Area Between Curves Formula:**
   If $f(x) \ge g(x)$ for all $x \in [a, b]$, the area of the region bounded by the two graphs and vertical lines $x = a$ and $x = b$ is:
   $$\text{Area} = \int_a^b [f(x) - g(x)]\,dx.$$
3. **Power Rule of Integration:**
   $$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Find the intersection points
To find where the line $y = x$ and the parabola $y = x^2$ intersect, we equate the two equations:
$$x = x^2.$$
Rearrange the equation into standard quadratic form:
$$x^2 - x = 0.$$
Factor out $x$:
$$x(x - 1) = 0.$$
This yields two real solutions:
$$x_1 = 0, \qquad x_2 = 1.$$

Substituting these $x$-values into $y = x$:
- For $x = 0$: $y = 0 \implies (0, 0)$.
- For $x = 1$: $y = 1 \implies (1, 1)$.

The curves intersect at the origin $(0, 0)$ and at $(1, 1)$. The relevant interval of integration is $[0, 1]$.

### Step 2: Justify which function is greater on $(0, 1)$
We must determine whether $x > x^2$ or $x^2 > x$ on the open interval $(0, 1)$:
1. **Algebraic Proof:**
   Consider the difference:
   $$x - x^2 = x(1 - x).$$
   For any $x \in (0, 1)$, both factors are strictly positive:
   $$x > 0 \quad \text{and} \quad 1 - x > 0.$$
   Therefore, their product is positive:
   $$x(1 - x) > 0 \iff x > x^2.$$
   Hence, the line $y = x$ lies strictly **above** the parabola $y = x^2$ on $(0, 1)$.

2. **Test Point Check:**
   At the midpoint $x = 0.5 = \frac{1}{2}$:
   - Line: $y_{\text{line}} = \frac{1}{2} = 0.5$.
   - Parabola: $y_{\text{parabola}} = \left(\frac{1}{2}\right)^2 = \frac{1}{4} = 0.25$.
   Since $0.5 > 0.25$, the line is upper and the parabola is lower.

```text
                  y
                1 |                 *(1, 1)
                  |               / |
                  |              /  |
                  |     y = x   /   |
                  |            / *  |  y = x^2
                  |           / .   |
                  |          /.     |
        ----------+---------*-------+----> x
                  0        (0,0)    1
```

### Step 3: Set up and evaluate the integral
Using the area formula $\int_a^b (y_{\text{upper}} - y_{\text{lower}})\,dx$:
$$\text{Area} = \int_0^1 (x - x^2)\,dx.$$
Integrate term by term:
$$\int (x - x^2)\,dx = \frac{x^2}{2} - \frac{x^3}{3}.$$
Apply the limits from $x = 0$ to $x = 1$ via the Newton-Leibniz formula:
$$\text{Area} = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1$$
$$= \left(\frac{1^2}{2} - \frac{1^3}{3}\right) - \left(\frac{0^2}{2} - \frac{0^3}{3}\right)$$
$$= \left(\frac{1}{2} - \frac{1}{3}\right) - 0.$$
Find a common denominator ($6$):
$$\text{Area} = \frac{3}{6} - \frac{2}{6} = \frac{1}{6}.$$

---

## 5. Why Each Step Is Valid
- **Step 1:** Equating function rules finds common points of continuous curves.
- **Step 2:** Comparing heights guarantees that the integrand $(y_{\text{upper}} - y_{\text{lower}})$ is non-negative, ensuring a positive geometric area.
- **Step 3:** The definite integral of the difference of two functions computes the exact net area bounded between them.

---

## 6. Final Answer in Words
The intersection points of $y = x$ and $y = x^2$ are $(0, 0)$ and $(1, 1)$. 
On the interval $(0, 1)$, the line $y = x$ is greater than the parabola $y = x^2$ because squaring a number strictly between $0$ and $1$ reduces its value ($x(1 - x) > 0$). 
The area of the enclosed crescent region is:
$$\int_0^1 (x - x^2)\,dx = \frac{1}{6} \approx 0.167.$$

---

## 7. Quick Verification
- Geometric bounding box:
  The region is enclosed inside the unit square $[0, 1] \times [0, 1]$ of area $1$.
  The triangle under the line $y = x$ on $[0, 1]$ has area $\frac{1}{2}(1)(1) = \frac{1}{2} = \frac{3}{6}$.
  The area under the parabola $y = x^2$ on $[0, 1]$ is $\int_0^1 x^2\,dx = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3} = \frac{2}{6}$.
  Subtracting the area under the parabola from the area under the line:
  $$\text{Area} = \frac{3}{6} - \frac{2}{6} = \frac{1}{6}.$$
The two independent integration methods match perfectly.

---

## 8. Common Mistakes to Avoid
- **Reversing the subtraction:** Integrating $x^2 - x$, which gives $-\frac{1}{6}$. Area is always a positive geometric quantity.
- **Assuming $x^2$ is always larger than $x$:** Extrapolating the fact that $x^2 > x$ for $x > 1$ into the interval $(0, 1)$, where the opposite is true.
- **Integrating beyond the intersection points:** Choosing limits such as $[-1, 1]$ without checking where the two curves actually intersect.

---

## 9. Classroom Presentation (3-Sentence Summary)
Setting $x = x^2$ shows that the curves intersect at $x = 0$ and $x = 1$. On this interval, the straight line $y = x$ lies strictly above the parabola $y = x^2$ because squaring any number between zero and one makes it smaller. Integrating the vertical distance between the curves, $\int_0^1 (x - x^2)\,dx$, yields an exact bounded area of $1/6$.
