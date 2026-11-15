# Problem 14 Solution: A 0/0 Limit with Trigonometry

## 1. Original Problem
Compute the limit of the trigonometric function:
$$\lim_{x\to0} \frac{1 - \cos x}{x^2}.$$
Rigorously justify the result **without** using l'Hôpital's rule, using a fundamental trigonometric identity (or conjugate multiplication) and the fundamental limit $\lim_{u\to0} \frac{\sin u}{u} = 1$.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the indeterminate form $\left[\frac{0}{0}\right]$ resulting from evaluating at $x = 0$.
2. Convert the difference $1 - \cos x$ into a sine-squared expression using either:
   - The half-angle identity: $1 - \cos x = 2\sin^2\left(\frac{x}{2}\right)$, or
   - Conjugate multiplication: $(1 - \cos x)(1 + \cos x) = 1 - \cos^2 x = \sin^2 x$.
3. Pair the resulting sine terms with the $x^2$ in the denominator to apply the fundamental limit $\lim_{u\to0} \frac{\sin u}{u} = 1$.
4. Calculate the exact rational limit value $\frac{1}{2}$.

---

## 3. Key Concepts and Theorems
1. **The Fundamental Trigonometric Limit:**
   $$\lim_{u\to0} \frac{\sin u}{u} = 1.$$
2. **Half-Angle Identity:**
   From the double-angle formula $\cos(2\theta) = 1 - 2\sin^2 \theta$, setting $2\theta = x \implies \theta = \frac{x}{2}$:
   $$\cos x = 1 - 2\sin^2\left(\frac{x}{2}\right) \iff 1 - \cos x = 2\sin^2\left(\frac{x}{2}\right).$$
3. **Pythagorean Identity:**
   $$\sin^2 x + \cos^2 x = 1 \iff 1 - \cos^2 x = \sin^2 x.$$
4. **Continuity of Cosine:**
   $$\lim_{x\to0} \cos x = \cos 0 = 1.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Indeterminate Form
Substitute $x = 0$ into the expression:
- Numerator: $1 - \cos 0 = 1 - 1 = 0$
- Denominator: $0^2 = 0$
We obtain the indeterminate form:
$$\left[\frac{0}{0}\right].$$

---

### Step 2: Method 1 — Using the Half-Angle Identity
1. Apply the identity $1 - \cos x = 2\sin^2\left(\frac{x}{2}\right)$:
   $$\frac{1 - \cos x}{x^2} = \frac{2\sin^2\left(\frac{x}{2}\right)}{x^2}.$$
2. We want to form the ratio $\frac{\sin(x/2)}{x/2}$. Notice that:
   $$\left(\frac{x}{2}\right)^2 = \frac{x^2}{4} \implies x^2 = 4\left(\frac{x}{2}\right)^2.$$
3. Substitute $x^2 = 4(x/2)^2$ into the denominator:
   $$\frac{2\sin^2\left(\frac{x}{2}\right)}{4\left(\frac{x}{2}\right)^2} = \frac{2}{4} \cdot \left(\frac{\sin(x/2)}{x/2}\right)^2 = \frac{1}{2} \cdot \left(\frac{\sin(x/2)}{x/2}\right)^2.$$
4. Let $u = \frac{x}{2}$. As $x \to 0$, $u \to 0$.
   Since $\lim_{u\to0} \frac{\sin u}{u} = 1$:
   $$\lim_{x\to0} \left(\frac{\sin(x/2)}{x/2}\right)^2 = 1^2 = 1.$$
5. Multiply by the constant factor:
   $$\lim_{x\to0} \frac{1 - \cos x}{x^2} = \frac{1}{2} \cdot 1 = \frac{1}{2}.$$

---

### Step 3: Method 2 — Using Conjugate Multiplication
To provide a complete algebraic picture, we also show the conjugate derivation:
1. Multiply numerator and denominator by $(1 + \cos x)$:
   $$\frac{1 - \cos x}{x^2} = \frac{(1 - \cos x)(1 + \cos x)}{x^2 (1 + \cos x)}.$$
2. Use the difference of squares and Pythagorean identity:
   $$(1 - \cos x)(1 + \cos x) = 1 - \cos^2 x = \sin^2 x.$$
