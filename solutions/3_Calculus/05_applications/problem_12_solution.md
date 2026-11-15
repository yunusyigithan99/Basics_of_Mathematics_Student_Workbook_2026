# Problem 12: Comprehensive Optimization Model and Verification — Museum Exhibition Room

## 1. Original Problem
A museum wants to create a rectangular exhibition room next to an existing straight wall. The side along the wall does not need to be built. The remaining three sides are to be constructed to two different standards: the two sides perpendicular to the wall cost $300\ \mathrm{PLN/m}$ each, while the side parallel to the wall costs $500\ \mathrm{PLN/m}$. The budget is $30\,000\ \mathrm{PLN}$.

Build a model that maximizes the area of the room and prepare a complete analysis containing:
- definition of variables and units,
- mathematical model,
- domain resulting from the problem statement,
- computation of the derivative,
- determination and verification of the optimum,
- interpretation of the result,
- graph of the objective function,
- numerical verification of several values near the optimum found.

Finally, indicate which part of the solution required modeling the problem and which part was only the execution of the calculation. Produce the graph and computer calculations only after completing the mathematical solution, and treat them as verification.

---

## 2. What We Are Trying to Find
1. Definitions of geometric and economic variables with explicit units.
2. The mathematical formulation of the objective function (area) and constraint (budget).
3. The exact feasible domain for the independent variable.
4. The calculus-based derivation of the critical point and proof of its optimality.
5. Physical, geometric, and economic interpretation of the optimum (budget distribution).
6. A ASCII graph and numerical sensitivity table near the optimum.
7. A clear pedagogical reflection separating the **modeling phase** from the **calculational phase**.

---

## 3. Key Concepts and Theorems
1. **Applied Constrained Optimization:**
   Expressing an objective quantity $A(x, y)$ subject to an equality constraint $g(x, y) = B$ by reducing it to a single-variable function $A(x)$.
2. **First and Second Derivative Tests for Global Extrema:**
   If $A'(x_0) = 0$ and $A''(x) < 0$ on the entire open interval, $x_0$ is the unique absolute maximum.
3. **Equipartition of Budget in Linear-Constraint Quadratic Optimization:**
   In cost-constrained rectangular optimization, optimal allocation splits the total expenditure equally between the independent coordinate directions.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Definition of variables and units
- Let $x$ denote the length of the new wall built **parallel** to the existing museum wall, measured in meters ($\mathrm{m}$).
- Let $y$ denote the length of each of the two walls built **perpendicular** to the existing museum wall, measured in meters ($\mathrm{m}$).
- Let $A$ denote the enclosed floor area of the exhibition room, measured in square meters ($\mathrm{m}^2$).
- Let $C$ denote the total construction expenditure, measured in Polish Złoty ($\mathrm{PLN}$).
- Unit cost of parallel wall: $c_x = 500\ \mathrm{PLN/m}$.
- Unit cost of perpendicular walls: $c_y = 300\ \mathrm{PLN/m}$.
- Total Budget: $B = 30\,000\ \mathrm{PLN}$.

```text
       Existing Straight Museum Wall (No cost: 0 PLN)
       ==============================================
             |                                  |
             |                                  |
      y (300 PLN/m)                      y (300 PLN/m)
             |                                  |
             |                                  |
             +----------------------------------+
                     x (500 PLN/m)
```

### Step 2: Mathematical model and reduction to one variable
1. **Objective Function (Enclosed Area):**
   $$A = x \cdot y \quad [\mathrm{m}^2].$$
2. **Budget Constraint:**
   The total expenditure consists of one parallel side of length $x$ and two perpendicular sides of length $y$:
   $$C(x, y) = 500x + 2(300y) = 500x + 600y.$$
   Setting the expenditure equal to the full budget of $30\,000\ \mathrm{PLN}$:
   $$500x + 600y = 30\,000.$$
3. **Elimination of $y$:**
   Solve for $y$ in terms of $x$:
   $$600y = 30\,000 - 500x \iff y = \frac{30\,000 - 500x}{600} = 50 - \frac{5}{6}x.$$
4. **Single-Variable Objective Function:**
   Substitute $y(x)$ into the area formula:
   $$A(x) = x \left(50 - \frac{5}{6}x\right) = 50x - \frac{5}{6}x^2.$$

### Step 3: Domain resulting from the problem statement
For a real physical room:
- The width must be positive: $x > 0$.
- The depth must also be positive:
  $$y > 0 \iff 50 - \frac{5}{6}x > 0 \iff \frac{5}{6}x < 50 \iff x < 50 \cdot \frac{6}{5} = 60.$$
