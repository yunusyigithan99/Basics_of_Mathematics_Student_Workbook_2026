# Problem 8 Solution: A Square Root in a Function Limit

## 1. Original Problem
Compute the limit of the function at a point:
$$\lim_{x\to4} \frac{\sqrt{x} - 2}{x - 4}$$
by rationalizing the numerator. Compare the underlying algebraic mechanism with Exercise 3 (which involved a square root in a sequence limit).

---

## 2. What We Are Trying to Find
We need to:
1. Identify the indeterminate form $\left[\frac{0}{0}\right]$ resulting from evaluating at $x = 4$.
2. Multiply and divide by the conjugate expression $(\sqrt{x} + 2)$ to eliminate the radical from the numerator.
3. Cancel the zero-producing factor $(x - 4)$ under the limit condition $x \neq 4$.
4. Calculate the finite numerical limit value.
5. Draw a direct structural comparison between rationalizing a function at a finite point ($\left[\frac{0}{0}\right]$) and rationalizing a sequence at infinity ($[\infty - \infty]$).

---

## 3. Key Concepts and Theorems
1. **The Indeterminate Form $\left[\frac{0}{0}\right]$ with Radicals:**
   When an algebraic difference of square roots produces $0$ in the numerator, multiplying by the conjugate converts the difference into a difference of squares:
   $$(\sqrt{A} - B)(\sqrt{A} + B) = A - B^2.$$
2. **Rationalizing the Numerator:**
   For $x \ge 0$ and $x \neq 4$:
   $$\frac{\sqrt{x} - 2}{x - 4} = \frac{(\sqrt{x} - 2)(\sqrt{x} + 2)}{(x - 4)(\sqrt{x} + 2)} = \frac{x - 4}{(x - 4)(\sqrt{x} + 2)}.$$
3. **Continuity of the Radical Function:**
   The function $g(x) = \sqrt{x}$ is continuous at all points in its domain $x \ge 0$, meaning $\lim_{x\to 4} \sqrt{x} = \sqrt{4} = 2$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Indeterminate Form
Substitute $x = 4$ directly into the expression:
- Numerator: $\sqrt{4} - 2 = 2 - 2 = 0$
- Denominator: $4 - 4 = 0$
We obtain the indeterminate form:
$$\left[\frac{0}{0}\right].$$
The function is undefined at $x = 4$.

### Step 2: Multiply Numerator and Denominator by the Conjugate
The conjugate of the numerator $(\sqrt{x} - 2)$ is $(\sqrt{x} + 2)$.
Multiply both numerator and denominator by $(\sqrt{x} + 2)$:
$$\frac{\sqrt{x} - 2}{x - 4} = \frac{(\sqrt{x} - 2)(\sqrt{x} + 2)}{(x - 4)(\sqrt{x} + 2)}.$$

### Step 3: Expand the Numerator
Apply the difference of squares identity $(a - b)(a + b) = a^2 - b^2$:
$$(\sqrt{x} - 2)(\sqrt{x} + 2) = (\sqrt{x})^2 - 2^2 = x - 4.$$
The expression becomes:
$$\frac{x - 4}{(x - 4)(\sqrt{x} + 2)}.$$

### Step 4: Cancel the Zero-Producing Factor
Because the limit considers values of $x$ close to $4$ with $x \neq 4$, the factor $x - 4$ is strictly non-zero ($x - 4 \neq 0$).
Cancel $(x - 4)$ from the numerator and denominator:
$$\frac{x - 4}{(x - 4)(\sqrt{x} + 2)} = \frac{1}{\sqrt{x} + 2} \quad (\text{for all } x \neq 4, x \ge 0).$$

### Step 5: Evaluate the Limit
Substitute $x = 4$ into the simplified continuous expression:
$$\lim_{x\to4} \frac{1}{\sqrt{x} + 2} = \frac{1}{\sqrt{4} + 2} = \frac{1}{2 + 2} = \frac{1}{4} = 0.25.$$

---

### Step 6: Comparison with Exercise 3 (Sequence vs. Function Conjugation)

