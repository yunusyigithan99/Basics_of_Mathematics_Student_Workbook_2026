# Problem 13 Solution: A Multi-Layer Composition

## 1. Original Problem
For the three-layer composite function:
$$f(x) = e^{\sin(x^2)}$$
1. Explicitly trace and write down the sequence of nested operational layers:
   $$x \longrightarrow x^2 \longrightarrow \sin(x^2) \longrightarrow e^{\sin(x^2)}.$$
2. Compute the complete derivative $f'(x)$ using the multi-stage Chain Rule.
3. Explain why the process of differentiation unwraps these nested layers in the exact **reverse order** (from outside to inside).

---

## 2. What We Are Trying to Find
We need to:
1. Decompose the function into three distinct functional layers: an innermost polynomial, a middle trigonometric function, and an outermost exponential.
2. Differentiate each layer with respect to its immediate input.
3. Apply the generalized Chain Rule:
   $$\frac{df}{dx} = \frac{df}{du} \cdot \frac{du}{dv} \cdot \frac{dv}{dx}.$$
4. Explain the conceptual and structural logic behind peeling composite functions like an onion, starting with the outermost envelope and working inward.

---

## 3. Key Concepts and Theorems
1. **The Multi-Stage Chain Rule:**
   If $y = f(u)$, $u = g(v)$, and $v = h(x)$ are differentiable functions, then the composite function $y = (f \circ g \circ h)(x)$ has derivative:
   $$\frac{dy}{dx} = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x).$$
   In Leibniz notation:
   $$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dv} \cdot \frac{dv}{dx}.$$
2. **Elementary Derivatives for Each Layer:**
   - Exponential layer: $\frac{d}{du}[e^u] = e^u$
   - Trigonometric layer: $\frac{d}{dv}[\sin v] = \cos v$
   - Power layer: $\frac{d}{dx}[x^2] = 2x$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Trace the Forward Sequence of Layers
Follow how a real input number $x$ is processed through the function to compute the output:
1. **Layer 1 (Innermost):** Square the input:
   $$v(x) = x^2.$$
2. **Layer 2 (Middle):** Take the sine of that squared value:
   $$u(v) = \sin v = \sin(x^2).$$
3. **Layer 3 (Outermost):** Exponentiate the result with base $e$:
   $$y = f(u) = e^u = e^{\sin(x^2)}.$$

Forward computational pipeline:
$$x \xrightarrow{\quad (\cdot)^2 \quad} v = x^2 \xrightarrow{\quad \sin(\cdot) \quad} u = \sin(x^2) \xrightarrow{\quad e^{(\cdot)} \quad} y = e^{\sin(x^2)}.$$

---

### Step 2: Differentiate Each Layer (Reverse Order)
To differentiate, we apply the Chain Rule starting from the outermost shell:

1. **Differentiate the Outermost Layer ($y = e^u$ with respect to $u$):**
   $$\frac{dy}{du} = e^u = e^{\sin(x^2)}.$$
2. **Differentiate the Middle Layer ($u = \sin v$ with respect to $v$):**
   $$\frac{du}{dv} = \cos v = \cos(x^2).$$
3. **Differentiate the Innermost Layer ($v = x^2$ with respect to $x$):**
   $$\frac{dv}{dx} = 2x.$$

---

### Step 3: Multiply the Layers Together
According to the multi-stage Chain Rule:
$$\frac{df}{dx} = \frac{dy}{du} \cdot \frac{du}{dv} \cdot \frac{dv}{dx}.$$
Substitute the three derivatives computed in Step 2:
$$f'(x) = \left[ e^{\sin(x^2)} \right] \cdot \left[ \cos(x^2) \right] \cdot \left[ 2x \right].$$
Writing in standard algebraic order with polynomial terms first:
$$f'(x) = 2x \cos(x^2) e^{\sin(x^2)}.$$

---

### Step 4: Why Differentiation Unwraps Layers in Reverse Order
- **Forward Construction vs. Backward Differentiation:**
  - When *evaluating* $f(x)$ for a number like $x = 2$, we start with the inner core: first $2^2 = 4$, then $\sin(4)$, and finally $e^{\sin(4)}$. We build the function from the **inside out**.
  - When *differentiating*, we observe how a tiny change $\Delta x$ propagates to the final output $f$. The final output is immediately enveloped by the exponential function.
  - To an external observer, the entire composite object is an exponential $e^u$. The first rule of calculus that must be applied is the rule governing the outermost structure: $\frac{d}{du}[e^u] = e^u$.
  - However, $u$ is not static; it is changing at the rate given by its own definition $\sin v$. Differentiating that second layer reveals the factor $\cos(x^2)$.
  - Finally, $v$ is changing at the rate $2x$.