Therefore, the physically feasible domain is:
$$D_A = (0, 60) \quad \text{meters}.$$
*(On the compact closure $[0, 60]$, the endpoints $x = 0$ and $x = 60$ represent degenerate rooms with zero area: $A(0) = 0$ and $A(60) = 0$.)*

### Step 4: Computation of the derivative and stationary point
Differentiate $A(x) = 50x - \frac{5}{6}x^2$ with respect to $x$:
$$A'(x) = \frac{d}{dx}\left(50x - \frac{5}{6}x^2\right) = 50 - \frac{5}{6}(2x) = 50 - \frac{5}{3}x.$$
Set the derivative to zero:
$$50 - \frac{5}{3}x = 0 \iff \frac{5}{3}x = 50 \iff x = 50 \cdot \frac{3}{5} = 30\text{ meters}.$$

Compute the corresponding perpendicular wall length $y$:
$$y = 50 - \frac{5}{6}(30) = 50 - 25 = 25\text{ meters}.$$

### Step 5: Verification of the optimum
1. **Second Derivative Test:**
   $$A''(x) = \frac{d}{dx}\left(50 - \frac{5}{3}x\right) = -\frac{5}{3}.$$
   Because $A''(x) = -\frac{5}{3} < 0$ for all $x \in (0, 60)$, the function $A(x)$ is strictly concave (a downward-opening parabola). Therefore, $x = 30$ is a **strict global maximum**.
2. **Maximum Area:**
   $$A_{\max} = A(30) = 30 \times 25 = 750\ \mathrm{m}^2.$$

### Step 6: Interpretation of the result
- **Optimal Dimensions:** The room should be $30\text{ m}$ wide along the wall and $25\text{ m}$ deep perpendicular to it.
- **Budget Allocation (The 50/50 Rule):**
  - Expenditure on parallel wall: $500\ \mathrm{PLN/m} \times 30\text{ m} = 15\,000\ \mathrm{PLN}$.
  - Expenditure on perpendicular walls: $2 \times (300\ \mathrm{PLN/m} \times 25\text{ m}) = 15\,000\ \mathrm{PLN}$.
  Notice that the optimal strategy divides the budget **equally**: exactly $50\%$ of the budget ($15\,000\ \mathrm{PLN}$) is spent on the parallel dimension, and exactly $50\%$ ($15\,000\ \mathrm{PLN}$) is spent on the two perpendicular walls combined! This equipartition of expenditure is a universal property of linear-budget rectangular optimization.

### Step 7: Graph of the objective function
```text
           Area A(x) [m^2]
            |
        750 |                       *(30, 750) Maximum
            |                     .   ` .
        600 |                   /         \
            |                  /           \
        400 |                 /             \
            |                /               \
        200 |               /                 \
            |              /                   \
          0 +-------------*---------------------*----> x [m]
            0            (0,0)       30         60
