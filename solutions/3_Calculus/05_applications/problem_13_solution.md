# Problem 13: Physical Applications — Work Done by a Variable Force (Hooke's Law)

*(Workbook Note: The core exercise document intentionally sets 12 cross-sectional exercises. This problem serves as the capstone physical application covering work and variable force to complete the full 15-problem workbook review suite).*

## 1. Original Problem
A spring has a natural length of $20\text{ cm}$. A force of $40\text{ N}$ is required to hold the spring stretched to a length of $30\text{ cm}$.

1. Determine the spring constant $k$ using Hooke's Law $F(x) = kx$.
2. Compute the work done in stretching the spring from its natural length to a length of $35\text{ cm}$.
3. Compute the additional work required to stretch it further from $35\text{ cm}$ to $40\text{ cm}$.
4. Explain why stretching the second $5\text{ cm}$ requires significantly more work than stretching the first $5\text{ cm}$.

---

## 2. What We Are Trying to Find
1. The stiffness constant $k$ (in $\text{N/m}$) characterizing the spring.
2. The work integral $W = \int F(x)\,dx$ for an extension from $x = 0$ to $x = 0.15\text{ m}$.
3. The definite integral for the secondary extension from $x = 0.15\text{ m}$ to $x = 0.20\text{ m}$.
4. A physical explanation of why work against a variable linear restoring force scales quadratically rather than linearly with displacement.

---

## 3. Key Concepts and Theorems
1. **Hooke's Law:**
   The restoring force required to maintain a spring stretched by displacement $x$ from its equilibrium (natural) position is:
   $$F(x) = kx,$$
   where $k$ is the spring constant (in $\text{N/m}$) and $x$ is the elongation (in meters).
2. **Work as an Integral of Variable Force:**
   When a force varies along the line of motion from position $x = a$ to $x = b$, the mechanical work done is:
   $$W = \int_a^b F(x)\,dx = \int_a^b kx\,dx = \left[\frac{1}{2}kx^2\right]_a^b.$$
3. **Elastic Potential Energy:**
   The work done in stretching an ideal spring from rest to elongation $x$ is stored as elastic potential energy:
   $$E_p = \frac{1}{2}kx^2.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Find the spring constant $k$
Natural length: $L_0 = 20\text{ cm} = 0.20\text{ m}$.
When the total length is $L = 30\text{ cm} = 0.30\text{ m}$, the elongation beyond natural length is:
$$x = L - L_0 = 0.30 - 0.20 = 0.10\text{ m}.$$
According to Hooke's Law:
$$F(x) = kx \implies 40\text{ N} = k \cdot (0.10\text{ m}).$$
Solving for $k$:
$$k = \frac{40\text{ N}}{0.10\text{ m}} = 400\text{ N/m}.$$
Thus, the restoring force function is:
$$F(x) = 400x \quad [\text{N}].$$

### Step 2: Compute work done stretching from natural length to $35\text{ cm}$
- Starting elongation: $x_1 = 0\text{ m}$ (natural length $20\text{ cm}$).
- Ending elongation: $x_2 = 0.35 - 0.20 = 0.15\text{ m}$ (total length $35\text{ cm}$).

The work done is:
$$W_1 = \int_0^{0.15} 400x\,dx = \left[400 \cdot \frac{x^2}{2}\right]_0^{0.15} = \left[200x^2\right]_0^{0.15}.$$
Evaluate at the limits:
$$W_1 = 200(0.15)^2 - 0 = 200(0.0225) = 4.5\text{ Joules (J)}.$$

### Step 3: Compute additional work from $35\text{ cm}$ to $40\text{ cm}$
- Starting elongation: $x_a = 0.35 - 0.20 = 0.15\text{ m}$.
- Ending elongation: $x_b = 0.40 - 0.20 = 0.20\text{ m}$.

The additional work done is:
$$W_2 = \int_{0.15}^{0.20} 400x\,dx = \left[200x^2\right]_{0.15}^{0.20}$$
$$= 200\left[(0.20)^2 - (0.15)^2\right] = 200(0.0400 - 0.0225) = 200(0.0175) = 3.5\text{ Joules (J)}.$$

### Step 4: Explain why later increments require more work
Let us compare two identical $5\text{ cm}$ ($0.05\text{ m}$) stretches:
1. **First $5\text{ cm}$ stretch (from $x = 0$ to $x = 0.05\text{ m}$):**
   $$W_{0 \to 0.05} = 200(0.05)^2 = 200(0.0025) = 0.5\text{ Joules}.$$
