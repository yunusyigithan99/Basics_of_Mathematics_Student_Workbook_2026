# Problem 11 Solution: Two Similar Surfaces (Hyperboloids of One and Two Sheets)

## 1. Original Problem
Compare the two second-degree surfaces in $\mathbb{R}^3$:
$$S_1 : x^2 + y^2 - z^2 = 1 \quad \text{and} \quad S_2 : x^2 + y^2 - z^2 = -1.$$
For each surface:
1. Slicing with horizontal planes $z = c$, test whether the cross-section exists for several values of $c$ (such as $c = 0, \pm 1, \pm 2$).
2. Determine the shape and radius of the cross-section when it exists.
3. Based on these cross-sections, explain the qualitative geometric differences between the two surfaces and describe their global shapes.

---

## 2. What We Are Trying to Find
We need to:
1. Express the horizontal cross-sections as 2D curves $x^2 + y^2 = R(c)^2$.
2. Analyze when the right-hand side is positive, zero, or negative for each surface.
3. Distinguish between a connected, single-piece surface (hyperboloid of one sheet) and a disconnected, two-piece surface (hyperboloid of two sheets).
4. Explain how the sign of the constant term ($+1$ vs. $-1$) fundamentally alters the topology and connectivity of the quadric.

---

## 3. Key Concepts and Theorems
1. **Hyperboloid of One Sheet:**
   An equation $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c_z^2} = 1$. The surface is connected in a single piece. The "waist" (cross-section at $z = 0$) is non-empty, forming an ellipse or circle of minimum radius.
2. **Hyperboloid of Two Sheets:**
   An equation $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c_z^2} = -1$ (or $-\frac{x^2}{a^2} - \frac{y^2}{b^2} + \frac{z^2}{c_z^2} = 1$). The surface consists of two separate, disjoint sheets: an upper sheet for $z \ge c_z$ and a lower sheet for $z \le -c_z$. The central region $|z| < c_z$ contains no real points.
3. **Circular Symmetry:**
   In both equations, the $x$ and $y$ variables appear exclusively as $x^2 + y^2 = r^2$, meaning both surfaces possess rotational symmetry around the $z$-axis (surfaces of revolution).

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze Horizontal Cross-Sections of $S_1 : x^2 + y^2 - z^2 = 1$
Rewrite the equation by isolating the circular term:
$$x^2 + y^2 = 1 + z^2.$$
For any horizontal cutting plane $z = c$:
$$x^2 + y^2 = 1 + c^2.$$
Notice that for **every** real number $c \in \mathbb{R}$, we have $c^2 \ge 0$, which implies:
$$1 + c^2 \ge 1 > 0.$$
Therefore, the right side is strictly positive for every value of $c$, meaning a real circular cross-section **always exists**:
- Radius: $R(c) = \sqrt{1 + c^2} \ge 1$.

**Evaluation at specific heights:**
- At $c = 0$: $x^2 + y^2 = 1 + 0^2 = 1$. This is a **circle of radius $R = 1$** (the narrowest waist / throat circle).
- At $c = \pm 1$: $x^2 + y^2 = 1 + (\pm 1)^2 = 2$. This is a **circle of radius $R = \sqrt{2} \approx 1.414$**.
- At $c = \pm 2$: $x^2 + y^2 = 1 + (\pm 2)^2 = 5$. This is a **circle of radius $R = \sqrt{5} \approx 2.236$**.

**Conclusion for $S_1$:**
The surface is seamless, continuous, and connected in a single piece. It resembles an hourglass or cooling tower with a circular waist of radius $1$ at $z = 0$ that flares outward as $|z| \to \infty$. This surface is a **hyperboloid of one sheet**.

---

### Step 2: Analyze Horizontal Cross-Sections of $S_2 : x^2 + y^2 - z^2 = -1$
Rewrite the equation by isolating the circular term:
$$x^2 + y^2 = z^2 - 1.$$
For a horizontal cutting plane $z = c$:
$$x^2 + y^2 = c^2 - 1.$$
Since $x^2 + y^2 \ge 0$ for any real coordinates, real solutions exist **if and only if** $c^2 - 1 \ge 0$, which means:
$$c^2 \ge 1 \iff |c| \ge 1 \iff c \ge 1 \quad \text{or} \quad c \le -1.$$

**Evaluation at specific heights:**
- At $c = 0$: $x^2 + y^2 = 0^2 - 1 = -1 < 0$. **No real points exist** (empty set $\emptyset$).
- At $c = 0.5$: $x^2 + y^2 = 0.25 - 1 = -0.75 < 0$. **No real points exist**.
- At $c = \pm 1$: $x^2 + y^2 = (\pm 1)^2 - 1 = 0$. The cross-section is a **single point**: $(0, 0, 1)$ at the top and $(0, 0, -1)$ at the bottom (the vertices / apexes of the two sheets).
- At $c = \pm 2$: $x^2 + y^2 = (\pm 2)^2 - 1 = 3$. This is a **circle of radius $R = \sqrt{3} \approx 1.732$**.
- At $c = \pm 3$: $x^2 + y^2 = 9 - 1 = 8$. This is a **circle of radius $R = \sqrt{8} = 2\sqrt{2} \approx 2.828$**.

