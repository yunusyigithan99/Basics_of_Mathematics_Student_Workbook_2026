# Problem 10: Complete Function Analysis of a Rational Function

## 1. Original Problem
Perform a complete analysis of
$$f(x) = \frac{x}{x^2 + 1}.$$
Include the domain, symmetry, zeros, limits, monotonicity, extrema, and convexity. Finally, produce a sketch based only on this information.

---

## 2. What We Are Trying to Find
A complete, structured calculus investigation of the function $f(x)$, specifically:
1. Domain and continuity.
2. Parity (symmetry with respect to the origin or $y$-axis).
3. Intercepts (zeros of the function).
4. Limits at $\pm\infty$ and identification of asymptotes.
5. First derivative $f'(x)$, intervals of monotonicity, and local/global extrema.
6. Second derivative $f''(x)$, intervals of convexity/concavity, and inflection points.
7. A summary table and an accurate qualitative sketch of the graph.

---

## 3. Key Concepts and Theorems
1. **Odd Symmetry:**
   If $f(-x) = -f(x)$ for all $x \in D_f$, the graph has point symmetry about the origin $(0, 0)$.
2. **Horizontal Asymptote:**
   If $\lim_{x \to \pm\infty} f(x) = L$, the line $y = L$ is a horizontal asymptote.
3. **Monotonicity and Stationary Points:**
   $f$ increases where $f'(x) > 0$ and decreases where $f'(x) < 0$. Critical points occur where $f'(x) = 0$.
4. **Quotient Rule:**
   $$\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}.$$
5. **Convexity and Inflection Points:**
   $f''(x) > 0$ implies convex (concave up), $f''(x) < 0$ implies concave (concave down). Transitions where $f''$ changes sign yield inflection points.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Domain and continuity
The denominator satisfies:
$$x^2 + 1 \ge 1 > 0 \quad \text{for all } x \in \mathbb{R}.$$
Because the denominator is strictly positive everywhere, there are no division-by-zero points.
Therefore:
$$D_f = \mathbb{R} = (-\infty, \infty),$$
and $f$ is continuous and infinitely differentiable on all of $\mathbb{R}$.

### Step 2: Symmetry
Substitute $-x$ in place of $x$:
$$f(-x) = \frac{-x}{(-x)^2 + 1} = \frac{-x}{x^2 + 1} = -f(x).$$
Since $f(-x) = -f(x)$, $f$ is an **odd function**. Its graph is symmetric with respect to the origin $(0, 0)$.

### Step 3: Zeros and intercepts
Set $f(x) = 0$:
$$\frac{x}{x^2 + 1} = 0 \iff x = 0.$$
At $x = 0$, $y = f(0) = 0$.
The only axis intercept is the origin $(0, 0)$.

### Step 4: Limits and asymptotes
- **Vertical asymptotes:** None, because $D_f = \mathbb{R}$.
- **Horizontal asymptotes:**
  $$\lim_{x \to \infty} \frac{x}{x^2 + 1} = \lim_{x \to \infty} \frac{\frac{1}{x}}{1 + \frac{1}{x^2}} = \frac{0}{1} = 0,$$
  $$\lim_{x \to -\infty} \frac{x}{x^2 + 1} = 0.$$
  Thus, the line $y = 0$ ($x$-axis) is a **horizontal asymptote** in both directions ($x \to +\infty$ and $x \to -\infty$).

### Step 5: First derivative, monotonicity, and extrema
Applying the quotient rule with $u = x$ and $v = x^2 + 1$:
$$f'(x) = \frac{1 \cdot (x^2 + 1) - x \cdot (2x)}{(x^2 + 1)^2} = \frac{x^2 + 1 - 2x^2}{(x^2 + 1)^2} = \frac{1 - x^2}{(x^2 + 1)^2}.$$
Factoring the numerator:
$$f'(x) = \frac{(1 - x)(1 + x)}{(x^2 + 1)^2}.$$
The denominator $(x^2 + 1)^2$ is strictly positive for all $x$. Thus, the sign of $f'(x)$ is that of $1 - x^2$:
- **On $(-\infty, -1)$:** $1 - x^2 < 0 \implies f'(x) < 0 \implies f$ is **strictly decreasing**.
- **On $(-1, 1)$:** $1 - x^2 > 0 \implies f'(x) > 0 \implies f$ is **strictly increasing**.
- **On $(1, \infty)$:** $1 - x^2 < 0 \implies f'(x) < 0 \implies f$ is **strictly decreasing**.

