# Problem 13 Solution: Fundamental Trigonometric Limit

## 1. Original Problem
Using the fundamental trigonometric limit:
$$\lim_{x\to0} \frac{\sin x}{x} = 1,$$
compute the limits of the two functions:
$$L_1 = \lim_{x\to0} \frac{\sin 5x}{x}, \qquad L_2 = \lim_{x\to0} \frac{\sin 2x}{\sin 3x}.$$
In each case, explicitly demonstrate the algebraic steps used to reduce the given expression to the fundamental limit pattern.

---

## 2. What We Are Trying to Find
We need to:
1. Identify the indeterminate form $\left[\frac{0}{0}\right]$ in both limits.
2. For $L_1$, introduce the necessary constant factor $5$ into the denominator to match the argument of the sine function.
3. For $L_2$, multiply and divide by appropriate linear factors $2x$ and $3x$ to create two independent fundamental trigonometric ratios.
4. Apply the limit product and quotient rules to evaluate both limits analytically.
5. Formulate the general rule for limits of the form $\lim_{x\to0} \frac{\sin(ax)}{\sin(bx)}$.

---

## 3. Key Concepts and Theorems
1. **The Fundamental Trigonometric Limit:**
   $$\lim_{u\to0} \frac{\sin u}{u} = 1.$$
   This limit requires that the argument of the sine function ($u$) and the denominator ($u$) be **identical** and both tend to zero.
2. **Argument Matching Technique:**
   To evaluate $\lim_{x\to0} \frac{\sin(kx)}{x}$, multiply and divide by the constant $k \neq 0$:
   $$\frac{\sin(kx)}{x} = k \cdot \frac{\sin(kx)}{kx}.$$
3. **Limit Product and Quotient Laws:**
   If $\lim f(x) = A$ and $\lim g(x) = B \neq 0$, then:
   $$\lim [f(x) \cdot g(x)] = A \cdot B, \qquad \lim \frac{f(x)}{g(x)} = \frac{A}{B}.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute Limit $L_1 = \lim_{x\to0} \frac{\sin 5x}{x}$
1. **Identify the Indeterminate Form:**
   As $x \to 0$, $\sin(5 \cdot 0) = \sin 0 = 0$ and the denominator is $0$, giving $\left[\frac{0}{0}\right]$.
2. **Match the Argument:**
   The sine function has argument $u = 5x$, but the denominator is only $x$.
   Multiply and divide the fraction by $5$:
   $$\frac{\sin 5x}{x} = \frac{5 \sin 5x}{5x} = 5 \cdot \frac{\sin 5x}{5x}.$$
3. **Substitute Variable $u = 5x$:**
   As $x \to 0$, we have $u = 5x \to 0$.
   Using the fundamental limit:
   $$\lim_{x\to0} \frac{\sin 5x}{5x} = \lim_{u\to0} \frac{\sin u}{u} = 1.$$
4. **Evaluate the Limit:**
   Applying the constant multiple rule:
   $$L_1 = \lim_{x\to0} \left(5 \cdot \frac{\sin 5x}{5x}\right) = 5 \cdot 1 = 5.$$

---

### Step 2: Compute Limit $L_2 = \lim_{x\to0} \frac{\sin 2x}{\sin 3x}$
1. **Identify the Indeterminate Form:**
   As $x \to 0$, $\sin(2 \cdot 0) = 0$ and $\sin(3 \cdot 0) = 0$, giving $\left[\frac{0}{0}\right]$.
2. **Decompose into Two Fundamental Ratios:**
   We want the expression $\frac{\sin 2x}{2x}$ for the numerator and $\frac{\sin 3x}{3x}$ for the denominator.
   Divide both the numerator and the denominator by $x$ (valid since $x \neq 0$):
   $$\frac{\sin 2x}{\sin 3x} = \frac{\frac{\sin 2x}{x}}{\frac{\sin 3x}{x}}.$$
3. **Insert the Appropriate Coefficients:**
   Multiply and divide the top by $2$, and multiply and divide the bottom by $3$:
   $$\frac{\frac{\sin 2x}{x}}{\frac{\sin 3x}{x}} = \frac{2 \cdot \frac{\sin 2x}{2x}}{3 \cdot \frac{\sin 3x}{3x}} = \frac{2}{3} \cdot \frac{\frac{\sin 2x}{2x}}{\frac{\sin 3x}{3x}}.$$
4. **Evaluate the Limits:**
   Let $u = 2x \to 0$ and $v = 3x \to 0$:
   $$\lim_{x\to0} \frac{\sin 2x}{2x} = 1, \qquad \lim_{x\to0} \frac{\sin 3x}{3x} = 1.$$
