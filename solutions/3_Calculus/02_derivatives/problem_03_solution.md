# Problem 3 Solution: The Product Rule — Why Is It Needed?

## 1. Original Problem
For the function:
$$f(x) = (x^2 + 1) e^x$$
1. Compute the correct derivative $f'(x)$ using the Product Rule.
2. Compare the correct result with the naive and incorrect proposition:
   $$f'(x) \stackrel{?}{=} (2x) e^x.$$
3. Explain in detail which term is missing from the naive calculation and provide the geometric and algebraic reasoning for why the Product Rule requires two terms instead of one.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the two factor functions $u(x) = x^2 + 1$ and $v(x) = e^x$.
2. State and apply the Product Rule $(uv)' = u'v + uv'$.
3. Factor and simplify the resulting derivative.
4. Diagnose the exact error in the student proposition $(2x)e^x$.
5. Explain the geometric intuition of dynamic rectangles (product of two changing sides).

---

## 3. Key Concepts and Theorems
1. **The Product Rule (Leibniz Rule):**
   If functions $u(x)$ and $v(x)$ are both differentiable at $x$, their product $f(x) = u(x)v(x)$ is also differentiable, and its derivative is given by:
   $$\frac{d}{dx}[u(x) v(x)] = u'(x) v(x) + u(x) v'(x).$$
   *The derivative of a product is NOT the product of the derivatives!*
2. **Derivative of the Natural Exponential Function:**
   $$\frac{d}{dx}[e^x] = e^x.$$
3. **Geometric Model (Area of an Expanding Rectangle):**
   Consider a rectangle with length $u(x)$ and width $v(x)$, whose area is $A(x) = u(x)v(x)$.
   When $x$ increases by a small increment $\Delta x$:
   $$\Delta A = A(x + \Delta x) - A(x) = (u + \Delta u)(v + \Delta v) - uv = u \Delta v + v \Delta u + \Delta u \Delta v.$$
   Dividing by $\Delta x$ and taking the limit as $\Delta x \to 0$:
   $$\frac{dA}{dx} = u \frac{dv}{dx} + v \frac{du}{dx}.$$
   The expansion has two primary linear terms: one from the growth of the width, and one from the growth of the length.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Component Functions and Their Derivatives
Let $f(x) = u(x) \cdot v(x)$, where:
- First factor: $u(x) = x^2 + 1$
- Second factor: $v(x) = e^x$

Compute the individual derivatives:
- $u'(x) = \frac{d}{dx}[x^2 + 1] = 2x$
- $v'(x) = \frac{d}{dx}[e^x] = e^x$

### Step 2: Apply the Product Rule
Substitute $u, u', v, v'$ into the Product Rule formula:
$$f'(x) = u'(x) v(x) + u(x) v'(x)$$
$$f'(x) = (2x)(e^x) + (x^2 + 1)(e^x).$$

### Step 3: Factor and Simplify the Correct Derivative
Factor out the common exponential factor $e^x$:
$$f'(x) = \big(2x + (x^2 + 1)\big) e^x = (x^2 + 2x + 1) e^x.$$
Recognize that $x^2 + 2x + 1 = (x + 1)^2$:
$$f'(x) = (x + 1)^2 e^x.$$

---

### Step 4: Compare with the Incorrect Idea
The naive proposition was:
$$f'_{\text{naive}}(x) \stackrel{?}{=} (2x) e^x.$$
Comparing this with the correct derivative:
$$f'(x) = \underbrace{(2x)e^x}_{\text{naive term}} + \underbrace{(x^2 + 1)e^x}_{\text{MISSING TERM}}.$$

**Which Term Is Missing?**
The missing term is:
$$(x^2 + 1) e^x = u(x) v'(x).$$

**Why Did the Mistake Happen?**
- The student differentiated the polynomial factor $x^2 + 1$ to get $2x$, but **held the exponential factor $e^x$ frozen as if it were a constant coefficient**.
- However, $e^x$ is not a constant number like 5; it is an active, rapidly growing function of $x$.
- As $x$ changes, **both** factors change simultaneously:
  1. $x^2 + 1$ changes at rate $2x$, contributing $(2x)e^x$ to the overall rate of change.
  2. $e^x$ changes at rate $e^x$, contributing $(x^2 + 1)e^x$ to the overall rate of change.
- By omitting the second term, the naive calculation completely ignores the change in the exponential factor, which drastically underestimates the true rate of change of the product.

---

## 5. Why Each Step Is Valid
1. **The Product Rule** is derived rigorously from the limit of the difference quotient:
   $$\lim_{h\to0} \frac{u(x+h)v(x+h) - u(x)v(x)}{h} = \lim_{h\to0} \left[ \frac{u(x+h) - u(x)}{h} v(x+h) + u(x) \frac{v(x+h) - v(x)}{h} \right] = u'v + uv'.$$
2. **Factoring $e^x$** is valid by the distributive law of algebra because $e^x \neq 0$ for all real $x$.
3. **The geometric rectangle argument** confirms that area rate of change depends on changes in both dimensions.

---

## 6. Final Answer in Words
The correct derivative of $f(x) = (x^2 + 1)e^x$ is $f'(x) = (x^2 + 2x + 1)e^x = (x + 1)^2 e^x$. The incorrect proposition $f'(x) \stackrel{?}{=} (2x)e^x$ is missing the crucial second term $(x^2 + 1)e^x = u(x)v'(x)$. The Product Rule is necessary because when two variable expressions are multiplied together, the rate of change of the overall product receives two separate contributions: one from the change in the first factor while holding the second factor fixed, and another from the change in the second factor while holding the first factor fixed.

---

## 7. Quick Verification
- Evaluate at $x = 0$:
  $$f(0) = (0^2 + 1)e^0 = 1 \cdot 1 = 1.$$
  - Correct derivative: $f'(0) = (0 + 1)^2 e^0 = 1 \cdot 1 = 1$.
  - Naive derivative: $f'_{\text{naive}}(0) = (2 \cdot 0)e^0 = 0$.
- Test with the difference quotient for $h = 0.001$:
  $$f(0.001) = (0.001^2 + 1)e^{0.001} \approx (1.000001)(1.0010005) \approx 1.0010015.$$
  $$\frac{f(0.001) - f(0)}{0.001} \approx \frac{1.0010015 - 1}{0.001} = 1.0015 \approx 1.0.$$
  The numerical rate of change is $1.0$, which agrees with the correct derivative $f'(0) = 1$ and completely disproves the naive claim $f'(0) = 0$.

---

## 8. Common Mistakes to Avoid
- **Product of derivatives rule:** Writing $(u \cdot v)' = u' \cdot v'$, which would give $(2x)(e^x)$.
- **Dropping the parenthesis when factoring:** Writing $2x + x^2 + 1 e^x$ instead of $(x^2 + 2x + 1)e^x$.
- **Assuming $e^x$ differentiates to something else:** Differentiating $e^x$ as $x e^{x-1}$ (confusing exponential functions $a^x$ with power functions $x^a$).

---

## 9. Classroom Presentation (3-Sentence Summary)
Applying the Product Rule $(uv)' = u'v + uv'$ to $f(x) = (x^2 + 1)e^x$ gives $f'(x) = (2x)e^x + (x^2 + 1)e^x$, which factors neatly into $(x + 1)^2 e^x$. The common misconception $(2x)e^x$ is missing the entire second term, $(x^2 + 1)e^x$, which accounts for the fact that the exponential factor is actively growing alongside the polynomial. Because both factors vary simultaneously, the Product Rule is essential to capture the two distinct contributions that make up the total rate of change.
