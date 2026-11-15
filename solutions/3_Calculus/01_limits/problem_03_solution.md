# Problem 3 Solution: A Square Root and Removing an Indeterminate Form

## 1. Original Problem
Compute the limit of the sequence:
$$\lim_{n\to\infty} \left(\sqrt{n^2 + 5n} - n\right).$$
Use multiplication by the conjugate expression, and explain in detail why this algebraic transformation successfully removes the mathematical difficulty of the indeterminate form.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the indeterminate form $[\infty - \infty]$ arising from direct substitution.
2. Apply the algebraic identity $(a - b)(a + b) = a^2 - b^2$ to rationalize the expression.
3. Factor out the leading power of $n$ from the resulting fraction.
4. Calculate the finite limit value.
5. Explain conceptually why subtracting two quantities that both tend to infinity cannot be evaluated by naive subtraction, and how the conjugate transforms difference into a manageable quotient.

---

## 3. Key Concepts and Theorems
1. **The Indeterminate Form $[\infty - \infty]$:**
   Infinity is not a real number; expressions of the form $\lim (a_n - b_n)$ where $a_n \to \infty$ and $b_n \to \infty$ can evaluate to any real number, $+\infty$, $-\infty$, or diverge by oscillation.
2. **Difference of Squares Identity (Conjugation):**
   $$a - b = \frac{(a - b)(a + b)}{a + b} = \frac{a^2 - b^2}{a + b} \quad (\text{for } a + b \neq 0).$$
   Applying this with $a = \sqrt{n^2 + 5n}$ and $b = n$ squares away the radical sign.
3. **Square Root Factoring:**
   For $n > 0$:
   $$\sqrt{n^2 + 5n} = \sqrt{n^2 \left(1 + \frac{5}{n}\right)} = \sqrt{n^2} \sqrt{1 + \frac{5}{n}} = n\sqrt{1 + \frac{5}{n}}.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Indeterminate Form
As $n \to \infty$:
- $\sqrt{n^2 + 5n} \to \sqrt{\infty} = \infty$
- $n \to \infty$
The limit has the indeterminate form:
$$[\infty - \infty].$$
We cannot simply write $\infty - \infty = 0$ because the two terms grow at subtly different rates.

### Step 2: Multiply and Divide by the Conjugate
The conjugate of $\left(\sqrt{n^2 + 5n} - n\right)$ is $\left(\sqrt{n^2 + 5n} + n\right)$.
Multiply and divide the expression by this conjugate:
$$\sqrt{n^2 + 5n} - n = \frac{\left(\sqrt{n^2 + 5n} - n\right)\left(\sqrt{n^2 + 5n} + n\right)}{\sqrt{n^2 + 5n} + n}.$$

### Step 3: Simplify the Numerator
Apply the difference of squares identity $(a - b)(a + b) = a^2 - b^2$:
$$\left(\sqrt{n^2 + 5n}\right)^2 - n^2 = (n^2 + 5n) - n^2 = 5n.$$
The expression becomes:
$$\frac{5n}{\sqrt{n^2 + 5n} + n}.$$

### Step 4: Factor Out $n$ from the Denominator
Since $n > 0$, we have $\sqrt{n^2} = n$. Factor $n^2$ out from inside the radical:
$$\sqrt{n^2 + 5n} = \sqrt{n^2 \left(1 + \frac{5}{n}\right)} = n\sqrt{1 + \frac{5}{n}}.$$
Substitute this into the denominator:
$$\sqrt{n^2 + 5n} + n = n\sqrt{1 + \frac{5}{n}} + n = n\left(\sqrt{1 + \frac{5}{n}} + 1\right).$$

### Step 5: Cancel the Factor $n$ and Compute the Limit
Substitute the factored denominator back into the fraction:
$$\frac{5n}{n\left(\sqrt{1 + \frac{5}{n}} + 1\right)} = \frac{5}{\sqrt{1 + \frac{5}{n}} + 1}.$$
Now take the limit as $n \to \infty$:
$$\lim_{n\to\infty} \frac{5}{n} = 0 \implies \lim_{n\to\infty} \sqrt{1 + \frac{5}{n}} = \sqrt{1 + 0} = 1.$$
Therefore:
$$\lim_{n\to\infty} \frac{5}{\sqrt{1 + \frac{5}{n}} + 1} = \frac{5}{1 + 1} = \frac{5}{2} = 2.5.$$

