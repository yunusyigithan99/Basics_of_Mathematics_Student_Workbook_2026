# Problem 11 Solution: Derivative from the Definition

## 1. Original Problem
Using strictly the formal limit definition of the derivative:
$$f'(x) = \lim_{h\to0} \frac{f(x + h) - f(x)}{h},$$
find the derivative of the basic quadratic function:
$$f(x) = x^2.$$
Compare the result with the standard Power Rule formula, and explicitly indicate at which step the limit operation is evaluated and why the limit removes the algebraic obstacle of division by zero.

---

## 2. What We Are Trying to Find
We need to:
1. Formulate the difference quotient $\frac{f(x+h) - f(x)}{h}$ for $f(x) = x^2$.
2. Expand $(x + h)^2$ algebraically.
3. Simplify the numerator to reveal the common factor of $h$.
4. Cancel $h$ under the condition $h \neq 0$ to eliminate the $\left[\frac{0}{0}\right]$ indeterminate form.
5. Take the limit as $h \to 0$ to obtain $2x$.
6. Reconcile this result with the Power Rule $\frac{d}{dx}[x^2] = 2x^{2-1} = 2x$.

---

## 3. Key Concepts and Theorems
1. **The Definition of the Derivative:**
   The derivative $f'(x)$ is defined as the limit of the average rate of change (secant slope) as the step size $h$ shrinks to zero:
   $$f'(x) = \lim_{h\to0} \frac{f(x + h) - f(x)}{h}.$$
2. **Binomial Expansion of Degree 2:**
   $$(x + h)^2 = x^2 + 2xh + h^2.$$
3. **The Role of the Limit:**
   The initial quotient has the indeterminate form $\left[\frac{0}{0}\right]$ at $h = 0$. By factoring out and canceling $h \neq 0$, the expression transforms into a continuous linear function in $h$, allowing direct substitution of $h = 0$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Difference Quotient
For $f(x) = x^2$:
- $f(x + h) = (x + h)^2$
- $f(x) = x^2$

Substitute into the definition of the derivative:
$$f'(x) = \lim_{h\to0} \frac{(x + h)^2 - x^2}{h}.$$
Notice that directly setting $h = 0$ yields:
$$\frac{(x + 0)^2 - x^2}{0} = \frac{x^2 - x^2}{0} = \left[\frac{0}{0}\right].$$
This is undefined. We must perform algebraic simplification before taking the limit.

---

### Step 2: Expand the Numerator
Expand the binomial $(x + h)^2$:
$$(x + h)^2 = x^2 + 2xh + h^2.$$
Substitute this expansion into the difference quotient:
$$\frac{(x + h)^2 - x^2}{h} = \frac{(x^2 + 2xh + h^2) - x^2}{h}.$$

---

### Step 3: Simplify and Factor Out $h$
Subtract $x^2 - x^2 = 0$:
$$= \frac{2xh + h^2}{h}.$$
Factor $h$ out of the numerator:
$$= \frac{h(2x + h)}{h}.$$

---

### Step 4: Cancel the Common Factor $h$
Because the limit considers values of $h$ approaching zero without ever reaching zero ($h \neq 0$), we can divide numerator and denominator by $h$:
$$\frac{h(2x + h)}{h} = 2x + h \quad (\text{for all } h \neq 0).$$
*Key Observation:* This algebraic cancellation removes the singularity. The difference quotient, which was initially undefined at $h = 0$, is now represented by the polynomial $2x + h$, which is smooth and continuous for all $h$.

---

### Step 5: Evaluate the Limit (Where the Limit Is Used)
Now that the division by zero has been eliminated, we evaluate the limit by letting $h \to 0$:
$$f'(x) = \lim_{h\to0} (2x + h) = 2x + 0 = 2x.$$
This completes the derivation from first principles:
$$f'(x) = 2x.$$

---

### Step 6: Comparison with the Power Rule
The standard Power Rule states that for any real exponent $n$:
$$\frac{d}{dx}[x^n] = n x^{n-1}.$$
For $n = 2$:
$$\frac{d}{dx}[x^2] = 2 x^{2-1} = 2 x^1 = 2x.$$
The result derived from the limit definition matches the Power Rule formula identically. This exercise demonstrates that the Power Rule is not an arbitrary rule, but a direct consequence of expanding $(x + h)^n$ via the Binomial Theorem and taking the limit as $h \to 0$.

---

## 5. Why Each Step Is Valid
1. **The difference quotient formulation** is the axiomatic definition of instantaneous rate of change in analysis.
2. **Binomial expansion $(x+h)^2 = x^2 + 2xh + h^2$** follows from the distributive property of ring arithmetic.
3. **Canceling $h / h = 1$** is valid because the definition of a limit explicitly restricts the neighborhood to $h \neq 0$ ($0 < |h| < \delta$).
4. **Evaluating $\lim_{h\to0}(2x + h) = 2x$** is valid by the continuity of polynomials in the variable $h$.

---

## 6. Final Answer in Words
Using the definition of the derivative, we form the difference quotient $\frac{(x+h)^2 - x^2}{h} = \frac{x^2 + 2xh + h^2 - x^2}{h} = \frac{2xh + h^2}{h}$. Factoring out $h$ gives $\frac{h(2x + h)}{h}$, which simplifies to $2x + h$ for $h \neq 0$. Taking the limit as $h \to 0$ evaluates to $2x + 0 = 2x$. This result agrees perfectly with the Power Rule $\frac{d}{dx}[x^2] = 2x^{2-1} = 2x$. The limit is formally applied in the final step where $h$ is set to 0, which is made possible by the algebraic cancellation of $h$ that eliminates the initial $0/0$ division by zero.

---

## 7. Quick Verification
- Compute for $x = 3$:
  - By formula: $f'(3) = 2(3) = 6$.
  - By difference quotient with $h = 0.01$:
    $$\frac{f(3 + 0.01) - f(3)}{0.01} = \frac{3.01^2 - 3^2}{0.01} = \frac{9.0601 - 9}{0.01} = \frac{0.0601}{0.01} = 6.01 \approx 6.0.$$
  - With $h = 0.0001$:
    $$\frac{3.0001^2 - 9}{0.0001} = \frac{9.00060001 - 9}{0.0001} = 6.0001 \approx 6.0.$$
  The numerical secant slopes converge to $6.0$.

---

## 8. Common Mistakes to Avoid
- **Setting $h = 0$ too early:** Writing $\frac{(x+0)^2 - x^2}{0} = \frac{0}{0}$ and stopping, claiming the derivative does not exist.
- **Incorrect binomial expansion:** Writing $(x + h)^2 = x^2 + h^2$, forgetting the cross term $2xh$.
- **Dropping the limit sign prematurely:** Writing $\frac{(x+h)^2 - x^2}{h} = 2x$ without showing the intermediate step $2x + h$ and the limit $h \to 0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Starting with the definition of the derivative, we set up the difference quotient $[(x+h)^2 - x^2]/h$ and expand the numerator to get $(x^2 + 2xh + h^2 - x^2)/h$. The $x^2$ terms cancel out, leaving $(2xh + h^2)/h$, which factors and cancels $h$ to become $2x + h$ for all $h \neq 0$. Taking the limit as $h$ goes to 0 evaluates to $2x$, rigorously proving the Power Rule from first principles by removing the division by zero before evaluating the limit.
