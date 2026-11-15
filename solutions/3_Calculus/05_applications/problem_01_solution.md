# Problem 01: Kinematics — Position, Velocity, Acceleration, and Direction of Motion

## 1. Original Problem
The position of a point is described by
$$s(t) = t^3 - 6t^2 + 9t + 2, \qquad t \ge 0.$$

1. Determine the velocity and acceleration.
2. Find the times at which the point stops.
3. Determine on which intervals the point moves in the positive direction of the axis and on which intervals it moves in the negative direction.

---

## 2. What We Are Trying to Find
1. The instantaneous velocity function $v(t) = s'(t)$.
2. The instantaneous acceleration function $a(t) = v'(t) = s''(t)$.
3. The exact non-negative times $t$ when the particle is instantaneously at rest ($v(t) = 0$).
4. The time intervals on which the particle travels forward ($v(t) > 0$) versus backward ($v(t) < 0$).

---

## 3. Key Concepts and Theorems
1. **Kinematics via Derivatives:**
   - Velocity is the first derivative of position with respect to time:
     $$v(t) = \frac{ds}{dt} = s'(t).$$
   - Acceleration is the derivative of velocity (second derivative of position):
     $$a(t) = \frac{dv}{dt} = s''(t).$$
2. **Instantaneous Rest:**
   A moving object stops instantaneously when its velocity is zero: $v(t) = 0$.
3. **Direction of Motion:**
   - If $v(t) > 0$, the position coordinate $s(t)$ is increasing (motion in the positive direction).
   - If $v(t) < 0$, the position coordinate $s(t)$ is decreasing (motion in the negative direction).

---

## 4. Detailed Step-by-Step Solution

### Step 1: Determine velocity $v(t)$ and acceleration $a(t)$
We are given the position function for $t \ge 0$:
$$s(t) = t^3 - 6t^2 + 9t + 2.$$

1. **Velocity:**
   Differentiating $s(t)$ with respect to $t$:
   $$v(t) = s'(t) = \frac{d}{dt}(t^3 - 6t^2 + 9t + 2) = 3t^2 - 12t + 9.$$

2. **Acceleration:**
   Differentiating $v(t)$ with respect to $t$:
   $$a(t) = v'(t) = \frac{d}{dt}(3t^2 - 12t + 9) = 6t - 12.$$

### Step 2: Find the times at which the point stops
The particle stops when its instantaneous velocity is zero:
$$v(t) = 0 \iff 3t^2 - 12t + 9 = 0.$$
Factor out the common scalar $3$:
$$3(t^2 - 4t + 3) = 0.$$
Factor the quadratic polynomial into linear terms:
$$3(t - 1)(t - 3) = 0.$$
This yields two solutions:
$$t_1 = 1, \qquad t_2 = 3.$$
Both times are non-negative ($t \ge 0$). Thus, the point stops instantaneously at:
$$t = 1 \quad \text{and} \quad t = 3.$$

### Step 3: Determine intervals of motion direction
We analyze the sign of $v(t) = 3(t - 1)(t - 3)$ for $t \in [0, \infty)$:

1. **Interval $[0, 1)$:**
   Choose test point $t = 0.5$:
   $$v(0.5) = 3(0.5 - 1)(0.5 - 3) = 3(-0.5)(-2.5) = +3.75 > 0.$$
   Because $v(t) > 0$, the point moves in the **positive direction** on $[0, 1)$.

2. **Interval $(1, 3)$:**
   Choose test point $t = 2$:
   $$v(2) = 3(2 - 1)(2 - 3) = 3(1)(-1) = -3 < 0.$$
   Because $v(t) < 0$, the point moves in the **negative direction** on $(1, 3)$.

3. **Interval $(3, \infty)$:**
   Choose test point $t = 4$:
   $$v(4) = 3(4 - 1)(4 - 3) = 3(3)(1) = +9 > 0.$$
   Because $v(t) > 0$, the point moves in the **positive direction** on $(3, \infty)$.

### Step 4: Physical interpretation of positions at turning points
- At $t = 0$: $s(0) = 2$ (initial position).
- At $t = 1$: $s(1) = 1 - 6 + 9 + 2 = 6$ (reaches peak position, turns around).
- At $t = 3$: $s(3) = 27 - 54 + 27 + 2 = 2$ (reaches trough position, turns around again).
- For $t > 3$: climbs continuously toward $+\infty$.

---

## 5. Why Each Step Is Valid
- **Step 1:** The derivative definitions of velocity and acceleration are the fundamental calculus models of 1D kinematics.
- **Step 2:** A continuously moving object reversing direction along a line must pass through instantaneous velocity zero by the Intermediate Value Theorem.
- **Step 3:** The sign of the velocity dictates whether the position coordinate is increasing or decreasing.
- **Step 4:** Evaluating $s(t)$ at stopping times yields the physical coordinates where the particle changes direction.

---

## 6. Final Answer in Words
1. The velocity is $v(t) = 3t^2 - 12t + 9$, and the acceleration is $a(t) = 6t - 12$.
2. The point stops at times $t = 1$ and $t = 3$.
3. The point moves in the **positive direction** on the intervals $[0, 1)$ and $(3, \infty)$, and moves in the **negative direction** on the interval $(1, 3)$.

---

## 7. Quick Verification
- At $t = 1$: $a(1) = 6(1) - 12 = -6 < 0$ (velocity is decreasing from positive to negative, indicating a maximum position of $s = 6$).
- At $t = 3$: $a(3) = 6(3) - 12 = +6 > 0$ (velocity is increasing from negative to positive, indicating a minimum position of $s = 2$).
Matches physical expectations.

---

## 8. Common Mistakes to Avoid
- **Confusing velocity with acceleration:** Setting $a(t) = 0$ instead of $v(t) = 0$ to find where the particle stops ($a(t) = 0$ gives $t = 2$, which is where velocity is at a minimum, not zero).
- **Ignoring the time domain $t \ge 0$:** If a root had been negative, it would need to be discarded. Here both $t = 1$ and $t = 3$ are valid.
- **Sign errors when factoring:** Writing $(t + 1)(t - 3)$ instead of $(t - 1)(t - 3)$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Differentiating the position $s(t) = t^3 - 6t^2 + 9t + 2$ yields velocity $v(t) = 3t^2 - 12t + 9$ and acceleration $a(t) = 6t - 12$. Setting velocity to zero gives $3(t - 1)(t - 3) = 0$, revealing that the object stops at $t = 1$ and $t = 3$. Analyzing the sign of the velocity shows that the object moves forward on $[0, 1)$, reverses direction backward on $(1, 3)$, and moves forward indefinitely for $t > 3$.