---

### Step 6: Why This Transformation Removes the Difficulty
- **The Core Problem:** In the original form $\sqrt{n^2 + 5n} - n$, both terms grow roughly proportionally to $n$. Their leading terms $n - n$ cancel each other out, but the "residual difference" is hidden under a square root, creating the fragile $[\infty - \infty]$ cancellation.
- **How Conjugation Resolves It:** The identity $(a - b)(a + b) = a^2 - b^2$ forces the square of the radical:
  $$(\sqrt{n^2 + 5n})^2 - n^2 = n^2 + 5n - n^2 = 5n.$$
  The leading quadratic terms $n^2$ subtract cleanly, exposing the previously hidden linear growth $5n$ in the numerator.
- Meanwhile, the minus sign in the denominator is replaced by an addition sign: $\sqrt{n^2 + 5n} + n$. Two positive infinities added together do **not** compete; they reinforce each other to form a stable denominator of order $2n$.
- This converts an unstable subtraction $[\infty - \infty]$ into a standard quotient of dominant terms $\frac{5n}{2n}$, which evaluates directly to $\frac{5}{2}$.

---

## 5. Why Each Step Is Valid
1. **Multiplying by $\frac{a+b}{a+b} = 1$** leaves the numerical value unchanged because $\sqrt{n^2 + 5n} + n > 0$ for all $n \ge 1$.
2. **$( \sqrt{A} )^2 = A$** holds because $n^2 + 5n > 0$ for all positive integers $n$.
3. **$\sqrt{n^2} = |n| = n$** is strictly valid because sequence indices satisfy $n \ge 1 > 0$.

---

## 6. Final Answer in Words
The limit of the sequence is $\lim_{n\to\infty} \left(\sqrt{n^2 + 5n} - n\right) = \frac{5}{2} = 2.5$. Multiplying by the conjugate expression removes the difficulty because it squares away the radical, allowing the dominant $n^2$ terms to cancel out cleanly in the numerator and revealing the linear term $5n$. Simultaneously, the denominator becomes a sum of two positively reinforcing infinite terms of order $2n$, yielding the stable ratio $\frac{5n}{2n} = \frac{5}{2}$.

---

## 7. Quick Verification
- For $n = 10$: $\sqrt{100 + 50} - 10 = \sqrt{150} - 10 \approx 12.2474 - 10 = 2.2474$.
- For $n = 100$: $\sqrt{10000 + 500} - 100 = \sqrt{10500} - 100 \approx 102.4695 - 100 = 2.4695$.
- For $n = 1000$: $\sqrt{10^6 + 5000} - 1000 = \sqrt{1005000} - 1000 \approx 1002.4969 - 1000 = 2.4969$.
- As $n \to \infty$, the sequence values approach $2.5$ with great precision.
- **Taylor expansion check:**
  $$\sqrt{n^2 + 5n} - n = n\sqrt{1 + \frac{5}{n}} - n = n\left(1 + \frac{1}{2}\frac{5}{n} + \mathcal{O}\left(\frac{1}{n^2}\right)\right) - n = \frac{5}{2} + \mathcal{O}\left(\frac{1}{n}\right) \to \frac{5}{2}.$$
  Verified completely.

---

## 8. Common Mistakes to Avoid
- **Naive distribution of the radical:** Writing $\sqrt{n^2 + 5n} = \sqrt{n^2} + \sqrt{5n} = n + \sqrt{5n}$, which is mathematically false because $\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$.
- **Assuming $\infty - \infty = 0$:** Concluding the limit is 0 without calculation.
- **Sign error in the conjugate:** Writing $\sqrt{n^2 + 5n} - n$ in the denominator instead of $\sqrt{n^2 + 5n} + n$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Direct substitution produces an indeterminate form of infinity minus infinity because both terms grow at a linear rate. Multiplying and dividing by the conjugate $\sqrt{n^2 + 5n} + n$ uses the difference of squares to cancel the leading $n^2$ terms, leaving $5n$ in the numerator. Factoring $n$ from the denominator turns it into $n(\sqrt{1 + 5/n} + 1)$, which simplifies the expression to $5 / (1 + 1)$, proving that the limit equals $5/2$.