Evaluating at critical points $x = \pm 1$:
- At $x = -1$: derivative changes from negative to positive.
  $$f(-1) = \frac{-1}{(-1)^2 + 1} = -\frac{1}{2} \quad (\text{local and global minimum}).$$
- At $x = 1$: derivative changes from positive to negative.
  $$f(1) = \frac{1}{1^2 + 1} = \frac{1}{2} \quad (\text{local and global maximum}).$$

### Step 6: Second derivative, curvature, and inflection points
Differentiating $f'(x) = \frac{1 - x^2}{(x^2 + 1)^2}$:
$$f''(x) = \frac{-2x(x^2 + 1)^2 - (1 - x^2) \cdot 2(x^2 + 1) \cdot 2x}{(x^2 + 1)^4}.$$
Factor $2x(x^2 + 1)$ from the numerator:
$$f''(x) = \frac{2x(x^2 + 1) [-(x^2 + 1) - 2(1 - x^2)]}{(x^2 + 1)^4} = \frac{2x [-x^2 - 1 - 2 + 2x^2]}{(x^2 + 1)^3} = \frac{2x(x^2 - 3)}{(x^2 + 1)^3}.$$
Factoring completely:
$$f''(x) = \frac{2x(x - \sqrt{3})(x + \sqrt{3})}{(x^2 + 1)^3}.$$
The roots of $f''(x)$ are $x = -\sqrt{3}$, $x = 0$, and $x = \sqrt{3}$.
Determining the sign of $f''(x)$:
- **$(-\infty, -\sqrt{3})$:** $f''(x) < 0 \implies f$ is **strictly concave** (concave down).
- **$(-\sqrt{3}, 0)$:** $f''(x) > 0 \implies f$ is **strictly convex** (concave up).
- **$(0, \sqrt{3})$:** $f''(x) < 0 \implies f$ is **strictly concave** (concave down).
- **$(\sqrt{3}, \infty)$:** $f''(x) > 0 \implies f$ is **strictly convex** (concave up).

Inflection points occur at each of these three sign changes:
1. $x = -\sqrt{3}$: $f(-\sqrt{3}) = \frac{-\sqrt{3}}{3 + 1} = -\frac{\sqrt{3}}{4} \approx -0.433 \implies I_1 = \left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right)$.
2. $x = 0$: $f(0) = 0 \implies I_2 = (0, 0)$.
3. $x = \sqrt{3}$: $f(\sqrt{3}) = \frac{\sqrt{3}}{3 + 1} = \frac{\sqrt{3}}{4} \approx 0.433 \implies I_3 = \left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)$.

### Step 7: Summary table and sketch
| $x$ | $(-\infty, -\sqrt{3})$ | $-\sqrt{3}$ | $(-\sqrt{3}, -1)$ | $-1$ | $(-1, 0)$ | $0$ | $(0, 1)$ | $1$ | $(1, \sqrt{3})$ | $\sqrt{3}$ | $(\sqrt{3}, \infty)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f'(x)$ | $-$ | $-$ | $-$ | $0$ | $+$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ |
| $f''(x)$ | $-$ | $0$ | $+$ | $+$ | $+$ | $0$ | $-$ | $-$ | $-$ | $0$ | $+$ |
| $f(x)$ | $\searrow$, concave | $-\frac{\sqrt{3}}{4}$ | $\searrow$, convex | $-\frac{1}{2}$ (Min) | $\nearrow$, convex | $0$ (Infl) | $\nearrow$, concave | $\frac{1}{2}$ (Max) | $\searrow$, concave | $\frac{\sqrt{3}}{4}$ | $\searrow$, convex |

