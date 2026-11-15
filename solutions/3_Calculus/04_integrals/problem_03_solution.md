# Problem 03: Recognizing Basic Antiderivatives

## 1. Original Problem
Compute
$$\int\left(2e^x + 3\cos x - 4\sin x\right)\,dx.$$
Match each term with a known derivative and verify the entire result with one differentiation.

---

## 2. What We Are Trying to Find
1. The identification of standard derivative rules corresponding to each term in the integrand.
2. The term-by-term evaluation of the indefinite integral.
3. The complete family of antiderivatives with the constant $C$.
4. A single, comprehensive differentiation step verifying the entire antiderivative.

---

## 3. Key Concepts and Theorems
1. **Catalog of Fundamental Derivatives and Their Inverses:**
   - $\frac{d}{dx}(e^x) = e^x \implies \int e^x\,dx = e^x + C$.
   - $\frac{d}{dx}(\sin x) = \cos x \implies \int \cos x\,dx = \sin x + C$.
   - $\frac{d}{dx}(\cos x) = -\sin x \implies \int \sin x\,dx = -\cos x + C$.
2. **Constant Multiple and Sum Rule of Integration:**
   For any constants $a, b, c$:
   $$\int (a f_1(x) + b f_2(x) + c f_3(x))\,dx = a \int f_1(x)\,dx + b \int f_2(x)\,dx + c \int f_3(x)\,dx.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Match each term with a known derivative
We decompose the integrand into its three elementary components and match each with a known derivative rule:
1. **Term $2e^x$:**
   Since the derivative of the natural exponential function is itself:
   $$\frac{d}{dx}(e^x) = e^x \implies \frac{d}{dx}(2e^x) = 2e^x.$$
   Therefore, an antiderivative of $2e^x$ is $2e^x$.

2. **Term $3\cos x$:**
   Since the derivative of the sine function is the cosine function:
   $$\frac{d}{dx}(\sin x) = \cos x \implies \frac{d}{dx}(3\sin x) = 3\cos x.$$
   Therefore, an antiderivative of $3\cos x$ is $3\sin x$.

3. **Term $-4\sin x$:**
   Since the derivative of the cosine function is the negative sine function:
   $$\frac{d}{dx}(\cos x) = -\sin x \implies \frac{d}{dx}(4\cos x) = 4(-\sin x) = -4\sin x.$$
   Notice that the negative sign in $-4\sin x$ is naturally absorbed by the derivative of $\cos x$.
   Therefore, an antiderivative of $-4\sin x$ is $+4\cos x$.

### Step 2: Assemble the indefinite integral
Combining the antiderivatives of all three terms by linearity and adding the integration constant $C \in \mathbb{R}$:
$$\int\left(2e^x + 3\cos x - 4\sin x\right)\,dx = 2e^x + 3\sin x + 4\cos x + C.$$

### Step 3: Verify the entire result with one differentiation
We take the entire proposed solution $F(x) = 2e^x + 3\sin x + 4\cos x + C$ and differentiate it in a single step:
$$F'(x) = \frac{d}{dx}\left(2e^x + 3\sin x + 4\cos x + C\right)$$
$$= 2 \cdot \frac{d}{dx}(e^x) + 3 \cdot \frac{d}{dx}(\sin x) + 4 \cdot \frac{d}{dx}(\cos x) + \frac{d}{dx}(C)$$
$$= 2(e^x) + 3(\cos x) + 4(-\sin x) + 0$$
$$= 2e^x + 3\cos x - 4\sin x.$$
This matches the original integrand $f(x)$ perfectly.

---

## 5. Why Each Step Is Valid
- **Step 1:** The fundamental theorem of calculus establishes that differentiation and indefinite integration are inverse operations.
- **Step 2:** Linearity allows integrating each summand independently and combining them with the original scalar coefficients.
- **Step 3:** The sum rule for derivatives applies, and the derivative of any constant is zero.

---

## 6. Final Answer in Words
Matching each term with its standard derivative gives:
- $2e^x$ comes from $2e^x$,
- $3\cos x$ comes from $3\sin x$,
- $-4\sin x$ comes from $+4\cos x$.
Summing these and appending the constant of integration yields:
$$2e^x + 3\sin x + 4\cos x + C, \quad C \in \mathbb{R}.$$
Differentiating this expression reproduces $2e^x + 3\cos x - 4\sin x$, verifying the result.

---

## 7. Quick Verification
Evaluate at $x = 0$:
- Integrand: $f(0) = 2e^0 + 3\cos 0 - 4\sin 0 = 2(1) + 3(1) - 4(0) = 5$.
- Derivative of antiderivative at $x = 0$:
  $F'(0) = 2e^0 + 3\cos 0 - 4\sin 0 = 2 + 3 - 0 = 5$.
The values match.

---

## 8. Common Mistakes to Avoid
- **Sign confusion with trigonometric antiderivatives:**
  A common mistake is writing $\int (-4\sin x)\,dx = -4\cos x$. Because $(\cos x)' = -\sin x$, we have $\int \sin x\,dx = -\cos x$, so $-4(-\cos x) = +4\cos x$.
- **Confusing $\int e^x\,dx$ with power rule:**
  Trying to write $\frac{e^{x+1}}{x+1}$, which is entirely invalid; exponential functions follow their own distinct calculus rules.

---

## 9. Classroom Presentation (3-Sentence Summary)
We integrate term by term by recognizing standard derivatives: $e^x$ is its own derivative, $\cos x$ is the derivative of $\sin x$, and $-\sin x$ is the derivative of $\cos x$. Combining these terms gives the general antiderivative $2e^x + 3\sin x + 4\cos x + C$. Differentiating the entire expression in one step confirms that the negative sign from the derivative of cosine correctly produces the original $-4\sin x$.
