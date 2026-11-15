# Problem 10: Routing Optimization — Laying Cable Through Water and Land

## 1. Original Problem
Point $A$ lies on one bank of a river of width $100$ m, and point $B$ lies on the other bank, $500$ m along the bank from the point directly opposite $A$.

The cost per meter of cable underwater is twice the cost per meter of cable on land.

Build a cost function depending on the point where the cable comes out of the water, determine the domain, and find the solution that minimizes the cost.

---

## 2. What We Are Trying to Find
1. A geometric coordinate model of the river crossing and cable path.
2. The distance formulas for the underwater path and the land path as functions of the landing point coordinate $x$.
3. The total cost objective function $C(x)$ and its physical domain.
4. The first derivative $C'(x)$ and the exact critical point.
5. Verification that this point is the unique global minimum (comparing with boundary endpoints).
6. The connection between the optimal angle and Snell's Law (law of refraction).

---

## 3. Key Concepts and Theorems
1. **Pythagorean Distance in a Plane:**
   The straight-line underwater distance from $(0, 100)$ to landing point $(x, 0)$ is:
   $$d_{\text{water}} = \sqrt{x^2 + 100^2}.$$
2. **Cost Function Formulation:**
   Let $c > 0$ be the cost per meter on land; then $2c$ is the cost per meter underwater.
   $$\text{Total Cost } C(x) = 2c \cdot d_{\text{water}} + c \cdot d_{\text{land}} = c\left(2\sqrt{x^2 + 10000} + (500 - x)\right).$$
3. **Fermat's Principle / Snell's Law of Refraction:**
   The path minimizing time or cost between two media with differing unit costs obeys:
   $$\frac{\sin\theta_{\text{water}}}{\sin\theta_{\text{land}}} = \frac{c_{\text{land}}}{c_{\text{water}}} = \frac{1}{2}.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Geometric setup and coordinate system
We set up a Cartesian coordinate system along the river:
- Let the opposite bank containing point $B$ lie along the $x$-axis ($y = 0$).
- Point $A$ is on the starting bank at $(0, 100)$, where the river width is $100\text{ m}$.
- The point directly opposite $A$ on the target bank is $(0, 0)$.
- Point $B$ lies downriver at $(500, 0)$.
- The cable travels in a straight line underwater from $A(0, 100)$ to a landing point $P(x, 0)$ on the opposite bank.
- From $P(x, 0)$, the cable runs along the straight bank on land to $B(500, 0)$.

```text
       Bank 1:  A(0, 100)
                *
                |  \  (Underwater path)
      100 m     |    \  d_water = √(x^2 + 100^2)
                |      \
       Bank 2:  +-------*-------------------------* B(500, 0)
              (0,0)   P(x, 0)       (500 - x)
                <---x---><----------(Land)-------->
```

### Step 2: Formulate the distances and cost function
1. **Underwater distance:**
   Using the Pythagorean theorem for the right triangle with legs $100$ and $x$:
   $$d_{\text{water}} = \sqrt{x^2 + 100^2} = \sqrt{x^2 + 10000}.$$
2. **Land distance:**
   The remaining straight-line distance along the bank to point $B$ is:
   $$d_{\text{land}} = 500 - x.$$
3. **Total Cost function:**
   Let $c > 0$ be the cost per meter of laying cable on land (in arbitrary currency units, e.g., PLN/m or USD/m).
   Then the underwater cost is $2c$ per meter.
   $$C(x) = 2c \cdot d_{\text{water}} + c \cdot d_{\text{land}} = c \left(2\sqrt{x^2 + 10000} + (500 - x)\right).$$
   Because $c$ is a positive constant scalar, minimizing $C(x)$ is mathematically equivalent to minimizing the normalized cost function:
   $$f(x) = 2\sqrt{x^2 + 10000} + 500 - x.$$

### Step 3: Determine the domain
The landing point $P(x, 0)$ can realistically be placed anywhere between the point directly across from $A$ ($x = 0$) and the destination point $B$ ($x = 500$):
$$D = [0, 500] \quad \text{meters}.$$
- If $x = 0$: The cable crosses perpendicularly ($100\text{ m}$ in water), then runs $500\text{ m}$ on land.
- If $x = 500$: The cable runs directly underwater from $A$ to $B$ in a single straight line (no land cable).

### Step 4: Differentiate and find the critical point
Differentiating $f(x) = 2(x^2 + 10000)^{1/2} + 500 - x$ with respect to $x$:
$$f'(x) = 2 \cdot \frac{1}{2}(x^2 + 10000)^{-1/2} \cdot (2x) + 0 - 1 = \frac{2x}{\sqrt{x^2 + 10000}} - 1.$$
Set $f'(x) = 0$ to find stationary points:
$$\frac{2x}{\sqrt{x^2 + 10000}} - 1 = 0 \iff \frac{2x}{\sqrt{x^2 + 10000}} = 1.$$
Multiply by the denominator:
$$2x = \sqrt{x^2 + 10000}.$$
Since $x \ge 0$, both sides are non-negative. We square both sides:
$$(2x)^2 = x^2 + 10000 \iff 4x^2 = x^2 + 10000.$$
Subtract $x^2$:
$$3x^2 = 10000 \iff x^2 = \frac{10000}{3}.$$
Taking the positive square root:
$$x = \sqrt{\frac{10000}{3}} = \frac{100}{\sqrt{3}} = \frac{100\sqrt{3}}{3} \approx 57.735\text{ meters}.$$
Notice that $0 < 57.735 < 500$, so this critical point lies comfortably inside the domain $[0, 500]$.