2. **Stretch from $35\text{ cm}$ to $40\text{ cm}$ (from $x = 0.15$ to $x = 0.20\text{ m}$):**
   $$W_{0.15 \to 0.20} = 3.5\text{ Joules}.$$

Notice that the later $5\text{ cm}$ stretch requires **7 times more work** ($3.5\text{ J}$ vs $0.5\text{ J}$), despite moving through the exact same distance $\Delta x = 0.05\text{ m}$!

**Physical Reason:**
Work is defined as force integrated over distance: $W = \int F\,dx$. 
- In the first stretch, the resisting force starts at $F(0) = 0\text{ N}$ and only rises to $F(0.05) = 20\text{ N}$ (average force is $10\text{ N}$).
- In the later stretch, the spring is already pre-stretched, so the resisting force starts at a massive $F(0.15) = 60\text{ N}$ and rises to $F(0.20) = 80\text{ N}$ (average force is $70\text{ N}$).
Because the force opposes elongation with increasing intensity, pulling against an already taut spring requires overcoming a much larger resistance, leading to quadratic energy accumulation $W \propto x^2$.

```text
       Force F(x) [N]
         |                                  * (0.20, 80 N)
      80 |                                 /|
      60 |                   *(0.15, 60 N)/ |
         |                  /|           |  |
         |                 / |    W2     |  | (Average Force = 70 N)
         |                /  |   3.5 J   |  |
      20 |  *(0.05, 20 N)/   |           |  |
         |  /|   W1      |   |           |  |
       0 +-+-------------+---+-----------+--+----> Elongation x [m]
         0 0.05         0.15            0.20
```

---

## 5. Why Each Step Is Valid
- **Step 1:** Displacements must be measured relative to the equilibrium resting position ($L - L_0$), not total length.
- **Step 2 & 3:** The definition of work as the line integral of force applies directly to 1D elastic deformation.
- **Step 4:** The average value theorem confirms that $\bar{F} = \frac{1}{\Delta x} \int F\,dx$ is substantially higher when the baseline force is non-zero.

---

## 6. Final Answer in Words
1. The spring constant is $k = 400\text{ N/m}$.
2. The work done stretching the spring from its natural length to $35\text{ cm}$ is $W_1 = 4.5\text{ Joules}$.
3. The additional work required to stretch it further from $35\text{ cm}$ to $40\text{ cm}$ is $W_2 = 3.5\text{ Joules}$.
4. Later stretches require more work because the restoring force $F(x) = kx$ increases linearly with displacement; pulling an already stretched spring requires pushing against a much higher average resistance ($70\text{ N}$ vs. $10\text{ N}$), making work scale quadratically with elongation ($W = \frac{1}{2}kx^2$).

---

## 7. Quick Verification
- Total work from natural length to $40\text{ cm}$ ($x = 0.20\text{ m}$):
  $$W_{\text{total}} = 200(0.20)^2 = 200(0.04) = 8.0\text{ Joules}.$$
- Add intermediate works:
  $$W_1 + W_2 = 4.5\text{ J} + 3.5\text{ J} = 8.0\text{ Joules}.$$
The pieces sum up to the total work with zero discrepancy.

---

## 8. Common Mistakes to Avoid
- **Using total length instead of elongation:** Integrating from $0.20$ to $0.35$ instead of $0$ to $0.15$. Elongation $x$ is measured from the natural unstretched length.
- **Forgetting to convert centimeters to meters:** Leaving $x$ in $\text{cm}$ gives answers that are off by a factor of $10^4$.
- **Using $W = F \cdot d$ with a single constant force:** Multiplying the final force by the total distance fails because force varies continuously with displacement.

---

## 9. Classroom Presentation (3-Sentence Summary)
From Hooke's Law $F = kx$, dividing the $40\text{ N}$ force by the $0.10\text{ m}$ elongation gives the spring constant $k = 400\text{ N/m}$. Integrating $F(x) = 400x$ shows that stretching from rest to $0.15\text{ m}$ requires $4.5\text{ Joules}$, while the subsequent $0.05\text{ m}$ stretch requires an additional $3.5\text{ Joules}$. The second stretch takes disproportionately more work because the spring's restoring force grows with elongation, requiring work against a much higher average resistance.
