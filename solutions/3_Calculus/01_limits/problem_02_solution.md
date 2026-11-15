# Problem 2 Solution: Different Growth Rates

## 1. Original Problem
Compute the limits of the two sequences:
$$L_1 = \lim_{n\to\infty} \frac{3n + 1}{n^2 + 4}, \qquad L_2 = \lim_{n\to\infty} \frac{2n^3 - n}{5n^2 + 1}.$$
Compare the two cases and formulate a general mathematical theorem regarding the relative degrees of polynomials in the numerator and denominator for rational sequences as $n \to \infty$.

---

## 2. What We Are Trying to Find
We need to:
1. Compute the limit of a sequence where the denominator's degree exceeds the numerator's degree ($L_1$).
2. Compute the limit of a sequence where the numerator's degree exceeds the denominator's degree ($L_2$).
3. Compare the growth rates of polynomials of different degrees.
4. Formulate the comprehensive 3-case rule for $\lim_{n\to\infty} \frac{P(n)}{Q(n)}$ based on $\deg(P)$ versus $\deg(Q)$.

---

## 3. Key Concepts and Theorems
1. **General Degree Rule for Rational Sequences:**
   Let $P(n) = a_p n^p + \dots$ and $Q(n) = b_q n^q + \dots$ be polynomials of degrees $p = \deg(P)$ and $q = \deg(Q)$ with leading coefficients $a_p \neq 0$ and $b_q \neq 0$. Then:
   $$\lim_{n\to\infty} \frac{P(n)}{Q(n)} = \begin{cases}
   0 & \text{if } p < q \text{ (denominator dominates)}, \\
   \frac{a_p}{b_q} & \text{if } p = q \text{ (degrees are equal)}, \\
   \pm\infty & \text{if } p > q \text{ (numerator dominates)}.
   \end{cases}$$
2. **Standard Technique:**
   Factor out the highest power of $n$ present in the denominator from both numerator and denominator.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute Limit $L_1 = \lim_{n\to\infty} \frac{3n + 1}{n^2 + 4}$
1. The highest power in the denominator is $n^2$.
2. Factor $n^2$ out of both numerator and denominator:
   $$\frac{3n + 1}{n^2 + 4} = \frac{n^2 \left(\frac{3}{n} + \frac{1}{n^2}\right)}{n^2 \left(1 + \frac{4}{n^2}\right)} = \frac{\frac{3}{n} + \frac{1}{n^2}}{1 + \frac{4}{n^2}}.$$
3. Take the limit as $n \to \infty$:
   $$\lim_{n\to\infty} \frac{3}{n} = 0, \qquad \lim_{n\to\infty} \frac{1}{n^2} = 0, \qquad \lim_{n\to\infty} \frac{4}{n^2} = 0.$$
4. Evaluate the quotient:
   $$L_1 = \frac{0 + 0}{1 + 0} = \frac{0}{1} = 0.$$
The limit is $0$.

---

### Step 2: Compute Limit $L_2 = \lim_{n\to\infty} \frac{2n^3 - n}{5n^2 + 1}$
1. The highest power in the denominator is $n^2$.
2. Factor $n^2$ out of both numerator and denominator:
   $$\frac{2n^3 - n}{5n^2 + 1} = \frac{n^2 \left(2n - \frac{1}{n}\right)}{n^2 \left(5 + \frac{1}{n^2}\right)} = \frac{2n - \frac{1}{n}}{5 + \frac{1}{n^2}}.$$
3. Alternatively, factor $n$ out of the entire fraction:
   $$= n \cdot \frac{2 - \frac{1}{n^2}}{5 + \frac{1}{n^2}}.$$
4. Take the limit as $n \to \infty$:
   $$\lim_{n\to\infty} \left(2 - \frac{1}{n^2}\right) = 2 - 0 = 2,$$
   $$\lim_{n\to\infty} \left(5 + \frac{1}{n^2}\right) = 5 + 0 = 5.$$
   Thus:
   $$\frac{2 - \frac{1}{n^2}}{5 + \frac{1}{n^2}} \to \frac{2}{5}.$$
