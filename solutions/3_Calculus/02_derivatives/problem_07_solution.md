# Problem 7 Solution: A Trigonometric Composition

## 1. Original Problem
For the composite function:
$$f(x) = \sin(x^2 + 1)$$
1. Compute the derivative $f'(x)$.
2. Explicitly identify the outer function $g(u)$, the inner function $u(x)$, and the derivative of the inner function $u'(x)$.
3. Combine these components using the Chain Rule.
4. Determine the exact value and algebraic sign of $f'(0)$, and explain its geometric meaning.

---

## 2. What We Are Trying to Find
We need to:
1. Deconstruct $f(x)$ into an inner polynomial $u(x) = x^2 + 1$ and an outer trigonometric function $g(u) = \sin u$.
2. Compute $g'(u) = \cos u$ and $u'(x) = 2x$.
3. Assemble the Chain Rule product $f'(x) = \cos(x^2 + 1) \cdot 2x$.
4. Evaluate $f'(0)$ and analyze whether the curve is climbing, falling, or stationary at $x = 0$.

---

## 3. Key Concepts and Theorems
1. **The Chain Rule for Trigonometric Compositions:**
   For any differentiable function $u(x)$:
   $$\frac{d}{dx}[\sin(u(x))] = \cos(u(x)) \cdot u'(x).$$
   *The argument inside the cosine function remains $u(x)$; it is multiplied on the outside by the derivative of the argument $u'(x)$.*
2. **Derivative of the Sine Function:**
   $$\frac{d}{du}[\sin u] = \cos u.$$
3. **Stationary Points:**
   A point $x_0$ where $f'(x_0) = 0$ is a stationary point where the tangent line is horizontal.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Outer and Inner Functions
Deconstruct the expression $f(x) = \sin(x^2 + 1)$:
- **Inner function:**
  $$u(x) = x^2 + 1$$
- **Outer function:**
  $$g(u) = \sin u$$
So that $f(x) = g(u(x))$.

### Step 2: Differentiate the Individual Layers
1. **Derivative of the outer function $g(u)$ with respect to $u$:**
   $$g'(u) = \frac{d}{du}[\sin u] = \cos u.$$
2. **Derivative of the inner function $u(x)$ with respect to $x$:**
   $$u'(x) = \frac{d}{dx}[x^2 + 1] = 2x + 0 = 2x.$$

### Step 3: Apply the Chain Rule
According to the Chain Rule:
$$f'(x) = g'(u(x)) \cdot u'(x).$$
Substitute the expressions from Step 2:
$$f'(x) = \cos(u(x)) \cdot (2x) = \cos(x^2 + 1) \cdot 2x.$$
Writing the algebraic factor in front for standard notation:
$$f'(x) = 2x \cos(x^2 + 1).$$

---

### Step 4: Determine the Value and Sign of $f'(0)$
Substitute $x = 0$ into the derivative formula:
$$f'(0) = 2(0) \cdot \cos(0^2 + 1) = 0 \cdot \cos(1).$$
Since $\cos(1)$ is a finite real number (where $1$ is in radians, $\cos(1) \approx 0.540302$):
$$f'(0) = 0 \cdot 0.540302 = 0.$$
- **Value:** $f'(0) = 0$.
- **Sign:** Zero is neither positive nor negative; it is a neutral zero.
- **Geometric Meaning:**
  At $x = 0$, the slope of the tangent line to the graph of $f(x)$ is $m = 0$.
  The tangent line is **perfectly horizontal**.
  Because $f(x) = \sin(x^2 + 1)$ is an even function ($f(-x) = f(x)$), the graph has bilateral reflectional symmetry across the $y$-axis. The point $(0, \sin(1)) \approx (0, 0.8415)$ is a stationary turning point of the curve.

---

## 5. Why Each Step Is Valid
1. **Identifying layers** correctly maps the function composition $g \circ u$.
2. **The Chain Rule theorem** guarantees that the instantaneous rate of change of $\sin(u)$ with respect to $x$ equals the rate of change of sine ($\cos u$) multiplied by the rate of change of its input argument ($2x$).
3. **The evaluation $0 \cdot \cos(1) = 0$** holds because zero multiplied by any finite real number is identically zero.

---

## 6. Final Answer in Words
The outer function is $g(u) = \sin u$ with derivative $g'(u) = \cos u$, and the inner function is $u(x) = x^2 + 1$ with derivative $u'(x) = 2x$. Combining them via the Chain Rule yields the derivative $f'(x) = 2x \cos(x^2 + 1)$. Evaluating at $x = 0$ gives $f'(0) = 2(0)\cos(1) = 0$. Because the derivative is zero, the tangent line to the graph at $x = 0$ is horizontal with slope $m = 0$, representing a symmetric stationary point on the curve.

---

## 7. Quick Verification
- **Numerical difference quotient check at $x = 0$ with $h = 0.001$:**
  $$f(0) = \sin(1) \approx 0.84147098.$$
  $$f(0.001) = \sin(0.001^2 + 1) = \sin(1.000001) \approx 0.84147152.$$
  $$\frac{f(0.001) - f(0)}{0.001} \approx \frac{0.84147152 - 0.84147098}{0.001} = \frac{0.00000054}{0.001} = 0.00054 \approx 0.$$
  The numerical rate of change is effectively 0, confirming $f'(0) = 0$.
- **Even function symmetry:**
  Since $f(x) = \sin(x^2 + 1)$ is an even function, its derivative must be an odd function:
  $$f'(-x) = 2(-x)\cos((-x)^2 + 1) = -2x\cos(x^2 + 1) = -f'(x).$$
  Any continuous odd function must pass through the origin at $x = 0$: $f'(0) = -f'(0) \implies 2f'(0) = 0 \implies f'(0) = 0$. This confirms the result independently through symmetry.

---

## 8. Common Mistakes to Avoid
- **Differentiating the inside without multiplying:** Writing $f'(x) = \cos(2x)$, which incorrectly changes the argument of the cosine function.
- **Forgetting the inner derivative entirely:** Writing $f'(x) = \cos(x^2 + 1)$.
- **Assuming $\cos(1) = 1$:** Confusing radians and degrees, or thinking $\cos(1)$ is zero; $1$ radian is approximately $57.3^\circ$, where $\cos(1) \approx 0.54 \neq 0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The function is a composition with an outer sine layer $g(u) = \sin u$ and an inner polynomial layer $u = x^2 + 1$. Differentiating the outer function gives $\cos(x^2 + 1)$ and multiplying by the inner derivative $2x$ produces $f'(x) = 2x \cos(x^2 + 1)$ according to the Chain Rule. Evaluating at $x = 0$ makes the $2x$ factor zero, giving $f'(0) = 0$, which proves that the graph has a horizontal tangent line at that point.
