# Problem 13: Analysis of the Function $f(x) = \frac{\ln x}{x}$

## 1. Original Problem
Perform a complete analysis of
$$f(x) = \frac{\ln x}{x}, \qquad x > 0.$$
Find the maximum and the behavior at the ends of the domain. Explain which information is necessary for a correct sketch.

---

## 2. What We Are Trying to Find
1. The domain of definition $D_f$.
2. The behavior at the boundary points of the domain: $\lim_{x \to 0^+} f(x)$ and $\lim_{x \to \infty} f(x)$.
3. The real zeros and the sign of $f(x)$.
4. The first derivative $f'(x)$, critical points, intervals of monotonicity, and the exact global maximum.
5. The second derivative $f''(x)$, intervals of convexity/concavity, and the inflection point.
6. A definitive explanation of which specific features are necessary to draw an accurate qualitative sketch of the graph.

---

## 3. Key Concepts and Theorems
1. **L'Hôpital's Rule:**
   For an indeterminate limit of form $\frac{\infty}{\infty}$:
   $$\lim_{x \to \infty} \frac{f(x)}{g(x)} = \lim_{x \to \infty} \frac{f'(x)}{g'(x)}.$$
2. **Quotient Rule of Differentiation:**
   $$\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}.$$
3. **Monotonicity and Extreme Values:**
   A sign change in $f'$ from positive to negative at a stationary point indicates a local (and here, global) maximum.
4. **Inflection Points and Convexity:**
   Determined by the sign of the second derivative $f''(x)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Domain, zeros, and signs
The function is given for:
$$D_f = (0, \infty).$$
- **Zeros:**
  $$f(x) = 0 \iff \frac{\ln x}{x} = 0 \iff \ln x = 0 \iff x = 1.$$
  The unique $x$-intercept is $(1, 0)$.
- **Sign of $f(x)$:**
  Since the denominator $x > 0$ for all $x \in D_f$:
  - For $0 < x < 1$: $\ln x < 0 \implies f(x) < 0$.
  - For $x > 1$: $\ln x > 0 \implies f(x) > 0$.

### Step 2: Behavior at the boundary ends of the domain
1. **As $x \to 0^+$ (Left boundary):**
   $$\lim_{x \to 0^+} \frac{\ln x}{x} = \frac{-\infty}{0^+} = -\infty.$$
   Therefore, the line:
   $$x = 0 \quad (y\text{-axis})$$
   is a **vertical asymptote** (plunging downwards as $x \to 0^+$).
2. **As $x \to \infty$ (Right boundary):**
   The limit presents the indeterminate form $\left[\frac{\infty}{\infty}\right]$.
   Applying L'Hôpital's Rule:
   $$\lim_{x \to \infty} \frac{\ln x}{x} \stackrel{\text{H}}{=} \lim_{x \to \infty} \frac{\frac{1}{x}}{1} = \lim_{x \to \infty} \frac{1}{x} = 0.$$
   Therefore, the line:
   $$y = 0 \quad (x\text{-axis})$$
   is a **horizontal asymptote** as $x \to \infty$. Because $\ln x > 0$ for $x > 1$, the curve approaches $y = 0$ strictly from above.

### Step 3: First derivative, monotonicity, and the global maximum
Applying the quotient rule to $f(x) = \frac{\ln x}{x}$:
$$f'(x) = \frac{\left(\frac{1}{x}\right) \cdot x - (\ln x) \cdot 1}{x^2} = \frac{1 - \ln x}{x^2}.$$
Setting $f'(x) = 0$:
$$1 - \ln x = 0 \iff \ln x = 1 \iff x = e \approx 2.718.$$

Determining the sign of $f'(x)$ (noting that the denominator $x^2 > 0$):
- **On $(0, e)$:** $\ln x < 1 \implies 1 - \ln x > 0 \implies f'(x) > 0$.
  Thus, $f(x)$ is **strictly increasing** on $(0, e]$.
- **On $(e, \infty)$:** $\ln x > 1 \implies 1 - \ln x < 0 \implies f'(x) < 0$.
  Thus, $f(x)$ is **strictly decreasing** on $[e, \infty)$.

Since $f$ increases up to $x = e$ and decreases for all $x > e$, $x = e$ is the **strict global maximum**.
The maximum value is:
$$f(e) = \frac{\ln e}{e} = \frac{1}{e} \approx 0.3679.$$

### Step 4: Second derivative, curvature, and the inflection point
Differentiating $f'(x) = \frac{1 - \ln x}{x^2}$:
$$f''(x) = \frac{\left(-\frac{1}{x}\right) \cdot x^2 - (1 - \ln x) \cdot 2x}{x^4} = \frac{-x - 2x + 2x\ln x}{x^4} = \frac{x(2\ln x - 3)}{x^4} = \frac{2\ln x - 3}{x^3}.$$
Setting $f''(x) = 0$:
$$2\ln x - 3 = 0 \iff \ln x = \frac{3}{2} \iff x = e^{3/2} = e\sqrt{e} \approx 4.4817.$$