5. Since $n \to +\infty$ and the fraction approaches the positive constant $\frac{2}{5} > 0$:
   $$L_2 = \lim_{n\to\infty} \left[ n \cdot \left(\frac{2}{5}\right) \right] = +\infty.$$
The limit is $+\infty$ (the sequence diverges to positive infinity).

---

### Step 3: Comparison and General Mathematical Observation
- In $L_1$: $\deg(\text{numerator}) = 1$ and $\deg(\text{denominator}) = 2$.
  Because $1 < 2$, the denominator grows orders of magnitude faster than the numerator ($n^2 \gg n$). The fraction is squeezed to $0$.
- In $L_2$: $\deg(\text{numerator}) = 3$ and $\deg(\text{denominator}) = 2$.
  Because $3 > 2$, the numerator grows faster than the denominator ($n^3 \gg n^2$), causing the fraction to grow without bound toward $+\infty$.

**General Formulation:**
For any rational sequence $a_n = \frac{a_p n^p + \dots + a_0}{b_q n^q + \dots + b_0}$ with $a_p, b_q \neq 0$:
1. **If $\deg(P) < \deg(Q)$ ($p < q$):** The limit is always **$0$**.
2. **If $\deg(P) = \deg(Q)$ ($p = q$):** The limit is the finite non-zero constant **$\frac{a_p}{b_q}$**.
3. **If $\deg(P) > \deg(Q)$ ($p > q$):** The limit is infinite (**$+\infty$ or $-\infty$**, with sign given by $\operatorname{sgn}(a_p / b_q)$).

---

## 5. Why Each Step Is Valid
1. **Factoring the denominator's leading power $n^2$** keeps the denominator's limit finite and non-zero ($1$ or $5$), preventing division by zero.
2. **The product limit theorem for infinite limits** ($[+\infty] \times [c > 0] = +\infty$) formally justifies that $n \cdot (2/5) \to +\infty$.
3. **The degree classification** is an exact consequence of the algebraic identity $n^p / n^q = n^{p - q}$.

---

## 6. Final Answer in Words
The first limit is $\lim_{n\to\infty} \frac{3n + 1}{n^2 + 4} = 0$, and the second limit is $\lim_{n\to\infty} \frac{2n^3 - n}{5n^2 + 1} = +\infty$. In general, when the degree of the denominator is greater than the degree of the numerator, the limit is always $0$; when the degrees are equal, the limit is the ratio of the leading coefficients; and when the degree of the numerator is strictly greater than the degree of the denominator, the sequence diverges to $\pm\infty$.

---

## 7. Quick Verification
- For $L_1$ with $n = 1000$:
  $$\frac{3(1000) + 1}{1000^2 + 4} = \frac{3001}{1000004} \approx 0.003 \approx 0.$$
- For $L_2$ with $n = 1000$:
  $$\frac{2(1000^3) - 1000}{5(1000^2) + 1} = \frac{2 \times 10^9 - 1000}{5 \times 10^6 + 1} \approx \frac{2}{5} \times 1000 = 400 \gg 1.$$
Numerical evaluations confirm the convergence to $0$ and divergence to $+\infty$.

---

## 8. Common Mistakes to Avoid
- **Writing $L_2 = 2/5$:** Forgetting the remaining factor of $n$ in the numerator and reporting only the coefficient ratio.
- **Treating $+\infty$ as non-existent without specifying divergence:** It is important to specify that the sequence diverges specifically to $+\infty$.
- **Canceling unequal powers:** Crossing out $n$ terms with different exponents without factoring.

---

## 9. Classroom Presentation (3-Sentence Summary)
Dividing the first expression by $n^2$ leaves $(3/n + 1/n^2) / (1 + 4/n^2)$, which approaches $0/1 = 0$ because the denominator's degree is strictly greater than the numerator's. For the second expression, factoring out $n^2$ leaves $n(2 - 1/n^2) / (5 + 1/n^2)$, which diverges to $+\infty$ because the numerator's cubic growth dominates the denominator's quadratic growth. In general, rational sequence limits are entirely determined by comparing polynomial degrees: $0$ when the denominator has higher degree, the ratio of leading coefficients when degrees match, and $\pm\infty$ when the numerator dominates.
