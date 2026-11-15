# Problem 6 Solution: From a Sequence to a Function — Limit at Infinity

## 1. Original Problem
Compute the limit of the rational function at positive infinity:
$$\lim_{x\to\infty} \frac{3x^2 - x + 1}{5x^2 + 4x - 2}.$$
Compare the solution method with Exercise 1 (the sequence limit). Explain in detail what changes when transitioning from a discrete integer index $n \in \mathbb{N}$ to a continuous real variable $x \in \mathbb{R}$, and what fundamental properties remain completely unchanged.

---

## 2. What We Are Trying to Find
We need to:
1. Evaluate the limit of a continuous rational function as $x \to +\infty$ encountering the indeterminate form $\left[\frac{\infty}{\infty}\right]$.
2. Apply the dominant term factoring technique to compute the exact limit value.
3. Compare the algebraic steps with those used for sequence limits.
4. Explain the theoretical bridge connecting sequence limits and function limits (the Heine definition / sequential characterization of limits).

---

## 3. Key Concepts and Theorems
1. **Dominant Term Factoring for Functions:**
   For a rational function $f(x) = \frac{P(x)}{Q(x)}$ as $x \to \infty$, factoring out the highest power of $x$ in the denominator reveals the horizontal asymptote.
2. **Elementary Limits of Real Functions at Infinity:**
   For any real constant $c$ and any exponent $p > 0$:
   $$\lim_{x\to\infty} \frac{c}{x^p} = 0.$$
3. **Heine's Theorem (Sequential Characterization of Limits):**
   A function limit $\lim_{x\to\infty} f(x) = L$ holds if and only if for **every** sequence $(x_n)$ of real numbers such that $\lim_{n\to\infty} x_n = \infty$, the corresponding sequence of function values satisfies:
   $$\lim_{n\to\infty} f(x_n) = L.$$
   In particular, setting $x_n = n$ (the natural numbers) produces the associated sequence limit.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Identify the Indeterminate Form
As $x \to \infty$:
- Numerator: $3x^2 - x + 1 \to \infty$
- Denominator: $5x^2 + 4x - 2 \to \infty$
Direct evaluation yields the indeterminate form:
$$\left[\frac{\infty}{\infty}\right].$$

### Step 2: Factor Out the Dominant Power $x^2$
The highest power of $x$ in both numerator and denominator is $x^2$. Factor $x^2$ out:
$$\frac{3x^2 - x + 1}{5x^2 + 4x - 2} = \frac{x^2 \left(3 - \frac{1}{x} + \frac{1}{x^2}\right)}{x^2 \left(5 + \frac{4}{x} - \frac{2}{x^2}\right)}.$$

### Step 3: Cancel the Common Factor $x^2$
For all $x > 0$, $x^2 \neq 0$, so we can divide numerator and denominator by $x^2$:
$$= \frac{3 - \frac{1}{x} + \frac{1}{x^2}}{5 + \frac{4}{x} - \frac{2}{x^2}}.$$

### Step 4: Evaluate the Limits of the Terms
As $x \to \infty$:
$$\lim_{x\to\infty} \frac{1}{x} = 0, \qquad \lim_{x\to\infty} \frac{1}{x^2} = 0,$$
$$\lim_{x\to\infty} \frac{4}{x} = 0, \qquad \lim_{x\to\infty} \frac{2}{x^2} = 0.$$

### Step 5: Compute the Final Limit
Applying the quotient and sum limit laws for functions:
$$\lim_{x\to\infty} \frac{3 - \frac{1}{x} + \frac{1}{x^2}}{5 + \frac{4}{x} - \frac{2}{x^2}} = \frac{3 - 0 + 0}{5 + 0 - 0} = \frac{3}{5} = 0.6.$$
This result also means that the line $y = \frac{3}{5}$ is a **horizontal asymptote** of the function $f(x)$ as $x \to \infty$.

---

### Step 6: Comparison: Moving from Sequence $n$ to Real Variable $x$

#### 1. What Stays the Same:
- **Algebraic Mechanics:** The factoring technique is identical. In both cases, we factor out the highest power of the variable ($n^2$ or $x^2$), cancel it, and let the reciprocals ($1/n^k$ or $1/x^k$) vanish to zero.
- **Dominance Principle:** The highest-degree terms completely control the behavior at infinity.
- **The Limit Value:** For the sequence $a_n = \frac{3n^2 - n + 1}{5n^2 + 4n - 2}$, the limit as $n \to \infty$ is identically $\frac{3}{5}$.

