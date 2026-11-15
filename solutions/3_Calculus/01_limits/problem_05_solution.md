# Problem 5 Solution: The Classical Limit Leading to the Number e

## 1. Original Problem
Compute the limit of the sequence:
$$\lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n.$$
Calculate several numerical values of the sequence for increasing values of $n$ (such as $n = 1, 2, 5, 10, 100, 1000$), compare the observed numerical behavior with the theoretical value of the limit, and explain in detail why calculating a finite set of sample values does not constitute a rigorous mathematical proof.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the indeterminate form $\left[1^\infty\right]$ that arises from naive substitution.
2. State the definition of Euler's number $e$ as the limit of this sequence.
3. Compute a sequence of empirical approximations for increasing values of $n$.
4. Observe the monotonicity and boundedness of the sequence.
5. Provide a clear epistemological explanation of why empirical observation differs from mathematical deduction and proof.

---

## 3. Key Concepts and Theorems
1. **Definition of Euler's Number $e$:**
   The fundamental mathematical constant $e \approx 2.718281828459\dots$ is analytically defined as:
   $$e = \lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n.$$
2. **The Indeterminate Form $\left[1^\infty\right]$:**
   A limit of the form $\lim a_n^{b_n}$ where $a_n \to 1$ and $b_n \to \infty$ is indeterminate because two opposing forces compete:
   - The base $a_n = 1 + \frac{1}{n}$ is shrinking toward $1$ (and $1^n = 1$).
   - The exponent $b_n = n$ is growing toward $\infty$ (and $(>1)^\infty = \infty$).
   The balance between these two competing rates produces the finite transcendental constant $e$.
3. **Monotone Convergence Theorem:**
   The sequence $a_n = \left(1 + \frac{1}{n}\right)^n$ is strictly increasing ($a_n < a_{n+1}$) and bounded above ($a_n < 3$ for all $n$). By the Monotone Convergence Theorem, its limit exists and belongs to the interval $(2, 3)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Indeterminate Form
Examine the base and exponent separately as $n \to \infty$:
- Base: $\lim_{n\to\infty} \left(1 + \frac{1}{n}\right) = 1 + 0 = 1$
- Exponent: $\lim_{n\to\infty} n = \infty$
This yields the indeterminate form:
$$\left[1^\infty\right].$$

### Step 2: Compute Concrete Numerical Terms
Let us evaluate $a_n = \left(1 + \frac{1}{n}\right)^n$ for increasing values of $n$:

1. **For $n = 1$:**
   $$a_1 = \left(1 + \frac{1}{1}\right)^1 = 2^1 = 2.000000$$
2. **For $n = 2$:**
   $$a_2 = \left(1 + \frac{1}{2}\right)^2 = \left(\frac{3}{2}\right)^2 = \frac{9}{4} = 2.250000$$
3. **For $n = 5$:**
   $$a_5 = \left(1 + \frac{1}{5}\right)^5 = (1.2)^5 = 2.488320$$
4. **For $n = 10$:**
   $$a_{10} = \left(1 + \frac{1}{10}\right)^{10} = (1.1)^{10} \approx 2.593742$$
5. **For $n = 100$:**
   $$a_{100} = \left(1 + \frac{1}{100}\right)^{100} = (1.01)^{100} \approx 2.704814$$
6. **For $n = 1000$:**
   $$a_{1000} = \left(1 + \frac{1}{1000}\right)^{1000} = (1.001)^{1000} \approx 2.716924$$
7. **For $n = 10{,}000$:**
   $$a_{10000} \approx 2.718146$$

### Step 3: Compare Numerical Behavior with the Theoretical Limit
- The true mathematical value of the limit to 9 decimal places is:
  $$e \approx 2.718281828\dots$$
- As $n$ increases from $1$ to $10{,}000$, the terms increase monotonically:
  $$2.0 < 2.25 < 2.488 < 2.594 < 2.705 < 2.717 < 2.718 \dots$$
- The growth is decelerating (concave down), approaching $e$ from below.
- This empirical evidence suggests that the limit exists and lies between $2.71$ and $2.72$.

---

### Step 4: Why Calculating a Few Values Does Not Constitute a Proof
While numerical tables build strong intuition, they cannot replace a formal mathematical proof for the following fundamental reasons:

1. **The Nature of Infinity:**
   Evaluating a sequence for $n = 10, 100, 1000$ tests only a finite number of points among an uncountably infinite collection of potential counterexamples. Behavior at $n = 10^3$ tells us nothing about whether the sequence might oscillate, stop increasing, or grow unbounded at $n = 10^{100}$.
