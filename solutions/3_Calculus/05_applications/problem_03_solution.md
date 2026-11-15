# Problem 03: Geometric Optimization — Maximum Volume of an Open Box

## 1. Original Problem
From a $30\text{ cm} \times 40\text{ cm}$ sheet, squares of side length $x$ are cut from the corners and the edges are folded up to form an open box.

Write the volume as a function of $x$, determine the physically meaningful domain, and find the value of $x$ for which the volume is greatest.

---

## 2. What We Are Trying to Find
1. The mathematical formula for the volume $V(x)$ as a function of the cut-out corner size $x$.
2. The physically meaningful domain of $x$ based on the dimensions of the cardboard sheet.
3. The derivative $V'(x)$ and the determination of all critical points.
4. Identification of the unique critical point lying inside the physical domain.
5. Verification that this point produces the absolute maximum volume, along with calculation of the maximum volume.

---

## 3. Key Concepts and Theorems
1. **Geometric Modeling of a Folded Box:**
   When four squares of side $x$ are cut from the corners of an $a \times b$ sheet:
   - Box Height: $h = x$.
   - Box Width: $w = a - 2x$.
   - Box Length: $l = b - 2x$.
   - Box Volume: $V(x) = x(a - 2x)(b - 2x)$.
2. **Physical Feasibility Domain:**
   All physical dimensions (height, width, length) must be strictly positive:
   $$x > 0, \quad a - 2x > 0, \quad b - 2x > 0.$$
3. **Extreme Value Theorem on Compact Intervals:**
   A continuous function on a closed interval $[0, x_{\max}]$ attains its absolute maximum either at an interior critical point where $V'(x) = 0$ or at the boundary endpoints where $V(0) = V(x_{\max}) = 0$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Formulate the volume function $V(x)$
The original cardboard sheet has dimensions $30\text{ cm} \times 40\text{ cm}$.
Cutting squares of side length $x$ from each of the four corners and folding the remaining flaps vertically produces an open rectangular box:
- Height: $h = x$
- Width: $w = 30 - 2x$
- Length: $l = 40 - 2x$

The volume of the box is the product of its three dimensions:
$$V(x) = x(30 - 2x)(40 - 2x).$$
Expanding the expression:
$$(30 - 2x)(40 - 2x) = 1200 - 60x - 80x + 4x^2 = 4x^2 - 140x + 1200.$$
Multiplying by $x$:
$$V(x) = 4x^3 - 140x^2 + 1200x.$$

### Step 2: Determine the physically meaningful domain
Every dimension must be strictly positive for a real three-dimensional box:
1. Height: $x > 0$.
2. Width: $30 - 2x > 0 \iff 2x < 30 \iff x < 15$.
3. Length: $40 - 2x > 0 \iff 2x < 40 \iff x < 20$.

The most restrictive upper bound comes from the shorter side of the sheet ($30\text{ cm}$). Therefore, the physically meaningful domain is:
$$D_V = (0, 15) \quad \text{cm}.$$
At the boundaries $x = 0$ (no fold) and $x = 15$ (sheet cut completely in half), the volume drops to zero: $V(0) = 0$ and $V(15) = 0$.

### Step 3: Compute the derivative and find critical points
Differentiating $V(x) = 4x^3 - 140x^2 + 1200x$ with respect to $x$:
$$V'(x) = 12x^2 - 280x + 1200.$$
Factor out the greatest common factor $4$:
$$V'(x) = 4(3x^2 - 70x + 300).$$
Set $V'(x) = 0$ to find stationary points:
$$3x^2 - 70x + 300 = 0.$$
Applying the quadratic formula with $a = 3$, $b = -70$, $c = 300$:
$$\Delta = b^2 - 4ac = (-70)^2 - 4(3)(300) = 4900 - 3600 = 1300.$$
$$\sqrt{\Delta} = \sqrt{1300} = \sqrt{100 \times 13} = 10\sqrt{13} \approx 36.0555.$$
The two roots are:
$$x = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{70 \pm 10\sqrt{13}}{2 \times 3} = \frac{35 \pm 5\sqrt{13}}{3}.$$

Evaluating the numerical values:
- **First root:**
  $$x_1 = \frac{35 - 5\sqrt{13}}{3} \approx \frac{35 - 18.0278}{3} = \frac{16.9722}{3} \approx 5.6574\text{ cm}.$$
- **Second root:**
  $$x_2 = \frac{35 + 5\sqrt{13}}{3} \approx \frac{35 + 18.0278}{3} = \frac{53.0278}{3} \approx 17.6759\text{ cm}.$$