| Feature | Exercise 3 (Sequence at Infinity) | Exercise 8 (Function at a Finite Point) |
| :--- | :--- | :--- |
| **Original Expression** | $\sqrt{n^2 + 5n} - n$ as $n \to \infty$ | $\frac{\sqrt{x} - 2}{x - 4}$ as $x \to 4$ |
| **Initial Indeterminate Form** | $[\infty - \infty]$ | $\left[\frac{0}{0}\right]$ |
| **Conjugate Used** | $\sqrt{n^2 + 5n} + n$ | $\sqrt{x} + 2$ |
| **What Gets Squared Away** | $(\sqrt{n^2 + 5n})^2 - n^2 = 5n$ | $(\sqrt{x})^2 - 2^2 = x - 4$ |
| **Algebraic Mechanism** | Converts a difference of two infinite terms into a quotient of stable leading terms ($5n / 2n$). | Exposes the hidden zero-factor $(x - 4)$ in the numerator so it cancels with $(x - 4)$ in the denominator. |
| **Final Result** | $\frac{5}{2} = 2.5$ | $\frac{1}{4} = 0.25$ |

**Common Underlying Idea:**
In both problems, the square root locks a term inside a non-linear radical, preventing direct cancellation. In both cases, multiplying by $(a + b)$ uses the difference of squares identity $(a - b)(a + b) = a^2 - b^2$ to eliminate the radical sign. In Exercise 3, this reveals the dominant linear growth ($5n$); in Exercise 8, this exposes the vanishing factor $(x - 4)$. The algebraic strategy is identical.

---

## 5. Why Each Step Is Valid
1. **Multiplying by $\frac{\sqrt{x}+2}{\sqrt{x}+2} = 1$** is valid because $\sqrt{x} + 2 \ge 2 > 0$ for all $x \ge 0$, introducing no spurious zeros.
2. **Canceling $(x - 4) / (x - 4) = 1$** is valid because $x \to 4$ restricts $x$ to $0 < |x - 4| < \delta$, ensuring $x \neq 4$.
3. **Evaluating at $x = 4$** is valid because the function $\frac{1}{\sqrt{x} + 2}$ is continuous on $[0, \infty)$.

---

## 6. Final Answer in Words
The limit of the function is $\lim_{x\to4} \frac{\sqrt{x} - 2}{x - 4} = \frac{1}{4} = 0.25$. Multiplying numerator and denominator by the conjugate $(\sqrt{x} + 2)$ squares the radical to produce $(x - 4)$ in the numerator, which cancels the identical zero-factor in the denominator. This shares the exact same mathematical mechanism as Exercise 3: the difference of squares identity $(a - b)(a + b) = a^2 - b^2$ is used to eliminate a square root that conceals the true algebraic relationship.

---

## 7. Quick Verification
- **Numerical test approaching $x = 4$:**
  - For $x = 4.01$: $\frac{\sqrt{4.01} - 2}{4.01 - 4} = \frac{2.0024984 - 2}{0.01} = \frac{0.0024984}{0.01} \approx 0.24984$.
  - For $x = 3.99$: $\frac{\sqrt{3.99} - 2}{3.99 - 4} = \frac{1.9974984 - 2}{-0.01} = \frac{-0.0025016}{-0.01} \approx 0.25016$.
  Both sides tightly approach $0.25 = \frac{1}{4}$.
- **Alternative factoring check:**
  Notice that $x - 4 = (\sqrt{x})^2 - 2^2 = (\sqrt{x} - 2)(\sqrt{x} + 2)$.
  Therefore:
  $$\frac{\sqrt{x} - 2}{x - 4} = \frac{\sqrt{x} - 2}{(\sqrt{x} - 2)(\sqrt{x} + 2)} = \frac{1}{\sqrt{x} + 2} \xrightarrow{x\to 4} \frac{1}{4}.$$
  Both methods produce the exact same result.

---

## 8. Common Mistakes to Avoid
- **Inverting the fraction:** Writing the answer as $4$ instead of $\frac{1}{4}$.
- **Sign error in the conjugate:** Multiplying by $(\sqrt{x} - 2)$ instead of $(\sqrt{x} + 2)$, which squares the minus sign instead of canceling the square root.
- **Applying l'Hôpital incorrectly:** Differentiating $\sqrt{x}$ as $\frac{1}{\sqrt{x}}$ instead of $\frac{1}{2\sqrt{x}}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Direct substitution of $x = 4$ gives the indeterminate form $0/0$ because the square root of 4 equals 2. We resolve this by multiplying the numerator and denominator by the conjugate $\sqrt{x} + 2$, which turns the numerator into the difference of squares $(\sqrt{x})^2 - 2^2 = x - 4$. Canceling the common $(x - 4)$ factor leaves $1 / (\sqrt{x} + 2)$, which evaluates to $1 / (2 + 2) = 1/4$, employing the exact same difference-of-squares mechanism used to resolve the sequence limit in Exercise 3.