- **The Russian Matryoshka Doll Analogy:**
  To see what is inside a nested set of boxes or Russian dolls, you cannot open the innermost box first; you must open the outermost box first, then the middle box, and finally reach the inner core.
  Differentiation works by "peeling the onion" from the outermost container down to the innermost variable $x$. Each peeled layer leaves behind its derivative factor:
  $$\text{Outer Derivative} \times \text{Middle Derivative} \times \text{Inner Derivative}.$$

---

## 5. Why Each Step Is Valid
1. **The associative property of functional composition** guarantees that $(f \circ g \circ h)'(x) = f'(g(h(x))) \cdot (g \circ h)'(x)$.
2. **Leibniz notation** $\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dv} \frac{dv}{dx}$ is algebraically justified by the product of limits of difference quotients where each denominator cancellation is valid.
3. **The commutative property of real multiplication** permits reordering the factors into $2x \cos(x^2) e^{\sin(x^2)}$.

---

## 6. Final Answer in Words
The forward operational pipeline is $x \to x^2 \to \sin(x^2) \to e^{\sin(x^2)}$. Differentiating through these three layers via the Chain Rule gives $f'(x) = 2x \cos(x^2) e^{\sin(x^2)}$. The process moves in reverse order (from outside to inside) because the outermost operation (the exponential) defines the overall container of the expression, so its rate of change must be calculated first, which is then sequentially scaled by the internal rates of change of the middle trigonometric layer ($\cos(x^2)$) and the innermost power layer ($2x$).

---

## 7. Quick Verification
- Evaluate at $x = 0$:
  $$f(0) = e^{\sin(0^2)} = e^0 = 1.$$
  $$f'(0) = 2(0) \cos(0^2) e^{\sin(0^2)} = 0 \cdot 1 \cdot 1 = 0.$$
- Numerical difference quotient check at $x = 0$ with $h = 0.001$:
  $$f(0.001) = e^{\sin(0.001^2)} = e^{\sin(10^{-6})} \approx e^{10^{-6}} \approx 1 + 10^{-6} = 1.000001.$$
  $$\frac{f(0.001) - f(0)}{0.001} \approx \frac{1.000001 - 1}{0.001} = \frac{0.000001}{0.001} = 0.001 \approx 0.$$
- Evaluate at $x = 1$:
  $$f(1) = e^{\sin(1)} \approx e^{0.84147} \approx 2.31976.$$
  $$f'(1) = 2(1) \cos(1) e^{\sin(1)} \approx 2(0.54030)(2.31976) \approx 2.5067.$$
  Difference quotient at $x = 1$ with $h = 0.0001$:
  $$f(1.0001) = e^{\sin(1.00020001)} \approx e^{\sin(1.0002)} \approx 2.32001.$$
  $$\frac{f(1.0001) - f(1)}{0.0001} \approx 2.507.$$
  Matches $f'(1)$ with extreme accuracy.

---

## 8. Common Mistakes to Avoid
- **Differentiating the inside and putting it inside the exponential:** Writing $f'(x) = e^{2x\cos(x^2)}$, which is a severe violation of the Chain Rule. The inner argument $\sin(x^2)$ remains untouched inside the exponential factor.
- **Dropping the innermost $2x$:** Writing $f'(x) = \cos(x^2) e^{\sin(x^2)}$, forgetting that $x^2$ is also a composite layer requiring differentiation.
- **Confusing $\cos(x^2)$ with $\cos^2(x)$:** Writing $\cos^2 x$ instead of $\cos(x^2)$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The function $e^{\sin(x^2)}$ is composed of three nested layers: an inner square $x^2$, a middle sine $\sin(x^2)$, and an outer exponential $e^u$. Differentiation unwraps these layers in reverse order—from the outside in—first differentiating the exponential to get $e^{\sin(x^2)}$, then the sine to get $\cos(x^2)$, and finally the inner square to get $2x$. Multiplying these three rates of change together produces the complete derivative $2x \cos(x^2) e^{\sin(x^2)}$.
