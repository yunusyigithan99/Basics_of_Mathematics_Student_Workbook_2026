# Problem 4 Solution: A Quotient and Domain Control

## 1. Original Problem
For the rational function:
$$f(x) = \frac{x^2 + 1}{x - 1}$$
1. Determine the natural domain $\operatorname{Dom}(f)$ of the function.
2. Compute the derivative $f'(x)$ using the Quotient Rule.
3. Simplify the resulting algebraic expression.
4. Explain why the domain restriction $x \neq 1$ remains critically important even after differentiation.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the restriction imposed by division by zero in the original function.
2. State and apply the Quotient Rule:
   $$\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}.$$
3. Expand and collect like terms in the numerator.
4. Analyze the domain of the derivative and connect it to the geometry of vertical asymptotes.

---

## 3. Key Concepts and Theorems
1. **The Quotient Rule:**
   For differentiable functions $u(x)$ and $v(x)$ with $v(x) \neq 0$:
   $$\left(\frac{u}{v}\right)' = \frac{u' v - u v'}{v^2}.$$
   *Notice the critical minus sign in the numerator: $u'v - uv'$. The order of terms matters!*
2. **Domain of a Rational Function:**
   The function is defined for all real numbers except where the denominator vanishes:
   $$v(x) = 0 \implies x \notin \operatorname{Dom}(f).$$
3. **Inheritance of Domain Restrictions:**
   A derivative $f'(x)$ can only exist at points where $f(x)$ is already defined and continuous. Therefore:
   $$\operatorname{Dom}(f') \subseteq \operatorname{Dom}(f).$$
   If $x_0 \notin \operatorname{Dom}(f)$, then $x_0$ can never belong to $\operatorname{Dom}(f')$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Determine the Domain of $f(x)$
The function is $f(x) = \frac{x^2 + 1}{x - 1}$.
The denominator is $x - 1$.
Division by zero is undefined in real arithmetic:
$$x - 1 = 0 \iff x = 1.$$
Therefore, $x = 1$ must be excluded from the domain:
$$\operatorname{Dom}(f) = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, \infty).$$

---

### Step 2: Set Up the Quotient Rule
Identify the numerator $u(x)$ and denominator $v(x)$:
- Numerator: $u(x) = x^2 + 1 \implies u'(x) = 2x$
- Denominator: $v(x) = x - 1 \implies v'(x) = 1$

Apply the Quotient Rule formula:
$$f'(x) = \frac{u'(x) v(x) - u(x) v'(x)}{\left[v(x)\right]^2} = \frac{(2x)(x - 1) - (x^2 + 1)(1)}{(x - 1)^2}.$$

---

### Step 3: Expand and Simplify the Numerator
Carefully expand the terms in the numerator:
$$(2x)(x - 1) - (x^2 + 1) = (2x^2 - 2x) - x^2 - 1.$$
Combine like powers of $x$:
$$(2x^2 - x^2) - 2x - 1 = x^2 - 2x - 1.$$
Thus, the simplified derivative is:
$$f'(x) = \frac{x^2 - 2x - 1}{(x - 1)^2}.$$

---

### Step 4: Determine the Domain of $f'(x)$ and Explain Why $x \neq 1$ Remains Essential
In the derivative:
$$f'(x) = \frac{x^2 - 2x - 1}{(x - 1)^2},$$
the denominator is $(x - 1)^2$, which vanishes at:
$$(x - 1)^2 = 0 \iff x = 1.$$
Thus, the derivative is undefined at $x = 1$:
$$\operatorname{Dom}(f') = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, \infty).$$

**Why the Restriction $x \neq 1$ Remains Critically Important:**
1. **Algebraic Reason:**
   Plugging $x = 1$ into $f'(x)$ attempts to compute $\frac{1^2 - 2(1) - 1}{(1 - 1)^2} = \frac{-2}{0}$, which is a severe division by zero.
2. **Foundational Calculus Principle:**
   The derivative at a point $x_0$ is defined as the limit of the secant slopes:
   $$f'(x_0) = \lim_{h\to0} \frac{f(x_0 + h) - f(x_0)}{h}.$$
   This difference quotient requires the function value $f(x_0)$ to exist. Since $f(1)$ does not exist (the function has a point missing from its domain), it is mathematically impossible to evaluate $f'(1)$. A function cannot have a derivative where it does not exist.
3. **Geometric Reason:**
   The line $x = 1$ is a vertical asymptote of the graph of $f(x)$. As $x \to 1^-$, $f(x) \to -\infty$; as $x \to 1^+$, $f(x) \to +\infty$. There is no point on the graph at $x = 1$, and therefore no tangent line can possibly be drawn at $x = 1$.

---

## 5. Why Each Step Is Valid
1. **The domain restriction** is mandatory because fractions with zero denominators are undefined in real arithmetic.
2. **The Quotient Rule** is derived from the product rule applied to $u(x) \cdot [v(x)]^{-1}$ using the chain rule.
3. **Distributing the negative sign** $-(x^2 + 1) = -x^2 - 1$ strictly preserves signs for all $x$.

---

## 6. Final Answer in Words
The domain of $f(x)$ is $\operatorname{Dom}(f) = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, \infty)$. Applying the Quotient Rule yields the simplified derivative $f'(x) = \frac{x^2 - 2x - 1}{(x - 1)^2}$. The restriction $x \neq 1$ remains critically important because $(x - 1)^2$ in the derivative's denominator would cause division by zero, the function value $f(1)$ does not exist (meaning the limit of the difference quotient cannot be formed), and geometrically the curve possesses a vertical asymptote at $x = 1$ where no tangent line exists.

---

## 7. Quick Verification
- Evaluate at $x = 0$:
  $$f(0) = \frac{0 + 1}{0 - 1} = -1.$$
  $$f'(0) = \frac{0^2 - 2(0) - 1}{(0 - 1)^2} = \frac{-1}{1} = -1.$$
- Difference quotient check at $x = 0$ with $h = 0.001$:
  $$f(0.001) = \frac{0.001^2 + 1}{0.001 - 1} = \frac{1.000001}{-0.999} \approx -1.001002.$$
  $$\frac{f(0.001) - f(0)}{0.001} \approx \frac{-1.001002 - (-1)}{0.001} = \frac{-0.001002}{0.001} = -1.002 \approx -1.0.$$
  The numerical rate of change matches $f'(0) = -1$ perfectly.

---

## 8. Common Mistakes to Avoid
- **Sign error in the Quotient Rule:** Writing $u'v + uv'$ (the product rule) instead of $u'v - uv'$. This would yield $3x^2 - 2x + 1$ instead of $x^2 - 2x - 1$.
- **Reversing the subtraction order:** Writing $uv' - u'v$, which negates the entire derivative.
- **Prematurely canceling $(x - 1)$:** Attempting to cancel $(x - 1)$ between numerator and denominator before factoring out a common term.

---

## 9. Classroom Presentation (3-Sentence Summary)
The rational function $f(x) = (x^2 + 1)/(x - 1)$ has domain all real numbers except $x = 1$, where division by zero occurs. Applying the Quotient Rule $(u'v - uv')/v^2$ produces $[2x(x - 1) - (x^2 + 1)(1)] / (x - 1)^2$, which simplifies to $(x^2 - 2x - 1) / (x - 1)^2$. The restriction $x \neq 1$ remains essential because the derivative also contains $(x - 1)^2$ in its denominator, and geometrically the line $x = 1$ is a vertical asymptote where no point or tangent line exists.