**Conclusion for $S_2$:**
For $-1 < z < 1$, there are no real points on the surface, leaving a physical gap of height 2 units centered at the origin. The surface is divided into **two separate, disconnected pieces**:
- An upper bowl-like sheet opening upwards starting from vertex $(0, 0, 1)$ for $z \ge 1$.
- A lower bowl-like sheet opening downwards starting from vertex $(0, 0, -1)$ for $z \le -1$.
This surface is a **hyperboloid of two sheets**.

---

### Step 3: Summary Comparison

| Property | $S_1 : x^2 + y^2 - z^2 = 1$ | $S_2 : x^2 + y^2 - z^2 = -1$ |
| :--- | :--- | :--- |
| **Standard Name** | Hyperboloid of one sheet | Hyperboloid of two sheets |
| **Cross-section at $z = 0$** | Circle of radius $R = 1$ | Empty (no real points) |
| **Existence condition** | Exists for all $z \in \mathbb{R}$ | Exists only for $|z| \ge 1$ |
| **Number of pieces** | 1 (connected single surface) | 2 (disconnected upper and lower sheets) |
| **Minimum throat/vertex** | Narrowest at $z = 0$ ($R = 1$) | Vertices at $(0, 0, \pm 1)$ ($R = 0$) |
| **Shape analogy** | Hourglass / nuclear cooling tower | Two opposing parabolic-like bowls |

---

## 5. Why Each Step Is Valid
1. **Expressing $x^2 + y^2 = f(z)$** reduces the 3D surface study to finding the non-negative level sets of a 1D function $f(z)$.
2. **The sign of $f(z)$** rigorously dictates the existence of real Euclidean points because $x^2 + y^2 \ge 0$ for all $(x, y) \in \mathbb{R}^2$.
3. **Topological connectivity** follows directly: $S_1$ is path-connected because its domain along $z$ is the connected interval $(-\infty, \infty)$, while $S_2$ has the disconnected domain $(-\infty, -1] \cup [1, \infty)$.

---

## 6. Final Answer in Words
For $S_1 : x^2 + y^2 - z^2 = 1$, the horizontal cross-sections are circles $x^2 + y^2 = 1 + c^2$ with radius $R(c) = \sqrt{1 + c^2}$, which exist for every real $c$ and have a minimum radius of $1$ at $z = 0$; this is a connected **hyperboloid of one sheet**. For $S_2 : x^2 + y^2 - z^2 = -1$, the cross-sections are circles $x^2 + y^2 = c^2 - 1$ with radius $R(c) = \sqrt{c^2 - 1}$, which exist only when $|c| \ge 1$ and are completely empty for $|c| < 1$; this forms two separate disconnected sheets opening away from each other with vertices at $(0, 0, \pm 1)$, known as a **hyperboloid of two sheets**.

---

## 7. Quick Verification
- Point $(1, 0, 0)$ on $S_1$: $1^2 + 0^2 - 0^2 = 1 = 1$. (Valid)
- Point $(0, 0, 0)$ tested on both:
  - On $S_1$: $0 - 0 = 0 \neq 1$.
  - On $S_2$: $0 - 0 = 0 \neq -1$.
  Neither surface contains the origin.
- Vertical slice $y = 0$:
  - On $S_1$: $x^2 - z^2 = 1$ is a hyperbola crossing the $x$-axis at $(\pm 1, 0)$.
  - On $S_2$: $x^2 - z^2 = -1 \iff z^2 - x^2 = 1$ is a hyperbola crossing the $z$-axis at $(0, \pm 1)$.
  This independently confirms that $S_1$ intersects the horizontal equator, whereas $S_2$ intersects the vertical axis.

---

## 8. Common Mistakes to Avoid
- **Confusing one sheet and two sheets:** Forgetting which sign corresponds to one sheet ($+1$) versus two sheets ($-1$).
- **Assuming $z = 0$ exists for both:** Believing that setting $z = 0$ in $S_2$ yields a circle with imaginary radius; in real geometry, it simply has no points.
- **Thinking the cross-sections are hyperbolas:** The cross-sections by planes $z = \text{const}$ are circles; it is the *vertical* slices ($x = \text{const}$ or $y = \text{const}$) that are hyperbolas.

---

## 9. Classroom Presentation (3-Sentence Summary)
Rearranging the equations gives $x^2 + y^2 = 1 + z^2$ for the first surface, which produces real circles of radius $\sqrt{1+z^2}$ at every height $z$, forming a single connected hourglass called a hyperboloid of one sheet. In contrast, the second equation gives $x^2 + y^2 = z^2 - 1$, which has no real solutions when $|z| < 1$ because the right side becomes negative. This creates a two-unit gap around the origin, splitting the surface into two disconnected opposing bowls known as a hyperboloid of two sheets.
