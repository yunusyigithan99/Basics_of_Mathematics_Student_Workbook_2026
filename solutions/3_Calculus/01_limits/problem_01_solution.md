# Problem 1 Solution: Dominant Terms in a Sequence

## 1. Original Problem
Compute the limit of the sequence:
$$\lim_{n\to\infty} \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}.$$
Explain in detail why the highest-degree terms in the numerator and denominator determine the final result of the limit.

---

## 2. What We Are Trying to Find
We are asked to:
1. Evaluate the limit of a rational sequence as $n \to \infty$ encountering an initial indeterminate form of type $\left[\frac{\infty}{\infty}\right]$.
2. Factor out the dominant power of $n$ ($n^2$) from both numerator and denominator to resolve the indeterminacy.
3. Apply limit arithmetic rules to calculate the exact numerical value of the limit.
4. Provide a clear, conceptual explanation of why lower-order terms become negligible compared to the leading quadratic terms as $n$ grows without bound.

---

## 3. Key Concepts and Theorems
1. **Dominant Term Factoring Technique:**
   For a rational function $\frac{P(n)}{Q(n)}$ as $n \to \infty$, factoring out the highest power of $n$ present in the denominator reveals the asymptotic behavior.
2. **Elementary Limits:**
   For any real exponent $p > 0$ and any real constant $c$:
   $$\lim_{n\to\infty} \frac{c}{n^p} = 0.$$
3. **Limit Arithmetic Theorems:**
   If $\lim a_n = A$ and $\lim b_n = B \neq 0$, then:
   $$\lim \frac{a_n}{b_n} = \frac{\lim a_n}{\lim b_n} = \frac{A}{B}.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Indeterminate Form
As $n \to \infty$:
- Numerator: $4n^2 - 3n + 1 \to \infty$
- Denominator: $2n^2 + 5n - 7 \to \infty$
Direct substitution yields the indeterminate form:
$$\left[\frac{\infty}{\infty}\right].$$
We must transform the expression algebraically before computing the limit.

### Step 2: Factor Out the Highest Power of $n$
The highest power of $n$ in both numerator and denominator is $n^2$. Factor $n^2$ out of both expressions:
$$\frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} = \frac{n^2 \left(4 - \frac{3}{n} + \frac{1}{n^2}\right)}{n^2 \left(2 + \frac{5}{n} - \frac{7}{n^2}\right)}.$$

### Step 3: Cancel the Common Factor $n^2$
Since $n \to \infty$, $n \neq 0$, so we can cancel $n^2$:
$$= \frac{4 - \frac{3}{n} + \frac{1}{n^2}}{2 + \frac{5}{n} - \frac{7}{n^2}}.$$

### Step 4: Evaluate the Limits of Individual Terms
As $n \to \infty$:
$$\lim_{n\to\infty} \frac{3}{n} = 0, \qquad \lim_{n\to\infty} \frac{1}{n^2} = 0,$$
$$\lim_{n\to\infty} \frac{5}{n} = 0, \qquad \lim_{n\to\infty} \frac{7}{n^2} = 0.$$

### Step 5: Compute the Limit of the Quotient
Apply the quotient and sum limit laws:
$$\lim_{n\to\infty} \frac{4 - \frac{3}{n} + \frac{1}{n^2}}{2 + \frac{5}{n} - \frac{7}{n^2}} = \frac{4 - 0 + 0}{2 + 0 - 0} = \frac{4}{2} = 2.$$

### Step 6: Conceptual Explanation of Dominant Terms
- Consider $n = 1{,}000{,}000 = 10^6$:
  - The leading term $4n^2 = 4 \times 10^{12}$ is four trillion.
  - The linear term $-3n = -3 \times 10^6$ is minus three million.
  - The constant term is simply $1$.
  The linear and constant terms make up less than $0.0001\%$ of the total value.
- Dividing every term by the leading power $n^2$ causes all lower-degree terms to take the form $\frac{c}{n^k}$ with $k \ge 1$. As $n$ approaches infinity, these fractions shrink to absolute zero.
- Consequently, the asymptotic trajectory of the sequence is dictated exclusively by the ratio of the coefficients of the highest-degree terms:
  $$\frac{4n^2}{2n^2} = \frac{4}{2} = 2.$$

---

## 5. Why Each Step Is Valid
1. **Factoring $n^2$** is valid by the distributive property of multiplication over addition.
2. **Canceling $n^2 / n^2 = 1$** is valid because $n \ge 1 > 0$ for all sequence indices.
3. **Applying limit laws to the resulting terms** is valid because the denominator limit $2 + 0 - 0 = 2$ is non-zero, satisfying the hypothesis of the quotient limit theorem.

---

## 6. Final Answer in Words
The limit of the sequence is $\lim_{n\to\infty} \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} = 2$. The highest-degree terms determine the result because when factoring out $n^2$, all lower-order terms become fractions of the form $\frac{c}{n}$ or $\frac{c}{n^2}$, which vanish to zero as $n \to \infty$, leaving only the ratio of the leading coefficients $\frac{4}{2} = 2$.

---

## 7. Quick Verification
Evaluate the sequence numerically for large values of $n$:
- For $n = 10$:
  $$a_{10} = \frac{4(100) - 30 + 1}{2(100) + 50 - 7} = \frac{371}{243} \approx 1.5267.$$
- For $n = 100$:
  $$a_{100} = \frac{4(10000) - 300 + 1}{2(10000) + 500 - 7} = \frac{39701}{20493} \approx 1.9373.$$
- For $n = 1000$:
  $$a_{1000} = \frac{4(10^6) - 3000 + 1}{2(10^6) + 5000 - 7} = \frac{3997001}{2004993} \approx 1.9935.$$
The values increase steadily toward the theoretical limit of $2.0$.

---

## 8. Common Mistakes to Avoid
- **Evaluating as $\infty / \infty = 1$:** Treating infinity as a real number that can be canceled.
- **Ignoring lower terms incorrectly:** Crossing out terms without formally factoring out $n^2$, which leads to errors when signs or degrees differ.
- **Dividing by different powers in numerator and denominator:** Dividing numerator by $n^2$ and denominator by $n$. Both must be divided by the same power.

---

## 9. Classroom Presentation (3-Sentence Summary)
When evaluating the limit of a rational sequence as $n$ goes to infinity, we encounter an indeterminate form of infinity over infinity. By factoring out the highest power $n^2$ from both the numerator and the denominator, all lower-degree terms transform into fractions that vanish to zero. This leaves only the ratio of the leading coefficients, $4/2$, rigorously proving that the limit of the sequence is 2.
