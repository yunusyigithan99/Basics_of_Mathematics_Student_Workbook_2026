# Problem 7 Solution: Limit at a Point and Canceling a Factor

## 1. Original Problem
Compute the limit of the rational function at a finite point:
$$\lim_{x\to3} \frac{x^2 - 4x + 3}{x - 3}.$$
Explain in detail why the actual value of the function at the point $x = 3$ is not needed (and in fact does not exist) in order to compute the limit.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the indeterminate form $\left[\frac{0}{0}\right]$ resulting from direct substitution of $x = 3$.
2. Factor the quadratic polynomial in the numerator into linear binomial factors.
3. Cancel the common factor $(x - 3)$ under the condition $x \neq 3$.
4. Calculate the finite limit value by evaluating the simplified continuous function.
5. Provide a clear pedagogical explanation separating the local behavior of a function near a point from its value at the point itself.

---

## 3. Key Concepts and Theorems
1. **The Indeterminate Form $\left[\frac{0}{0}\right]$:**
   When both the numerator and the denominator of a rational function approach zero as $x \to c$, direct substitution yields $\frac{0}{0}$, which is undefined. By the Factor Theorem, $x - c$ must be a factor of both polynomials.
2. **Factoring a Quadratic Trinomial:**
   If $r_1, r_2$ are roots of $x^2 + Bx + C = 0$, then:
   $$x^2 + Bx + C = (x - r_1)(x - r_2).$$
   Here, sum of roots is $r_1 + r_2 = 4$ and product is $r_1 r_2 = 3$, giving roots $1$ and $3$.
3. **Formal Definition of a Limit:**
   The statement $\lim_{x\to c} f(x) = L$ means that for every $\varepsilon > 0$, there exists $\delta > 0$ such that:
   $$\text{for all } x \text{ with } 0 < |x - c| < \delta, \quad |f(x) - L| < \varepsilon.$$
   Crucially, the inequality $0 < |x - c|$ **explicitly excludes** the point $x = c$. A limit describes what $f(x)$ approaches as $x$ gets arbitrarily close to $c$, completely independent of what happens *at* $x = c$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Attempt Direct Substitution
Let $f(x) = \frac{x^2 - 4x + 3}{x - 3}$.
Attempt to evaluate $f(3)$ directly:
- Numerator: $3^2 - 4(3) + 3 = 9 - 12 + 3 = 0$
- Denominator: $3 - 3 = 0$
Direct substitution gives the indeterminate form:
$$\left[\frac{0}{0}\right].$$
The function $f(x)$ is **not defined** at $x = 3$ (it has a division by zero). The domain of $f$ is:
$$\operatorname{Dom}(f) = \mathbb{R} \setminus \{3\} = (-\infty, 3) \cup (3, \infty).$$

### Step 2: Factor the Numerator
Find the roots of the quadratic numerator $x^2 - 4x + 3$:
$$\Delta = (-4)^2 - 4(1)(3) = 16 - 12 = 4 = 2^2.$$
$$x_{1,2} = \frac{4 \pm 2}{2} \implies x_1 = 3, \quad x_2 = 1.$$
Thus, the numerator factors as:
$$x^2 - 4x + 3 = (x - 3)(x - 1).$$

### Step 3: Cancel the Discontinuous Factor
Substitute the factored form into the fraction:
$$\frac{x^2 - 4x + 3}{x - 3} = \frac{(x - 3)(x - 1)}{x - 3}.$$
Since the definition of the limit considers only values of $x$ in a punctured neighborhood of $3$ (where $x \neq 3$), the term $x - 3$ is **strictly non-zero**:
$$x - 3 \neq 0.$$
Therefore, we can divide numerator and denominator by $(x - 3)$:
$$\frac{(x - 3)(x - 1)}{x - 3} = x - 1 \quad (\text{for all } x \neq 3).$$

### Step 4: Evaluate the Limit of the Simplified Function
Now substitute $x = 3$ into the simplified linear expression:
$$\lim_{x\to3} \frac{x^2 - 4x + 3}{x - 3} = \lim_{x\to3} (x - 1) = 3 - 1 = 2.$$

