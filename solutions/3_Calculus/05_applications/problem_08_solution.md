# Problem 08: Server Traffic Modeling — Accumulation of Requests and Average Rate

## 1. Original Problem
The rate at which requests arrive at a server during the first 5 minutes is described by the function
$$r(t) = 100 + 20t \quad [\text{requests/min}], \qquad 0 \le t \le 5.$$

1. Compute the total number of requests that arrived during this time.
2. Compute the average rate of incoming requests over this interval.
3. Compare the average rate with the values $r(0)$ and $r(5)$.

---

## 2. What We Are Trying to Find
1. The total cumulative count of requests arriving at the server between $t = 0$ and $t = 5$ minutes via definite integration.
2. The average arrival rate $r_{\text{avg}}$ across the 5-minute window.
3. The boundary arrival rates $r(0)$ and $r(5)$, and a formal comparison with the calculated average rate.
4. A mathematical explanation for why the integral average matches the endpoint arithmetic mean for linear models.

---

## 3. Key Concepts and Theorems
1. **Accumulation of a Time-Varying Rate:**
   If $r(t) = \frac{dR}{dt}$ represents the instantaneous arrival rate of events per unit time, the total number of events accumulated over $[t_1, t_2]$ is given by the definite integral:
   $$R_{\text{total}} = \int_{t_1}^{t_2} r(t)\,dt.$$
2. **Average Value of a Continuous Function:**
   $$r_{\text{avg}} = \frac{1}{b - a} \int_a^b r(t)\,dt.$$
3. **Linear Mean Property:**
   For any linear function $f(t) = mt + b$, the integral average on $[a, b]$ is exactly equal to the arithmetic average of the endpoint values:
   $$f_{\text{avg}} = \frac{f(a) + f(b)}{2} = f\left(\frac{a + b}{2}\right).$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the total number of requests
The arrival rate is $r(t) = 100 + 20t$ requests/min for $t \in [0, 5]$.
The total number of requests $R_{\text{total}}$ is the definite integral of $r(t)$ from $t = 0$ to $t = 5$:
$$R_{\text{total}} = \int_0^5 (100 + 20t)\,dt.$$

Find an antiderivative:
$$\int (100 + 20t)\,dt = 100t + 20 \cdot \frac{t^2}{2} = 100t + 10t^2.$$
Apply the limits from $t = 0$ to $t = 5$ via the Newton-Leibniz formula:
$$R_{\text{total}} = \left[100t + 10t^2\right]_0^5 = \left[100(5) + 10(5^2)\right] - \left[100(0) + 10(0^2)\right]$$
$$= [500 + 10(25)] - 0$$
$$= 500 + 250 = 750\text{ requests}.$$

### Step 2: Compute the average arrival rate over $[0, 5]$
The time duration is:
$$b - a = 5 - 0 = 5\text{ minutes}.$$
Using the formula for the average value of a function:
$$r_{\text{avg}} = \frac{1}{b - a} \int_a^b r(t)\,dt = \frac{1}{5} \cdot 750 = 150\text{ requests/min}.$$

### Step 3: Evaluate $r(0)$ and $r(5)$ and compare with $r_{\text{avg}}$
We compute the arrival rate at the start and end of the 5-minute interval:
- **At the start ($t = 0$):**
  $$r(0) = 100 + 20(0) = 100\text{ requests/min}.$$
- **At the end ($t = 5$):**
  $$r(5) = 100 + 20(5) = 100 + 100 = 200\text{ requests/min}.$$

Now, calculate the arithmetic mean of these two boundary values:
$$\frac{r(0) + r(5)}{2} = \frac{100 + 200}{2} = \frac{300}{2} = 150\text{ requests/min}.$$

**Comparison:**
The integral average rate $r_{\text{avg}} = 150\text{ requests/min}$ is **identically equal** to the arithmetic mean of the initial and final rates:
$$r_{\text{avg}} = \frac{r(0) + r(5)}{2} = 150\text{ requests/min}.$$
Furthermore, it equals the value of the function at the exact midpoint of the time interval $t = 2.5$:
$$r(2.5) = 100 + 20(2.5) = 100 + 50 = 150\text{ requests/min}.$$

### Step 4: Geometric explanation of the linear property
The region under the graph of $r(t) = 100 + 20t$ on $[0, 5]$ is a trapezoid with:
- Parallel vertical sides of heights $h_1 = r(0) = 100$ and $h_2 = r(5) = 200$,
- Width $w = 5$.
The geometric area of a trapezoid is:
$$\text{Area} = \frac{h_1 + h_2}{2} \cdot w = \frac{100 + 200}{2} \cdot 5 = 150 \cdot 5 = 750.$$
Dividing this area by the width $w = 5$ naturally recovers the average height $\frac{h_1 + h_2}{2} = 150$. Because the rate increases at a constant, linear speed, the steady increase is perfectly symmetric about the midpoint.

---

## 5. Why Each Step Is Valid
- **Step 1:** By the Net Change Theorem, integrating an arrival rate gives the net accumulated count of discrete events over that time.
- **Step 2:** The integral average gives the equivalent constant rate that would process the same total volume of requests in the same time.
- **Step 3:** The arithmetic mean of endpoints equals the integral mean for all degree-1 polynomials due to the symmetry of trapezoidal geometry.
- **Step 4:** Euclidean trapezoid area formulas match the Riemann integral of linear functions exactly.

---

## 6. Final Answer in Words
1. The total number of requests that arrived at the server during the 5 minutes is:
   $$\int_0^5 (100 + 20t)\,dt = 750\text{ requests}.$$
2. The average arrival rate over this interval is $r_{\text{avg}} = \frac{750}{5} = 150\text{ requests/minute}$.
3. The boundary rates are $r(0) = 100\text{ requests/min}$ and $r(5) = 200\text{ requests/min}$. The average rate of $150$ is exactly the arithmetic mean $\frac{100 + 200}{2} = 150$, which occurs because the arrival rate increases linearly with time.

---

## 7. Quick Verification
- Check with average rate:
  If a server receives a constant average of $150\text{ requests/min}$ for $5\text{ minutes}$:
  $$\text{Total} = 150\text{ requests/min} \times 5\text{ min} = 750\text{ requests}.$$
This immediately confirms that $r_{\text{avg}}$ correctly preserves the total count.

---

## 8. Common Mistakes to Avoid
- **Multiplying the final rate by total time:** Computing $r(5) \times 5 = 200 \times 5 = 1000\text{ requests}$, which falsely assumes the rate was $200$ during the entire period.
- **Assuming the arithmetic mean always works for any function:** Believing that $f_{\text{avg}} = \frac{f(a) + f(b)}{2}$ holds for quadratic or exponential rates (it only holds for linear functions).
- **Omitting units:** Forgetting that the total count has units of "requests", while the rate has units of "requests/min".

---

## 9. Classroom Presentation (3-Sentence Summary)
Integrating the incoming request rate $r(t) = 100 + 20t$ from $t = 0$ to $5$ yields $[100t + 10t^2]_0^5 = 750\text{ requests}$. Dividing this total by the 5-minute interval gives an average arrival rate of $150\text{ requests/minute}$. Because the rate is a linear function, this average rate is exactly equal to the arithmetic mean of the starting rate of $100$ and the ending rate of $200$.