2. **Slowly Diverging Sequences (The Harmonic Counterexample):**
   Consider the harmonic partial sums $S_n = \sum_{k=1}^n \frac{1}{k}$. For $n = 1000$, $S_n \approx 7.48$; for $n = 10^6$, $S_n \approx 14.39$. A student looking only at a table of values might wrongly conclude that $S_n$ converges to a finite number around 15 or 20, whereas it is proven to diverge to $+\infty$.
3. **Ghost Boundaries (Skewes' Type Phenomena):**
   In mathematics, some expressions maintain a pattern for millions of terms before suddenly failing. A finite calculation cannot prove that a sequence does not drop or jump at a larger index.
4. **Precision and Rounding Limits:**
   Calculators and computers truncate decimal representations. Rounding errors accumulate, which can simulate false convergence or obscure divergent drift.
5. **What a Real Proof Requires:**
   A rigorous mathematical proof must show that:
   - $a_n$ is strictly increasing: $\frac{a_{n+1}}{a_n} > 1$ for all $n \in \mathbb{N}$ (via Bernoulli's inequality or AM-GM inequality).
   - $a_n$ is bounded above: $a_n < \sum_{k=0}^n \frac{1}{k!} < 1 + 1 + \frac{1}{2} + \frac{1}{4} + \dots = 3$.
   Only the combination of monotonicity and boundedness guarantees the existence of the limit by the completeness axiom of real numbers.

---

## 5. Why Each Step Is Valid
1. **The numerical values** are exact rational numbers ($9/4$, $248832/100000$) computed directly from the definition $a_n = (1 + 1/n)^n$.
2. **Binomial expansion** $a_n = \sum_{k=0}^n \binom{n}{k} \frac{1}{n^k} = \sum_{k=0}^n \frac{1}{k!} \left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right)\dots\left(1 - \frac{k-1}{n}\right)$ proves that each term in the sum increases with $n$, confirming strict monotonicity.
3. **The critique of empirical evidence** follows the standard deductive methodology of mathematical analysis.

---

## 6. Final Answer in Words
The limit of the sequence is $\lim_{n\to\infty} \left(1 + \frac{1}{n}\right)^n = e \approx 2.71828\dots$ The numerical calculations for $n = 1, 2, 5, 10, 100, 1000$ produce values increasing from $2.0$ to approximately $2.7169$, which closely track the theoretical value of $e$. However, computing a finite set of terms does not constitute a proof because empirical observations can never survey infinitely many terms, cannot rule out very slow divergence or sudden changes at enormous values of $n$, and do not establish the necessary properties of monotonicity and boundedness required by mathematical analysis.

---

## 7. Quick Verification
- **Upper bound check:**
  For $n = 1$: $a_1 = 2 < e$.
  For $n = 1000$: $a_{1000} \approx 2.71692 < 2.71828 = e$.
- **Companion sequence (decreasing upper bound):**
  $$b_n = \left(1 + \frac{1}{n}\right)^{n+1} = a_n \left(1 + \frac{1}{n}\right).$$
  For $n = 1000$: $b_{1000} = 2.716924 \times 1.001 \approx 2.719641 > e$.
  Since $a_{1000} < e < b_{1000}$, the number $e$ is tightly trapped:
  $$2.71692 < e < 2.71964.$$
  This double bound verifies the limit rigorously.

---

## 8. Common Mistakes to Avoid
- **Treating $1^\infty$ as equal to $1$:** Forgetting that the base is not identically 1, but rather a sequence approaching 1 from above while the exponent grows to infinity.
- **Thinking a table proves a theorem:** Believing that plotting 5 points on a graph or in a table suffices as a mathematical proof.
- **Confusing $e$ with $2.72$:** Stating the limit is $2.72$; $2.72$ is merely a 2-decimal rounded approximation of the irrational, transcendental number $e$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The expression $(1 + 1/n)^n$ is an indeterminate form of type $1^\infty$ whose value converges to Euler's number $e$, approximately equal to $2.71828$. Computing values for $n = 1, 2, 10, 1000$ produces terms increasing from 2 to approximately $2.717$, illustrating that the sequence is strictly increasing and bounded above. However, a finite table of values is not a proof because empirical sampling cannot inspect infinitely many terms or detect slow divergence, which requires a rigorous proof based on monotonicity and the Monotone Convergence Theorem.
