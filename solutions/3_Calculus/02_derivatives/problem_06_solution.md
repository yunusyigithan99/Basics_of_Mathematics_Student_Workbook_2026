# Problem 6 Solution: Product Rule and Trigonometry

## 1. Original Problem
For the function:
$$f(x) = x \sin x + \cos x$$
1. Compute the general derivative $f'(x)$ and simplify the resulting expression as far as possible.
2. Evaluate the derivative at $x = 0$, giving $f'(0)$.
3. Interpret the geometric meaning and spatial direction of the tangent line to the graph of $f(x)$ at the point where $x = 0$.

---

## 2. What We Are Trying to Find
We need to:
1. Differentiate the product term $x \sin x$ using the Product Rule.
2. Differentiate the single term $\cos x$.
3. Combine the terms and observe the algebraic cancellation between opposing trigonometric derivatives.
4. Calculate $f'(0)$.
5. Interpret a zero derivative geometrically as a horizontal tangent line.

---

## 3. Key Concepts and Theorems
1. **Derivatives of Trigonometric Functions:**
   $$\frac{d}{dx}[\sin x] = \cos x, \qquad \frac{d}{dx}[\cos x] = -\sin x.$$
2. **The Product Rule:**
   $$\frac{d}{dx}[u(x) v(x)] = u'(x) v(x) + u(x) v'(x).$$
3. **Horizontal Tangent Condition:**
   If $f'(x_0) = 0$, the tangent line to the curve at $(x_0, f(x_0))$ has slope $m = 0$. A line with zero slope is perfectly **horizontal** (parallel to the $x$-axis), which indicates a stationary point (such as a local minimum, local maximum, or horizontal inflection point).

---

## 4. Detailed Step-by-Step Solution

### Step 1: Differentiate the First Term $x \sin x$
The first term is a product of two functions:
$$u(x) = x \quad \text{and} \quad v(x) = \sin x.$$
Differentiate each factor:
$$u'(x) = \frac{d}{dx}[x] = 1,$$
$$v'(x) = \frac{d}{dx}[\sin x] = \cos x.$$
Apply the Product Rule:
$$\frac{d}{dx}[x \sin x] = u'(x) v(x) + u(x) v'(x) = (1)(\sin x) + (x)(\cos x) = \sin x + x \cos x.$$

### Step 2: Differentiate the Second Term $\cos x$
The second term is $\cos x$:
$$\frac{d}{dx}[\cos x] = -\sin x.$$

### Step 3: Combine and Simplify $f'(x)$
Add the derivatives of the two terms together:
$$f'(x) = \frac{d}{dx}[x \sin x] + \frac{d}{dx}[\cos x] = (\sin x + x \cos x) + (-\sin x).$$
Group the terms:
$$f'(x) = (\sin x - \sin x) + x \cos x.$$
Notice that $\sin x - \sin x = 0$. The terms cancel out completely:
$$f'(x) = x \cos x.$$
The derivative simplifies to a single compact product: $x \cos x$.

---

### Step 4: Compute $f'(0)$
Substitute $x = 0$ into the simplified derivative $f'(x) = x \cos x$:
$$f'(0) = 0 \cdot \cos(0) = 0 \cdot 1 = 0.$$
Thus, the derivative at $x = 0$ is exactly:
$$f'(0) = 0.$$

---

### Step 5: Geometric Interpretation of the Tangent Line
1. **Point of Tangency:**
   Evaluate the original function at $x = 0$:
   $$f(0) = 0 \cdot \sin(0) + \cos(0) = 0 + 1 = 1.$$
   The point of tangency on the curve is:
   $$P_0 = (0, 1).$$
2. **Direction and Equation of the Tangent Line:**
   The slope of the tangent line is $m = f'(0) = 0$.
   Using the point-slope formula $y - y_0 = m(x - x_0)$:
   $$y - 1 = 0 \cdot (x - 0) \implies y = 1.$$
3. **Geometric Meaning:**
   - The slope $m = 0$ means the tangent line is **completely horizontal** (parallel to the $x$-axis).
   - At $x = 0$, the function's instantaneous rate of change is zero.
   - For small values of $x$, since $\cos x \approx 1 - \frac{x^2}{2}$ and $\sin x \approx x$, we have $f(x) \approx x(x) + (1 - \frac{x^2}{2}) = 1 + \frac{x^2}{2} \ge 1$.
   - This indicates that the point $(0, 1)$ is a **strict local minimum** of the function, where the curve rests flatly against its horizontal tangent before curving upward on both sides.

---

## 5. Why Each Step Is Valid
1. **Applying the Product Rule to $x\sin x$** is required because both $x$ and $\sin x$ vary with $x$.
2. **The cancellation $\sin x - \sin x = 0$** follows from the additive inverse axiom of real numbers.
3. **Evaluating $f'(0) = 0$** follows from the zero property of multiplication ($0 \cdot 1 = 0$).

---

## 6. Final Answer in Words
The derivative of $f(x) = x \sin x + \cos x$ is $f'(x) = x \cos x$, obtained after the $\sin x$ term from the product rule cancels with the $-\sin x$ term from the derivative of $\cos x$. Evaluating at $x = 0$ yields $f'(0) = 0$. Geometrically, this means the tangent line to the graph at the point $(0, 1)$ has a slope of zero; it is a **horizontal line** with equation $y = 1$, indicating that the curve is momentarily flat and achieves a local minimum at that point.

---

## 7. Quick Verification
- **Numerical difference quotient check at $x = 0$ with $h = 0.01$ rad:**
  $$f(0) = 1.$$
  $$f(0.01) = 0.01 \sin(0.01) + \cos(0.01) \approx 0.01(0.0099998) + 0.9999500 = 0.000099998 + 0.9999500 = 1.0000500.$$
  $$\frac{f(0.01) - f(0)}{0.01} = \frac{1.0000500 - 1}{0.01} = \frac{0.0000500}{0.01} = 0.005 \approx 0.0.$$
- With $h = 0.001$:
  $$\frac{f(0.001) - 1}{0.001} \approx \frac{0.0000005}{0.001} = 0.0005 \to 0.$$
  The numerical difference quotient converges to $0$, matching $f'(0) = 0$.

---

## 8. Common Mistakes to Avoid
- **Sign error on $\frac{d}{dx}[\cos x]$:** Writing $\frac{d}{dx}[\cos x] = +\sin x$, which would yield $2\sin x + x\cos x$ instead of allowing the sine terms to cancel.
- **Forgetting the Product Rule on $x\sin x$:** Differentiating $x\sin x$ as $1 \cdot \cos x = \cos x$.
- **Thinking $f'(0) = 0$ means the tangent line does not exist:** A slope of zero defines a valid horizontal line $y = c$; it does not mean non-existence.

---

## 9. Classroom Presentation (3-Sentence Summary)
Differentiating $x \sin x$ using the Product Rule gives $\sin x + x \cos x$, and differentiating $\cos x$ gives $-\sin x$. Adding these together causes the positive and negative sine terms to cancel out completely, leaving the simple derivative $f'(x) = x \cos x$. Plugging in $x = 0$ yields $f'(0) = 0$, which proves geometrically that the tangent line to the graph at $(0, 1)$ is perfectly horizontal, with equation $y = 1$.
