# Problem 15 Solution: Observation Versus Proof in Limits

## 1. Original Problem
From this problem set, select:
1. One sequence, specifically:
   $$a_n = \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} \quad (\text{from Exercise 1}),$$
2. One function, specifically:
   $$f(x) = \frac{x^2 - 4x + 3}{x - 3} \quad (\text{from Exercise 7}).$$

For the sequence, compute several concrete numerical values for increasingly large indices $n$. For the function, prepare a structured table of values with arguments approaching the limit point $c = 3$ from both the left and right. Sketch and describe the geometric behavior of both objects.
Finally, compare these empirical observations with the formal analytical results, and explain in detail why a finite number of calculations or a visual sketch does not constitute a rigorous mathematical proof that a limit exists.

---

## 2. What We Are Trying to Find
We need to:
1. Calculate a table of numerical terms for $a_n$ as $n \to \infty$ showing convergence toward $L = 2$.
2. Calculate a two-sided table of values for $f(x)$ as $x \to 3^-$ and $x \to 3^+$ showing convergence toward $L = 2$.
3. Provide geometric and graphical descriptions for both objects.
4. Explain the difference between empirical observation (inductive reasoning) and mathematical proof (deductive reasoning) in the context of analysis.

---

## 3. Key Concepts and Theorems
1. **The Nature of Mathematical Induction vs. Empirical Sampling:**
   Observing that a property holds for a finite set of sample points $n \in \{1, 10, 100, 1000\}$ does not prove that it holds for all $n \in \mathbb{N}$, nor does it prove that the sequence does not deviate at $n = 10^{20}$.
2. **Formal $(\varepsilon, \delta)$ and $(\varepsilon, M)$ Definitions:**
   - A sequence converges to $L$ if $\forall \varepsilon > 0$, $\exists M$ such that $\forall n > M$, $|a_n - L| < \varepsilon$.
   - A function limit equals $L$ if $\forall \varepsilon > 0$, $\exists \delta > 0$ such that $\forall x$ with $0 < |x - c| < \delta$, $|f(x) - L| < \varepsilon$.
   A proof must verify these conditions for **all** $\varepsilon > 0$ simultaneously.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Numerical Calculations for the Sequence $a_n = \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}$
Compute values for $n = 1, 2, 5, 10, 50, 100, 1000, 10000$:

| $n$ | Numerator ($4n^2 - 3n + 1$) | Denominator ($2n^2 + 5n - 7$) | Exact Fraction | Decimal Approximation |
| :--- | :--- | :--- | :--- | :--- |
| **$1$** | $4 - 3 + 1 = 2$ | $2 + 5 - 7 = 0$ | Undefined | Division by zero |
| **$2$** | $16 - 6 + 1 = 11$ | $8 + 10 - 7 = 11$ | $\frac{11}{11}$ | **$1.000000$** |
| **$5$** | $100 - 15 + 1 = 86$ | $50 + 25 - 7 = 68$ | $\frac{86}{68}$ | **$1.264706$** |
| **$10$** | $400 - 30 + 1 = 371$ | $200 + 50 - 7 = 243$ | $\frac{371}{243}$ | **$1.526749$** |
| **$50$** | $10000 - 150 + 1 = 9851$ | $5000 + 250 - 7 = 5243$ | $\frac{9851}{5243}$ | **$1.878886$** |
| **$100$** | $39701$ | $20493$ | $\frac{39701}{20493}$ | **$1.937295$** |
| **$1000$** | $3997001$ | $2004993$ | $\frac{3997001}{2004993}$ | **$1.993523$** |
| **$10000$** | $399970001$ | $200049993$ | $\frac{399970001}{200049993}$ | **$1.999350$** |

**Observation:**
The sequence starts undefined at $n = 1$, equals $1$ at $n = 2$, and then increases steadily: $1.26 \to 1.53 \to 1.88 \to 1.94 \to 1.9935 \to 1.99935$. It appears to be approaching the value $2.0$ from below.

---

### Step 2: Numerical Calculations for the Function $f(x) = \frac{x^2 - 4x + 3}{x - 3}$
We construct a table approaching the limit point $c = 3$ from the left ($x \to 3^-$) and from the right ($x \to 3^+$):

| Approach | $x$ | Numerator ($x^2 - 4x + 3$) | Denominator ($x - 3$) | $f(x)$ Value |
| :--- | :--- | :--- | :--- | :--- |
| **From Left** | $2.9$ | $8.41 - 11.6 + 3 = -0.19$ | $-0.1$ | **$1.900000$** |
| | $2.99$ | $8.9401 - 11.96 + 3 = -0.0199$ | $-0.01$ | **$1.990000$** |
| | $2.999$ | $8.994001 - 11.996 + 3 = -0.001999$ | $-0.001$ | **$1.999000$** |
| | $2.9999$ | $-0.00019999$ | $-0.0001$ | **$1.999900$** |
| **At Point** | **$3.0$** | **$0$** | **$0$** | **Undefined ($\frac{0}{0}$)** |
| **From Right** | $3.0001$ | $+0.00020001$ | $+0.0001$ | **$2.000100$** |
| | $3.001$ | $+0.002001$ | $+0.001$ | **$2.001000$** |
| | $3.01$ | $+0.0201$ | $+0.01$ | **$2.010000$** |
| | $3.1$ | $+0.21$ | $+0.1$ | **$2.100000$** |

**Observation:**
From the left, the values rise through $1.9, 1.99, 1.999 \to 2$. From the right, the values descend through $2.1, 2.01, 2.001 \to 2$. Both sides tightly converge to $2.0$.