#### 2. What Changes:
- **The Domain of Arguments:**
  - In a sequence, $n$ takes only discrete positive integers: $n \in \{1, 2, 3, 4, \dots\}$. The variable "hops" from one integer to the next.
  - In a function limit, $x$ is a continuous real variable: $x \in (0, \infty)$. The variable passes smoothly through all intermediate real values (e.g., $x = \pi, \sqrt{2}, 10.732$).
- **The Path to Infinity:**
  - For a sequence, there is only one way to go to infinity: stepping through the ordered sequence of integers.
  - For a function, $x$ can approach infinity along continuous paths, and the condition must hold for every possible path.
- **The Implication Direction (Heine's Theorem):**
  - If the function limit exists, the sequence limit automatically exists and has the exact same value:
    $$\lim_{x\to\infty} f(x) = L \implies \lim_{n\to\infty} f(n) = L.$$
  - However, the converse is **not generally true**! A sequence limit can exist while the continuous function limit fails.
    *Classic Counterexample:* Consider $f(x) = \sin(2\pi x)$.
    For integers $n \in \mathbb{N}$, $f(n) = \sin(2\pi n) = 0$ for all $n$, so the sequence limit is $\lim_{n\to\infty} f(n) = 0$.
    Yet for the continuous function, as $x \to \infty$, $f(x)$ oscillates perpetually between $-1$ and $+1$; hence, $\lim_{x\to\infty} \sin(2\pi x)$ does not exist!

---

## 5. Why Each Step Is Valid
1. **Factoring $x^2$** preserves algebraic equivalence for all $x \neq 0$.
2. **The limits $\lim_{x\to\infty} \frac{1}{x^p} = 0$** hold in the continuous topology of the real numbers $(\mathbb{R}, |\cdot|)$.
3. **The quotient rule for limits** applies because the denominator limit is $5 \neq 0$.

---

## 6. Final Answer in Words
The limit of the function is $\lim_{x\to\infty} \frac{3x^2 - x + 1}{5x^2 + 4x - 2} = \frac{3}{5} = 0.6$. The algebraic method is identical to that of sequence limits: factoring out the dominant power $x^2$ leaves fractions $\frac{1}{x}$ and $\frac{1}{x^2}$ that vanish to zero. The fundamental difference is that $x$ moves continuously through all real numbers rather than discrete integers, meaning the function limit requires every continuous path to approach $3/5$, which geometrically establishes the horizontal asymptote $y = 3/5$.

---

## 7. Quick Verification
- For $x = 10$: $f(10) = \frac{300 - 10 + 1}{500 + 40 - 2} = \frac{291}{538} \approx 0.5409$.
- For $x = 100$: $f(100) = \frac{30000 - 100 + 1}{50000 + 400 - 2} = \frac{29901}{50398} \approx 0.5933$.
- For $x = 1000$: $f(1000) = \frac{3 \times 10^6 - 1000 + 1}{5 \times 10^6 + 4000 - 2} = \frac{2999001}{5003998} \approx 0.59932$.
The values converge monotonically toward $\frac{3}{5} = 0.6$.

---

## 8. Common Mistakes to Avoid
- **Confusing $\lim_{x\to\infty}$ with $\lim_{x\to 0}$:** Trying to plug in $x = 0$ instead of analyzing asymptotic growth as $x \to \infty$.
- **Assuming sequence limits always generalize to functions:** Overlooking that continuous functions can oscillate between integer values (like $\sin(\pi x)$).
- **Arithmetic slips with signs:** Getting $-2/x^2$ wrong when factoring out $x^2$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Just like in sequence limits, evaluating this rational function at infinity involves the indeterminate form infinity over infinity, which we resolve by factoring out the dominant term $x^2$ from the numerator and the denominator. This reduces the lower-degree terms to reciprocals of $x$ that vanish to zero, leaving the ratio of leading coefficients, $3/5$, which geometrically represents the horizontal asymptote of the function. The key conceptual transition from sequences to functions is that $x$ takes all continuous real values rather than just discrete integers, requiring the limit to hold smoothly across the entire real continuum.
