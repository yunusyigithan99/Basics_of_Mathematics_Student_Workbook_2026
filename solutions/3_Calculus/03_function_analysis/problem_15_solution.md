# Problem 15: Error Diagnosis in Monotonicity and Extrema Analysis

## 1. Original Problem
For the function
$$f(x) = x^3 - 3x$$
the derivative was correctly computed as
$$f'(x) = 3(x - 1)(x + 1).$$

However, a student wrote the following conclusion:
> "The derivative is positive between its zeros and negative outside them. Therefore, the function is decreasing on $(-\infty, -1) \cup (1, \infty)$, increasing on $(-1, 1)$, has a local minimum at $x = -1$, and a local maximum at $x = 1$."

1. Without differentiating again, explain why merely identifying the zeros of the derivative does not justify the stated sign chart, and find the error in the student's reasoning.
2. Construct the correct sign chart for $f'(x)$.
3. Give the correct intervals of monotonicity and the character of the extrema.
4. In each of the three intervals, choose one simple test point and show that the sign of the derivative confirms your classification.

---

## 2. What We Are Trying to Find
1. Identification and diagnosis of the student's conceptual and procedural errors.
2. A sound mathematical justification for why zeros alone do not determine signs.
3. The correct sign distribution of $f'(x)$ across the real line.
4. The true intervals of monotonicity and correct classification of local extrema for $f(x)$.
5. Explicit numerical evaluation of test points in all three intervals confirming the correct signs.

---

## 3. Key Concepts and Theorems
1. **Sign of a Quadratic Expression:**
   For a quadratic polynomial $P(x) = a x^2 + bx + c = a(x - x_1)(x - x_2)$ with $x_1 < x_2$:
   - If $a > 0$ (parabola opens upwards), $P(x) < 0$ strictly between the roots $x \in (x_1, x_2)$, and $P(x) > 0$ outside the roots $x \in (-\infty, x_1) \cup (x_2, \infty)$.
   - If $a < 0$ (parabola opens downwards), the signs are inverted.
2. **Intermediate Value Property and Test Point Method:**
   A continuous function can change sign only at its zeros. Therefore, between any two consecutive zeros, the function maintains a single, constant sign, which can be verified by testing any single point within each interval.
3. **First Derivative Test for Extrema:**
   - Sign change $+ \to - \implies$ local maximum.
   - Sign change $- \to + \implies$ local minimum.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Diagnose the error in the student's reasoning
The student made two fatal errors:
1. **Unjustified sign assumption:** Identifying that $f'(x) = 0$ at $x = \pm 1$ only determines the boundaries of the intervals where the sign could change. It provides zero information about *which* interval is positive and *which* is negative. To claim a sign chart, one must either check the leading coefficient or evaluate test points.
2. **Inverted quadratic sign:** The student wrote: *"The derivative is positive between its zeros and negative outside them."* 
   Expanding the derivative:
   $$f'(x) = 3(x - 1)(x + 1) = 3(x^2 - 1) = 3x^2 - 3.$$
   The leading coefficient is $a = 3 > 0$. An upward-opening parabola is **negative** between its roots (where it dips below the $x$-axis) and **positive** outside them. 
   The student asserted the exact opposite of reality. Because the signs of the derivative were inverted, every single conclusion regarding monotonicity and extrema was completely reversed.

### Step 2: Construct the correct sign chart for $f'(x)$
The zeros of $f'(x) = 3(x - 1)(x + 1)$ partition $\mathbb{R}$ into three open intervals:
- $(-\infty, -1)$
- $(-1, 1)$
- $(1, \infty)$

Since the leading coefficient $a = 3$ is positive:
- On $(-\infty, -1)$: $(x - 1) < 0$ and $(x + 1) < 0 \implies f'(x) = 3(-)(-) > 0$ ($\mathbf{+}$).
- On $(-1, 1)$: $(x - 1) < 0$ and $(x + 1) > 0 \implies f'(x) = 3(-)(+) < 0$ ($\mathbf{-}$).
- On $(1, \infty)$: $(x - 1) > 0$ and $(x + 1) > 0 \implies f'(x) = 3(+)(+) > 0$ ($\mathbf{+}$).

**Correct Sign Chart:**
```text
x          |   (-∞, -1)   |   -1   |   (-1, 1)   |   1   |   (1, ∞)
-----------+--------------+--------+-------------+-------+-----------
f'(x)      |      +       |   0    |      -      |   0   |     +
f(x)       |  increasing  | Max(2) | decreasing  |Min(-2)| increasing
```

### Step 3: Determine correct monotonicity and extrema
- **Monotonicity:**
  - $f(x)$ is **strictly increasing** on $(-\infty, -1]$ and on $[1, \infty)$.
  - $f(x)$ is **strictly decreasing** on $[-1, 1]$.
