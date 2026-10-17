# Problem 5 Solution: Hyperbola and Asymptotes

## 1. Original Problem
For the hyperbola given in canonical form:
$$\frac{x^2}{16} - \frac{y^2}{9} = 1,$$
find the intercepts with the $x$-axis, determine the equations of the asymptotes, and provide a guide for sketching the curve. Explain why the asymptotes accurately describe the asymptotic behavior of the curve far from the center.

---

## 2. What We Are Trying to Find
We need to:
1. Calculate the $x$-intercepts (the real vertices) of the hyperbola by setting $y = 0$.
2. State why there are no real $y$-intercepts.
3. Derive the equations of the pair of asymptotes $y = \pm \frac{b}{a} x$.
4. Provide instructions for drawing the hyperbola using the central bounding rectangle.
5. Provide a rigorous algebraic and limit-based explanation of why the hyperbola approaches its asymptotes as $|x| \to \infty$.

---

## 3. Key Concepts and Theorems
1. **Canonical Form of a Horizontal Hyperbola:**
   $$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1,$$
   where $a > 0$ is the transverse semiaxis length and $b > 0$ is the conjugate semiaxis length.
2. **Vertices (Intercepts):**
   Setting $y = 0$ yields $x^2 = a^2 \implies x = \pm a$, giving vertices $(\pm a, 0)$. Setting $x = 0$ yields $-y^2/b^2 = 1 \implies y^2 = -b^2$, which has no real solutions.
3. **Asymptotes of a Hyperbola:**
   The lines obtained by setting the right-hand constant from $1$ to $0$:
   $$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 0 \implies \left(\frac{x}{a} - \frac{y}{b}\right)\left(\frac{x}{a} + \frac{y}{b}\right) = 0 \implies y = \pm \frac{b}{a} x.$$
4. **Behavior at Infinity:**
   As $|x| \to \infty$, the constant $1$ on the right side becomes negligible compared to the large quadratic terms $x^2/a^2$ and $y^2/b^2$, causing the curve to approach the straight lines $y = \pm \frac{b}{a}x$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify Semiaxes $a$ and $b$
From the equation $\frac{x^2}{16} - \frac{y^2}{9} = 1$:
$$a^2 = 16 \implies a = 4,$$
$$b^2 = 9 \implies b = 3.$$
- Transverse semi-axis length: $a = 4$
- Conjugate semi-axis length: $b = 3$

### Step 2: Find the Intercepts with the Coordinate Axes
1. **$x$-intercepts (Vertices):**
   Set $y = 0$:
   $$\frac{x^2}{16} - 0 = 1 \implies x^2 = 16 \implies x = \pm 4.$$
   The hyperbola intersects the $x$-axis at the two vertices:
   $$V_1 = (-4, 0) \quad \text{and} \quad V_2 = (4, 0).$$
2. **$y$-intercepts:**
   Set $x = 0$:
   $$0 - \frac{y^2}{9} = 1 \implies y^2 = -9.$$
   Since the square of any real number cannot be negative ($y^2 \ge 0$), there are **no real $y$-intercepts**. The curve never crosses the $y$-axis.

### Step 3: Find the Equations of the Asymptotes
Set the constant $1$ on the right-hand side to $0$:
$$\frac{x^2}{16} - \frac{y^2}{9} = 0 \implies \frac{y^2}{9} = \frac{x^2}{16}.$$
Multiply both sides by 9 and take the square root:
$$y^2 = \frac{9}{16} x^2 \implies y = \pm \frac{3}{4} x.$$
Thus, the two asymptotes are:
$$L_1 : y = \frac{3}{4} x \quad \text{and} \quad L_2 : y = -\frac{3}{4} x.$$

### Step 4: Explain Why Asymptotes Describe the Curve Far from the Center
Solve the hyperbola equation explicitly for $y$ in terms of $x$:
$$\frac{y^2}{9} = \frac{x^2}{16} - 1 = \frac{x^2}{16}\left(1 - \frac{16}{x^2}\right).$$
Taking the square root for $x \ge 4$:
$$y_{\text{curve}} = \pm \frac{3}{4} x \sqrt{1 - \frac{16}{x^2}}.$$
Now analyze what happens when $|x|$ becomes very large ($|x| \to \infty$):
1. The fraction $\frac{16}{x^2}$ shrinks rapidly toward zero:
   $$\lim_{|x| \to \infty} \frac{16}{x^2} = 0.$$
2. Consequently, the radical approaches $1$:
   $$\lim_{|x| \to \infty} \sqrt{1 - \frac{16}{x^2}} = \sqrt{1 - 0} = 1.$$
3. Therefore:
   $$y_{\text{curve}} \approx \pm \frac{3}{4} x = y_{\text{asymptote}}.$$
