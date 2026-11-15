# Problem 11: Strategic Method Selection and Evaluation

## 1. Original Problem
For each integral, first write which method you choose and how you recognize it, and then compute:
1. $\int\sin(3x)\,dx$,
2. $\int x\ln x\,dx$,
3. $\int\frac{x}{\sqrt{x^2+1}}\,dx$.

---

## 2. What We Are Trying to Find
For each of the three integrals:
1. The identification of the optimal integration method (e.g., linear substitution, integration by parts, algebraic substitution).
2. The exact structural clues in the integrand that dictate this choice.
3. The step-by-step evaluation of the integral.
4. Verification by differentiation.

---

## 3. Key Concepts and Theorems
1. **Linear Argument Substitution:**
   When the argument of an elementary function is linear $g(x) = ax + b$, substitution $u = ax + b$ introduces a simple scalar factor $\frac{1}{a}$:
   $$\int f(ax + b)\,dx = \frac{1}{a}F(ax + b) + C.$$
2. **LIATE Rule for Integration by Parts:**
   When integrating a product of algebraic and logarithmic functions, choose:
   - $u = \ln x$ (Logarithmic comes first in LIATE, differentiating to $\frac{1}{x}$).
   - $dv = x\,dx$ (Algebraic integrated to $\frac{x^2}{2}$).
3. **Chain Rule Substitution $\int f(g(x))g'(x)\,dx$:**
   When an expression $g(x)$ is nested inside a root or power, and its derivative $g'(x)$ appears outside up to a constant scalar, substitution $u = g(x)$ converts it into a basic power integral.

---

## 4. Detailed Step-by-Step Solution

### Part 1: $\int\sin(3x)\,dx$

#### Method and Recognition:
- **Chosen Method:** Linear substitution (or mental reversal of the chain rule).
- **How it is recognized:** The trigonometric sine function contains a linear argument $3x$. The derivative of $3x$ is the constant $3$. Because constants can be factored in and out of integrals freely, this is a standard linear substitution.

#### Computation:
Let:
$$u = 3x \implies du = 3\,dx \iff dx = \frac{1}{3}du.$$
Substitute into the integral:
$$\int\sin(3x)\,dx = \int\sin(u) \cdot \left(\frac{1}{3}du\right) = \frac{1}{3}\int\sin(u)\,du.$$
Since $\int\sin(u)\,du = -\cos(u) + C$:
$$= -\frac{1}{3}\cos(u) + C_1 = -\frac{1}{3}\cos(3x) + C_1.$$

#### Verification:
$$\frac{d}{dx}\left[-\frac{1}{3}\cos(3x)\right] = -\frac{1}{3}\left(-\sin(3x) \cdot 3\right) = \sin(3x).$$

---

### Part 2: $\int x\ln x\,dx$

#### Method and Recognition:
- **Chosen Method:** Integration by parts.
- **How it is recognized:** The integrand is a product of two dissimilar functions: an algebraic monomial ($x$) and a transcendental logarithm ($\ln x$). Differentiating $\ln x$ turns it into the algebraic fraction $1/x$, which eliminates the transcendental nature and allows combination with powers of $x$. According to the LIATE hierarchy, logarithms must be assigned to $u$.

#### Computation:
Set up the parts:
$$u = \ln x \implies du = \frac{1}{x}\,dx,$$
$$dv = x\,dx \implies v = \int x\,dx = \frac{x^2}{2}.$$
Apply the integration-by-parts formula $\int u\,dv = uv - \int v\,du$:
$$\int x\ln x\,dx = (\ln x)\left(\frac{x^2}{2}\right) - \int \left(\frac{x^2}{2}\right)\left(\frac{1}{x}\right)\,dx$$
$$= \frac{x^2}{2}\ln x - \frac{1}{2}\int x\,dx.$$
Integrating the remaining linear term:
$$= \frac{x^2}{2}\ln x - \frac{1}{2}\left(\frac{x^2}{2}\right) + C_2$$
$$= \frac{x^2}{2}\ln x - \frac{x^2}{4} + C_2 \quad \left(\text{or } \frac{x^2}{4}(2\ln x - 1) + C_2\right).$$

#### Verification:
Using the product rule on $\frac{x^2}{2}\ln x$:
$$\frac{d}{dx}\left[\frac{x^2}{2}\ln x - \frac{x^2}{4}\right] = \left(\frac{2x}{2}\ln x + \frac{x^2}{2} \cdot \frac{1}{x}\right) - \frac{2x}{4} = x\ln x + \frac{x}{2} - \frac{x}{2} = x\ln x.$$