### Step 5: Verify that this is the absolute minimum
We check the second derivative:
$$f''(x) = \frac{d}{dx}\left[\frac{2x}{\sqrt{x^2 + 10000}} - 1\right] = \frac{2\sqrt{x^2 + 10000} - 2x \cdot \frac{2x}{2\sqrt{x^2 + 10000}}}{x^2 + 10000}$$
$$= \frac{2(x^2 + 10000) - 2x^2}{(x^2 + 10000)^{3/2}} = \frac{20000}{(x^2 + 10000)^{3/2}}.$$
Because the numerator is $+20000 > 0$ and the denominator is strictly positive for all real $x$:
$$f''(x) > 0 \quad \text{for all } x \in [0, 500].$$
Since $f(x)$ is strictly convex on the entire interval, $x = \frac{100}{\sqrt{3}}$ is a **strict global minimum**.

Let us also evaluate the normalized cost at the critical point and at both boundaries to confirm:
1. **At left boundary $x = 0$ (perpendicular water crossing):**
   $$f(0) = 2\sqrt{0 + 10000} + 500 - 0 = 2(100) + 500 = 700.$$
2. **At right boundary $x = 500$ (pure underwater diagonal):**
   $$f(500) = 2\sqrt{500^2 + 100^2} + 0 = 2\sqrt{250000 + 10000} = 2\sqrt{260000} \approx 2(509.90) = 1019.8.$$
3. **At critical point $x = \frac{100}{\sqrt{3}} \approx 57.74\text{ m}$:**
   The underwater distance is $\sqrt{\frac{10000}{3} + 10000} = \sqrt{\frac{40000}{3}} = \frac{200}{\sqrt{3}} \approx 115.47\text{ m}$.
   $$f\left(\frac{100}{\sqrt{3}}\right) = 2\left(\frac{200}{\sqrt{3}}\right) + 500 - \frac{100}{\sqrt{3}} = 500 + \frac{300}{\sqrt{3}} = 500 + 100\sqrt{3} \approx 673.21.$$

Comparing the costs:
$$673.21 < 700 < 1019.8.$$
The critical point saves approximately $4\%$ compared to crossing straight across, and saves over $34\%$ compared to laying cable purely underwater.

### Step 6: Snell's Law interpretation
Notice that at the critical point:
$$\frac{x}{\sqrt{x^2 + 10000}} = \sin\theta = \frac{1}{2},$$
where $\theta$ is the angle between the underwater cable and the normal (perpendicular) to the river bank.
This gives:
$$\sin\theta = \frac{1}{2} \implies \theta = 30^\circ.$$
This is Fermat's principle of least cost: the sine of the angle of refraction equals the ratio of costs $\frac{c_{\text{land}}}{c_{\text{water}}} = \frac{1}{2}$.

---

## 5. Why Each Step Is Valid
- **Step 1:** The geometry of the river bank is represented by a right triangle and a straight segment.
- **Step 2:** The cost is proportional to distance traveled through each medium.
- **Step 3:** Laying cable beyond $x = 500$ or before $x = 0$ would add unnecessary distance in both media.
- **Step 4:** Differentiating via the Chain Rule and solving the radical equation locates the stationary point.
- **Step 5:** The quotient rule confirms a strictly positive second derivative, proving global convexity.
- **Step 6:** The critical condition matches the optical law of refraction.

---

## 6. Final Answer in Words
1. The cost function is $C(x) = c \left(2\sqrt{x^2 + 10000} + 500 - x\right)$, where $c$ is the land cost per meter.
2. The domain is $x \in [0, 500]$ meters.
3. The cable should emerge from the water at:
   $$x = \frac{100}{\sqrt{3}} = \frac{100\sqrt{3}}{3} \approx 57.74\text{ meters}$$
downriver from the point directly opposite $A$. 
At this landing point, the cable travels approximately $115.47\text{ m}$ underwater and $442.26\text{ m}$ on land, minimizing total cost to $c(500 + 100\sqrt{3}) \approx 673.21 c$, which is strictly cheaper than both the perpendicular crossing ($700 c$) and direct underwater routing ($1019.8 c$).

---

## 7. Quick Verification
- Test nearby points:
  - If $x = 50$: $f(50) = 2\sqrt{2500 + 10000} + 450 = 2\sqrt{12500} + 450 \approx 2(111.80) + 450 = 673.61 > 673.21$.
  - If $x = 65$: $f(65) = 2\sqrt{4225 + 10000} + 435 = 2\sqrt{14225} + 435 \approx 2(119.27) + 435 = 673.54 > 673.21$.
The cost increases in both directions away from $57.74\text{ m}$.

---

## 8. Common Mistakes to Avoid
- **Squaring without verifying signs:** Forgetting to ensure $2x \ge 0$ before squaring both sides (valid here since $x \ge 0$).
- **Assuming the cheapest route is the shortest distance:** Running straight across at $x = 0$ gives a shorter water crossing ($100\text{ m}$) but results in $700c$, which is more expensive than $673.21c$ because it fails to optimize the angle.
- **Forgetting the land cost:** Minimizing only the water distance or only the land distance rather than the combined total cost.

---

## 9. Classroom Presentation (3-Sentence Summary)
By setting up a coordinate system along the river, the total cost function is $C(x) = c(2\sqrt{x^2 + 100^2} + 500 - x)$ for landing position $x \in [0, 500]$. Setting the derivative to zero gives $2x/\sqrt{x^2 + 10000} = 1$, which solves to $x = 100/\sqrt{3} \approx 57.74\text{ meters}$. This optimal landing point satisfies Snell's Law with an exit angle of $30^\circ$, successfully minimizing the combined cost of the expensive underwater cable and the cheaper land cable.
