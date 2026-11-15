# Problem 5 Solution: The Chain Rule as Working Through Layers

## 1. Original Problem
For the composite function:
$$f(x) = (3x^2 - 2x + 1)^5$$
1. Explicitly identify the inner function $u(x)$ and the outer function $g(u)$.
2. Compute their individual derivatives $u'(x)$ and $g'(u)$.
3. Combine the results according to the Chain Rule to find $f'(x)$.
4. Explain in detail the origin and physical/geometric meaning of the additional multiplying factor that appears during chain rule differentiation.

---

## 2. What We Are Trying to Find
We need to:
1. Deconstruct the composite function $f(x) = g(u(x))$ into its two operational layers: the inner quadratic polynomial and the outer quintic power.
2. Differentiate the outer layer with respect to its variable $u$, keeping the inner expression intact.
3. Differentiate the inner layer with respect to $x$.
4. Multiply the two derivative layers together: $f'(x) = g'(u(x)) \cdot u'(x)$.
5. Explain the Chain Rule as a multiplicative transmission ratio of rates of change (like interlocking mechanical gears).

---

## 3. Key Concepts and Theorems
1. **The Chain Rule:**
   If $u = h(x)$ is differentiable at $x$ and $y = g(u)$ is differentiable at $u = h(x)$, then the composite function $f(x) = g(h(x))$ is differentiable at $x$, and its derivative is given by:
   $$f'(x) = g'(h(x)) \cdot h'(x).$$
2. **Leibniz Notation for the Chain Rule:**
   $$\frac{df}{dx} = \frac{df}{du} \cdot \frac{du}{dx}.$$
   This notation clearly displays the Chain Rule as a product of rates: the sensitivity of $f$ to changes in $u$, multiplied by the sensitivity of $u$ to changes in $x$.
3. **The General Power Rule (Special Case of the Chain Rule):**
   For any differentiable function $u(x)$ and real power $n$:
   $$\frac{d}{dx}\left[ (u(x))^n \right] = n (u(x))^{n-1} \cdot u'(x).$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Inner and Outer Layers
Examine how an input value $x$ is processed by $f(x) = (3x^2 - 2x + 1)^5$:
- **Step A (Inner Layer):** The input $x$ is first evaluated by the polynomial:
  $$u(x) = 3x^2 - 2x + 1.$$
- **Step B (Outer Layer):** The intermediate result $u$ is then raised to the fifth power:
  $$g(u) = u^5.$$
Thus, $f(x) = g(u(x)) = (u(x))^5$.

---

### Step 2: Compute the Derivatives of the Layers
1. **Derivative of the outer function $g(u) = u^5$ with respect to $u$:**
   $$\frac{dg}{du} = g'(u) = 5 u^{5-1} = 5u^4.$$
2. **Derivative of the inner function $u(x) = 3x^2 - 2x + 1$ with respect to $x$:**
   $$\frac{du}{dx} = u'(x) = \frac{d}{dx}[3x^2 - 2x + 1] = 6x - 2.$$

---

### Step 3: Combine Using the Chain Rule
Apply the Chain Rule formula $f'(x) = g'(u(x)) \cdot u'(x)$:
$$f'(x) = 5\big(u(x)\big)^4 \cdot u'(x).$$
Substitute back the explicit formula $u(x) = 3x^2 - 2x + 1$:
$$f'(x) = 5(3x^2 - 2x + 1)^4 \cdot (6x - 2).$$

We can optionally factor out $2$ from the linear term $(6x - 2) = 2(3x - 1)$:
$$f'(x) = 5 \cdot 2(3x - 1)(3x^2 - 2x + 1)^4 = 10(3x - 1)(3x^2 - 2x + 1)^4.$$

---

### Step 4: Explanation of the Additional Factor $(6x - 2)$
- **Why Can't We Just Write $5(3x^2 - 2x + 1)^4$?**
  Writing only $5(3x^2 - 2x + 1)^4$ would be the derivative with respect to $u$, which answers: *"How fast does $f$ change per unit change in $u$?"* ($\frac{df}{du}$).
  However, we are asked to find the derivative with respect to $x$, which answers: *"How fast does $f$ change per unit change in $x$?"* ($\frac{df}{dx}$).
