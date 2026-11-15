# Problem 8 Solution: Two Exponential Functions

## 1. Original Problem
For the function:
$$f(x) = e^{2x - 3} + 5^x$$
1. Compute the derivative $f'(x)$.
2. Explain in detail the exact mathematical reason why the numerical factor $2$ appears in the derivative of the first term $e^{2x - 3}$.
3. Explain in detail the exact mathematical reason why the factor $\ln 5$ appears in the derivative of the second term $5^x$.

---

## 2. What We Are Trying to Find
We need to:
1. Differentiate the natural exponential composition $e^{2x - 3}$ using the Chain Rule.
2. Differentiate the general base exponential function $5^x$ using the general exponential rule.
3. Compare the two distinct mechanisms generating multiplying factors:
   - An inner linear argument ($2x - 3$) requiring a Chain Rule factor of $2$.
   - A non-natural base ($5$) requiring a base-change conversion factor of $\ln 5$.

---

## 3. Key Concepts and Theorems
1. **Natural Exponential Chain Rule:**
   For any differentiable function $u(x)$:
   $$\frac{d}{dx}[e^{u(x)}] = e^{u(x)} \cdot u'(x).$$
2. **Derivative of General Exponential Functions ($a^x$):**
   For any positive base $a > 0, a \neq 1$:
   $$\frac{d}{dx}[a^x] = a^x \ln a.$$
3. **The Base-Change Identity for Exponentials:**
   Any exponential $a^x$ can be rewritten in base $e$ using the natural logarithm:
   $$a^x = \left(e^{\ln a}\right)^x = e^{x \ln a}.$$
   Differentiating $e^{x \ln a}$ with respect to $x$ via the Chain Rule brings down the constant factor $\ln a$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Differentiate the First Term $e^{2x - 3}$
The first term is a composite function:
$$f_1(x) = e^{2x - 3}.$$
- Outer function: $g(u) = e^u \implies g'(u) = e^u$
- Inner function: $u(x) = 2x - 3 \implies u'(x) = 2$

Apply the Chain Rule:
$$\frac{d}{dx}[e^{2x - 3}] = e^{u(x)} \cdot u'(x) = e^{2x - 3} \cdot 2 = 2e^{2x - 3}.$$

---

### Step 2: Differentiate the Second Term $5^x$
The second term is an exponential with general base $a = 5$:
$$f_2(x) = 5^x.$$
Using the general exponential differentiation rule:
$$\frac{d}{dx}[5^x] = 5^x \ln 5.$$

---

### Step 3: Combine to Form the Complete Derivative
By the sum rule of differentiation:
$$f'(x) = \frac{d}{dx}[e^{2x - 3}] + \frac{d}{dx}[5^x] = 2e^{2x - 3} + 5^x \ln 5.$$

---

### Step 4: Why the Factor 2 Appears in the First Term
- In $e^{2x - 3}$, the base is already the natural base $e$.
- For the standard function $e^x$, its derivative is simply itself ($e^x$).
- However, the exponent is not simply $x$; it is the linear function $u(x) = 2x - 3$.
- By the **Chain Rule**, the rate of change of an outer function must be multiplied by the internal rate of change of its argument:
  $$\frac{d}{dx}[2x - 3] = 2.$$
- When $x$ advances by 1 unit, the argument $2x - 3$ advances twice as fast (by 2 units). Therefore, the overall exponential growth rate is doubled.
- Thus, the factor $2$ arises entirely from the **Chain Rule applied to the linear exponent**.

---

### Step 5: Why the Factor $\ln 5$ Appears in the Second Term
- In $5^x$, the exponent is simply $x$ (whose derivative is 1), so no Chain Rule scaling is needed for the exponent.
- However, the base is $5$, not the natural base $e$.
- The number $e \approx 2.71828$ is unique in mathematics because it is the **only base** whose exponential function has an instantaneous growth rate exactly equal to its height: $\frac{d}{dx}[e^x]_{x=0} = 1$.
- Any other base $a$ grows at a rate proportional to $a^x$, scaled by the constant slope at the origin:
  $$\lim_{h\to0} \frac{a^h - 1}{h} = \ln a.$$