- **Classification of Extrema:**
  - At $x = -1$: $f'(x)$ changes sign from positive to negative. Hence, $x = -1$ is a **local maximum** (not a minimum!). The maximum value is:
    $$f(-1) = (-1)^3 - 3(-1) = -1 + 3 = 2.$$
  - At $x = 1$: $f'(x)$ changes sign from negative to positive. Hence, $x = 1$ is a **local minimum** (not a maximum!). The minimum value is:
    $$f(1) = 1^3 - 3(1) = 1 - 3 = -2.$$

### Step 4: Verify with test points in each interval
We pick one convenient test point in each of the three intervals and compute $f'(x) = 3(x - 1)(x + 1)$:
1. **Interval $(-\infty, -1)$:** Choose $x = -2$.
   $$f'(-2) = 3(-2 - 1)(-2 + 1) = 3(-3)(-1) = +9 > 0.$$
   Confirming $f'(x) > 0$ (increasing).
2. **Interval $(-1, 1)$:** Choose $x = 0$.
   $$f'(0) = 3(0 - 1)(0 + 1) = 3(-1)(1) = -3 < 0.$$
   Confirming $f'(x) < 0$ (decreasing).
3. **Interval $(1, \infty)$:** Choose $x = 2$.
   $$f'(2) = 3(2 - 1)(2 + 1) = 3(1)(3) = +9 > 0.$$
   Confirming $f'(x) > 0$ (increasing).

---

## 5. Why Each Step Is Valid
- **Step 1:** Identifying mathematical errors requires pointing to the false assumption (ignoring the sign of the leading coefficient of the parabola).
- **Step 2:** Polynomials are continuous functions whose signs are invariant between real roots.
- **Step 3:** The First Derivative Test guarantees that a $+ \to -$ transition produces a peak (maximum) and a $- \to +$ transition produces a valley (minimum).
- **Step 4:** By the Intermediate Value Theorem, evaluating a single point in an interval between roots rigorously proves the sign for all points in that interval.

---

## 6. Final Answer in Words
The student's error lies in assuming without verification that the quadratic derivative is positive between its roots and negative outside them; in reality, because the leading coefficient is $3 > 0$, the parabola opens upward and is negative between $-1$ and $1$, and positive outside. 
The correct behavior is:
- $f(x)$ is **strictly increasing** on $(-\infty, -1]$ and on $[1, \infty)$.
- $f(x)$ is **strictly decreasing** on $[-1, 1]$.
- $x = -1$ is a **local maximum** with value $f(-1) = 2$.
- $x = 1$ is a **local minimum** with value $f(1) = -2$.
Test points $x = -2$ ($f' = 9 > 0$), $x = 0$ ($f' = -3 < 0$), and $x = 2$ ($f' = 9 > 0$) confirm these signs.

---

## 7. Quick Verification
Evaluating the function values directly:
- $f(-2) = (-2)^3 - 3(-2) = -8 + 6 = -2$.
- $f(-1) = 2$.
- $f(0) = 0$.
- $f(1) = -2$.
- $f(2) = 2$.
From $x = -2$ to $x = -1$, the function climbs from $-2$ to $2$ (increasing).
From $x = -1$ to $x = 1$, the function drops from $2$ to $-2$ (decreasing).
From $x = 1$ to $x = 2$, the function climbs from $-2$ to $2$ (increasing).
This completely disproves the student's claims and verifies our solution.

---

## 8. Common Mistakes to Avoid
- **Guessing signs instead of testing:** Assuming signs alternate $+ - +$ or $- + -$ without checking the leading term or plugging in test values.
- **Reversing extrema rules:** Mistakenly believing that passing from negative to positive derivative means a maximum. A negative derivative means the function was going down, and a positive derivative means it goes up, creating a valley (minimum).
- **Writing unions of intervals for monotonicity:** Writing $(-\infty, -1] \cup [1, \infty)$ as a single interval where $f$ is increasing is mathematically incorrect (e.g., $f(2) = 2$ but $f(-1) = 2$, so $f$ is not increasing on the union, but separately on each interval).

---

## 9. Classroom Presentation (3-Sentence Summary)
The student incorrectly assumed the derivative parabola was positive between its roots, but because the leading coefficient is $+3$, the parabola opens upward and is actually negative between $-1$ and $1$. Testing $x = 0$ gives $f'(0) = -3$, proving that the function is decreasing on $[-1, 1]$ and increasing on $(-\infty, -1]$ and $[1, \infty)$. Consequently, $x = -1$ is a local maximum and $x = 1$ is a local minimum, completely reversing the student's erroneous conclusions.