```text
                  y
                  |            Max (1, 0.5)
                  |               *
                  |           .       ` .  I3 (√3, 0.43)
        ----------+--------.------------*---------------> y = 0 (asymptote)
                 0|      /                  ` .
         . '      |    .
 I1 (-√3, -0.43)  *  .
              . `
             *
        Min (-1, -0.5)
```

---

## 5. Why Each Step Is Valid
- **Step 1:** $x^2 \ge 0 \implies x^2 + 1 \ge 1 > 0$, guaranteeing that the denominator never vanishes for real $x$.
- **Step 2:** Evaluating $f(-x)$ checks the symmetry test; $-f(x)$ confirms odd parity.
- **Step 3:** A fraction is zero if and only if its numerator is zero and denominator is defined.
- **Step 4:** The denominator degree ($2$) exceeds the numerator degree ($1$), ensuring the limit as $x \to \pm\infty$ is zero.
- **Step 5:** The quotient rule correctly handles rates of change of rational functions, and the square in the denominator $(x^2+1)^2$ is strictly positive.
- **Step 6:** Factoring out $(x^2+1)$ from the numerator of $f''$ simplifies the rational expression before determining roots.

---

## 6. Final Answer in Words
The function $f(x) = \frac{x}{x^2 + 1}$ is an odd function defined on all of $\mathbb{R}$ with only one root at $(0, 0)$. 
The $x$-axis ($y = 0$) is a horizontal asymptote as $x \to \pm\infty$. 
The function attains its global minimum of $-\frac{1}{2}$ at $x = -1$ and its global maximum of $\frac{1}{2}$ at $x = 1$. 
It is strictly decreasing on $(-\infty, -1]$ and $[1, \infty)$, and strictly increasing on $[-1, 1]$. 
The graph is concave down on $(-\infty, -\sqrt{3})$ and $(0, \sqrt{3})$, and concave up on $(-\sqrt{3}, 0)$ and $(\sqrt{3}, \infty)$, with three inflection points: $\left(-\sqrt{3}, -\frac{\sqrt{3}}{4}\right)$, $(0, 0)$, and $\left(\sqrt{3}, \frac{\sqrt{3}}{4}\right)$.

---

## 7. Quick Verification
- As $x \to \infty$, $f(x) \approx \frac{x}{x^2} = \frac{1}{x} > 0$, approaching $0$ from above, which matches the positive values for $x > 0$.
- Extrema values verify that $|f(x)| \le \frac{1}{2}$ for all $x \in \mathbb{R}$, which is the classic algebraic inequality $|x| \le \frac{1}{2}(x^2 + 1) \iff (x \pm 1)^2 \ge 0$.

---

## 8. Common Mistakes to Avoid
- **Looking for vertical asymptotes:** Mistakenly setting $x^2 + 1 = 0$, which has no real solutions.
- **Algebraic errors when simplifying the second derivative:** Forgetting to cancel the common factor $(x^2 + 1)$ before expanding the numerator, leading to cumbersome higher-degree polynomials.
- **Missing the inflection point at $x = 0$:** Overlooking the factor $2x$ in $f''(x) = \frac{2x(x^2 - 3)}{(x^2 + 1)^3}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The function $f(x) = x/(x^2 + 1)$ is an odd function defined everywhere on $\mathbb{R}$ that approaches the horizontal asymptote $y = 0$ at both infinities. Its first derivative reveals a global minimum of $-1/2$ at $x = -1$ and a global maximum of $1/2$ at $x = 1$, increasing between them and decreasing outside. Its second derivative changes sign at $x = -\sqrt{3}$, $0$, and $\sqrt{3}$, giving three inflection points that connect the alternating convex and concave segments of the curve.
