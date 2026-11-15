# Problem 15 Solution: The Difference Quotient as a Check of the Derivative

## 1. Original Problem
Select one function from this problem set and a specific point $x_0$ where its derivative exists.
Let us choose:
$$f(x) = x^2 - 3x + 1 \quad (\text{from Problem 10}) \quad \text{at the point } x_0 = 2.$$
1. Compute the exact theoretical derivative $f'(x_0)$ using differentiation rules.
2. Calculate the numerical difference quotient:
   $$Q(h) = \frac{f(x_0 + h) - f(x_0)}{h}$$
   explicitly for step sizes $h = 1$, $h = 0.1$, and $h = 0.01$.
3. Compare the calculated values with the exact derivative $f'(x_0)$.
4. Explain why the difference quotients approaching a single number is consistent with the definition of the derivative, and explain why a finite number of calculations cannot replace a formal mathematical limit argument.

---

## 2. What We Are Trying to Find
We need to:
1. Differentiate $f(x) = x^2 - 3x + 1$ and evaluate the exact slope $f'(2)$.
2. Calculate $f(2)$ and the stepped values $f(2 + 1) = f(3)$, $f(2 + 0.1) = f(2.1)$, and $f(2 + 0.01) = f(2.01)$.
3. Compute the three corresponding secant line slopes $Q(1)$, $Q(0.1)$, and $Q(0.01)$.
4. Show how the secant lines rotate towards the tangent line as $h \to 0$.
5. Reiterate the crucial distinction between empirical approximation and analytical deduction in calculus.

---

## 3. Key Concepts and Theorems
1. **The Difference Quotient (Secant Slope):**
   For any step size $h \neq 0$, the ratio:
   $$Q(h) = \frac{f(x_0 + h) - f(x_0)}{h}$$
   measures the average rate of change of $f$ over the interval $[x_0, x_0 + h]$. Geometrically, this represents the slope of the secant line passing through $(x_0, f(x_0))$ and $(x_0 + h, f(x_0 + h))$.
2. **The Derivative as a Tangent Limit:**
   $$f'(x_0) = \lim_{h\to0} Q(h) = \lim_{h\to0} \frac{f(x_0 + h) - f(x_0)}{h}.$$
   As $h \to 0$, the second point slides along the curve toward the base point, and the secant lines pivot into the tangent line.
3. **Difference Quotient Identity for Quadratics:**
   For any quadratic $f(x) = Ax^2 + Bx + C$, the difference quotient simplifies linearly in $h$:
   $$Q(h) = f'(x_0) + A h.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Exact Theoretical Derivative
Given $f(x) = x^2 - 3x + 1$ and base point $x_0 = 2$:
1. General derivative using the Power Rule:
   $$f'(x) = 2x - 3.$$
2. Exact derivative at $x_0 = 2$:
   $$f'(2) = 2(2) - 3 = 4 - 3 = 1.$$
The exact theoretical slope of the tangent line is:
$$f'(2) = 1.$$

---

### Step 2: Compute Base Point Value $f(2)$
Evaluate $f(2)$:
$$f(2) = 2^2 - 3(2) + 1 = 4 - 6 + 1 = -1.$$
So $(x_0, f(x_0)) = (2, -1)$.

---

### Step 3: Compute Difference Quotients for $h = 1$, $0.1$, and $0.01$

#### Case 1: Step size $h = 1$
- Evaluated point: $x_0 + h = 2 + 1 = 3$.
- Function value:
  $$f(3) = 3^2 - 3(3) + 1 = 9 - 9 + 1 = 1.$$
- Difference quotient:
  $$Q(1) = \frac{f(3) - f(2)}{1} = \frac{1 - (-1)}{1} = \frac{1 + 1}{1} = 2.0.$$

#### Case 2: Step size $h = 0.1$
- Evaluated point: $x_0 + h = 2 + 0.1 = 2.1$.
- Function value:
  $$f(2.1) = (2.1)^2 - 3(2.1) + 1 = 4.41 - 6.30 + 1 = -0.89.$$
- Difference quotient:
  $$Q(0.1) = \frac{f(2.1) - f(2)}{0.1} = \frac{-0.89 - (-1)}{0.1} = \frac{-0.89 + 1}{0.1} = \frac{0.11}{0.1} = 1.1.$$

#### Case 3: Step size $h = 0.01$
- Evaluated point: $x_0 + h = 2 + 0.01 = 2.01$.
- Function value:
  $$f(2.01) = (2.01)^2 - 3(2.01) + 1 = 4.0401 - 6.03 + 1 = -0.9899.$$
- Difference quotient:
  $$Q(0.01) = \frac{f(2.01) - f(2)}{0.01} = \frac{-0.9899 - (-1)}{0.01} = \frac{-0.9899 + 1}{0.01} = \frac{0.0101}{0.01} = 1.01.$$

---

### Step 4: Summary Table and Comparison with $f'(2) = 1$

| Step Size $h$ | New Point $x_0 + h$ | Function Value $f(x_0 + h)$ | Difference Quotient $Q(h)$ | Error $|Q(h) - f'(2)|$ |
| :--- | :--- | :--- | :--- | :--- |
| **$h = 1$** | $3.0$ | $1.0$ | **$2.0$** | $1.0$ |
| **$h = 0.1$** | $2.1$ | $-0.89$ | **$1.1$** | $0.1$ |
| **$h = 0.01$** | $2.01$ | $-0.9899$ | **$1.01$** | $0.01$ |
| **$h = 0.001$** | $2.001$ | $-0.998999$ | **$1.001$** | $0.001$ |
| **$h \to 0$** | $\to 2$ | $\to -1$ | $\to \mathbf{1.0}$ | $\to 0$ |