5. **Apply the Quotient Rule:**
   $$L_2 = \frac{2}{3} \cdot \frac{\lim_{x\to0} \frac{\sin 2x}{2x}}{\lim_{x\to0} \frac{\sin 3x}{3x}} = \frac{2}{3} \cdot \frac{1}{1} = \frac{2}{3}.$$

---

### Step 3: General Formula
For any non-zero real constants $a, b \neq 0$:
$$\lim_{x\to0} \frac{\sin(ax)}{\sin(bx)} = \lim_{x\to0} \left[ \frac{a}{b} \cdot \frac{\frac{\sin(ax)}{ax}}{\frac{\sin(bx)}{bx}} \right] = \frac{a}{b} \cdot \frac{1}{1} = \frac{a}{b}.$$
Setting $a = 5, b = 1$ gives $5/1 = 5$ for $L_1$, and setting $a = 2, b = 3$ gives $2/3$ for $L_2$.

---

## 5. Why Each Step Is Valid
1. **Multiplying by $\frac{5}{5} = 1$ and $\frac{x}{x} = 1$** is algebraically valid for all $x \neq 0$.
2. **The substitution $u = kx$** is valid because $kx$ is a continuous bijection that vanishes only at $x = 0$.
3. **The quotient rule for limits** applies because the denominator limit is $3 \cdot 1 = 3 \neq 0$.

---

## 6. Final Answer in Words
The limits are $\lim_{x\to0} \frac{\sin 5x}{x} = 5$ and $\lim_{x\to0} \frac{\sin 2x}{\sin 3x} = \frac{2}{3}$. In the first case, multiplying and dividing by 5 produces $5 \cdot \frac{\sin 5x}{5x}$, which evaluates to $5 \cdot 1 = 5$. In the second case, dividing both numerator and denominator by $x$ and inserting the respective factors 2 and 3 produces $\frac{2}{3} \cdot \frac{(\sin 2x)/(2x)}{(\sin 3x)/(3x)}$, which evaluates to $\frac{2}{3} \cdot \frac{1}{1} = \frac{2}{3}$.

---

## 7. Quick Verification
- **Numerical check for $L_1$:**
  - For $x = 0.01$ rad: $\sin(0.05) \approx 0.049979169$.
    $$\frac{\sin 0.05}{0.01} = 4.9979 \approx 5.0.$$
  - For $x = 0.001$ rad: $\sin(0.005) \approx 0.004999979$.
    $$\frac{\sin 0.005}{0.001} = 4.99998 \approx 5.0.$$
- **Numerical check for $L_2$:**
  - For $x = 0.01$ rad: $\sin(0.02) \approx 0.01999867$, $\sin(0.03) \approx 0.0299955$.
    $$\frac{\sin 0.02}{\sin 0.03} = \frac{0.01999867}{0.0299955} \approx 0.66672 \approx \frac{2}{3}.$$
- **Small-angle approximation (Taylor series):**
  Since $\sin \theta = \theta - \frac{\theta^3}{6} + \dots$:
  $$\frac{\sin 5x}{x} \approx \frac{5x}{x} = 5, \qquad \frac{\sin 2x}{\sin 3x} \approx \frac{2x}{3x} = \frac{2}{3}.$$
  Both checks confirm the results.

---

## 8. Common Mistakes to Avoid
- **Attempting to factor $5$ outside the sine function:** Writing $\sin(5x) = 5\sin(x)$, which is completely false (sine is not a linear function).
- **Evaluating in degrees instead of radians:** The fundamental limit $\lim_{x\to0} \frac{\sin x}{x} = 1$ is valid **only in radians**. In degrees, the limit is $\frac{\pi}{180}$.
- **Inverting the coefficient ratio in $L_2$:** Writing $3/2$ instead of $2/3$.

---

## 9. Classroom Presentation (3-Sentence Summary)
To compute $\lim_{x\to0} (\sin 5x)/x$, we multiply and divide by 5 to match the denominator with the argument of the sine function, yielding $5 \cdot (\sin 5x)/(5x) = 5 \cdot 1 = 5$. For the second limit, dividing both the numerator and denominator by $x$ allows us to rewrite the expression as the ratio of two fundamental limits scaled by their coefficients, $(2 \cdot \frac{\sin 2x}{2x}) / (3 \cdot \frac{\sin 3x}{3x})$. This evaluates directly to $2/3$, demonstrating the general principle that the limit of $\sin(ax)/\sin(bx)$ as $x \to 0$ is simply the ratio of their coefficients, $a/b$.
