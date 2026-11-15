# Problem 4 Solution: Powers and Oscillation

## 1. Original Problem
Analyze the limiting behavior of the four sequences as $n \to \infty$:
1. $a_n = \left(\frac{2}{3}\right)^n$
2. $b_n = \left(\frac{3}{2}\right)^n$
3. $c_n = (-1)^n$
4. $d_n = \frac{(-1)^n}{n}$

For each sequence, describe the type of behavior (convergence, divergence to infinity, or oscillation without limit), compute the limit if it exists, and provide a full mathematical justification.

---

## 2. What We Are Trying to Find
We need to:
1. Classify the behavior of geometric sequences $q^n$ for base values $|q| < 1$ and $q > 1$.
2. Analyze the alternating sequence $(-1)^n$ and prove why it fails to converge.
3. Apply the Squeeze (Sandwich) Theorem to evaluate $\frac{(-1)^n}{n}$, demonstrating that oscillation does not necessarily prevent convergence.
4. Establish the general criteria separating bounded damped oscillation from undamped or diverging oscillation.

---

## 3. Key Concepts and Theorems
1. **Geometric Sequence Limit Theorem:**
   For a real number $q$:
   $$\lim_{n\to\infty} q^n = \begin{cases}
   0 & \text{if } |q| < 1, \\
   1 & \text{if } q = 1, \\
   +\infty & \text{if } q > 1, \\
   \text{diverges (oscillates)} & \text{if } q \le -1.
   \end{cases}$$
2. **Subsequence Convergence Criterion:**
   If a sequence $(x_n)$ converges to a limit $L$, then every subsequence of $(x_n)$ must converge to the same limit $L$. Conversely, if two subsequences converge to two distinct limits ($L_1 \neq L_2$), the sequence diverges.
3. **Squeeze (Sandwich) Theorem for Sequences:**
   If $a_n \le b_n \le c_n$ for all $n \ge n_0$, and $\lim_{n\to\infty} a_n = \lim_{n\to\infty} c_n = L$, then:
   $$\lim_{n\to\infty} b_n = L.$$
4. **Absolute Value Null Sequence Theorem:**
   $$\lim_{n\to\infty} |x_n| = 0 \iff \lim_{n\to\infty} x_n = 0.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze $a_n = \left(\frac{2}{3}\right)^n$
- **Form:** Geometric sequence with base $q = \frac{2}{3}$.
- **Magnitude:**
  $$|q| = \left|\frac{2}{3}\right| = \frac{2}{3} < 1.$$
- **Proof:**
  Since $0 < \frac{2}{3} < 1$, each successive term is obtained by multiplying the previous term by $\frac{2}{3}$, causing the terms to strictly decrease toward zero:
  $$a_1 = \frac{2}{3} \approx 0.667, \quad a_2 = \frac{4}{9} \approx 0.444, \quad a_3 = \frac{8}{27} \approx 0.296, \quad \dots$$
  By the Geometric Sequence Limit Theorem:
  $$\lim_{n\to\infty} \left(\frac{2}{3}\right)^n = 0.$$
- **Classification:** **Convergent** (converges monotonically to $0$).

---

### Step 2: Analyze $b_n = \left(\frac{3}{2}\right)^n$
- **Form:** Geometric sequence with base $q = \frac{3}{2} = 1.5$.
- **Magnitude:**
  $$q = \frac{3}{2} > 1.$$
- **Proof:**
  We can write $q = 1 + h$ with $h = \frac{1}{2} > 0$. By Bernoulli's Inequality:
  $$b_n = (1 + h)^n \ge 1 + nh = 1 + \frac{n}{2}.$$
  As $n \to \infty$, $1 + \frac{n}{2} \to +\infty$.
  By the comparison test:
  $$\lim_{n\to\infty} \left(\frac{3}{2}\right)^n = +\infty.$$
- **Classification:** **Divergent** (diverges to $+\infty$).

---

### Step 3: Analyze $c_n = (-1)^n$
- **Terms:**
  The sequence alternates perpetually between two values:
  $$c_1 = -1, \quad c_2 = 1, \quad c_3 = -1, \quad c_4 = 1, \quad \dots$$
- **Proof via Subsequences:**
  - Take the subsequence of even indices $n = 2k$:
    $$c_{2k} = (-1)^{2k} = ((-1)^2)^k = 1^k = 1 \implies \lim_{k\to\infty} c_{2k} = 1.$$
  - Take the subsequence of odd indices $n = 2k - 1$:
    $$c_{2k-1} = (-1)^{2k-1} = -1 \implies \lim_{k\to\infty} c_{2k-1} = -1.$$
  Since the even subsequence approaches $1$ and the odd subsequence approaches $-1$, and $1 \neq -1$, the sequence cannot converge to any single real number.
- **Classification:** **Divergent by bounded oscillation** (does not converge, no limit exists).

