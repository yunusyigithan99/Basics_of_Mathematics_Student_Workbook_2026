# Problem 1 Solution: Recognizing Curves from Canonical Form

## 1. Original Problem
Recognize and classify each of the following four planar second-degree curves given in canonical form:
1. $x^2 + y^2 = 9$
2. $\frac{x^2}{16} + \frac{y^2}{9} = 1$
3. $y^2 = 8x$
4. $\frac{x^2}{9} - \frac{y^2}{4} = 1$

For each curve, identify its most important geometric features, describe its shape and scale for sketching, and explain which specific algebraic components of the equation determine the curve type.

---

## 2. What We Are Trying to Find
We need to:
1. Classify each equation into its proper conic section family (circle, ellipse, parabola, hyperbola).
2. Extract the key quantitative parameters: center, vertices, intercepts, axes of symmetry, semiaxes, focal parameters, and asymptotes.
3. Provide coordinate descriptions for plotting/sketching.
4. Formulate the general algebraic recognition rules connecting signs and degrees of variables to geometric curve shapes.

---

## 3. Key Concepts and Theorems
1. **Canonical Forms of Non-Degenerate Conic Sections:**
   - **Circle:** $x^2 + y^2 = R^2$. Both variables squared, equal positive coefficients.
   - **Ellipse:** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a \neq b$). Both variables squared, unequal positive coefficients, sum equals $+1$.
   - **Parabola:** $y^2 = 2px$ or $x^2 = 2py$. One variable quadratic, the other linear.
   - **Hyperbola:** $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ (or $-\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$). Both variables squared with opposite signs.
2. **Asymptotes of a Hyperbola:**
   For $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$, setting the constant 1 to 0 yields the pair of asymptotic lines:
   $$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 0 \implies y = \pm \frac{b}{a} x.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze Curve 1 ($x^2 + y^2 = 9$)
- **Classification:** **Circle** centered at the origin $(0, 0)$.
- **Why we recognize it:** Both $x$ and $y$ are raised to degree 2 with identical coefficients ($+1$), and their sum equals a positive constant $9 = 3^2$.
- **Key Features:**
  - Center: $(0, 0)$
  - Radius: $R = \sqrt{9} = 3$
  - Intercepts: $(3, 0), (-3, 0), (0, 3), (0, -3)$
- **Sketching Guide:** Draw a perfectly round, symmetric circle centered at $(0, 0)$ passing through $\pm 3$ on both coordinate axes.

### Step 2: Analyze Curve 2 ($\frac{x^2}{16} + \frac{y^2}{9} = 1$)
- **Classification:** **Ellipse** centered at the origin $(0, 0)$ with horizontal major axis.
- **Why we recognize it:** Both $x^2$ and $y^2$ appear with positive signs and sum to 1, but their denominators are unequal ($16 \neq 9$), indicating unequal stretching along the axes.
- **Key Features:**
  - Center: $(0, 0)$
  - Horizontal semi-major axis: $a = \sqrt{16} = 4$
  - Vertical semi-minor axis: $b = \sqrt{9} = 3$
  - Intercepts: $x$-intercepts at $(\pm 4, 0)$, $y$-intercepts at $(0, \pm 3)$
  - Linear eccentricity: $c = \sqrt{a^2 - b^2} = \sqrt{16 - 9} = \sqrt{7} \approx 2.65$
  - Foci: $F_1 = (-\sqrt{7}, 0), F_2 = (\sqrt{7}, 0)$
- **Sketching Guide:** Draw an oval centered at $(0, 0)$ stretched wider horizontally (width 8 from $-4$ to $4$) than vertically (height 6 from $-3$ to $3$).

### Step 3: Analyze Curve 3 ($y^2 = 8x$)
- **Classification:** **Parabola** with vertex at the origin opening horizontally to the right.
- **Why we recognize it:** Exactly one variable is squared ($y^2$) while the other appears linearly ($x^1$). Since $x = \frac{y^2}{8} \ge 0$, real solutions only exist for $x \ge 0$.
- **Key Features:**
  - Vertex: $(0, 0)$
  - Axis of symmetry: the $x$-axis ($y = 0$)
  - Focal parameter: $2p = 8 \implies p = 4$
  - Focus: $\left(\frac{p}{2}, 0\right) = (2, 0)$
  - Directrix: $x = -\frac{p}{2} = -2$
  - Sample points: For $x = 2 \implies y^2 = 16 \implies y = \pm 4$; for $x = 8 \implies y = \pm 8$.
- **Sketching Guide:** Draw an open, U-shaped curve starting at vertex $(0, 0)$, symmetric about the positive $x$-axis, passing through $(2, 4)$ and $(2, -4)$.

