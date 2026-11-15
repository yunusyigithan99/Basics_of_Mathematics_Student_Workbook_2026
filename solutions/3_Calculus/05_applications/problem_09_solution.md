# Problem 09: Constrained Optimization — Minimizing Surface Area of a Can

## 1. Original Problem
A closed cylinder has fixed volume $V$.

1. Write the volume constraint.
2. Eliminate one of the variables.
3. Express the surface area as a function of the radius $r$.
4. Find the relation between the height $h$ and the radius $r$ for which the material usage is minimal.

Interpret the obtained relation geometrically.

---

## 2. What We Are Trying to Find
1. The mathematical equation for the fixed volume constraint $V = \text{constant}$.
2. The algebraic elimination of the height $h$ in terms of the radius $r$ and volume $V$.
3. The total surface area function $S(r)$ in terms of a single variable $r$.
4. The derivative $S'(r)$ and the critical point minimizing the material.
5. The optimal geometric relation between height $h$ and radius $r$.
6. The geometric interpretation of the resulting cylinder shape.

---

## 3. Key Concepts and Theorems
1. **Geometry of a Right Circular Cylinder:**
   - Volume: $V = \pi r^2 h$.
   - Lateral Surface Area: $S_{\text{lat}} = 2\pi r h$.
   - Base Area (two circular discs, top and bottom): $2 S_{\text{base}} = 2\pi r^2$.
   - Total Surface Area: $S = 2\pi r^2 + 2\pi r h$.
2. **Single-Variable Optimization with Equality Constraint:**
   Using the constraint $V = \pi r^2 h$ allows expressing $h = \frac{V}{\pi r^2}$, reducing the two-variable area $S(r, h)$ to a single-variable function $S(r)$.
3. **Second Derivative Test:**
   If $S'(r_0) = 0$ and $S''(r_0) > 0$ on an open interval where $S$ is continuous, $r_0$ is a strict minimum.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Write the volume constraint
Let $r > 0$ be the radius of the circular base and $h > 0$ be the height of the cylinder.
The volume of a right circular cylinder is given by the base area times the height:
$$V = \pi r^2 h.$$
Because the volume is fixed, $V$ is treated as a positive constant.

### Step 2: Eliminate one of the variables
We isolate the height $h$ in terms of the radius $r$ and the constant volume $V$:
$$h = \frac{V}{\pi r^2}.$$

### Step 3: Express the surface area as a function of $r$
The can is closed, meaning material is used for the curved lateral side and both circular ends (top and bottom lids):
$$S = 2(\text{Area of base}) + \text{Area of side} = 2(\pi r^2) + 2\pi r h.$$
Substitute $h = \frac{V}{\pi r^2}$ into the surface area equation:
$$S(r) = 2\pi r^2 + 2\pi r \left(\frac{V}{\pi r^2}\right).$$
Simplify the second term by canceling the common factor of $\pi r$:
$$S(r) = 2\pi r^2 + \frac{2V}{r} = 2\pi r^2 + 2V r^{-1}.$$
The domain for the radius is $r \in (0, \infty)$.

### Step 4: Minimize material usage and find the relation between $h$ and $r$
Differentiate $S(r)$ with respect to $r$:
$$S'(r) = \frac{d}{dr}\left(2\pi r^2 + 2V r^{-1}\right) = 4\pi r - 2V r^{-2} = 4\pi r - \frac{2V}{r^2}.$$
Set $S'(r) = 0$ to find stationary points:
$$4\pi r - \frac{2V}{r^2} = 0 \iff 4\pi r = \frac{2V}{r^2}.$$
Multiply both sides by $r^2$:
$$4\pi r^3 = 2V \iff 2\pi r^3 = V.$$
Solving for $r$ gives the unique critical radius:
$$r = \sqrt[3]{\frac{V}{2\pi}}.$$

Now, to find the relation between $h$ and $r$, substitute the volume constraint $V = \pi r^2 h$ back into $2\pi r^3 = V$:
$$2\pi r^3 = \pi r^2 h.$$
Divide both sides by $\pi r^2$ (which is strictly positive):
$$2r = h \iff h = 2r.$$

### Step 5: Verify that this is a strict global minimum
Compute the second derivative:
$$S''(r) = \frac{d}{dr}\left(4\pi r - \frac{2V}{r^2}\right) = 4\pi + \frac{4V}{r^3}.$$
Since $V > 0$ and $r > 0$, both terms are strictly positive:
$$S''(r) > 0 \quad \text{for all } r \in (0, \infty).$$
Because the second derivative is positive throughout the entire domain, $S(r)$ is strictly convex. Therefore, the critical point is the **unique global minimum**.
Furthermore, as $r \to 0^+$, $S(r) \to \infty$ (infinitely tall, skinny can), and as $r \to \infty$, $S(r) \to \infty$ (infinitely wide, flat discs), confirming that the minimum occurs in the interior.

