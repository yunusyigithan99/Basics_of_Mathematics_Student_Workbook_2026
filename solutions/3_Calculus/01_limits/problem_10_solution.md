# Problem 10 Solution: Continuity of a Piecewise Function

## 1. Original Problem
Find the real parameter value $a$ such that the piecewise-defined function:
$$f(x) = \begin{cases}
ax + 1, & \text{if } x < 2, \\
x^2 - 1, & \text{if } x \ge 2
\end{cases}$$
is continuous at the transition point $x = 2$. Explicitly compute and compare the left-hand limit, the right-hand limit, and the function value at $x = 2$.

---

## 2. What We Are Trying to Find
We need to:
1. Compute the left-hand limit $\lim_{x\to2^-} f(x)$ using the linear formula $ax + 1$.
2. Compute the right-hand limit $\lim_{x\to2^+} f(x)$ using the quadratic formula $x^2 - 1$.
3. Evaluate the exact function value $f(2)$ using the branch containing $x \ge 2$.
4. Set up the continuity equation requiring equality among all three quantities:
   $$\lim_{x\to2^-} f(x) = \lim_{x\to2^+} f(x) = f(2).$$
5. Solve this linear equation for the parameter $a$.

---

## 3. Key Concepts and Theorems
1. **Definition of Continuity at a Point:**
   A function $f(x)$ is continuous at a point $x = c$ if and only if three conditions are satisfied:
   - Condition 1: $f(c)$ is defined (belongs to the domain).
   - Condition 2: The two-sided limit $\lim_{x\to c} f(x)$ exists, which means:
     $$\lim_{x\to c^-} f(x) = \lim_{x\to c^+} f(x) = L.$$
   - Condition 3: The limit equals the function value:
     $$\lim_{x\to c} f(x) = f(c).$$
2. **Continuity of Polynomial Branches:**
   Both individual branches $f_1(x) = ax + 1$ and $f_2(x) = x^2 - 1$ are polynomials and therefore continuous on their respective intervals $(-\infty, 2)$ and $[2, \infty)$. The only potential point of discontinuity is the boundary point $x = 2$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Function Value $f(2)$
Examine the piecewise definition. For $x = 2$, the inequality $x \ge 2$ applies, directing us to the second branch $f_2(x) = x^2 - 1$:
$$f(2) = 2^2 - 1 = 4 - 1 = 3.$$
The function is well-defined at $x = 2$, and its value is $3$.

### Step 2: Compute the Right-Hand Limit ($x \to 2^+$)
When $x$ approaches $2$ from the right ($x > 2$), the function is defined by $f(x) = x^2 - 1$.
Since $x^2 - 1$ is a polynomial, it is continuous from the right at $2$:
$$\lim_{x\to2^+} f(x) = \lim_{x\to2^+} (x^2 - 1) = 2^2 - 1 = 4 - 1 = 3.$$
Notice that $\lim_{x\to2^+} f(x) = f(2) = 3$. The function is automatically continuous from the right.

### Step 3: Compute the Left-Hand Limit ($x \to 2^-$)
When $x$ approaches $2$ from the left ($x < 2$), the function is defined by $f(x) = ax + 1$.
Since $ax + 1$ is a linear polynomial, we can evaluate the limit by direct substitution:
$$\lim_{x\to2^-} f(x) = \lim_{x\to2^-} (ax + 1) = a(2) + 1 = 2a + 1.$$

### Step 4: Enforce the Continuity Condition
For $f(x)$ to be continuous at $x = 2$, the left-hand limit must equal the right-hand limit and the function value:
$$\lim_{x\to2^-} f(x) = \lim_{x\to2^+} f(x) = f(2)$$
$$2a + 1 = 3.$$

### Step 5: Solve for the Parameter $a$
Solve the linear equation:
$$2a + 1 = 3$$
$$2a = 3 - 1 = 2$$
$$a = \frac{2}{2} = 1.$$

### Step 6: Verify the Three Quantities with $a = 1$
Substitute $a = 1$ into the piecewise function:
$$f(x) = \begin{cases}
x + 1, & \text{if } x < 2, \\
x^2 - 1, & \text{if } x \ge 2
\end{cases}$$
1. **Left-hand limit:**
   $$\lim_{x\to2^-} (x + 1) = 2 + 1 = 3.$$
2. **Right-hand limit:**
   $$\lim_{x\to2^+} (x^2 - 1) = 2^2 - 1 = 3.$$
3. **Function value:**
   $$f(2) = 2^2 - 1 = 3.$$
Since:
$$\lim_{x\to2^-} f(x) = \lim_{x\to2^+} f(x) = f(2) = 3,$$
the two branches meet smoothly at the common point $(2, 3)$, with no jump or hole. The function is continuous everywhere on $\mathbb{R}$.

---

## 5. Why Each Step Is Valid
1. **Evaluating branches by direct substitution** is valid because polynomials are continuous on all of $\mathbb{R}$.
2. **Setting left-hand limit equal to right-hand limit** is the necessary and sufficient condition for the existence of the two-sided limit.
3. **Equating to $f(2)$** satisfies the third axiom of continuity according to Cauchy and Weierstrass.

---

## 6. Final Answer in Words
The function is continuous at $x = 2$ if and only if $a = 1$. The function value is $f(2) = 3$, the right-hand limit is $\lim_{x\to2^+} f(x) = 3$, and the left-hand limit is $\lim_{x\to2^-} f(x) = 2a + 1$. Setting $2a + 1 = 3$ gives $a = 1$, which ensures that all three quantities agree at the value $3$, removing any potential jump discontinuity at the boundary.

---

## 7. Quick Verification
- **Left branch with $a = 1$:**
  $f(1.9) = 1.9 + 1 = 2.9$.
  $f(1.99) = 1.99 + 1 = 2.99$.
  $f(1.999) = 1.999 + 1 = 2.999 \to 3$.
- **Right branch:**
  $f(2.1) = 2.1^2 - 1 = 4.41 - 1 = 3.41$.
  $f(2.01) = 2.01^2 - 1 = 4.0401 - 1 = 3.0401$.
  $f(2.001) = 2.001^2 - 1 = 4.004001 - 1 = 3.004001 \to 3$.
The function connects seamlessly from both sides at the coordinate point $(2, 3)$.

---

## 8. Common Mistakes to Avoid
- **Using the wrong branch for $f(2)$:** Evaluating $f(2)$ using $ax + 1$ instead of $x^2 - 1$, despite the condition $x \ge 2$.
- **Arithmetic slip in $2a + 1 = 3$:** Calculating $2a = 4 \implies a = 2$.
- **Assuming continuity without checking the function value:** Only checking that $\lim_{x\to2^-} = \lim_{x\to2^+}$ without confirming equality to $f(2)$ (which could leave a removable point discontinuity).

---

## 9. Classroom Presentation (3-Sentence Summary)
At the transition point $x = 2$, the function value and right-hand limit both evaluate to $2^2 - 1 = 3$ using the quadratic branch. Approaching from the left along the linear branch gives the limit $2a + 1$. Equating the left-hand limit to the function value yields the linear equation $2a + 1 = 3$, which uniquely solves to $a = 1$, ensuring that the two pieces glue together seamlessly into a continuous curve.
