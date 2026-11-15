# Problem 11 Solution: An n-th Root Limit and Exponential Dominance

## 1. Original Problem
Compute the limit of the sequence:
$$\lim_{n\to\infty} \sqrt[n]{5^n + 2^n}.$$
Explain which term dominates the sum under the radical, why it dominates, and why the algebraic transformation needed here is structurally different from the case of a quotient of polynomials.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the indeterminate form $\left[\infty^0\right]$ arising from the expression $(5^n + 2^n)^{1/n}$.
2. Compare the exponential growth rates of $5^n$ and $2^n$ to identify the dominant term.
3. Factor out the dominant base $5^n$ from under the radical.
4. Calculate the finite limit value using power rules and the Squeeze Theorem.
5. Contrast factoring an $n$-th root of exponential sums with factoring dominant powers in rational polynomials.

---

## 3. Key Concepts and Theorems
1. **Dominant Exponential Growth:**
   For any two bases $b > a > 0$:
   $$\lim_{n\to\infty} \left(\frac{a}{b}\right)^n = 0.$$
   Therefore, as $n \to \infty$, $a^n$ becomes completely negligible compared to $b^n$:
   $$b^n + a^n = b^n \left(1 + \left(\frac{a}{b}\right)^n\right) \approx b^n.$$
2. **Elementary $n$-th Root Limit:**
   For any constant $c > 0$:
   $$\lim_{n\to\infty} \sqrt[n]{c} = \lim_{n\to\infty} c^{1/n} = c^0 = 1.$$
3. **The Squeeze Theorem for $n$-th Roots:**
   For any positive terms $0 < a \le b$:
   $$b^n < a^n + b^n \le 2 b^n \implies \sqrt[n]{b^n} < \sqrt[n]{a^n + b^n} \le \sqrt[n]{2 b^n} \implies b < \sqrt[n]{a^n + b^n} \le b \sqrt[n]{2}.$$
   Since $\lim_{n\to\infty} b\sqrt[n]{2} = b \cdot 1 = b$, the limit is strictly $b$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Dominant Term
Examine the two exponential terms under the radical:
$$5^n \quad \text{and} \quad 2^n.$$
Since $5 > 2$, the base $5$ grows much faster than $2$.
Look at the ratio:
$$\frac{2^n}{5^n} = \left(\frac{2}{5}\right)^n = (0.4)^n.$$
Since $0 < 0.4 < 1$, as $n \to \infty$:
$$\lim_{n\to\infty} \left(\frac{2}{5}\right)^n = 0.$$
This proves that $5^n$ is the **dominant term**, while $2^n$ is asymptotically negligible.

### Step 2: Factor the Dominant Term Out of the Radical
Factor $5^n$ inside the $n$-th root:
$$\sqrt[n]{5^n + 2^n} = \sqrt[n]{5^n \left(1 + \frac{2^n}{5^n}\right)} = \sqrt[n]{5^n \left(1 + \left(\frac{2}{5}\right)^n\right)}.$$
Using the radical product rule $\sqrt[n]{A \cdot B} = \sqrt[n]{A} \cdot \sqrt[n]{B}$:
$$= \sqrt[n]{5^n} \cdot \sqrt[n]{1 + \left(\frac{2}{5}\right)^n}.$$
Since $5 > 0$, $\sqrt[n]{5^n} = (5^n)^{1/n} = 5^{n/n} = 5^1 = 5$:
$$= 5 \cdot \left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n}.$$

### Step 3: Evaluate the Limit of the Remaining Factor
Let us evaluate the limit of the second factor using the Squeeze Theorem:
1. For all $n \ge 1$, because $(2/5)^n > 0$:
   $$1 < 1 + \left(\frac{2}{5}\right)^n \le 1 + \frac{2}{5} = \frac{7}{5} < 2.$$
2. Taking the $n$-th root preserves the inequalities:
   $$\sqrt[n]{1} < \sqrt[n]{1 + \left(\frac{2}{5}\right)^n} < \sqrt[n]{2}$$
   $$1 < \left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n} < \sqrt[n]{2}.$$
3. Since $\lim_{n\to\infty} 1 = 1$ and $\lim_{n\to\infty} \sqrt[n]{2} = 2^0 = 1$, by the Squeeze Theorem:
   $$\lim_{n\to\infty} \left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n} = 1.$$