---

### Step 5: Why the Function Value at $x = 3$ Is Not Needed
1. **The Limit Is About the Journey, Not the Destination:**
   A limit answers the question: *"What value do the outputs $f(x)$ get closer and closer to as the inputs $x$ get closer and closer to $3$?"* It does not ask: *"What is the output at $3$?"*
2. **Removable Discontinuity (A Hole in the Graph):**
   The graph of $f(x) = \frac{x^2 - 4x + 3}{x - 3}$ is the straight line $y = x - 1$ with a single point removed (a "hole") at coordinates $(3, 2)$.
   - For $x = 2.99$: $f(2.99) = 1.99$.
   - For $x = 3.01$: $f(3.01) = 2.01$.
   As $x$ approaches $3$ from either side, $f(x)$ approaches $2$ seamlessly.
3. **Independence of $f(c)$:**
   Whether $f(3)$ is undefined (as it is here), or whether we arbitrarily defined $f(3) = 100$ or $f(3) = 2$, the limit as $x \to 3$ would remain **strictly equal to 2**. The limit depends solely on the behavior in the punctured neighborhood $0 < |x - 3| < \delta$.

---

## 5. Why Each Step Is Valid
1. **The Factor Theorem** guarantees that because $x = 3$ is a zero of the polynomial $x^2 - 4x + 3$, $(x - 3)$ is an exact algebraic factor.
2. **Canceling $(x - 3)$** is valid because the limit operation specifies $x \to 3$, which explicitly excludes the singular point $x = 3$, meaning $\frac{x-3}{x-3} = 1$.
3. **Evaluating $\lim_{x\to 3}(x - 1) = 2$** is valid by the continuity of linear polynomial functions.

---

## 6. Final Answer in Words
The limit of the function is $\lim_{x\to3} \frac{x^2 - 4x + 3}{x - 3} = 2$. The actual value of the function at $x = 3$ does not exist (resulting in division by zero), and it is not needed to compute the limit because the definition of a limit inspects only the behavior of function values at points arbitrarily close to $3$ (where $x \neq 3$). In this punctured neighborhood, the factor $(x - 3)$ cancels out completely, reducing the function to the continuous line $x - 1$, which approaches $3 - 1 = 2$.

---

## 7. Quick Verification
- **Left approach ($x \to 3^-$):**
  - $x = 2.9 \implies f(2.9) = \frac{2.9^2 - 4(2.9) + 3}{2.9 - 3} = \frac{8.41 - 11.6 + 3}{-0.1} = \frac{-0.19}{-0.1} = 1.9$.
  - $x = 2.999 \implies f(2.999) = 1.999$.
- **Right approach ($x \to 3^+$):**
  - $x = 3.1 \implies f(3.1) = \frac{3.1^2 - 4(3.1) + 3}{3.1 - 3} = \frac{9.61 - 12.4 + 3}{0.1} = \frac{0.21}{0.1} = 2.1$.
  - $x = 3.001 \implies f(3.001) = 2.001$.
Both one-sided approaches converge unambiguously to $2.0$.

---

## 8. Common Mistakes to Avoid
- **Stating the limit does not exist because $f(3)$ is undefined:** Confusing the existence of a function value with the existence of a limit.
- **Applying l'Hôpital's rule unnecessarily:** While $\frac{2x - 4}{1} \to 2$ gives the right answer, factoring provides direct algebraic understanding without derivatives.
- **Canceling $(x - 3)$ without noting $x \neq 3$:** Division by zero is undefined; one must explicitly state that $x \neq 3$ during the limit process.

---

## 9. Classroom Presentation (3-Sentence Summary)
Direct substitution of $x = 3$ produces the indeterminate form $0/0$, showing that the function is undefined at that specific point. Factoring the numerator gives $(x - 3)(x - 1)$, and because the limit process considers only points where $x$ is near 3 but not equal to 3, we can cancel the $(x - 3)$ factor. This leaves the continuous expression $x - 1$, which evaluates to $3 - 1 = 2$, proving that a limit depends entirely on the surrounding neighborhood rather than the function value at the point itself.