4. More precisely, evaluate the vertical distance between the hyperbola and its asymptote:
   $$|y_{\text{asymptote}}| - |y_{\text{curve}}| = \frac{3}{4} |x| \left(1 - \sqrt{1 - \frac{16}{x^2}}\right).$$
   Multiply by the conjugate $(1 + \sqrt{1 - 16/x^2}) / (1 + \sqrt{1 - 16/x^2})$:
   $$= \frac{3}{4} |x| \frac{1 - (1 - 16/x^2)}{1 + \sqrt{1 - 16/x^2}} = \frac{3}{4} |x| \frac{16/x^2}{1 + \sqrt{1 - 16/x^2}} = \frac{12}{|x|\big(1 + \sqrt{1 - 16/x^2}\big)}.$$
   As $|x| \to \infty$, the denominator grows without bound while the numerator is fixed at 12:
   $$\lim_{|x| \to \infty} \Big(|y_{\text{asymptote}}| - |y_{\text{curve}}|\Big) = \lim_{|x| \to \infty} \frac{12}{2|x|} = 0.$$
   The vertical separation approaches 0, meaning the hyperbola draws arbitrarily close to the straight lines $y = \pm \frac{3}{4}x$ without ever crossing them.

### Step 5: Description for Sketching
1. Draw the **central guide box** centered at $(0, 0)$ with horizontal width $2a = 8$ (from $-4$ to $4$) and vertical height $2b = 6$ (from $-3$ to $3$).
2. Draw the diagonals of this rectangle through $(0, 0)$; these lines extended to infinity are the asymptotes $y = \pm \frac{3}{4}x$.
3. Plot the vertices at $(-4, 0)$ and $(4, 0)$ on the $x$-axis.
4. Draw two smooth branches: the right branch opens rightwards starting at vertex $(4, 0)$ and approaches the asymptotes; the left branch opens leftwards starting at $(-4, 0)$ and approaches the asymptotes symmetrically.

---

## 5. Why Each Step Is Valid
1. **Setting $y = 0$** isolates the geometric intersection with the line of symmetry $y = 0$.
2. **Replacing $1$ with $0$** captures the homogeneous leading-order balance between $x^2/16$ and $y^2/9$.
3. **The conjugate rationalization** rigorously proves that the gap between the hyperbola and the asymptotes scales as $\mathcal{O}(1/|x|) \to 0$.

---

## 6. Final Answer in Words
The $x$-intercepts (vertices) of the hyperbola are $V_1 = (-4, 0)$ and $V_2 = (4, 0)$, with no real $y$-intercepts. The asymptotes are the straight lines $y = \frac{3}{4} x$ and $y = -\frac{3}{4} x$. The asymptotes govern the curve far from the center because solving for $y$ yields $y = \pm \frac{3}{4}x \sqrt{1 - 16/x^2}$; as $|x| \to \infty$, the term $16/x^2$ tends to $0$, causing the square root to approach $1$ and the vertical distance between the hyperbola and the lines to vanish toward zero.

---

## 7. Quick Verification
- **Numerical test of asymptote convergence:**
  - Let $x = 20$.
    Asymptote gives $y_{\text{asymp}} = \frac{3}{4}(20) = 15$.
    On the hyperbola: $\frac{y^2}{9} = \frac{400}{16} - 1 = 25 - 1 = 24 \implies y^2 = 216 \implies y_{\text{curve}} = \sqrt{216} \approx 14.6969$.
    Gap: $15 - 14.6969 \approx 0.303$.
  - Let $x = 100$.
    Asymptote gives $y_{\text{asymp}} = \frac{3}{4}(100) = 75$.
    On the hyperbola: $\frac{y^2}{9} = \frac{10000}{16} - 1 = 625 - 1 = 624 \implies y^2 = 5616 \implies y_{\text{curve}} = \sqrt{5616} \approx 74.93998$.
    Gap: $75 - 74.94 \approx 0.06$.
  The gap clearly decreases toward 0 as predicted.

---

## 8. Common Mistakes to Avoid
- **Inverting the asymptote slope:** Writing $y = \pm \frac{4}{3} x$ instead of $\pm \frac{b}{a} x = \pm \frac{3}{4} x$.
- **Thinking the hyperbola crosses the asymptotes:** The curve approaches the asymptotes from the inside but never touches or intersects them for finite real $x$.
- **Believing vertices lie on the $y$-axis:** The minus sign is attached to $y^2$, meaning the transverse axis is horizontal and the vertices lie strictly on the $x$-axis.

---

## 9. Classroom Presentation (3-Sentence Summary)
Setting $y = 0$ gives the hyperbola's vertices on the $x$-axis at $(\pm 4, 0)$, while setting $x = 0$ yields no real solutions because $y^2 = -9$ is impossible. Replacing the right-hand constant $1$ with $0$ gives the two diagonal asymptotes $y = \pm (3/4)x$. When $|x|$ becomes very large, the constant 1 becomes negligible compared to the quadratic terms, causing the vertical distance between the hyperbola branches and the asymptotes to vanish to zero.

