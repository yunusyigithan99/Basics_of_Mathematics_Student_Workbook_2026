# Problem 07: Analysis of a Trigonometric Function on a Bounded Interval

## 1. Original Problem
On $[0, 2\pi]$, find the intervals of monotonicity and the extrema of
$$f(x) = \sin x + \cos x.$$
Include the endpoints of the interval and compare the function values at the critical points and at the endpoints.

---

## 2. What We Are Trying to Find
1. The first derivative $f'(x)$ on $(0, 2\pi)$.
2. All critical (stationary) points inside the open interval $(0, 2\pi)$.
3. The intervals on $[0, 2\pi]$ where $f$ is strictly increasing or strictly decreasing.
4. The exact function values at the critical points and at the boundary endpoints $x = 0$ and $x = 2\pi$.
5. The identification of all local and global (absolute) extrema on the closed interval $[0, 2\pi]$.

---

## 3. Key Concepts and Theorems
1. **Derivatives of Trigonometric Functions:**
   $$\frac{d}{dx}(\sin x) = \cos x, \qquad \frac{d}{dx}(\cos x) = -\sin x.$$
2. **Stationary Points:**
   Points where $f'(x) = 0$. For $\cos x - \sin x = 0$, dividing by $\cos x$ (when $\cos x \neq 0$) yields $\tan x = 1$.
3. **Monotonicity via First Derivative:**
   A differentiable function on an interval increases where its derivative is positive and decreases where its derivative is negative.
4. **Extreme Value Theorem and Global Extrema on a Closed Interval $[a, b]$:**
   By the Extreme Value Theorem, a continuous function on a closed interval attains its absolute maximum and minimum. The candidates are:
   - Interior critical points where $f'(x) = 0$.
   - The boundary endpoints $x = a$ and $x = b$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Differentiate the function
The function $f(x) = \sin x + \cos x$ is infinitely differentiable everywhere on $[0, 2\pi]$.
Applying the sum rule:
$$f'(x) = \cos x - \sin x.$$

### Step 2: Find the critical points in $(0, 2\pi)$
Set $f'(x) = 0$:
$$\cos x - \sin x = 0 \iff \cos x = \sin x.$$
Notice that if $\cos x = 0$, then $\sin x = \pm 1 \neq 0$, so $\cos x = 0$ is never a solution. Thus, we can safely divide both sides by $\cos x$:
$$\tan x = 1.$$
In the interval $[0, 2\pi]$, the tangent function equals $1$ in the first and third quadrants:
$$x_1 = \frac{\pi}{4}, \qquad x_2 = \frac{\pi}{4} + \pi = \frac{5\pi}{4}.$$
Both points lie inside the open interval $(0, 2\pi)$.

### Step 3: Determine the sign of $f'(x)$ and intervals of monotonicity
We partition the interval $[0, 2\pi]$ using the critical points into three sub-intervals:
1. **On $\left[0, \frac{\pi}{4}\right)$:**
   Choose test point $x = 0$:
   $$f'(0) = \cos 0 - \sin 0 = 1 - 0 = 1 > 0.$$
   Therefore, $f'(x) > 0$, so $f(x)$ is **strictly increasing** on $\left[0, \frac{\pi}{4}\right]$.
2. **On $\left(\frac{\pi}{4}, \frac{5\pi}{4}\right)$:**
   Choose test point $x = \frac{\pi}{2}$:
   $$f'\left(\frac{\pi}{2}\right) = \cos\frac{\pi}{2} - \sin\frac{\pi}{2} = 0 - 1 = -1 < 0.$$
   Therefore, $f'(x) < 0$, so $f(x)$ is **strictly decreasing** on $\left[\frac{\pi}{4}, \frac{5\pi}{4}\right]$.
3. **On $\left(\frac{5\pi}{4}, 2\pi\right]$:**
   Choose test point $x = \frac{3\pi}{2}$:
   $$f'\left(\frac{3\pi}{2}\right) = \cos\frac{3\pi}{2} - \sin\frac{3\pi}{2} = 0 - (-1) = 1 > 0.$$
   Therefore, $f'(x) > 0$, so $f(x)$ is **strictly increasing** on $\left[\frac{5\pi}{4}, 2\pi\right]$.

### Step 4: Evaluate the function at critical points and endpoints
Now we calculate the exact value of $f(x) = \sin x + \cos x$ at all candidate points:
- **Left boundary point $x = 0$:**
  $$f(0) = \sin 0 + \cos 0 = 0 + 1 = 1.$$
- **Critical point $x = \frac{\pi}{4}$:**
  $$f\left(\frac{\pi}{4}\right) = \sin\frac{\pi}{4} + \cos\frac{\pi}{4} = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2} \approx 1.414.$$
- **Critical point $x = \frac{5\pi}{4}$:**
  $$f\left(\frac{5\pi}{4}\right) = \sin\frac{5\pi}{4} + \cos\frac{5\pi}{4} = -\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = -\sqrt{2} \approx -1.414.$$