- To see this algebraically, express $5^x$ in natural base $e$:
  $$5^x = \left(e^{\ln 5}\right)^x = e^{(\ln 5) x}.$$
  Now differentiate $e^{(\ln 5) x}$ using the Chain Rule, treating the constant $\ln 5$ as a coefficient:
  $$\frac{d}{dx}\left[e^{(\ln 5) x}\right] = e^{(\ln 5) x} \cdot \frac{d}{dx}[(\ln 5) x] = e^{(\ln 5) x} \cdot \ln 5 = 5^x \ln 5.$$
- Thus, the factor $\ln 5 \approx 1.6094$ arises as a **base-conversion scaling factor** compensating for the fact that base 5 grows faster than base $e$.

---

## 5. Why Each Step Is Valid
1. **The Chain Rule on $e^{2x-3}$** is valid because the exponent $2x - 3$ is a differentiable function of $x$.
2. **The base change $5^x = e^{x\ln 5}$** is an exact algebraic identity since $\exp$ and $\ln$ are inverse bijections on $(0, \infty)$.
3. **The sum rule** applies because differentiation is a linear operator.

---

## 6. Final Answer in Words
The derivative of $f(x) = e^{2x - 3} + 5^x$ is $f'(x) = 2e^{2x - 3} + 5^x \ln 5$. The factor of $2$ appears in the first term due to the **Chain Rule**, because the exponent $2x - 3$ has an inner derivative of $\frac{d}{dx}[2x - 3] = 2$. The factor of $\ln 5$ appears in the second term as a **base-scaling constant**, because $5^x$ has base 5 rather than the natural base $e$; rewriting $5^x$ as $e^{x\ln 5}$ reveals that differentiating with respect to $x$ pulls down the constant multiplier $\ln 5$.

---

## 7. Quick Verification
- Evaluate at $x = 0$:
  $$f(0) = e^{-3} + 5^0 = e^{-3} + 1 \approx 0.049787 + 1 = 1.049787.$$
  $$f'(0) = 2e^{-3} + 5^0 \ln 5 = 2e^{-3} + \ln 5 \approx 2(0.049787) + 1.609438 = 0.099574 + 1.609438 = 1.709012.$$
- Numerical difference quotient check at $x = 0$ with $h = 0.0001$:
  $$f(0.0001) = e^{2(0.0001) - 3} + 5^{0.0001} = e^{-2.9998} + 5^{0.0001} \approx 0.0497970 + 1.00016095 = 1.0499580.$$
  $$\frac{f(0.0001) - f(0)}{0.0001} \approx \frac{1.0499580 - 1.0497871}{0.0001} = \frac{0.0001709}{0.0001} = 1.709.$$
  The numerical rate of change agrees with $f'(0) \approx 1.7090$.

---

## 8. Common Mistakes to Avoid
- **Treating $5^x$ as a power rule function:** Writing $\frac{d}{dx}[5^x] = x 5^{x-1}$. The power rule applies to $x^n$ (variable base, constant power), not $a^x$ (constant base, variable power).
- **Forgetting $\ln 5$:** Writing $\frac{d}{dx}[5^x] = 5^x$, treating 5 as if it were $e$.
- **Writing $\ln 5$ in the denominator:** Dividing by $\ln 5$ (which is what one does when *integrating* $5^x$, not differentiating).

---

## 9. Classroom Presentation (3-Sentence Summary)
Differentiating the first term $e^{2x - 3}$ produces $2e^{2x - 3}$ because the Chain Rule multiplies by the derivative of the inner exponent $2x - 3$, which is 2. Differentiating the second term $5^x$ produces $5^x \ln 5$ because base 5 must be converted to base $e$ via $e^{x \ln 5}$, which brings down the constant factor $\ln 5$. Combining these gives the full derivative $f'(x) = 2e^{2x - 3} + 5^x \ln 5$, clearly illustrating the contrast between an inner Chain Rule factor and a base-change factor.