---

### Step 4: Analyze $d_n = \frac{(-1)^n}{n}$
- **Terms:**
  $$d_1 = -1, \quad d_2 = \frac{1}{2}, \quad d_3 = -\frac{1}{3}, \quad d_4 = \frac{1}{4}, \quad \dots$$
  The signs alternate, but the absolute values shrink steadily: $|d_n| = \frac{1}{n}$.
- **Proof via Squeeze Theorem:**
  For any integer $n \ge 1$, we know that $-1 \le (-1)^n \le 1$.
  Divide this double inequality by the positive integer $n > 0$:
  $$-\frac{1}{n} \le \frac{(-1)^n}{n} \le \frac{1}{n}.$$
  Now take the limits of the bounding sequences as $n \to \infty$:
  $$\lim_{n\to\infty} \left(-\frac{1}{n}\right) = 0 \quad \text{and} \quad \lim_{n\to\infty} \left(\frac{1}{n}\right) = 0.$$
  Because the left and right sequences both converge to $0$, by the Squeeze Theorem:
  $$\lim_{n\to\infty} \frac{(-1)^n}{n} = 0.$$
- **Classification:** **Convergent** (damped oscillation converging to $0$).

---

### Step 5: Comparative Synthesis
1. **$a_n$ vs. $b_n$:** Compares base $q < 1$ with $q > 1$. Exponential decay forces convergence to $0$, whereas exponential growth causes divergence to $+\infty$.
2. **$c_n$ vs. $d_n$:** Compares undamped vs. damped oscillation.
   - In $c_n = (-1)^n$, the amplitude of oscillation remains constant at $1$; the sequence endlessly jumps between $-1$ and $+1$ without settling, preventing convergence.
   - In $d_n = \frac{(-1)^n}{n}$, the alternating sign $(-1)^n$ is multiplied by an amplitude factor $\frac{1}{n}$ that decays to zero. The oscillations are squeezed toward zero, proving that **oscillation alone does not prevent convergence** as long as the amplitude is damped to zero.

---

## 5. Why Each Step Is Valid
1. **The geometric sequence theorem** is a fundamental theorem of analysis derived from the Archimedean property.
2. **The distinct limits of subsequences ($1 \neq -1$)** rigorously violates the uniqueness of limits for metric spaces, proving divergence of $c_n$.
3. **The Squeeze Theorem** applies because $n > 0$ preserves the inequality direction and the outer limits are equal.

---

## 6. Final Answer in Words
1. $\lim_{n\to\infty} \left(\frac{2}{3}\right)^n = 0$ (converges to $0$ because the base magnitude is strictly less than 1).
2. $\lim_{n\to\infty} \left(\frac{3}{2}\right)^n = +\infty$ (diverges to $+\infty$ because the base is greater than 1).
3. $\lim_{n\to\infty} (-1)^n$ does not exist (diverges by perpetual oscillation between $-1$ and $+1$).
4. $\lim_{n\to\infty} \frac{(-1)^n}{n} = 0$ (converges to $0$ by the Squeeze Theorem because $-\frac{1}{n} \le \frac{(-1)^n}{n} \le \frac{1}{n}$).

---

## 7. Quick Verification
- For $a_{20} = (2/3)^{20} \approx 0.00030 \approx 0$.
- For $b_{20} = (3/2)^{20} \approx 3325.26 \gg 1$.
- For $c_{100} = 1$, $c_{101} = -1$. Distance between successive terms remains $|1 - (-1)| = 2$ forever, failing the Cauchy convergence criterion.
- For $d_{100} = +0.01$, $d_{101} = -0.0099$. Both are within $0.01$ of $0$, confirming convergence.

---

## 8. Common Mistakes to Avoid
- **Claiming $\frac{(-1)^n}{n}$ does not converge because of $(-1)^n$:** Assuming any sequence with $(-1)^n$ diverges; one must check whether the amplitude decays to 0.
- **Writing $\lim (-1)^n = \pm 1$:** A limit must be a unique single number; writing $\pm 1$ denotes two numbers, meaning the limit does not exist.
- **Confusing $\left(\frac{2}{3}\right)^n$ with $\frac{2}{3n}$:** Both converge to zero, but one is exponential decay while the other is rational decay.

---

## 9. Classroom Presentation (3-Sentence Summary)
The geometric sequence $(2/3)^n$ decays to 0 because its ratio is less than 1, while $(3/2)^n$ grows without bound to infinity because its ratio exceeds 1. The alternating sequence $(-1)^n$ diverges because its even terms approach 1 while its odd terms approach $-1$, violating the uniqueness of limits. In contrast, dividing by $n$ in $(-1)^n/n$ damps the oscillating amplitude to zero, allowing the Squeeze Theorem between $-1/n$ and $1/n$ to prove that the sequence converges to 0.
