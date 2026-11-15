# Problem 13: The Accumulation Function and the Fundamental Theorem of Calculus

## 1. Original Problem
Let
$$F(x) = \int_0^x (t^2 + 1)\,dt.$$
Determine $F(x)$, compute $F'(x)$, and compare the result with the integrand. Explain in your own words why the height of the function describes the local rate of increase of the accumulated area.

---

## 2. What We Are Trying to Find
1. An explicit algebraic formula for the accumulation function $F(x)$ by evaluating the definite integral with variable upper limit $x$.
2. The derivative $F'(x)$ with respect to $x$.
3. A formal comparison between $F'(x)$ and the original integrand $f(t) = t^2 + 1$.
4. A physical and geometric explanation in intuitive prose of why the rate of change of accumulated area equals the instantaneous height of the curve (Fundamental Theorem of Calculus, Part 1).

---

## 3. Key Concepts and Theorems
1. **The Fundamental Theorem of Calculus (Part 1):**
   If $f$ is continuous on an interval containing $a$, then the area accumulation function
   $$F(x) = \int_a^x f(t)\,dt$$
   is differentiable on that interval, and its derivative is simply the integrand evaluated at the upper limit:
   $$F'(x) = \frac{d}{dx}\left[\int_a^x f(t)\,dt\right] = f(x).$$
2. **Dummy Variable of Integration:**
   In $\int_0^x f(t)\,dt$, $t$ is a dummy integration variable (the horizontal coordinate being summed over), while $x$ is the independent variable representing the right boundary of the accumulating region.
3. **Differential Area Strip:**
   An incremental horizontal change $dx$ accumulates a rectangular area strip of height $f(x)$ and width $dx$, so $dF = f(x)\,dx \implies \frac{dF}{dx} = f(x)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Evaluate the integral to determine $F(x)$ explicitly
We treat $x$ as a fixed upper limit and integrate the polynomial $t^2 + 1$ with respect to the integration variable $t$:
$$\int (t^2 + 1)\,dt = \frac{t^3}{3} + t.$$
Applying the limits from $t = 0$ to $t = x$:
$$F(x) = \left[\frac{t^3}{3} + t\right]_0^x = \left(\frac{x^3}{3} + x\right) - \left(\frac{0^3}{3} + 0\right).$$
Simplifying:
$$F(x) = \frac{x^3}{3} + x.$$

### Step 2: Differentiate $F(x)$ with respect to $x$
Now, we differentiate the resulting function $F(x)$ using standard power rules:
$$F'(x) = \frac{d}{dx}\left(\frac{x^3}{3} + x\right) = \frac{1}{3} \cdot (3x^2) + 1 = x^2 + 1.$$

### Step 3: Compare $F'(x)$ with the integrand
- The original integrand was $f(t) = t^2 + 1$.
- Evaluating this integrand at $t = x$ yields $f(x) = x^2 + 1$.
- We observe that:
  $$F'(x) = f(x) = x^2 + 1.$$
The derivative of the accumulation function $F(x)$ exactly reproduces the integrand function evaluated at the upper boundary. This is a direct verification of the Fundamental Theorem of Calculus.

### Step 4: Explain why the height describes the rate of area accumulation
Consider what happens geometrically when the right edge of the accumulated area moves from $x$ to $x + \Delta x$:
1. **Added area $\Delta F$:**
   The change in accumulated area is the area of a thin vertical slice between $t = x$ and $t = x + \Delta x$:
   $$\Delta F = F(x + \Delta x) - F(x) = \int_x^{x + \Delta x} f(t)\,dt.$$
2. **Approximation as a rectangle:**
   For a very small step $\Delta x$, the continuous curve $f(t)$ barely changes height across the narrow interval $[x, x + \Delta x]$. The added slice is virtually a rectangle with:
   - Width equal to $\Delta x$,
   - Height equal to the value of the function at the boundary, $f(x)$.
   Therefore:
   $$\Delta F \approx \text{Height} \times \text{Width} = f(x) \cdot \Delta x.$$
3. **The rate of accumulation:**
   Dividing the change in area by the horizontal step size gives the average rate of area increase:
   $$\frac{\Delta F}{\Delta x} \approx f(x).$$
