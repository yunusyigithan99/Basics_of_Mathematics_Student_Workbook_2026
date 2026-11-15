# Problem 10: Bounding, Estimation, and Exact Calculation of a Definite Integral

## 1. Original Problem
Before carrying out the exact calculation, estimate the possible range of values of the integral
$$\int_0^2(x^2 + 1)\,dx,$$
using
$$1 \le x^2 + 1 \le 5$$
on $[0, 2]$. Only then compute the integral exactly, compare the result with the earlier estimate, and explain what type of computational error such a check can detect.

---

## 2. What We Are Trying to Find
1. An a priori lower and upper bound (interval estimate) for the integral using the comparison property of Riemann integrals.
2. The exact evaluation of $\int_0^2(x^2 + 1)\,dx$ via the Fundamental Theorem of Calculus.
3. Verification that the exact value falls strictly within the predicted bounds.
4. An analysis of the specific categories of mathematical and computational errors that this estimation technique reliably catches.

---

## 3. Key Concepts and Theorems
1. **Comparison / Bounding Property of Integrals:**
   If a function $f$ is continuous on $[a, b]$ with minimum value $m$ and maximum value $M$ such that $m \le f(x) \le M$ for all $x \in [a, b]$, then:
   $$m(b - a) \le \int_a^b f(x)\,dx \le M(b - a).$$
2. **Fundamental Theorem of Calculus (Newton-Leibniz Formula):**
   $$\int_a^b f(x)\,dx = [F(x)]_a^b = F(b) - F(a).$$
3. **Power Rule for Polynomials:**
   $$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Establish the a priori range of values (Estimation)
We are given the integrand $f(x) = x^2 + 1$ on the interval $[0, 2]$.
Because $x^2$ is strictly increasing for $x \ge 0$:
- At the left endpoint $x = 0$: $f(0) = 0^2 + 1 = 1$ (the absolute minimum $m$).
- At the right endpoint $x = 2$: $f(2) = 2^2 + 1 = 5$ (the absolute maximum $M$).

Thus, on $[0, 2]$:
$$1 \le x^2 + 1 \le 5.$$

The width of the interval of integration is:
$$b - a = 2 - 0 = 2.$$

Applying the integral bounding property:
$$\int_0^2 1\,dx \le \int_0^2 (x^2 + 1)\,dx \le \int_0^2 5\,dx.$$
Since $\int_a^b c\,dx = c(b - a)$:
$$1 \cdot (2 - 0) \le \int_0^2 (x^2 + 1)\,dx \le 5 \cdot (2 - 0),$$
$$2 \le \int_0^2 (x^2 + 1)\,dx \le 10.$$
Before performing any integration, we know with mathematical certainty that the true value must lie between $2$ and $10$.

### Step 2: Compute the exact value of the integral
We find an antiderivative of $f(x) = x^2 + 1$:
$$F(x) = \frac{x^3}{3} + x.$$
Applying the Newton-Leibniz formula on $[0, 2]$:
$$\int_0^2 (x^2 + 1)\,dx = \left[\frac{x^3}{3} + x\right]_0^2$$
$$= \left(\frac{2^3}{3} + 2\right) - \left(\frac{0^3}{3} + 0\right)$$
$$= \left(\frac{8}{3} + 2\right) - 0$$
$$= \frac{8}{3} + \frac{6}{3} = \frac{14}{3} \approx 4.667.$$

### Step 3: Compare the exact result with the estimate
We compare the exact result $\frac{14}{3} \approx 4.67$ with the predicted interval $[2, 10]$:
$$2 < \frac{14}{3} < 10 \iff 2 < 4.667 < 10.$$
The result is completely consistent with the bounds. Furthermore, because $x^2$ curves upward (strictly convex), the area is slightly below the midpoint of the bounds: $\frac{2 + 10}{2} = 6$, which matches geometric intuition (the curve sits below its secant line).

### Step 4: What types of computational errors does this check detect?
A quick pre-calculation estimate serves as an invaluable sanity check capable of detecting:
1. **Sign errors:** 
   If a student inadvertently swaps limits or introduces an extraneous minus sign and obtains a negative answer (e.g., $-4.67$), the estimate immediately flags it as impossible, since the entire region lies above the $x$-axis and the integral must be at least $+2$.
2. **Gross arithmetic or exponent errors:**
   - Forgetting the denominator $3$ in the antiderivative produces $2^3 + 2 = 10$, which hits the theoretical upper ceiling for a flat line of height $5$, signaling an error.
   - Differentiating instead of integrating gives $[2x]_0^2 = 4$, which is accidentally inside the range, but for functions where $f'$ is small, it would fall outside.
3. **Order-of-magnitude mistakes:**
   Multiplying or dividing by unintended factors (e.g., obtaining $14$ or $0.46$) is immediately caught because the answer falls completely outside $[2, 10]$.

---

## 5. Why Each Step Is Valid
- **Step 1:** The preservation of inequalities under integration guarantees that if $g(x) \le f(x) \le h(x)$, then $\int g \le \int f \le \int h$.
- **Step 2:** The function $x^2 + 1$ is continuous on $[0, 2]$, satisfying the conditions of the Fundamental Theorem of Calculus.
- **Step 3:** The exact fraction $14/3 \approx 4.67$ is strictly bounded by $2$ and $10$.
- **Step 4:** A physical or geometric bound acts as an invariant filter against common mechanical mistakes.

---

## 6. Final Answer in Words
Using the bounds $1 \le x^2 + 1 \le 5$ on the interval $[0, 2]$ of width $2$, the integral is estimated to lie within:
$$2 \le \int_0^2 (x^2 + 1)\,dx \le 10.$$
The exact calculation gives:
$$\int_0^2 (x^2 + 1)\,dx = \left[\frac{x^3}{3} + x\right]_0^2 = \frac{8}{3} + 2 = \frac{14}{3} \approx 4.67,$$
which comfortably falls inside $[2, 10]$. 
This estimation method reliably detects sign errors (e.g., yielding negative values), order-of-magnitude mistakes, and missing denominators from differentiation/integration power rules.

---

## 7. Quick Verification
- Average value of the function on $[0, 2]$:
  $f_{\text{avg}} = \frac{1}{2 - 0} \int_0^2 (x^2 + 1)\,dx = \frac{1}{2} \cdot \frac{14}{3} = \frac{7}{3} \approx 2.33$.
  Since $1 \le f(x) \le 5$, an average value of $2.33$ is reasonable and realistic.

---

## 8. Common Mistakes to Avoid
- **Evaluating limits into the original function instead of the antiderivative:**
  Writing $f(2) - f(0) = 5 - 1 = 4$.
- **Arithmetic errors with fractions:**
  Writing $\frac{8}{3} + 2 = \frac{10}{3}$. Remember to find a common denominator: $2 = \frac{6}{3}$, so $\frac{8 + 6}{3} = \frac{14}{3}$.
- **Assuming the average must be $(1+5)/2 = 3$:**
  Because the curve is parabolic and not a straight line, the average is not simply the arithmetic mean of the endpoints.

---

## 9. Classroom Presentation (3-Sentence Summary)
Because $x^2 + 1$ ranges between $1$ and $5$ on the interval $[0, 2]$, multiplying by the interval width of $2$ guarantees the integral must lie between $2$ and $10$. Carrying out the exact integration yields $[x^3/3 + x]_0^2 = 14/3 \approx 4.67$, which comfortably satisfies our estimated bounds. Performing this initial estimate is a crucial diagnostic habit because it immediately exposes sign errors, misplaced denominators, and order-of-magnitude blunders.
