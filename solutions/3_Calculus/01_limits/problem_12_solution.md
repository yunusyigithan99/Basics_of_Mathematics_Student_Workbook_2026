# Problem 12 Solution: Exponential Function Limit Related to e

## 1. Original Problem
Compute the limit of the exponential function:
$$\lim_{x\to0} (1 + 3x)^{1/x}.$$
Connect this result with the classical limit from Exercise 5, and demonstrate the appropriate algebraic transformation (change of variable and exponent manipulation) needed to evaluate it.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the indeterminate form $\left[1^\infty\right]$ resulting from $x \to 0$.
2. Connect this function limit to the foundational Euler limit definition:
   $$\lim_{u\to0} (1 + u)^{1/u} = e \quad \text{or} \quad \lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n = e.$$
3. Apply a substitution $u = 3x$ (or adjust exponents) to transform the expression into the exact Euler form.
4. Calculate the exact analytical value of the limit in terms of Euler's number $e$.

---

## 3. Key Concepts and Theorems
1. **The Fundamental Euler Limit for Functions:**
   As $u \to 0$:
   $$\lim_{u\to0} (1 + u)^{1/u} = e.$$
   Equivalently, letting $u = \frac{1}{t}$ as $t \to \pm\infty$:
   $$\lim_{t\to\infty} \left(1 + \frac{1}{t}\right)^t = e.$$
2. **General Power-Exponential Theorem:**
   For any real constant $k \in \mathbb{R}$:
   $$\lim_{x\to0} (1 + kx)^{1/x} = e^k.$$
3. **Continuity of the Exponential Function:**
   Because $g(y) = y^k$ and $h(t) = e^t$ are continuous functions on their domains, limits commute across exponents:
   $$\lim \left[f(x)\right]^k = \left[\lim f(x)\right]^k.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Indeterminate Form
Examine the base and exponent as $x \to 0$:
- Base: $1 + 3x \to 1 + 3(0) = 1$
- Exponent: $\frac{1}{x} \to \pm\infty$ (depending on whether $x \to 0^+$ or $x \to 0^-$)
This yields the classical indeterminate form:
$$\left[1^\infty\right].$$

### Step 2: Method 1 — Exponent Manipulation
To utilize the standard limit $\lim_{u\to0} (1 + u)^{1/u} = e$, the exponent must be the exact reciprocal of the inner perturbation $3x$.
The reciprocal of $3x$ is:
$$\frac{1}{3x}.$$
Notice that we can rewrite the original exponent $\frac{1}{x}$ as:
$$\frac{1}{x} = \frac{3}{3x} = \left(\frac{1}{3x}\right) \cdot 3.$$
Using the power of a power law $(A^{BC}) = (A^B)^C$:
$$(1 + 3x)^{1/x} = (1 + 3x)^{\frac{1}{3x} \cdot 3} = \left[ (1 + 3x)^{\frac{1}{3x}} \right]^3.$$

### Step 3: Method 2 — Change of Variable (Substitution)
Let $u = 3x$.
- As $x \to 0$, we have $u = 3(0) \to 0$.
- Since $u = 3x$, solving for $x$ gives $x = \frac{u}{3}$, so:
  $$\frac{1}{x} = \frac{3}{u}.$$
Substitute $u$ into the expression:
$$\lim_{x\to0} (1 + 3x)^{1/x} = \lim_{u\to0} (1 + u)^{3/u} = \lim_{u\to0} \left[ (1 + u)^{1/u} \right]^3.$$

### Step 4: Evaluate the Limit
By the fundamental definition of the number $e$ (connected directly to Exercise 5):
$$\lim_{u\to0} (1 + u)^{1/u} = e.$$
Because the cubic function $f(t) = t^3$ is continuous on all of $\mathbb{R}$, we can pass the limit inside the power:
$$\lim_{u\to0} \left[ (1 + u)^{1/u} \right]^3 = \left[ \lim_{u\to0} (1 + u)^{1/u} \right]^3 = e^3.$$

### Step 5: Connection to Exercise 5
- In Exercise 5, we studied the discrete sequence:
  $$\lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n = e.$$
- If we substitute $x = \frac{1}{3n}$, then as $n \to \infty$, $x \to 0^+$.
- The expression becomes:
  $$(1 + 3x)^{1/x} = \left(1 + 3\left(\frac{1}{3n}\right)\right)^{3n} = \left(1 + \frac{1}{n}\right)^{3n} = \left[\left(1 + \frac{1}{n}\right)^n\right]^3.$$
- Taking the limit as $n \to \infty$:
  $$\lim_{n\to\infty} \left[\left(1 + \frac{1}{n}\right)^n\right]^3 = e^3.$$
This shows that Exercise 12 is the continuous functional counterpart of Exercise 5 with an added internal scaling factor of $3$.

---

## 5. Why Each Step Is Valid
1. **The power identity $(A^{1/(3x)})^3 = A^{1/x}$** is valid by the standard laws of exponents for positive bases ($1 + 3x > 0$ near $x = 0$).
2. **The substitution $u = 3x$** is valid because $u(x) = 3x$ is a continuous bijection near $0$ with $u(x) \neq 0$ for $x \neq 0$.
3. **Passing the limit inside the cubic power** is valid because $t \mapsto t^3$ is a continuous mapping.

---

## 6. Final Answer in Words
The limit of the function is $\lim_{x\to0} (1 + 3x)^{1/x} = e^3 \approx 20.0855$. We evaluate it by rewriting the exponent as $\frac{1}{x} = \frac{3}{3x}$, which allows us to express the function as $\left[(1 + 3x)^{\frac{1}{3x}}\right]^3$. Substituting $u = 3x$ transforms the inner term into the classical definition of Euler's number $\lim_{u\to0}(1 + u)^{1/u} = e$, which raised to the outer power of 3 yields the final value $e^3$.

---

## 7. Quick Verification
- Compute values for small values of $x$:
  - $e^3 \approx 20.0855369\dots$
  - For $x = 0.1$: $(1 + 0.3)^{10} = (1.3)^{10} \approx 13.7858$.
  - For $x = 0.01$: $(1 + 0.03)^{100} = (1.03)^{100} \approx 19.2186$.
  - For $x = 0.001$: $(1 + 0.003)^{1000} = (1.001)^{3000} \approx 19.9955$.
  - For $x = 0.0001$: $(1.0003)^{10000} \approx 20.0765 \approx e^3$.
- Check from the left ($x < 0$):
  - For $x = -0.001$: $(1 - 0.003)^{-1000} = (0.997)^{-1000} \approx 20.1762 \approx e^3$.
The numerical values converge smoothly to $e^3$ from both sides.

---

## 8. Common Mistakes to Avoid
- **Multiplying the base instead of the exponent:** Writing the answer as $3e$ instead of $e^3$.
- **Believing $1^\infty = 1$:** Assuming that since $1 + 3x \to 1$, $1^{\text{anything}} = 1$.
- **Applying l'Hôpital directly to $(1 + 3x)^{1/x}$:** Forgetting that l'Hôpital applies only to quotients $\frac{0}{0}$ or $\frac{\infty}{\infty}$, requiring logarithmic transformation $\exp(\ln f(x))$ first.

---

## 9. Classroom Presentation (3-Sentence Summary)
The expression $(1 + 3x)^{1/x}$ represents the indeterminate form $1^\infty$ as $x$ approaches zero. By decomposing the exponent as $(1/3x) \cdot 3$, we rewrite the function as the cube of $(1 + 3x)^{1/(3x)}$. Since the inner term matches the fundamental definition of Euler's number $e$ via the substitution $u = 3x$, the limit evaluates directly to $e^3$.