### Step 4: Analyze Curve 4 ($\frac{x^2}{9} - \frac{y^2}{4} = 1$)
- **Classification:** **Hyperbola** centered at the origin opening horizontally along the $x$-axis.
- **Why we recognize it:** Both variables are squared, but with opposite signs ($x^2$ is positive, $y^2$ is negative). The positive sign on $x^2$ indicates that the transverse axis lies along the $x$-axis.
- **Key Features:**
  - Center: $(0, 0)$
  - Transverse semi-axis: $a = \sqrt{9} = 3$
  - Conjugate semi-axis: $b = \sqrt{4} = 2$
  - Vertices ($x$-intercepts): $(\pm 3, 0)$
  - $y$-intercepts: None (setting $x = 0$ yields $-\frac{y^2}{4} = 1 \implies y^2 = -4$, no real solutions).
  - Asymptotes: $y = \pm \frac{b}{a} x = \pm \frac{2}{3} x$
  - Foci: $c = \sqrt{a^2 + b^2} = \sqrt{9 + 4} = \sqrt{13} \approx 3.61$, so $F_{1,2} = (\pm \sqrt{13}, 0)$
- **Sketching Guide:** Draw the asymptotic guide lines $y = \frac{2}{3}x$ and $y = -\frac{2}{3}x$. Then draw two symmetric branches opening left and right, with vertices at $(-3, 0)$ and $(3, 0)$, approaching the asymptotes as $|x| \to \infty$.

---

## 5. Why Each Step Is Valid
1. **The equality of quadratic coefficients in $x^2 + y^2 = R^2$** represents isotropic Euclidean distance $\sqrt{x^2 + y^2} = R$.
2. **Dividing by $a^2$ and $b^2$ in the ellipse equation** performs an independent coordinate scaling along each orthogonal axis.
3. **The linear degree of $x$ in $y^2 = 8x$** prevents closure, forcing the curve to extend infinitely in one direction.
4. **The subtraction in $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$** factors into $(\frac{x}{a} - \frac{y}{b})(\frac{x}{a} + \frac{y}{b}) \approx 0$ for large values, mathematically proving the existence of straight-line asymptotes.

---

## 6. Final Answer in Words
1. $x^2 + y^2 = 9$ is a **circle** with center $(0, 0)$ and radius $R = 3$.
2. $\frac{x^2}{16} + \frac{y^2}{9} = 1$ is an **ellipse** with center $(0, 0)$, horizontal semi-major axis $a = 4$, and vertical semi-minor axis $b = 3$.
3. $y^2 = 8x$ is a **parabola** with vertex $(0, 0)$, horizontal axis of symmetry $y = 0$, opening rightwards with focus at $(2, 0)$.
4. $\frac{x^2}{9} - \frac{y^2}{4} = 1$ is a **hyperbola** with center $(0, 0)$, vertices at $(\pm 3, 0)$, opening horizontally, with asymptotes $y = \pm \frac{2}{3} x$.

---

## 7. Quick Verification
- **Test points on each curve:**
  - Circle: $(3, 0) \implies 3^2 + 0^2 = 9$. (Verified)
  - Ellipse: $(4, 0) \implies \frac{16}{16} + 0 = 1$; $(0, 3) \implies 0 + \frac{9}{9} = 1$. (Verified)
  - Parabola: $(2, 4) \implies 4^2 = 16 = 8(2)$. (Verified)
  - Hyperbola: $(3, 0) \implies \frac{9}{9} - 0 = 1$. (Verified)
  Asymptote behavior: For $x = 30$, asymptote gives $y = \pm 20$. On the hyperbola, $\frac{y^2}{4} = \frac{900}{9} - 1 = 99 \implies y^2 = 396 \implies y = \sqrt{396} \approx 19.8995 \approx 20$. The curve closely tracks the asymptote.

---

## 8. Common Mistakes to Avoid
- **Confusing radius with $R^2$:** Stating the radius of $x^2 + y^2 = 9$ is $9$ instead of $\sqrt{9} = 3$.
- **Inverting the ellipse axes:** Stating that $a = 16$ instead of $a = \sqrt{16} = 4$.
- **Wrong parabola opening direction:** Thinking $y^2 = 8x$ opens upwards like $y = x^2$; when $y$ is squared, the parabola opens horizontally along $x$.
- **Flipping hyperbola asymptote slopes:** Writing $y = \pm \frac{a}{b} x = \pm \frac{3}{2} x$ instead of $\pm \frac{b}{a} x = \pm \frac{2}{3} x$.

---

## 9. Classroom Presentation (3-Sentence Summary)
We classify each conic section by inspecting the degrees and signs of its variables: equal positive squares form a circle with radius 3, while unequal positive squares form an ellipse with semiaxes 4 and 3. When one variable is linear and one is quadratic, we have a parabola opening along the positive $x$-axis with vertex at the origin. Finally, when the two squared variables have opposite signs, the curve is a hyperbola with vertices at $(\pm 3, 0)$ that approaches the diagonal asymptotes $y = \pm (2/3)x$ as it extends to infinity.