Determining the sign of $f''(x)$ (since $x^3 > 0$):
- **On $(0, e^{3/2})$:** $\ln x < \frac{3}{2} \implies f''(x) < 0 \implies f$ is **strictly concave** (concave down).
- **On $(e^{3/2}, \infty)$:** $\ln x > \frac{3}{2} \implies f''(x) > 0 \implies f$ is **strictly convex** (concave up).

Because $f''$ changes sign, $x = e^{3/2}$ is an **inflection point**.
The function value at the inflection point is:
$$f(e^{3/2}) = \frac{\frac{3}{2}}{e^{3/2}} = \frac{3}{2e\sqrt{e}} \approx 0.3347.$$

### Step 5: What information is necessary for a correct sketch?
To produce an accurate sketch without guessing, a student must explicitly include:
1. **The vertical asymptote at $x = 0$:** The graph starts at $y \to -\infty$ running along the right side of the $y$-axis.
2. **The root at $(1, 0)$:** The graph crosses the $x$-axis from negative to positive.
3. **The maximum at $(e, 1/e) \approx (2.72, 0.37)$:** The peak of the curve where the tangent is horizontal.
4. **The inflection point at $(e^{3/2}, \frac{3}{2}e^{-3/2}) \approx (4.48, 0.33)$:** Crucial because the curve changes from curving downward (concave) to curving upward (convex) to seamlessly flatten out.
5. **The horizontal asymptote $y = 0$:** The tail decays toward $0$ for large $x$, remaining strictly positive.

```text
                  y
             1/e _|           Max (e, 1/e)
                  |              *
                  |            .    ` .  Inflection (e^(3/2), ~0.33)
                  |          /          *
                  |        .              ` . . . . . . . . . -> y = 0
       -----------+-------*------------------------------------> x
               0  |       1 (root)
                  |      .
                  |     /
                  |    /
                  |   |
                  |   |  x = 0 (vertical asymptote)
                  v
```

---

## 5. Why Each Step Is Valid
- **Step 1:** The natural logarithm is non-positive on $(0, 1]$ and positive on $(1, \infty)$.
- **Step 2:** Approaching $0^+$ gives a quotient of $-\infty$ over an infinitesimal positive number, diverging to $-\infty$. L'Hôpital's rule is valid because the limit at infinity is of type $\infty/\infty$.
- **Step 3:** The quotient rule computes the exact slope, and the sign of $1 - \ln x$ governs the monotonicity completely.
- **Step 4:** A single change in sign of the second derivative identifies the exact geometric transition from concave to convex curvature.
- **Step 5:** Without the inflection point, a student would incorrectly draw the curve crossing below the horizontal asymptote or curving sharply.

---

## 6. Final Answer in Words
The function $f(x) = \frac{\ln x}{x}$ is defined on $(0, \infty)$, has a vertical asymptote at $x = 0$ with $\lim_{x \to 0^+} f(x) = -\infty$, and a horizontal asymptote $y = 0$ as $x \to \infty$. 
Its single real root is at $x = 1$. 
The function reaches a global maximum at $x = e$ with maximum value $f(e) = \frac{1}{e}$. 
It is strictly increasing on $(0, e]$ and strictly decreasing on $[e, \infty)$. 
The graph is concave down on $(0, e^{3/2})$ and concave up on $(e^{3/2}, \infty)$, with an inflection point at $\left(e^{3/2}, \frac{3}{2e\sqrt{e}}\right)$. 
A correct sketch strictly requires: the vertical asymptote $x = 0$, the $x$-intercept $(1, 0)$, the maximum $(e, 1/e)$, the inflection point $(e^{3/2}, f(e^{3/2}))$, and the horizontal asymptote $y = 0$.

---

## 7. Quick Verification
- Compute values:
  - $f(1) = 0$.
  - $f(2) = \frac{\ln 2}{2} \approx \frac{0.693}{2} = 0.3465$.
  - $f(e) = \frac{1}{e} \approx 0.3679$.
  - $f(4) = \frac{\ln 4}{4} = \frac{2\ln 2}{4} = \frac{\ln 2}{2} \approx 0.3465$.
Notice that $f(2) = f(4) \approx 0.3465 < 0.3679 = f(e)$, verifying that the peak occurs between $2$ and $4$ at $e \approx 2.718$.

---

## 8. Common Mistakes to Avoid
- **Assuming $f(x) \to \infty$ as $x \to \infty$:** Overlooking that linear growth $x$ in the denominator completely overwhelms logarithmic growth $\ln x$.
- **Missing the vertical asymptote:** Forgetting that $\lim_{x \to 0^+} \ln x = -\infty$.
- **Omitting the inflection point when sketching:** Drawing the curve descending concave all the way to the asymptote, which would force it to cut across the $x$-axis or develop a corner.

---

## 9. Classroom Presentation (3-Sentence Summary)
The function $f(x) = (\ln x)/x$ starts at negative infinity near the vertical asymptote $x = 0$, crosses the $x$-axis at $(1,0)$, and climbs to a global maximum of $1/e$ at $x = e$. Past this peak, the function decreases toward the horizontal asymptote $y = 0$ as linear growth in the denominator dominates the logarithm. To correctly sketch the flattening tail without cutting through the axis, one must locate the inflection point at $x = e^{3/2}$, where the curvature transitions from concave down to concave up.
