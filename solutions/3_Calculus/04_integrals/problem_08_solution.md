# Problem 08: Strategic Selection of Factors in Integration by Parts

## 1. Original Problem
Compute
$$\int x\cos x\,dx.$$
Before calculating, justify why it is convenient to differentiate $x$ and integrate $\cos x$, rather than the other way around.

---

## 2. What We Are Trying to Find
1. A rigorous comparative justification explaining why differentiating $x$ and integrating $\cos x$ is the only productive strategy.
2. An explicit demonstration of what goes wrong if the opposite assignment is chosen.
3. The step-by-step computation of $\int x\cos x\,dx$ using the integration-by-parts formula.
4. Verification of the resulting antiderivative by differentiation.

---

## 3. Key Concepts and Theorems
1. **Integration-by-Parts Formula:**
   $$\int u\,dv = uv - \int v\,du.$$
2. **Criterion for Success in Integration by Parts:**
   The goal is to produce a new integral $\int v\,du$ that is strictly simpler than the original integral $\int u\,dv$.
   - Differentiating an algebraic polynomial $x^n$ decreases its degree: $\frac{d}{dx}(x) = 1$.
   - Integrating or differentiating sinusoidal functions ($\sin x, \cos x$) cycles between them without changing complexity.
3. **Product Rule for Verification:**
   $$\frac{d}{dx}(f \cdot g) = f' g + f g'.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Justify the choice of factors before calculating
We consider the two possible assignments for the integrand $x \cos x\,dx$:

- **Recommended Assignment ($u = x$ and $dv = \cos x\,dx$):**
  - Differentiating $u = x$ yields $du = dx$, reducing the algebraic power from $1$ to $0$ (a simple constant).
  - Integrating $dv = \cos x\,dx$ yields $v = \sin x$, which remains at the same level of complexity.
  - The resulting integral is $\int v\,du = \int \sin x\,dx$, which is an elementary integral that can be evaluated immediately.

- **Opposite Assignment ($u = \cos x$ and $dv = x\,dx$):**
  - Differentiating $u = \cos x$ gives $du = -\sin x\,dx$ (no simplification).
  - Integrating $dv = x\,dx$ gives $v = \frac{x^2}{2}$.
  - The resulting integral becomes:
    $$\int v\,du = \int \frac{x^2}{2}(-\sin x)\,dx = -\frac{1}{2} \int x^2 \sin x\,dx.$$
  - This new integral is **strictly worse** than the original: the power of $x$ has grown from $1$ to $2$. Evaluating it would now require two further steps of integration by parts.

**Conclusion:** Differentiating $x$ and integrating $\cos x$ actively reduces the algebraic complexity, whereas the opposite choice escalates it.

### Step 2: Set up the components
Following our justified choice:
$$u = x \implies du = dx,$$
$$dv = \cos x\,dx \implies v = \int \cos x\,dx = \sin x.$$

### Step 3: Apply the integration-by-parts formula
Substitute into $\int u\,dv = uv - \int v\,du$:
$$\int x\cos x\,dx = x \sin x - \int \sin x\,dx.$$
Since $\int \sin x\,dx = -\cos x$:
$$\int x\cos x\,dx = x \sin x - (-\cos x) + C.$$
Simplifying the signs:
$$x \sin x + \cos x + C.$$

### Step 4: Verify the result by differentiation
We differentiate $F(x) = x \sin x + \cos x + C$ with respect to $x$:
$$F'(x) = \frac{d}{dx}(x \sin x) + \frac{d}{dx}(\cos x) + \frac{d}{dx}(C).$$
Applying the product rule to $x \sin x$:
$$\frac{d}{dx}(x \sin x) = \frac{d}{dx}(x) \cdot \sin x + x \cdot \frac{d}{dx}(\sin x) = 1 \cdot \sin x + x \cos x.$$
The derivative of $\cos x$ is $-\sin x$:
$$\frac{d}{dx}(\cos x) = -\sin x.$$
Combining these:
$$F'(x) = (\sin x + x \cos x) - \sin x + 0 = x \cos x.$$
The terms $+\sin x$ and $-\sin x$ cancel exactly, leaving $x \cos x$, which verifies the solution.

---

## 5. Why Each Step Is Valid
- **Step 1:** The utility of integration by parts depends entirely on making the remaining integral $\int v\,du$ simpler; evaluating both directions demonstrates why one works and the other fails.
- **Step 2:** Standard derivatives and antiderivatives of elementary functions: $(x)' = 1$ and $\int \cos x\,dx = \sin x$.
- **Step 3:** The integration-by-parts formula correctly accounts for the signs, with the double negative $-(- \cos x)$ turning positive.
- **Step 4:** Product rule differentiation confirms that the derivative of the combined expression reduces to the original integrand.

---

## 6. Final Answer in Words
It is convenient to differentiate $x$ because its derivative is $1$, which eliminates the polynomial factor, while integrating $\cos x$ produces $\sin x$ without escalating complexity. The reverse choice would increase the power of $x$ to $x^2$, making the problem harder. 
Applying integration by parts with $u = x$ and $dv = \cos x\,dx$ gives:
$$\int x\cos x\,dx = x\sin x - \int \sin x\,dx = x\sin x + \cos x + C, \quad C \in \mathbb{R}.$$
Differentiating $x\sin x + \cos x$ yields $(1\cdot \sin x + x\cos x) - \sin x = x\cos x$, confirming the result.

---

## 7. Quick Verification
- At $x = 0$:
  Integrand: $f(0) = 0 \cdot \cos 0 = 0$.
  Derivative: $F'(0) = 0 \cdot \cos 0 = 0$.
- At $x = \pi$:
  Integrand: $f(\pi) = \pi \cos \pi = \pi(-1) = -\pi$.
  Antiderivative derivative: $F'(\pi) = \sin\pi + \pi\cos\pi - \sin\pi = \pi(-1) = -\pi$.
Matches.

---

## 8. Common Mistakes to Avoid
- **Sign error with trigonometric antiderivatives:** Writing $\int \sin x\,dx = \cos x$, which results in an incorrect sign: $x\sin x - \cos x$. Remember that $\int \sin x\,dx = -\cos x$, so $- (-\cos x) = +\cos x$.
- **Choosing $dv = x\,dx$:** Failing to realize that integrating polynomials increases their power.
- **Forgetting the $+ C$:** Omitting the integration constant for an indefinite integral.

---

## 9. Classroom Presentation (3-Sentence Summary)
We differentiate $x$ rather than $\cos x$ because the derivative of $x$ is $1$, which eliminates the variable, whereas integrating $x$ would mistakenly increase its power to $x^2/2$. Setting $u = x$ and $dv = \cos x\,dx$ yields $x\sin x - \int \sin x\,dx$, where the integral of sine gives $-\cos x$. The resulting antiderivative is $x\sin x + \cos x + C$, which upon differentiation produces an exact cancellation that leaves $x\cos x$.