4. **Taking the limit as $\Delta x \to 0$:**
   $$\lim_{\Delta x \to 0} \frac{F(x + \Delta x) - F(x)}{\Delta x} = F'(x) = f(x).$$

**Intuitive analogy (The paint roller):**
Imagine rolling paint horizontally across a wall. If the paint roller has width $dx$, the amount of paint applied per unit of forward movement depends entirely on how tall the roller is at that moment. Where the function graph is tall ($f(x)$ is large), advancing the edge adds area rapidly. Where the function is low ($f(x)$ is near zero), advancing the edge adds area very slowly. Hence, the local vertical height $f(x)$ directly controls the instantaneous speed of area accumulation.

```text
                  y
                  |            f(t) = t^2 + 1
                  |                   /
                  |                  /|
                  |            f(x) | |
                  |            ---  | |
                  |                 | |
                  |  Accumulated    | | New strip: ΔF ≈ f(x) · Δx
                  |    Area F(x)    | | (Width Δx, Height f(x))
        ----------+-----------------+-+--------> t
                  0                 x x+Δx
```

---

## 5. Why Each Step Is Valid
- **Step 1:** The polynomial $t^2 + 1$ is continuous everywhere, so its antiderivative is well-defined and evaluates directly via the Newton-Leibniz formula.
- **Step 2:** Differentiating a polynomial term by term follows standard power rules.
- **Step 3:** The definition of the Fundamental Theorem of Calculus states that $\frac{d}{dx} \int_a^x f(t)\,dt = f(x)$.
- **Step 4:** The Mean Value Theorem for Integrals guarantees there exists $c \in [x, x + \Delta x]$ such that $\int_x^{x+\Delta x} f(t)\,dt = f(c)\Delta x$; as $\Delta x \to 0$, $c \to x$, and $f(c) \to f(x)$ by continuity.

---

## 6. Final Answer in Words
The accumulation function is:
$$F(x) = \frac{x^3}{3} + x.$$
Its derivative is:
$$F'(x) = x^2 + 1,$$
which is identical to the integrand $f(x) = x^2 + 1$. 
The height of the function represents the local rate of increase of accumulated area because nudging the upper boundary forward by an infinitesimal step $dx$ adds a thin vertical strip of area $dF \approx f(x) \cdot dx$. Dividing this added area by the step width $dx$ yields $\frac{dF}{dx} = f(x)$, showing that the rate at which area is swept out is determined directly by the height of the curve at that boundary.

---

## 7. Quick Verification
- At $x = 1$:
  $F(1) = \frac{1}{3} + 1 = \frac{4}{3}$.
  $F'(1) = 1^2 + 1 = 2$.
  Integrand at $1$: $f(1) = 1^2 + 1 = 2$.
- At $x = 2$:
  $F(2) = \frac{8}{3} + 2 = \frac{14}{3}$.
  $F'(2) = 2^2 + 1 = 5$.
  Integrand at $2$: $f(2) = 2^2 + 1 = 5$.
$F'(x) = f(x)$ holds at every single point.

---

## 8. Common Mistakes to Avoid
- **Confusing the dummy variable $t$ with the limit variable $x$:** Writing $\int_0^x (x^2 + 1)\,dx$, which uses $x$ in two conflicting mathematical roles simultaneously.
- **Treating $x$ in the upper limit as a constant:** Trying to evaluate the integral as a number rather than as a function of the upper limit $x$.
- **Believing that differentiating an integral gives zero:** Forgetting that the upper limit is a variable, so Leibniz's rule applies.

---

## 9. Classroom Presentation (3-Sentence Summary)
Integrating $t^2 + 1$ from $0$ to $x$ produces the accumulation function $F(x) = x^3/3 + x$, whose derivative is exactly $x^2 + 1$. This directly illustrates the Fundamental Theorem of Calculus, confirming that differentiation and integration are inverse operations. Geometrically, moving the boundary forward by a tiny width $dx$ adds a rectangular strip of area $f(x) \cdot dx$, which means the height of the curve is the exact rate at which area accumulates.