**Comparison:**
As $h$ shrinks from $1$ to $0.1$ to $0.01$, the secant slope $Q(h)$ steps through $2.0 \to 1.1 \to 1.01$. The difference between $Q(h)$ and the theoretical value $1$ is exactly equal to $h$ itself ($Q(h) = 1 + h$). This behavior matches the definition of the derivative:
$$\lim_{h\to0} Q(h) = \lim_{h\to0} (1 + h) = 1 = f'(2).$$

---

### Step 5: Why a Few Computations Cannot Replace a Limit Argument
1. **The Difference Between Sampling and Proof:**
   - Calculating $Q(1), Q(0.1), Q(0.01)$ gives three discrete snapshots. It shows what happens for those specific three numbers, but says nothing about whether $Q(h)$ might oscillate wildly or diverge for $h = 10^{-10}$.
2. **Pathology and High-Frequency Noise:**
   - Consider the function $g(x) = x^2 + 10^{-5} \sin(10^8 x)$. For step sizes $h = 0.1$ and $0.01$, a student might sample points where the sine wave happens to be zero, giving differences that look like a smooth derivative. However, the true derivative contains the term $10^3 \cos(10^8 x)$, which oscillates violently by $\pm 1000$. Discrete sampling completely misses high-frequency oscillations.
3. **Machine Precision and Catastrophic Cancellation:**
   - In numerical computing, taking $h$ too small (e.g., $h = 10^{-16}$) results in subtractive cancellation in floating-point arithmetic ($f(x_0 + h) - f(x_0)$ evaluates to zero due to rounding), leading to an erroneous calculation of $0/h = 0$. Pure mathematics requires an analytical limit to circumvent the physical limitations of finite precision.
4. **Conclusion:**
   Computing numerical difference quotients is an essential diagnostic and intuitive check that confirms whether an analytical derivative is plausibly correct, but only a deductive limit argument guarantees mathematical truth across all arbitrarily small intervals.

---

## 5. Why Each Step Is Valid
1. **The difference quotient formula** is the exact definition of secant slope.
2. **Expanding $f(2+h) = (2+h)^2 - 3(2+h) + 1 = 4 + 4h + h^2 - 6 - 3h + 1 = -1 + h + h^2$** proves analytically that $Q(h) = \frac{(-1 + h + h^2) - (-1)}{h} = \frac{h + h^2}{h} = 1 + h$, validating the table values $2, 1.1, 1.01$ exactly.
3. **The limit $\lim_{h\to0}(1+h) = 1$** is rigorously justified by the continuity of linear functions.

---

## 6. Final Answer in Words
The exact derivative at $x_0 = 2$ is $f'(2) = 1$. Evaluating the difference quotients produces $Q(1) = 2.0$, $Q(0.1) = 1.1$, and $Q(0.01) = 1.01$. These values steadily converge toward $1.0$, which is completely consistent with the definition of the derivative as the limit of the secant slopes as $h \to 0$. However, three discrete calculations do not constitute a proof because empirical sampling cannot test all infinitely many step sizes, can miss rapid micro-oscillations, and is subject to numerical truncation errors, whereas an analytical limit argument proves convergence universally.

---

## 7. Quick Verification
- **Left-hand difference quotient check (negative $h$):**
  - For $h = -0.1$: $x = 1.9 \implies f(1.9) = 1.9^2 - 3(1.9) + 1 = 3.61 - 5.7 + 1 = -1.09$.
    $$Q(-0.1) = \frac{-1.09 - (-1)}{-0.1} = \frac{-0.09}{-0.1} = 0.9.$$
  - For $h = -0.01$: $x = 1.99 \implies f(1.99) = 3.9601 - 5.97 + 1 = -1.0099$.
    $$Q(-0.01) = \frac{-1.0099 - (-1)}{-0.01} = \frac{-0.0099}{-0.01} = 0.99.$$
  As $h \to 0^-$, $Q(h) = 1 + h$ approaches $1$ from below ($0.9 \to 0.99 \to 1.0$). Both one-sided approaches converge symmetrically to $1.0$.

---

## 8. Common Mistakes to Avoid
- **Confusing secant slope with tangent slope:** Treating $Q(1) = 2$ as the derivative instead of recognizing it as an approximation with step size 1.
- **Arithmetic sign in $f(x_0 + h) - f(x_0)$:** Since $f(2) = -1$, subtracting $f(2)$ means *adding* 1: $-0.89 - (-1) = -0.89 + 1 = +0.11$.
- **Assuming linear behavior for all functions:** The difference quotient $Q(h) = 1 + h$ is linear here only because $f(x)$ is a quadratic. For higher-degree functions, $Q(h)$ contains higher-order powers of $h$.

---

## 9. Classroom Presentation (3-Sentence Summary)
For $f(x) = x^2 - 3x + 1$ at $x_0 = 2$, the exact analytical derivative is $f'(2) = 2(2) - 3 = 1$. Evaluating the difference quotient $(f(2+h) - f(2))/h$ for $h = 1$, $0.1$, and $0.01$ yields the values $2.0$, $1.1$, and $1.01$, demonstrating concretely how secant slopes approach the tangent slope as the interval shrinks. This numerical convergence validates the intuition behind calculus, but a formal limit proof remains irreplaceable because finite sampling cannot survey infinitely many step sizes or detect high-frequency oscillations.