### Step 6: Geometric interpretation of $h = 2r$
The optimal relation:
$$h = 2r = d \quad (\text{height} = \text{diameter})$$
has an elegant geometric interpretation:
1. **Square Cross-Section:**
   A vertical cross-section through the central symmetry axis of the optimal cylinder is a rectangle of width $2r$ and height $h$. Because $h = 2r$, this cross-section is an exact **square** of dimensions $2r \times 2r$.
2. **Equidistance / Compactness:**
   A cylinder whose height equals its diameter is the most "compact" cylinder possible: it fits tightly inside a cube of edge length $2r$, and circumscribes a sphere of diameter $2r$. 
   It strikes the perfect mathematical balance between minimizing the area of the circular ends (which grow with $r^2$) and the lateral wall (which shrinks with $r$ for fixed volume).

```text
                  Optimal Can (h = 2r)
                     . - - - - .
                   '             '
                  +---------------+  ---
                  |               |   |
                  |               |   |
                  |     2r x 2r   |   h = 2r (Diameter)
                  |    (Square)   |   |
                  |               |   |
                  +---------------+  ---
                   .             .
                     ' - - - - '
                  |<------2r----->|
```

---

## 5. Why Each Step Is Valid
- **Step 1:** The formulas for circular cylinder volume and surface area are standard Euclidean geometric theorems.
- **Step 2:** An equality constraint on two positive variables reduces the dimension of the optimization space from 2 to 1.
- **Step 3:** The total surface area of a closed container includes both lids ($2\pi r^2$) and the side wrapper ($2\pi r h$).
- **Step 4:** Setting the first derivative to zero identifies the only stationary point on $(0, \infty)$.
- **Step 5:** A strictly positive second derivative across an entire open convex domain guarantees a unique global minimum.
- **Step 6:** $2r$ is by definition the diameter of a circle of radius $r$.

---

## 6. Final Answer in Words
1. The volume constraint is $V = \pi r^2 h$.
2. Eliminating height gives $h = \frac{V}{\pi r^2}$.
3. The surface area function is $S(r) = 2\pi r^2 + \frac{2V}{r}$.
4. Setting the derivative $S'(r) = 4\pi r - \frac{2V}{r^2} = 0$ yields the relation:
   $$h = 2r.$$
The geometric interpretation is that the cylinder's height must equal its diameter. This means the cylinder is as wide as it is tall, having a square axial cross-section of dimensions $2r \times 2r$, which maximizes compactness and minimizes surface area.

---

## 7. Quick Verification
- Let $V = 2\pi \approx 6.28$:
  Then $r = \sqrt[3]{\frac{2\pi}{2\pi}} = \sqrt[3]{1} = 1$.
  $h = 2r = 2(1) = 2$.
  Check volume: $\pi r^2 h = \pi(1^2)(2) = 2\pi = V$.
  Surface area at optimum ($r = 1, h = 2$):
  $S(1) = 2\pi(1^2) + \frac{2(2\pi)}{1} = 2\pi + 4\pi = 6\pi \approx 18.85$.
- Test $r = 0.5 \implies h = \frac{2\pi}{\pi(0.25)} = 8$:
  $S(0.5) = 2\pi(0.25) + 2\pi(0.5)(8) = 0.5\pi + 8\pi = 8.5\pi \approx 26.70 > 6\pi$.
- Test $r = 2 \implies h = \frac{2\pi}{\pi(4)} = 0.5$:
  $S(2) = 2\pi(4) + 2\pi(2)(0.5) = 8\pi + 2\pi = 10\pi \approx 31.42 > 6\pi$.
The minimum at $h = 2r$ is verified numerically.

---

## 8. Common Mistakes to Avoid
- **Forgetting one or both lids:** Using $S = \pi r^2 + 2\pi r h$ (open can) instead of $2\pi r^2 + 2\pi r h$ (closed can). (For an open can, the optimum is $h = r$).
- **Differentiating with respect to both variables simultaneously without the constraint:** You cannot set $\frac{\partial S}{\partial r} = 0$ and $\frac{\partial S}{\partial h} = 0$ independently because $r$ and $h$ are linked by $V$.
- **Algebraic error in derivative of $r^{-1}$:** Writing $\frac{d}{dr}(\frac{1}{r}) = \frac{1}{r^2}$ instead of $-\frac{1}{r^2}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
From the fixed volume $V = \pi r^2 h$, we eliminate height to express the cylinder's total surface area as $S(r) = 2\pi r^2 + 2V/r$. Differentiating and setting $S'(r) = 4\pi r - 2V/r^2 = 0$ yields the optimal condition $2\pi r^3 = V$, which simplifies directly to $h = 2r$. Geometrically, this means the can's height must equal its diameter, producing a square cross-section that maximizes volumetric compactness while using minimal material.
