# Problem 05: Accumulation of Distance from Velocity — Displacement vs. Total Distance

## 1. Original Problem
The velocity of a car during the first five seconds is described by the function
$$v(t) = 4t + 2 \quad [\mathrm{m/s}].$$

Compute the distance traveled and explain why the integral of velocity gives the change in position.

Then answer what would have to be changed in the reasoning if the velocity also took negative values.

---

## 2. What We Are Trying to Find
1. The exact distance traveled by the car during the first five seconds ($t \in [0, 5]$).
2. A rigorous conceptual explanation of why the definite integral of velocity equals the change in position.
3. The distinction between **displacement** (net position change) and **total distance traveled**.
4. The required mathematical modification (using $|v(t)|$) if velocity takes negative values.

---

## 3. Key Concepts and Theorems
1. **Velocity as Rate of Change of Position:**
   $$v(t) = \frac{ds}{dt} = s'(t).$$
2. **Fundamental Theorem of Calculus (Net Change Theorem):**
   The integral of the rate of change of a quantity over $[a, b]$ gives the net change of that quantity:
   $$\int_a^b v(t)\,dt = \int_a^b s'(t)\,dt = s(b) - s(a) = \Delta s \quad (\text{Displacement}).$$
3. **Total Distance Traveled vs. Displacement:**
   - **Displacement (net change in position):**
     $$\Delta s = \int_{t_1}^{t_2} v(t)\,dt.$$
   - **Total distance traveled (path length):**
     $$D = \int_{t_1}^{t_2} |v(t)|\,dt = \int_{t_1}^{t_2} \text{speed}(t)\,dt.$$
   When $v(t) \ge 0$ throughout the interval, displacement and total distance traveled are identical.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the distance traveled during the first five seconds
We are given $v(t) = 4t + 2$ on the time interval $[0, 5]$ seconds.
Notice that for all $t \in [0, 5]$:
$$v(t) \ge 4(0) + 2 = 2\text{ m/s} > 0.$$
Because the velocity is strictly positive throughout the interval, the car never stops or reverses; it moves exclusively forward.
Thus, the total distance traveled equals the net displacement:
$$\text{Distance} = \int_0^5 v(t)\,dt = \int_0^5 (4t + 2)\,dt.$$

Find an antiderivative:
$$\int (4t + 2)\,dt = 4 \cdot \frac{t^2}{2} + 2t = 2t^2 + 2t.$$
Apply the limits from $t = 0$ to $t = 5$:
$$\text{Distance} = \left[2t^2 + 2t\right]_0^5 = \left[2(5^2) + 2(5)\right] - \left[2(0^2) + 2(0)\right]$$
$$= [2(25) + 10] - 0 = 50 + 10 = 60\text{ meters}.$$

### Step 2: Explain why the integral of velocity gives position change
1. **Differential formulation:**
   Velocity is defined as the instantaneous time rate of change of position:
   $$v(t) = \frac{ds}{dt}.$$
   Multiplying by the differential $dt$ gives the infinitesimal position displacement:
   $$ds = v(t)\,dt.$$
   In an infinitesimal interval of time $dt$, the velocity is virtually constant, so the distance covered is simply $\text{speed} \times \text{time} = v(t)\,dt$.

2. **Accumulation over time:**
   The total change in position from time $t = 0$ to $t = 5$ is the continuous sum (Riemann integral) of all these tiny displacements:
   $$\Delta s = \int_0^5 ds = \int_0^5 v(t)\,dt.$$
   By the Fundamental Theorem of Calculus, integrating the derivative of a function over an interval recovers the total net change:
   $$\int_0^5 s'(t)\,dt = s(5) - s(0).$$
   Therefore, the definite integral of velocity mathematically accumulates each forward step into the total position change.

### Step 3: What must be changed if velocity takes negative values?
If velocity takes negative values, the car is moving in the reverse direction (backward along the axis).

