# Problem 07: Exponential Growth Dynamics, Differential Relations, and Doubling Time

## 1. Original Problem
Assume the model
$$N(t) = N_0 e^{kt}, \qquad k > 0.$$

1. Verify by differentiation that the model satisfies the relation $N'(t) = kN(t)$.
2. Find the population doubling time.
3. Explain why the doubling time does not depend on $N_0$.

---

## 2. What We Are Trying to Find
1. Verification by the chain rule that the derivative of the exponential function is proportional to the function itself ($N'(t) = k N(t)$).
2. The exact analytical expression and numerical approximation for the doubling time $T_d$.
3. Both algebraic and conceptual explanations for why the doubling time is completely independent of the initial population size $N_0$.

---

## 3. Key Concepts and Theorems
1. **Exponential Differentiation and Chain Rule:**
   $$\frac{d}{dt}\left(e^{u(t)}\right) = e^{u(t)} \cdot u'(t) \implies \frac{d}{dt}\left(e^{kt}\right) = k e^{kt}.$$
2. **Proportional Growth Rate:**
   The differential equation $\frac{dN}{dt} = k N$ characterizes unrestrained population growth where the instantaneous rate of increase is directly proportional to the current population size.
3. **Doubling Time Definition:**
   The time interval $T_d$ required for an initial quantity to double:
   $$N(t + T_d) = 2 N(t) \iff N(T_d) = 2 N_0.$$
4. **Logarithmic Inversion:**
   $$\ln(e^u) = u.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Verify the relation $N'(t) = kN(t)$ by differentiation
We are given the exponential growth model:
$$N(t) = N_0 e^{kt},$$
where $N_0 > 0$ represents the initial population at $t = 0$, and $k > 0$ is the continuous growth rate constant.

Differentiate $N(t)$ with respect to time $t$:
$$N'(t) = \frac{d}{dt}\left(N_0 e^{kt}\right) = N_0 \cdot \frac{d}{dt}\left(e^{kt}\right).$$
Using the Chain Rule on $e^{kt}$ with inner function $u(t) = kt$ (so $u'(t) = k$):
$$N'(t) = N_0 \cdot \left(e^{kt} \cdot k\right) = k \cdot \left(N_0 e^{kt}\right).$$
Because the quantity in parentheses is the original function $N(t)$, we substitute $N(t)$ back into the expression:
$$N'(t) = k N(t).$$
This confirms that the function satisfies the differential equation $N'(t) = kN(t)$ identically for all $t$.

### Step 2: Find the population doubling time $T_d$
Let $T_d$ denote the doubling time. By definition, at time $t = T_d$, the population reaches twice its initial value $N_0$:
$$N(T_d) = 2N_0.$$
Substitute the formula for $N(T_d)$:
$$N_0 e^{k T_d} = 2N_0.$$
Divide both sides by the non-zero initial population $N_0$:
$$e^{k T_d} = 2.$$
Take the natural logarithm of both sides to invert the exponential:
$$\ln\left(e^{k T_d}\right) = \ln(2).$$
Using the inverse property $\ln(e^x) = x$:
$$k T_d = \ln 2.$$
Divide both sides by the growth constant $k$:
$$T_d = \frac{\ln 2}{k} \approx \frac{0.69315}{k}.$$

### Step 3: Explain why the doubling time does not depend on $N_0$

1. **Algebraic Explanation:**
   In the equation defining the doubling condition:
   $$N_0 e^{k T_d} = 2 N_0,$$
   the initial population $N_0$ appears as a linear multiplying factor on both the left-hand side and the right-hand side. Because $N_0 > 0$, dividing both sides by $N_0$ completely eliminates it:
   $$e^{k T_d} = 2.$$
   The resulting equation involves only the growth rate $k$ and the target ratio $2$. Therefore, the solution $T_d = \frac{\ln 2}{k}$ is mathematically invariant with respect to $N_0$.

2. **Conceptual / Biological Explanation:**
   Exponential growth is **scale-invariant** (self-similar). The equation $N'(t) = k N(t)$ states that every single individual reproduces at the exact same constant per-capita rate $k$, independently of the size of the crowd.
   - To double a colony of $100$ bacteria into $200$, each of the $100$ bacteria must on average divide once.
   - To double a colony of $1,000,000$ bacteria into $2,000,000$, each of the $1,000,000$ bacteria must also divide once.
   Because all bacteria divide concurrently at the same individual rate $k$, doubling 100 cells takes the exact same amount of time as doubling 1 million cells. The absolute size of the population affects the *absolute number of new individuals produced*, but not the *relative time required for a two-fold multiplication*.

---

## 5. Why Each Step Is Valid
- **Step 1:** The derivative of an exponential function with a linear exponent is $k e^{kt}$ by the Chain Rule.
- **Step 2:** The natural logarithm is a strictly increasing bijection from $(0, \infty)$ to $\mathbb{R}$, ensuring a unique positive real solution $T_d$.
- **Step 3:** The cancellation law of real numbers ($a \cdot b = a \cdot c \iff b = c$ for $a \neq 0$) proves algebraic independence.

---

## 6. Final Answer in Words
1. Differentiating $N(t) = N_0 e^{kt}$ yields $N'(t) = N_0(ke^{kt}) = k(N_0e^{kt}) = kN(t)$, verifying the relationship.
2. The population doubling time is:
   $$T_d = \frac{\ln 2}{k} \approx \frac{0.693}{k}.$$
3. The doubling time is independent of $N_0$ because $N_0$ cancels from both sides of $N_0 e^{k T_d} = 2N_0$. Conceptually, exponential growth is a constant per-capita process: every member of the population reproduces at the same rate $k$, so doubling from any starting level requires the exact same duration.

---

## 7. Quick Verification
- Let $k = 0.05$ (5% continuous growth):
  $T_d = \frac{\ln 2}{0.05} \approx \frac{0.69315}{0.05} \approx 13.86$ time units (the well-known "Rule of 70" in finance: $70 / 5 = 14$).
- Test with $N_0 = 10$: $N(13.86) = 10 e^{0.05 \times 13.86} = 10 e^{0.693} = 10(2) = 20$.
- Test with $N_0 = 500$: $N(13.86) = 500 e^{0.05 \times 13.86} = 500(2) = 1000$.
Both initial populations double in exactly $13.86$ time units.

---

## 8. Common Mistakes to Avoid
- **Forgetting the chain rule:** Writing $\frac{d}{dt}(e^{kt}) = e^{kt}$ without multiplying by the inner derivative $k$.
- **Using $\log_{10}$ instead of $\ln$:** Writing $T_d = \frac{\log_{10} 2}{k} \approx \frac{0.301}{k}$, forgetting that the base of the natural exponential $e$ requires the natural logarithm $\ln$.
- **Thinking doubling time increases with larger populations:** Confusing the total number of births per second (which is much larger for big populations) with the percentage doubling time (which is constant).

---

## 9. Classroom Presentation (3-Sentence Summary)
Differentiating $N(t) = N_0 e^{kt}$ with the chain rule produces $k N_0 e^{kt}$, which directly confirms the proportional rate of change $N'(t) = k N(t)$. Setting $N(T_d) = 2N_0$ allows $N_0$ to cancel from both sides, yielding the doubling time $T_d = (\ln 2)/k$. The doubling time is independent of the initial population because the growth rate is per-capita, meaning a large population and a small population double their numbers in the exact same time.