3. Substitute into the fraction:
   $$= \frac{\sin^2 x}{x^2 (1 + \cos x)} = \left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x}.$$
4. Evaluate the limits of the two independent factors as $x \to 0$:
   - $\lim_{x\to0} \left(\frac{\sin x}{x}\right)^2 = 1^2 = 1$
   - $\lim_{x\to0} \frac{1}{1 + \cos x} = \frac{1}{1 + \cos 0} = \frac{1}{1 + 1} = \frac{1}{2}$
5. Multiply the two limits:
   $$\lim_{x\to0} \frac{1 - \cos x}{x^2} = 1 \cdot \frac{1}{2} = \frac{1}{2}.$$

Both methods rigorously establish that the limit is $\frac{1}{2}$ without invoking derivatives.

---

## 5. Why Each Step Is Valid
1. **The trigonometric identity $1 - \cos x = 2\sin^2(x/2)$** is an exact identity derived from the sum-of-angles formula $\cos(\alpha + \beta)$.
2. **Multiplying by $\frac{1+\cos x}{1+\cos x}$** is valid near $x = 0$ because $1 + \cos 0 = 2 \neq 0$.
3. **The limit product rule** applies because both factors have finite, well-defined limits.

---

## 6. Final Answer in Words
The limit of the function is $\lim_{x\to0} \frac{1 - \cos x}{x^2} = \frac{1}{2} = 0.5$. Using the trigonometric identity $1 - \cos x = 2\sin^2(x/2)$, the expression can be rewritten as $\frac{1}{2} \cdot \left(\frac{\sin(x/2)}{x/2}\right)^2$. Since $\frac{\sin(x/2)}{x/2} \to 1$ as $x \to 0$ by the fundamental trigonometric limit, the squared term evaluates to $1^2 = 1$, yielding the final limit of $\frac{1}{2}$. Alternatively, multiplying by the conjugate $1 + \cos x$ produces $\left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x} \to 1 \cdot \frac{1}{2} = \frac{1}{2}$.

---

## 7. Quick Verification
- **Numerical test for small values of $x$ (in radians):**
  - For $x = 0.1$:
    $$\cos(0.1) \approx 0.995004165 \implies 1 - \cos(0.1) \approx 0.004995835.$$
    $$\frac{1 - \cos(0.1)}{0.1^2} = \frac{0.004995835}{0.01} = 0.49958 \approx 0.5.$$
  - For $x = 0.01$:
    $$\cos(0.01) \approx 0.9999500004 \implies 1 - \cos(0.01) \approx 0.0000499996.$$
    $$\frac{1 - \cos(0.01)}{0.01^2} = \frac{0.0000499996}{0.0001} = 0.499996 \approx 0.5.$$
- **Taylor Series expansion check:**
  $$\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \dots \implies 1 - \cos x = \frac{x^2}{2} - \frac{x^4}{24} + \dots$$
  $$\frac{1 - \cos x}{x^2} = \frac{1}{2} - \frac{x^2}{24} + \dots \xrightarrow{x\to0} \frac{1}{2}.$$
  Verified completely.

---

## 8. Common Mistakes to Avoid
- **Forgetting the factor of $4$ in the denominator:** When setting $u = x/2$, writing $x^2 = u^2$ instead of $x^2 = 4u^2$, which leads to $2$ instead of $1/2$.
- **Canceling $\cos x$ with $x$:** Incorrectly treating $\cos x$ as a product $\cos \cdot x$.
- **Using l'Hôpital's rule when explicitly asked not to:** The problem requires justifying the result using fundamental trigonometric identities.

---

## 9. Classroom Presentation (3-Sentence Summary)
Direct substitution produces an indeterminate form of 0 over 0, which we resolve without derivatives by applying the half-angle identity $1 - \cos x = 2\sin^2(x/2)$. Rewriting the denominator as $4(x/2)^2$ isolates the squared fundamental limit term, $(2/4) \cdot [\sin(x/2) / (x/2)]^2$. Because $\sin(u)/u$ approaches 1 as $u$ goes to 0, the expression simplifies cleanly to $(1/2) \cdot 1^2 = 1/2$.