### Step 4: Discard the non-physical root and verify the maximum
- The second root $x_2 \approx 17.68\text{ cm}$ lies outside the domain $(0, 15)$ because cutting $17.68\text{ cm}$ from both sides requires $2 \times 17.68 = 35.36\text{ cm} > 30\text{ cm}$, which is physically impossible.
- The first root $x_1 = \frac{35 - 5\sqrt{13}}{3} \approx 5.66\text{ cm}$ lies comfortably within $(0, 15)$.

We verify that $x_1$ is a maximum using the Second Derivative Test:
$$V''(x) = \frac{d}{dx}(12x^2 - 280x + 1200) = 24x - 280.$$
Evaluate $V''(x)$ at $x_1 \approx 5.66$:
$$V''(5.66) \approx 24(5.66) - 280 = 135.84 - 280 = -144.16 < 0.$$
Because $V''(x_1) < 0$, $x_1$ is a **strict local maximum**.
Since $V(x)$ is continuous on the closed interval $[0, 15]$ with $V(0) = 0$ and $V(15) = 0$, $x_1$ is the **unique absolute global maximum**.

### Step 5: Compute the dimensions and maximum volume
Using $x \approx 5.66\text{ cm}$:
- Height: $h \approx 5.66\text{ cm}$
- Width: $w = 30 - 2(5.6574) \approx 18.69\text{ cm}$
- Length: $l = 40 - 2(5.6574) \approx 28.69\text{ cm}$
- Maximum Volume:
  $$V_{\max} \approx 5.6574 \times 18.6852 \times 28.6852 \approx 3032.3\text{ cm}^3.$$

---

## 5. Why Each Step Is Valid
- **Step 1:** Folding an open box creates a rectangular prism whose volume is length $\times$ width $\times$ height.
- **Step 2:** The shorter side limits the size of the corner square; cutting two squares of size $15\text{ cm}$ consumes the entire $30\text{ cm}$ edge.
- **Step 3:** The quadratic formula determines the exact zeros of the polynomial derivative.
- **Step 4:** Discarding extraneous roots outside the physical domain is mandatory in applied optimization.
- **Step 5:** The second derivative test guarantees concavity at the critical point.

---

## 6. Final Answer in Words
1. The volume function is $V(x) = 4x^3 - 140x^2 + 1200x$.
2. The physically meaningful domain is $D_V = (0, 15)\text{ cm}$.
3. The value of $x$ for which the volume is greatest is:
   $$x = \frac{35 - 5\sqrt{13}}{3} \approx 5.66\text{ cm}.$$
At this cut size, the box dimensions are approximately $28.69\text{ cm} \times 18.69\text{ cm} \times 5.66\text{ cm}$, producing a maximum volume of approximately $3032.3\text{ cm}^3$.

---

## 7. Quick Verification
- Test nearby integer values of $x$:
  - If $x = 5$: $V(5) = 5(30 - 10)(40 - 10) = 5(20)(30) = 3000\text{ cm}^3$.
  - If $x = 6$: $V(6) = 6(30 - 12)(40 - 12) = 6(18)(28) = 3024\text{ cm}^3$.
  - If $x = 7$: $V(7) = 7(30 - 14)(40 - 14) = 7(16)(26) = 2912\text{ cm}^3$.
Notice that $V(5) = 3000 < 3024 < 3032.3 > 3024 > 2912$, confirming that the peak lies right around $5.66$.

---

## 8. Common Mistakes to Avoid
- **Selecting the larger root $x_2 \approx 17.68$:** Failing to check the domain and choosing a cut size that exceeds half the cardboard's width.
- **Expanding $(30 - 2x)(40 - 2x)$ incorrectly:** Forgetting that cutting corners removes $2x$ from each dimension, not just $x$.
- **Not proving it is a maximum:** Omitting the second derivative check or boundary comparison.

---

## 9. Classroom Presentation (3-Sentence Summary)
Cutting corner squares of side $x$ yields an open box with volume $V(x) = x(30 - 2x)(40 - 2x)$, which is physically valid on the domain $(0, 15)\text{ cm}$. Differentiating and setting $V'(x) = 12x^2 - 280x + 1200 = 0$ gives two mathematical roots, but only $x = (35 - 5\sqrt{13})/3 \approx 5.66\text{ cm}$ lies within the physical sheet boundaries. Because the second derivative is negative at this point, cutting $5.66\text{ cm}$ squares maximizes the box's capacity at approximately $3032.3\text{ cm}^3$.