- **Right boundary point $x = 2\pi$:**
  $$f(2\pi) = \sin(2\pi) + \cos(2\pi) = 0 + 1 = 1.$$

### Step 5: Classify and compare all extrema
Ordering the computed values:
$$-\sqrt{2} < 1 < \sqrt{2}.$$
- At $x = \frac{\pi}{4}$, the derivative changes from positive to negative, and $f(\frac{\pi}{4}) = \sqrt{2}$ is the highest value achieved on the entire interval. Hence, $x = \frac{\pi}{4}$ is both a **local maximum** and the **global (absolute) maximum**.
- At $x = \frac{5\pi}{4}$, the derivative changes from negative to positive, and $f(\frac{5\pi}{4}) = -\sqrt{2}$ is the lowest value achieved on the entire interval. Hence, $x = \frac{5\pi}{4}$ is both a **local minimum** and the **global (absolute) minimum**.
- At the endpoints $x = 0$ and $x = 2\pi$, $f(0) = f(2\pi) = 1$. 
  - Since $f$ increases immediately to the right of $x = 0$, $x = 0$ is a boundary local minimum.
  - Since $f$ increases up into $x = 2\pi$, $x = 2\pi$ is a boundary local maximum.
  Neither boundary value equals the global extrema.

---

## 5. Why Each Step Is Valid
- **Step 1:** The trigonometric functions $\sin x$ and $\cos x$ are continuously differentiable on all of $\mathbb{R}$.
- **Step 2:** $\tan x = 1$ is periodic with period $\pi$; inside $[0, 2\pi)$, it has exactly two solutions corresponding to quadrant I ($\pi/4$) and quadrant III ($5\pi/4$).
- **Step 3:** The intermediate value theorem guarantees that a continuous derivative cannot change sign without passing through zero; hence sign is constant on each sub-interval.
- **Step 4:** Evaluating trigonometric values using standard unit circle angles gives exact radical expressions.
- **Step 5:** Comparing critical points against boundary values satisfies the closed interval method for finding global extrema.

---

## 6. Final Answer in Words
On the interval $[0, 2\pi]$:
- The function is **strictly increasing** on $\left[0, \frac{\pi}{4}\right]$ and on $\left[\frac{5\pi}{4}, 2\pi\right]$.
- The function is **strictly decreasing** on $\left[\frac{\pi}{4}, \frac{5\pi}{4}\right]$.
- The **global maximum** is attained at $x = \frac{\pi}{4}$ with maximum value $f\left(\frac{\pi}{4}\right) = \sqrt{2}$.
- The **global minimum** is attained at $x = \frac{5\pi}{4}$ with minimum value $f\left(\frac{5\pi}{4}\right) = -\sqrt{2}$.
- At the endpoints, $f(0) = 1$ (a boundary local minimum) and $f(2\pi) = 1$ (a boundary local maximum), both strictly between the global minimum $-\sqrt{2}$ and global maximum $\sqrt{2}$.

---

## 7. Quick Verification
Using the harmonic addition formula (linear combination of sine and cosine):
$$f(x) = \sin x + \cos x = \sqrt{2} \left(\frac{1}{\sqrt{2}}\sin x + \frac{1}{\sqrt{2}}\cos x\right) = \sqrt{2}\sin\left(x + \frac{\pi}{4}\right).$$
Because $-1 \le \sin\theta \le 1$, the amplitude is immediately $\sqrt{2}$:
- Maximum is $\sqrt{2}$, occurring when $x + \frac{\pi}{4} = \frac{\pi}{2} \implies x = \frac{\pi}{4}$.
- Minimum is $-\sqrt{2}$, occurring when $x + \frac{\pi}{4} = \frac{3\pi}{2} \implies x = \frac{5\pi}{4}$.
This confirms both the values and the locations of the extrema.

---

## 8. Common Mistakes to Avoid
- **Missing the second critical point in $[0, 2\pi]$:** Forgetting that $\tan x = 1$ has two solutions in $[0, 2\pi]$, not just $x = \frac{\pi}{4}$.
- **Ignoring the interval endpoints:** Assuming critical points are the only candidates for extrema without testing $x = 0$ and $x = 2\pi$.
- **Sign confusion in derivatives:** Accidentally writing $(\cos x)' = \sin x$ instead of $-\sin x$.

---

## 9. Classroom Presentation (3-Sentence Summary)
By differentiating $f(x) = \sin x + \cos x$, we set $f'(x) = \cos x - \sin x = 0$, which gives critical points at $x = \pi/4$ and $x = 5\pi/4$. The sign of the derivative shows the function increases on $[0, \pi/4]$, decreases on $[\pi/4, 5\pi/4]$, and increases again on $[5\pi/4, 2\pi]$. Comparing values at the critical points and boundary endpoints confirms a global maximum of $\sqrt{2}$ at $x = \pi/4$, a global minimum of $-\sqrt{2}$ at $x = 5\pi/4$, and boundary values of $1$ at both $x = 0$ and $x = 2\pi$.
