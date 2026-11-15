# Problem 14 Solution: Continuity and Differentiability of a Piecewise Function

## 1. Original Problem
Investigate the behavior at the junction point $x = 0$ of the piecewise function:
$$f(x) = \begin{cases}
x^2, & \text{if } x \ge 0, \\
ax, & \text{if } x < 0,
\end{cases}$$
where $a$ is a real parameter.
1. For which values of the parameter $a$ is the function continuous at $x = 0$?
2. Compute the one-sided derivatives $f'_-(0)$ and $f'_+(0)$ from first principles. For which values of $a$ do the one-sided derivatives exist and agree?
3. For which value of $a$ is the function differentiable at $x = 0$?
4. Explain in detail why continuity at a point is a necessary, but **not sufficient**, condition for differentiability.

---

## 2. What We Are Trying to Find
We need to:
1. Test continuity by checking whether $\lim_{x\to0^-} f(x) = \lim_{x\to0^+} f(x) = f(0)$ for any or all values of $a$.
2. Formulate the one-sided difference quotients at $x = 0$ for $h \to 0^-$ and $h \to 0^+$.
3. Compute the left-hand derivative $f'_-(0) = a$ and the right-hand derivative $f'_+(0) = 0$.
4. Determine the unique value of $a$ where the two one-sided slopes match smoothly ($a = 0$).
5. Clarify the fundamental theoretical hierarchy: Differentiability $\implies$ Continuity, but Continuity $\centernot\implies$ Differentiability.

---

## 3. Key Concepts and Theorems
1. **Definition of One-Sided Derivatives:**
   - **Right-hand derivative at $0$:**
     $$f'_+(0) = \lim_{h\to0^+} \frac{f(0 + h) - f(0)}{h} = \lim_{h\to0^+} \frac{f(h) - f(0)}{h}.$$
   - **Left-hand derivative at $0$:**
     $$f'_-(0) = \lim_{h\to0^-} \frac{f(0 + h) - f(0)}{h} = \lim_{h\to0^-} \frac{f(h) - f(0)}{h}.$$
2. **Criterion for Differentiability at a Point:**
   A function $f(x)$ is differentiable at $x_0$ if and only if both one-sided derivatives exist, are finite, and are **strictly equal**:
   $$f'(x_0) \text{ exists} \iff f'_-(x_0) = f'_+(x_0).$$
3. **Continuity vs. Differentiability Theorem:**
   - If $f$ is differentiable at $x_0$, it is guaranteed to be continuous at $x_0$.
   - A function can be continuous at $x_0$ but have a sharp "corner" or "kink" (e.g., $f(x) = |x|$), meaning the one-sided tangent slopes disagree, preventing differentiability.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze Continuity at $x = 0$
To determine for which values of $a$ the function is continuous at $x = 0$, evaluate the three required quantities:
1. **Function value at $x = 0$:**
   Since $x = 0$ falls under $x \ge 0$, use $f(x) = x^2$:
   $$f(0) = 0^2 = 0.$$
2. **Right-hand limit as $x \to 0^+$:**
   Using the branch for $x \ge 0$:
   $$\lim_{x\to0^+} f(x) = \lim_{x\to0^+} (x^2) = 0^2 = 0.$$
3. **Left-hand limit as $x \to 0^-$:**
   Using the branch for $x < 0$:
   $$\lim_{x\to0^-} f(x) = \lim_{x\to0^-} (ax) = a(0) = 0.$$

Notice that:
$$\lim_{x\to0^-} f(x) = 0 = \lim_{x\to0^+} f(x) = f(0) = 0.$$
This equality holds **for every real number $a \in \mathbb{R}$**!
- **Conclusion for Continuity:**
  The function $f(x)$ is continuous at $x = 0$ for **all $a \in \mathbb{R}$** ($a \in (-\infty, \infty)$). The parameter $a$ has no influence on continuity because multiplying any number $a$ by $0$ always yields $0$.

---

### Step 2: Compute the One-Sided Derivatives at $x = 0$
We compute the derivatives using the formal definition:

1. **Right-Hand Derivative $f'_+(0)$:**
   For $h > 0$, $f(h) = h^2$, and we know $f(0) = 0$:
   $$f'_+(0) = \lim_{h\to0^+} \frac{f(h) - f(0)}{h} = \lim_{h\to0^+} \frac{h^2 - 0}{h} = \lim_{h\to0^+} \frac{h^2}{h} = \lim_{h\to0^+} h = 0.$$
   The right-hand derivative exists and equals **$0$** (independent of $a$).

2. **Left-Hand Derivative $f'_-(0)$:**
   For $h < 0$, $f(h) = ah$, and $f(0) = 0$:
   $$f'_-(0) = \lim_{h\to0^-} \frac{f(h) - f(0)}{h} = \lim_{h\to0^-} \frac{ah - 0}{h} = \lim_{h\to0^-} \frac{ah}{h} = \lim_{h\to0^-} a = a.$$
   The left-hand derivative exists and equals **$a$**.