```

### Step 8: Numerical verification table near the optimum
We calculate the dimensions, costs, and resulting areas for several values of $x$ around $x = 30$:

| $x$ [m] | $y = 50 - \frac{5}{6}x$ [m] | Parallel Cost [PLN] | Perpendicular Cost [PLN] | Total Cost [PLN] | Area $A = x y$ [$\mathrm{m}^2$] | Difference from $A_{\max}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$20$** | $33.33$ | $10\,000$ | $20\,000$ | $30\,000$ | $666.67$ | $-83.33\ \mathrm{m}^2$ |
| **$24$** | $30.00$ | $12\,000$ | $18\,000$ | $30\,000$ | $720.00$ | $-30.00\ \mathrm{m}^2$ |
| **$27$** | $27.50$ | $13\,500$ | $16\,500$ | $30\,000$ | $742.50$ | $-7.50\ \mathrm{m}^2$ |
| **$30$ (Opt)** | **$25.00$** | **$15\,000$** | **$15\,000$** | **$30\,000$** | **$750.00$** | **$0.00$ (Optimal)** |
| **$33$** | $22.50$ | $16\,500$ | $13\,500$ | $30\,000$ | $742.50$ | $-7.50\ \mathrm{m}^2$ |
| **$36$** | $20.00$ | $18\,000$ | $12\,000$ | $30\,000$ | $720.00$ | $-30.00\ \mathrm{m}^2$ |
| **$40$** | $16.67$ | $20\,000$ | $10\,000$ | $30\,000$ | $666.67$ | $-83.33\ \mathrm{m}^2$ |

The numerical table confirms absolute symmetry about $x = 30$ and verifies that any deviation strictly reduces the room's area.

### Step 9: Modeling vs. Calculational Execution
- **Modeling Phase (Problem Formulation):**
  1. Reading the verbal description and identifying that only three walls need construction.
  2. Defining physical variables ($x, y, A$) with explicit units ($\mathrm{m, m^2, PLN}$).
  3. Setting up the cost equation $500x + 600y = 30\,000$ from unit rates and the budget.
  4. Determining the realistic physical domain $(0, 60)\text{ m}$.
  5. Formulating the economic interpretation: recognizing that optimal construction splits capital equally between the two coordinate directions ($15\,000\ \mathrm{PLN}$ each).
- **Calculational Execution (Mechanical Calculus):**
  1. Algebraically isolating $y$ and substituting into $A(x) = 50x - \frac{5}{6}x^2$.
  2. Differentiating using the power rule to obtain $A'(x) = 50 - \frac{5}{3}x$.
  3. Solving the linear equation $A'(x) = 0$ for $x = 30$.
  4. Evaluating the second derivative $A''(30) = -\frac{5}{3} < 0$.
  5. Generating the numerical sensitivity table and plotting the curve.

---

## 5. Why Each Step Is Valid
- **Step 1:** Clearly defining variables with units prevents dimensional inconsistencies.
- **Step 2:** The single existing wall eliminates one parallel boundary, reducing perimeter cost.
- **Step 3:** Lengths must be positive; $y > 0$ restricts $x < 60$.
- **Step 4:** Differentiating a quadratic function gives a linear derivative with a unique root.
- **Step 5:** The strictly negative second derivative proves global concavity.
- **Step 6 & 8:** The numerical verification confirms the calculus result independently.

---

## 6. Final Answer in Words
The optimal exhibition room should have a parallel wall length of $x = 30\text{ meters}$ and perpendicular wall lengths of $y = 25\text{ meters}$. 
This configuration yields a maximum exhibition floor area of $750\ \mathrm{m}^2$. 
Economically, the solution splits the $30\,000\ \mathrm{PLN}$ budget exactly in half: $15\,000\ \mathrm{PLN}$ is spent on the parallel wall ($30\text{ m} \times 500\ \mathrm{PLN/m}$) and $15\,000\ \mathrm{PLN}$ is spent on the two perpendicular walls ($2 \times 25\text{ m} \times 300\ \mathrm{PLN/m}$). 
The modeling component consists of translating the architectural and budgetary constraints into $A(x) = 50x - \frac{5}{6}x^2$ on $(0, 60)\text{ m}$, while the calculational component consists of differentiating, solving $A'(x) = 0$, and verifying the maximum via $A''(x) < 0$ and the numerical sensitivity table.

---

## 7. Quick Verification
- Budget check: $500(30) + 600(25) = 15\,000 + 15\,000 = 30\,000\ \mathrm{PLN}$.
- Table symmetry: $A(27) = A(33) = 742.5\ \mathrm{m}^2 < 750\ \mathrm{m}^2$.
- Extreme boundary check: $A(0) = 0$, $A(60) = 0$.
The peak at $(30, 750)$ is thoroughly confirmed.

---

## 8. Common Mistakes to Avoid
- **Including four sides:** Budgeting for an unnecessary fourth wall along the existing museum wall.
- **Forgetting that there are TWO perpendicular walls:** Writing $500x + 300y = 30\,000$ instead of $500x + 600y = 30\,000$.
- **Assuming equal side lengths ($x = y$):** Setting $x = y$ without accounting for the unequal unit construction costs ($500$ vs $300\ \mathrm{PLN/m}$).

---

## 9. Classroom Presentation (3-Sentence Summary)
By setting up the budget constraint $500x + 600y = 30\,000$, we eliminate $y$ to obtain the area function $A(x) = 50x - \frac{5}{6}x^2$ on the feasible domain $(0, 60)\text{ m}$. Setting the derivative $A'(x) = 50 - \frac{5}{3}x = 0$ yields optimal dimensions of $x = 30\text{ m}$ and $y = 25\text{ m}$, producing a maximum area of $750\ \mathrm{m}^2$. This demonstrates the classic economic principle of equipartition, where the optimal room splits the budget equally, allocating $15\,000\ \mathrm{PLN}$ to the parallel wall and $15\,000\ \mathrm{PLN}$ to the two perpendicular walls.