### Step 4: Compute the Final Limit
Combine the factors:
$$\lim_{n\to\infty} \sqrt[n]{5^n + 2^n} = 5 \cdot \lim_{n\to\infty} \left(1 + \left(\frac{2}{5}\right)^n\right)^{1/n} = 5 \cdot 1 = 5.$$

---

### Step 5: Why This Transformation Is Structurally Different from Polynomial Quotients
1. **Algebraic Nature of the Dominance:**
   - In a **polynomial quotient** $\frac{P(n)}{Q(n)}$, dominance is determined by polynomial power laws ($n^k$). We factor out powers of $n$ from both numerator and denominator so they cancel, leaving a constant ratio.
   - In an **$n$-th root of exponentials**, we are dealing with base growth $b^n$. We do not have a fraction to cancel; instead, we have an outer root $1/n$ that exactly neutralizes the inner exponent $n$ of the dominant base:
     $$\sqrt[n]{b^n} = (b^n)^{1/n} = b.$$
2. **The Role of the Outer Operation:**
   - In polynomial fractions, dividing by $n^k$ leaves terms like $\frac{c}{n} \to 0$ in the denominator, which sum to a non-zero constant ($b_0$).
   - In an $n$-th root, factoring pulls a pure constant $5$ completely outside the radical, while the inner part $(1 + 0.4^n) \to 1$. Then the outer exponent $1/n \to 0$ acts on $1$, yielding $1^0 = 1$. The outer $1/n$ exponent and the inner $n$ exponent are tightly coupled, which never occurs in rational polynomial quotients.

---

## 5. Why Each Step Is Valid
1. **Factoring $5^n$ from a sum** is valid by distributivity: $5^n + 2^n = 5^n(1 + (2/5)^n)$.
2. **$\sqrt[n]{5^n} = 5$** holds unconditionally for any positive real base.
3. **The Squeeze Theorem** applies because $1 < 1 + (2/5)^n \le 2$ traps the $n$-th root between $1$ and $\sqrt[n]{2} \to 1$.

---

## 6. Final Answer in Words
The limit of the sequence is $\lim_{n\to\infty} \sqrt[n]{5^n + 2^n} = 5$. The term $5^n$ dominates because its base $5$ is larger than $2$, meaning the ratio $(2/5)^n$ vanishes to zero as $n \to \infty$. The transformation is structurally different from a polynomial quotient because rather than canceling like powers between numerator and denominator, the $n$-th root $(1/n)$ directly neutralizes the $n$-th power of the factored dominant base ($5^n)^{1/n} = 5$, while the remaining factor $(1 + (2/5)^n)^{1/n}$ converges to $1^0 = 1$.

---

## 7. Quick Verification
- For $n = 1$: $\sqrt[1]{5^1 + 2^1} = 7$.
- For $n = 2$: $\sqrt{5^2 + 2^2} = \sqrt{25 + 4} = \sqrt{29} \approx 5.385$.
- For $n = 5$: $\sqrt[5]{3125 + 32} = \sqrt[5]{3157} \approx 5.020$.
- For $n = 10$: $\sqrt[10]{5^{10} + 2^{10}} = \sqrt[10]{9765625 + 1024} \approx 5.000105$.
- For $n = 100$: $\approx 5.0000000000$.
The terms decrease monotonically toward the limit $5$.

---

## 8. Common Mistakes to Avoid
- **Distributing the $n$-th root across the sum:** Writing $\sqrt[n]{5^n + 2^n} = \sqrt[n]{5^n} + \sqrt[n]{2^n} = 5 + 2 = 7$, which is completely false since $\sqrt[n]{A+B} \neq \sqrt[n]{A} + \sqrt[n]{B}$.
- **Believing the answer is $5 + 2 = 7$:** As shown above, this error stems from invalid radical distribution.
- **Applying polynomial techniques:** Trying to divide by $n^2$ or apply l'Hôpital's rule directly, which leads to complicated and unnecessary algebra.

---

## 9. Classroom Presentation (3-Sentence Summary)
Because 5 is strictly greater than 2, the term $5^n$ grows much faster than $2^n$, allowing us to factor $5^n$ out of the radical as $5 \cdot \sqrt[n]{1 + (2/5)^n}$. The ratio $(2/5)^n$ decays to 0, trapping the radical between 1 and $\sqrt[n]{2}$, both of which approach 1 as $n$ goes to infinity by the Squeeze Theorem. This proves that the limit equals 5, showing that an $n$-th root of an exponential sum is always determined entirely by the largest base.