---

### Step 3: Graphical and Geometric Descriptions
1. **The Sequence:** Plotted on coordinate axes with $n$ on the horizontal axis and $a_n$ on the vertical axis, the points form a discrete series of dots climbing asymptotically toward the horizontal guide line $y = 2$.
2. **The Function:** Plotted on the Cartesian plane, the graph of $f(x)$ is the straight line $y = x - 1$ with a slope of $1$ and $y$-intercept at $-1$. At the point $(3, 2)$, there is a small hollow circle (a "removable hole") indicating that the point is excluded from the domain.

---

### Step 4: Comparison of Observation vs. Proof

#### Why Empirical Observation and Sketches Do Not Constitute a Proof:
1. **The Finiteness Trap:**
   A table of values evaluates only a finite sample (e.g., 8 points). In mathematics, infinity ($\infty$) cannot be reached by counting. Even evaluating $10^{100}$ terms leaves an infinite number of untested terms.
2. **False Convergence Counterexamples:**
   Consider the sequence $b_n = \frac{1}{n} + \sin\left(\frac{n\pi}{10^6}\right)$. For the first $1000$ terms, $\sin\left(\frac{n\pi}{10^6}\right) \approx 0$, and a student would see $b_n \approx \frac{1}{n} \to 0$. Yet for $n = 500{,}000$, $b_n \approx 1$. Numerical testing alone completely misses this behavior.
3. **Slow Divergence (The Harmonic Series):**
   The sequence $H_n = \sum_{k=1}^n \frac{1}{k}$ increases so slowly that for $n = 10^9$ it is only around $21$. A computer table might suggest that $H_n$ converges to a finite ceiling around $22$, whereas analytical proof demonstrates that it diverges to $+\infty$.
4. **Visual Limitations of Sketches:**
   A visual sketch is drawn with a pencil or pixels of finite width. High-frequency oscillations (such as $\sin(1/x)$ near $x = 0$) cannot be rendered accurately; the drawing simply blurs into a solid block, concealing the true behavior.
5. **What Constitutes an Analytical Proof:**
   An analytical proof establishes a **universal deduction** valid for all possible inputs:
   - For the sequence: We proved algebraically that $a_n - 2 = \frac{-13n + 15}{2n^2 + 5n - 7} \to 0$ by showing that $|a_n - 2| < \frac{K}{n} < \varepsilon$ for all $n > M(\varepsilon)$.
   - For the function: We proved that for all $x \neq 3$, the algebraic identity $\frac{(x-3)(x-1)}{x-3} = x - 1$ holds identically, and since $|(x - 1) - 2| = |x - 3| < \delta = \varepsilon$, the limit is unconditionally $2$.
   Deductive proof guarantees truth everywhere; observation merely suggests a hypothesis.

---

## 5. Why Each Step Is Valid
1. **The tables of values** are computed using exact arithmetic directly from the formulas.
2. **The domain restriction $x \neq 3$** explains why $f(3)$ cannot be evaluated numerically.
3. **The philosophical distinction between induction and deduction** follows the foundational principles of mathematical logic (Popper, Russell, and Weierstrass).

---

## 6. Final Answer in Words
For the sequence $a_n = \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7}$, numerical calculations for $n = 2$ up to $n = 10000$ produce values increasing from $1.0$ to $1.99935$, approaching $2$. For the function $f(x) = \frac{x^2 - 4x + 3}{x - 3}$, one-sided tables from the left ($1.9, 1.99, 1.999$) and from the right ($2.1, 2.01, 2.001$) both converge toward $2$, despite the function being undefined at $x = 3$. However, these finite calculations and sketches do not constitute a mathematical proof because empirical observations test only a finite subset of points, cannot rule out slow divergence or hidden oscillations, and cannot substitute for the deductive epsilon-delta verification required to guarantee the limit across all infinite arguments.

---

## 7. Quick Verification
- **Analytical limit checks:**
  $$\lim_{n\to\infty} \frac{4n^2 - 3n + 1}{2n^2 + 5n - 7} = \frac{4}{2} = 2. \quad \text{(Matches table)}$$
  $$\lim_{x\to3} \frac{x^2 - 4x + 3}{x - 3} = \lim_{x\to3}(x - 1) = 3 - 1 = 2. \quad \text{(Matches table)}$$
Both tables converge with absolute consistency to their analytically proven values.

---

## 8. Common Mistakes to Avoid
- **Confusing numerical evidence with mathematical proof:** Assuming that showing 5 decimal approximations is sufficient to "prove" a limit.
- **Ignoring the undefined point at $x = 3$:** Trying to write $f(3) = 2$ in the table rather than explicitly recording it as undefined ($\frac{0}{0}$).
- **Claiming the sequence is defined at $n = 1$:** The denominator $2(1)^2 + 5(1) - 7 = 0$ is zero at $n = 1$, which must be noted.

---

## 9. Classroom Presentation (3-Sentence Summary)
Evaluating the sequence for increasing values of $n$ yields numbers rising from 1.0 to 1.99935, while calculating function values on either side of $x = 3$ yields numbers tightly squeezing 2.0 from above and below. Graphically, the sequence forms discrete points climbing toward the horizontal asymptote $y = 2$, and the function forms the line $y = x - 1$ containing a removable hole at $(3, 2)$. However, these tables and sketches serve only as intuitive observation; a true mathematical proof requires algebraic factoring and the epsilon-delta definition to guarantee that the limit holds unconditionally across all infinite arguments.