---

### Step 3: Determine Differentiability at $x = 0$
For the two-sided derivative $f'(0)$ to exist, the left-hand derivative and right-hand derivative must be identical:
$$f'_-(0) = f'_+(0) \iff a = 0.$$
- **If $a = 0$:**
  Both one-sided derivatives equal $0$ ($f'_-(0) = f'_+(0) = 0$). The function is **differentiable** at $x = 0$, and its derivative is $f'(0) = 0$.
- **If $a \neq 0$:**
  $f'_-(0) = a \neq 0 = f'_+(0)$. The two one-sided slopes disagree. The function has a sharp **corner point** (kink) at the origin and is **not differentiable** at $x = 0$.

---

### Step 4: Why Continuity Alone Is Not Sufficient for Differentiability
This problem provides an ideal case study demonstrating the distinction between continuity and differentiability:
1. **What Continuity Guarantees:**
   Continuity ensures that the graph has **no breaks, jumps, or holes**. The two branches $x^2$ and $ax$ connect at the point $(0, 0)$. As we proved in Step 1, this connection holds for *every* value of $a$, so the graph is always a single unbroken curve.
2. **What Differentiability Demands:**
   Differentiability is a much stronger condition: it requires the curve to be **smooth** (having a unique, unambiguous tangent line with a well-defined slope).
   - If $a = 2$, the graph approaches the origin from the left along the line $y = 2x$ with steep slope $m = 2$.
   - At the instant it crosses the origin, the graph suddenly flattens out to match the parabola $y = x^2$ with slope $m = 0$.
   - This abrupt change in direction creates a sharp "corner" at $(0, 0)$. At a sharp corner, you could place a straightedge at multiple different angles without deciding which one is the true tangent line.
   - Therefore, a function can easily be connected (continuous) without being smooth (differentiable). Continuity is necessary to have a derivative, but it is not sufficient to guarantee one.

---

## 5. Why Each Step Is Valid
1. **Checking limits of $x^2$ and $ax$** as $x \to 0$ follows directly from the continuity of monomials.
2. **Canceling $h/h = 1$ in the difference quotients** is valid because $h \to 0^\pm$ guarantees $h \neq 0$.
3. **The requirement $f'_-(0) = f'_+(0)$** is the definitive condition for differentiability on an open neighborhood.

---

## 6. Final Answer in Words
1. The function is continuous at $x = 0$ for **all real values of $a$** ($a \in \mathbb{R}$), because both one-sided limits and the function value equal 0 regardless of $a$.
2. The one-sided derivatives are $f'_+(0) = 0$ and $f'_-(0) = a$. They exist for all $a$, but agree if and only if $a = 0$.
3. The function is differentiable at $x = 0$ **only when $a = 0$**, where $f'(0) = 0$.
4. Continuity alone is not sufficient because continuity only guarantees that the graph is connected with no gaps, whereas differentiability further requires that the curve connects smoothly without a sharp corner. When $a \neq 0$, the incoming line with slope $a$ meets the horizontal parabola with slope $0$ at a sharp angle, destroying differentiability despite perfect continuity.

---

## 7. Quick Verification
- For $a = 0$: $f(x) = \begin{cases} x^2, & x \ge 0 \\ 0, & x < 0 \end{cases}$.
  - Tangent from left: $y = 0$ (slope 0).
  - Tangent from right: $y = 0$ (slope 0).
  The two branches merge seamlessly with horizontal tangent line $y = 0$. The graph is smooth.
- For $a = 1$: $f(x) = \begin{cases} x^2, & x \ge 0 \\ x, & x < 0 \end{cases}$.
  - $f'_-(0) = 1$ (slope of $45^\circ$).
  - $f'_+(0) = 0$ (slope of $0^\circ$).
  The slope jumps abruptly from 1 to 0 at the origin, creating a visible corner. Differentiability fails.

---

## 8. Common Mistakes to Avoid
- **Restricting $a$ for continuity:** Thinking that $a$ must equal 0 for the function to be continuous. Since $a \cdot 0 = 0$, continuity holds for every value of $a$.
- **Differentiating branches by formula without using the limit definition:** Differentiating $\frac{d}{dx}[x^2] = 2x \to 0$ and $\frac{d}{dx}[ax] = a$ works here, but at boundary points one must formally justify the one-sided derivatives using difference quotients.
- **Claiming the derivative exists for all $a$ because both branches are differentiable:** Differentiability on open intervals does not automatically guarantee differentiability at the boundary junction.

---

## 9. Classroom Presentation (3-Sentence Summary)
Because both branches evaluate to zero at $x = 0$, the function is continuous for every real value of $a$, meaning the graph is always connected without any gap. Using one-sided difference quotients, we find the right-hand derivative is 0 while the left-hand derivative is $a$, which means the slopes only match when $a = 0$. Therefore, the function is differentiable exclusively when $a = 0$, providing a classic demonstration that continuity is merely a necessary prerequisite for differentiability, but not sufficient to prevent sharp non-differentiable corners.
