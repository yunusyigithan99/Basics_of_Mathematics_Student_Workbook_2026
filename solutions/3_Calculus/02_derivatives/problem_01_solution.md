# Problem 1 Solution: Derivative of a Polynomial and the Slope of a Tangent Line

## 1. Original Problem
For the polynomial function:
$$f(x) = 3x^5 - 2x^3 + 7x - 4$$
1. Find the general derivative $f'(x)$.
2. Compute the exact values $f'(0)$ and $f'(1)$.
3. Determine the algebraic signs of the obtained values.
4. Explain what these values and signs reveal about the slope, inclination, and direction of the tangent line to the graph of $f(x)$ at $x = 0$ and $x = 1$.

---

## 2. What We Are Trying to Find
We need to:
1. Apply the power rule, constant multiple rule, and sum/difference rule of differentiation to find $f'(x)$.
2. Evaluate $f'(0)$ and $f'(1)$.
3. Interpret the derivative geometrically as the slope $m = \tan \alpha = f'(x_0)$ of the tangent line.
4. Conclude whether the graph is increasing, decreasing, or flat at these specific points.

---

## 3. Key Concepts and Theorems
1. **The Power Rule:**
   For any real exponent $n$:
   $$\frac{d}{dx}[x^n] = n x^{n-1}.$$
2. **Linearity of Differentiation:**
   For constants $c_1, c_2$ and differentiable functions $u(x), v(x)$:
   $$\frac{d}{dx}[c_1 u(x) \pm c_2 v(x)] = c_1 u'(x) \pm c_2 v'(x).$$
   The derivative of any constant is zero: $\frac{d}{dx}[c] = 0$.
3. **Geometric Interpretation of the Derivative:**
   The derivative $f'(x_0)$ represents the instantaneous rate of change of $f$ at $x_0$, which equals the slope $m$ of the tangent line to the curve $y = f(x)$ at the point $(x_0, f(x_0))$:
   - If $f'(x_0) > 0$, the tangent line has positive slope (slants upward to the right), and the function is strictly increasing near $x_0$.
   - If $f'(x_0) < 0$, the tangent line has negative slope (slants downward to the right), and the function is strictly decreasing near $x_0$.
   - If $f'(x_0) = 0$, the tangent line is horizontal.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Differentiate Term by Term
Differentiate each term of $f(x) = 3x^5 - 2x^3 + 7x - 4$ using the power rule:
1. For $3x^5$:
   $$\frac{d}{dx}[3x^5] = 3 \cdot (5x^{5-1}) = 15x^4.$$
2. For $-2x^3$:
   $$\frac{d}{dx}[-2x^3] = -2 \cdot (3x^{3-1}) = -6x^2.$$
3. For $7x = 7x^1$:
   $$\frac{d}{dx}[7x] = 7 \cdot (1x^{1-1}) = 7x^0 = 7(1) = 7.$$
4. For $-4$ (constant):
   $$\frac{d}{dx}[-4] = 0.$$

Combine the differentiated terms:
$$f'(x) = 15x^4 - 6x^2 + 7.$$

---

### Step 2: Compute $f'(0)$ and Interpret Geometrically
Substitute $x = 0$ into the derivative formula:
$$f'(0) = 15(0)^4 - 6(0)^2 + 7 = 0 - 0 + 7 = 7.$$
- **Value and Sign:** $f'(0) = 7 > 0$ (strictly positive).
- **Geometric Interpretation:**
  At $x = 0$, the slope of the tangent line is $m = 7$.
  Because $m > 0$, the tangent line rises steeply from left to right at an angle of $\alpha = \arctan(7) \approx 81.87^\circ$ relative to the positive $x$-axis. The function $f(x)$ is strictly increasing at $x = 0$ at a rate of 7 vertical units per horizontal unit.

---

### Step 3: Compute $f'(1)$ and Interpret Geometrically
Substitute $x = 1$ into the derivative formula:
$$f'(1) = 15(1)^4 - 6(1)^2 + 7 = 15(1) - 6(1) + 7 = 15 - 6 + 7 = 16.$$
- **Value and Sign:** $f'(1) = 16 > 0$ (strictly positive).
- **Geometric Interpretation:**
  At $x = 1$, the slope of the tangent line is $m = 16$.
  Because $16 > 7 > 0$, the curve is increasing more than twice as steeply as it was at $x = 0$. The tangent line is nearly vertical, slanting upward at an angle of $\alpha = \arctan(16) \approx 86.42^\circ$.

---

## 5. Why Each Step Is Valid
1. **Term-by-term differentiation** is valid because differentiation is a linear operator over the algebra of polynomials.
2. **Applying the power rule $n x^{n-1}$** is valid for all positive integers $n \ge 1$.
3. **Equating $f'(x_0)$ to the tangent slope** is the foundational theorem of differential calculus established by Newton and Leibniz.

---

## 6. Final Answer in Words
The derivative of the polynomial is $f'(x) = 15x^4 - 6x^2 + 7$. Evaluating at the given points yields $f'(0) = 7$ and $f'(1) = 16$. Both values are strictly positive ($> 0$), which indicates that the tangent lines at both $x = 0$ and $x = 1$ have positive slopes, slanting steeply upwards to the right. This proves that the function is strictly increasing at both points, with the rate of climb being significantly steeper at $x = 1$ ($m = 16$) than at $x = 0$ ($m = 7$).

---

## 7. Quick Verification
- **Minimum slope analysis:**
  Notice that $f'(x) = 15(x^2)^2 - 6(x^2) + 7$.
  Let $u = x^2 \ge 0$. Then $g(u) = 15u^2 - 6u + 7$.
  The minimum of this quadratic occurs at $u = \frac{6}{30} = \frac{1}{5} = 0.2$.
  The minimum value is $g(0.2) = 15(0.04) - 6(0.2) + 7 = 0.6 - 1.2 + 7 = 6.4 > 0$.
  Because $f'(x) \ge 6.4$ for all $x \in \mathbb{R}$, the derivative is **always positive everywhere**, meaning the function is strictly increasing on its entire domain and the tangent slope is never negative or zero.

---

## 8. Common Mistakes to Avoid
- **Differentiating a constant into 1:** Writing $\frac{d}{dx}[-4] = -1$ or leaving it as $-4$. The derivative of any standalone constant is 0.
- **Forgetting to subtract 1 from the exponent:** Writing $\frac{d}{dx}[x^5] = 5x^5$.
- **Confusing tangent slope with function value:** Thinking $f'(0)$ gives the $y$-intercept ($f(0) = -4$), rather than the rate of change ($f'(0) = 7$).

---

## 9. Classroom Presentation (3-Sentence Summary)
Applying the power and constant multiple rules term by term gives the derivative $f'(x) = 15x^4 - 6x^2 + 7$. Evaluating at $x = 0$ and $x = 1$ produces $f'(0) = 7$ and $f'(1) = 16$, both of which are strictly positive numbers. Geometrically, these positive values represent the slopes of the tangent lines, proving that the graph is climbing steeply to the right at both points, with an even steeper incline at $x = 1$ than at $x = 0$.