---

### Part 3: $\int\frac{x}{\sqrt{x^2+1}}\,dx$

#### Method and Recognition:
- **Chosen Method:** Integration by substitution.
- **How it is recognized:** The denominator contains the quadratic radicand $x^2 + 1$. The numerator contains $x\,dx$. Because $\frac{d}{dx}(x^2 + 1) = 2x$, the derivative of the inner function is proportional to the numerator factor $x\,dx$. This is the signature structure of substitution.

#### Computation:
Let:
$$u = x^2 + 1 \implies du = 2x\,dx \iff x\,dx = \frac{1}{2}du.$$
Express the square root as a negative fractional power $u^{-1/2}$:
$$\int\frac{x}{\sqrt{x^2+1}}\,dx = \int \frac{1}{\sqrt{u}} \cdot \left(\frac{1}{2}du\right) = \frac{1}{2}\int u^{-1/2}\,du.$$
Apply the power rule with exponent $-1/2$:
$$= \frac{1}{2} \cdot \frac{u^{-1/2 + 1}}{-\frac{1}{2} + 1} + C_3 = \frac{1}{2} \cdot \frac{u^{1/2}}{\frac{1}{2}} + C_3 = u^{1/2} + C_3 = \sqrt{u} + C_3.$$
Back-substitute $u = x^2 + 1$:
$$\sqrt{x^2 + 1} + C_3.$$

#### Verification:
Differentiating $\sqrt{x^2 + 1} = (x^2 + 1)^{1/2}$ via the Chain Rule:
$$\frac{d}{dx}\left[\sqrt{x^2 + 1}\right] = \frac{1}{2}(x^2 + 1)^{-1/2} \cdot 2x = \frac{x}{\sqrt{x^2 + 1}}.$$

---

## 5. Why Each Step Is Valid
- **Part 1:** Linear substitutions scale the differential by $1/a$ without altering the form of the antiderivative.
- **Part 2:** Differentiating $\ln x$ produces $1/x$, reducing the degree of the integrand polynomial in the second integral.
- **Part 3:** The inner quadratic expression's derivative is degree $1$, perfectly matching the degree of the multiplying numerator.

---

## 6. Final Answer in Words
1. For $\int\sin(3x)\,dx$, **linear substitution** ($u = 3x$) is chosen because the argument is linear; the result is:
   $$-\frac{1}{3}\cos(3x) + C.$$
2. For $\int x\ln x\,dx$, **integration by parts** ($u = \ln x, dv = x\,dx$) is chosen because differentiating $\ln x$ simplifies the product into a pure power; the result is:
   $$\frac{x^2}{2}\ln x - \frac{x^2}{4} + C.$$
3. For $\int\frac{x}{\sqrt{x^2+1}}\,dx$, **algebraic substitution** ($u = x^2 + 1$) is chosen because the numerator contains the derivative of the radicand up to a constant; the result is:
   $$\sqrt{x^2 + 1} + C.$$

---

## 7. Quick Verification
All three antiderivatives have been verified by direct differentiation:
1. $\left(-\frac{1}{3}\cos(3x)\right)' = \sin(3x)$.
2. $\left(\frac{x^2}{2}\ln x - \frac{x^2}{4}\right)' = x\ln x$.
3. $\left(\sqrt{x^2 + 1}\right)' = \frac{x}{\sqrt{x^2+1}}$.

---

## 8. Common Mistakes to Avoid
- **Attempting substitution on $x\ln x$:** Trying $u = \ln x$ yields $du = \frac{1}{x}\,dx$, which would require $x^2 du$, failing to simplify.
- **Forgetting the inner derivative factor $\frac{1}{3}$:** Writing $-\cos(3x)$ without dividing by $3$.
- **Attempting trigonometric substitution for Part 3:** Setting $x = \tan\theta$ works, but is vastly more complicated than the direct $u$-substitution $u = x^2 + 1$.

---

## 9. Classroom Presentation (3-Sentence Summary)
We select our integration methods based purely on structure: linear substitution for $\sin(3x)$ because the inner argument is linear; integration by parts for $x\ln x$ because differentiating $\ln x$ converts the product into an elementary polynomial; and substitution $u = x^2 + 1$ for $x/\sqrt{x^2+1}$ because the numerator supplies the derivative of the radicand. Evaluating these produces $-\frac{1}{3}\cos(3x) + C$, $\frac{x^2}{2}\ln x - \frac{x^2}{4} + C$, and $\sqrt{x^2+1} + C$, respectively. Differentiating each result confirms our method choices and verifies all three solutions.