1. **Displacement vs. Distance:**
   - The plain integral $\int_{t_1}^{t_2} v(t)\,dt$ computes **displacement** (the straight-line vector difference between the starting point and finishing point). In this integral, negative velocities contribute negative numbers, canceling out earlier forward travel.
   - For example, if a car drives $100\text{ m}$ forward and then $100\text{ m}$ backward, its displacement is $100 - 100 = 0\text{ m}$, but its odometer records $200\text{ m}$.

2. **Required modification for total distance:**
   To compute the **actual total distance traveled** when velocity can be negative, we must integrate the absolute value of velocity (the scalar speed):
   $$\text{Total Distance} = \int_{t_1}^{t_2} |v(t)|\,dt.$$

3. **Practical calculation procedure:**
   To calculate this integral:
   - Solve $v(t) = 0$ to find the exact turning points where direction reverses.
   - Partition the integration interval at these stopping times into forward intervals ($v(t) > 0$) and backward intervals ($v(t) < 0$).
   - Integrate each piece separately and take the absolute value of each result before adding them together:
     $$\text{Total Distance} = \int_{\text{forward}} v(t)\,dt + \left| \int_{\text{backward}} v(t)\,dt \right|.$$

---

## 5. Why Each Step Is Valid
- **Step 1:** The polynomial $4t + 2$ is continuous on $[0, 5]$, allowing direct evaluation via the Newton-Leibniz formula.
- **Step 2:** The Net Change Theorem is an immediate consequence of the Fundamental Theorem of Calculus applied to physical rates.
- **Step 3:** The definition of arc length / distance traveled along a line requires summing absolute step lengths rather than signed vectors.

---

## 6. Final Answer in Words
The distance traveled by the car during the first 5 seconds is:
$$\int_0^5 (4t + 2)\,dt = \left[2t^2 + 2t\right]_0^5 = 60\text{ meters}.$$
The integral of velocity gives the change in position because velocity is the derivative of position ($v = ds/dt$); integrating this rate of change across time continuously sums all infinitesimal displacements $ds = v(t)\,dt$ into the net change $\Delta s = s(5) - s(0)$. 
If velocity took negative values, the simple integral $\int v(t)\,dt$ would only yield net displacement (allowing forward and backward motion to cancel). To find the actual total distance traveled, one would have to integrate the scalar speed $|v(t)|$ by splitting the integral at the stopping points where $v(t) = 0$ and summing the absolute values of the separate displacements.

---

## 7. Quick Verification
- Average velocity over the 5 seconds:
  Since $v(t)$ is linear, the average velocity is the arithmetic mean of the initial and final velocities:
  $v(0) = 4(0) + 2 = 2\text{ m/s}$,
  $v(5) = 4(5) + 2 = 22\text{ m/s}$.
  $$v_{\text{avg}} = \frac{v(0) + v(5)}{2} = \frac{2 + 22}{2} = \frac{24}{2} = 12\text{ m/s}.$$
- Distance $=$ Average velocity $\times$ Time:
  $$\text{Distance} = 12\text{ m/s} \times 5\text{ s} = 60\text{ meters}.$$
Matches the integral calculation identically.

---

## 8. Common Mistakes to Avoid
- **Confusing displacement with total distance:** Using $\int v(t)\,dt$ when asked for distance in a problem where velocity changes sign.
- **Arithmetic errors in antiderivative:** Writing $\int 4t\,dt = 4t^2$ instead of $2t^2$.
- **Omitting units:** Forgetting that distance has physical units ($\text{meters}$).

---

## 9. Classroom Presentation (3-Sentence Summary)
Integrating the velocity function $v(t) = 4t + 2$ over the interval $[0, 5]$ yields $[2t^2 + 2t]_0^5 = 60\text{ meters}$, which represents the distance traveled because velocity is positive throughout. The integral gives the change in position because it continuously sums the infinitesimal displacements $ds = v(t)\,dt$ according to the Net Change Theorem. If velocity took negative values, the standard integral would compute net displacement where reversals cancel out, requiring us to integrate the speed $|v(t)|$ to determine the true distance traveled.