- **The Transmission / Gear Analogy:**
  Imagine three connected gears: Gear $x$ turns Gear $u$, which in turn turns Gear $f$.
  - When $x$ moves by a tiny step $\Delta x$, the inner variable $u$ responds by changing by $\Delta u \approx (6x - 2) \Delta x$.
  - Then, this change $\Delta u$ is fed into the outer function $f$, which amplifies it by $5u^4$:
    $$\Delta f \approx (5u^4) \Delta u.$$
  - Combining these two stages by substitution:
    $$\Delta f \approx (5u^4) \cdot \Big((6x - 2) \Delta x\Big) = \big[5(3x^2 - 2x + 1)^4 \cdot (6x - 2)\big] \Delta x.$$
- The additional factor $(6x - 2) = u'(x)$ is therefore the **internal transmission ratio** that converts changes in $x$ into changes in $u$ before the outer function operates on them. Without it, the rate calculation is incomplete.

---

## 5. Why Each Step Is Valid
1. **Decomposing into layers** is valid because composition of functions is associative: $f = g \circ u$.
2. **The Chain Rule theorem** is proven via linear approximation: $\Delta f = g'(u)\Delta u + o(\Delta u) = g'(u)[u'(x)\Delta x + o(\Delta x)] + \dots = g'(u)u'(x)\Delta x + o(\Delta x)$.
3. **Factoring 2** uses basic algebraic distributive rules.

---

## 6. Final Answer in Words
The inner function is $u(x) = 3x^2 - 2x + 1$ with derivative $u'(x) = 6x - 2$, and the outer function is $g(u) = u^5$ with derivative $g'(u) = 5u^4$. Combining them using the Chain Rule gives the derivative $f'(x) = 5(3x^2 - 2x + 1)^4(6x - 2) = 10(3x - 1)(3x^2 - 2x + 1)^4$. The additional factor $(6x - 2)$ represents the derivative of the inner layer $\frac{du}{dx}$, which acts as a conversion factor translating how a change in the primary input $x$ induces a change in the intermediate variable $u$ before that change is amplified by the outer power function.

---

## 7. Quick Verification
- Evaluate at $x = 0$:
  $$u(0) = 3(0)^2 - 2(0) + 1 = 1.$$
  $$f(0) = 1^5 = 1.$$
  $$f'(0) = 5(1)^4 \cdot (6(0) - 2) = 5(1)(-2) = -10.$$
- Difference quotient check at $x = 0$ with $h = 0.001$:
  $$u(0.001) = 3(0.001)^2 - 2(0.001) + 1 = 0.000003 - 0.002 + 1 = 0.998003.$$
  $$f(0.001) = (0.998003)^5 \approx 0.9900597.$$
  $$\frac{f(0.001) - f(0)}{0.001} = \frac{0.9900597 - 1}{0.001} = \frac{-0.0099403}{0.001} \approx -9.94 \approx -10.0.$$
  The numerical rate of change agrees with $f'(0) = -10$.

---

## 8. Common Mistakes to Avoid
- **Forgetting the inner derivative factor:** Writing $f'(x) = 5(3x^2 - 2x + 1)^4$, omitting $(6x - 2)$ entirely.
- **Differentiating the inside at the same time as the outside:** Writing $f'(x) = 5(6x - 2)^4$, which is completely invalid.
- **Dropping parentheses around the inner derivative:** Writing $5(3x^2 - 2x + 1)^4 \cdot 6x - 2$, which implies multiplying only $6x$ and then subtracting 2 at the end. Parentheses around $(6x - 2)$ are mandatory.

---

## 9. Classroom Presentation (3-Sentence Summary)
We break the composite function into an inner polynomial layer $u = 3x^2 - 2x + 1$ and an outer power layer $g(u) = u^5$. Differentiating the outer layer gives $5u^4$ and differentiating the inner layer gives $6x - 2$. Multiplying these layers together by the Chain Rule yields $5(3x^2 - 2x + 1)^4(6x - 2)$, where the extra factor $(6x - 2)$ acts as a transmission ratio translating the rate of change from the inner variable $x$ to the outer power.
