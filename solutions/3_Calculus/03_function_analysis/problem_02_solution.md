# Problem 2 Solution: A Parabola from the Perspective of the Derivative

## 1. Original Problem
For the quadratic function:
$$f(x) = x^2 - 4x + 1$$
1. Find the global minimum point using calculus (the first derivative).
2. Rewrite the quadratic function into vertex form by completing the square, and find the minimum point geometrically.
3. Compare both results and explain why both mathematical approaches necessarily lead to the exact same point.

---

## 2. What We Are Trying to Find
We need to:
1. Differentiate $f(x)$ and solve $f'(x) = 0$ to find the stationary point.
2. Verify that this point is a strict minimum using the first and second derivative tests.
3. Complete the square to put $f(x)$ into the vertex form $a(x - p)^2 + q$.
4. Read the vertex coordinates $(p, q)$ directly from the completed square.
5. Provide the mathematical bridge connecting the geometric vertex of a parabola with the vanishing derivative of a smooth function.

---

## 3. Key Concepts and Theorems
1. **Calculus Approach (Fermat's Theorem on Stationary Points):**
   For a differentiable function, a local extremum in an open interval can only occur at a point where the derivative vanishes:
   $$f'(x) = 0.$$
2. **Algebraic Approach (Vertex Form of a Parabola):**
   Any quadratic $f(x) = ax^2 + bx + c$ with $a > 0$ can be rewritten as:
   $$f(x) = a(x - p)^2 + q, \quad \text{where } p = -\frac{b}{2a}, \; q = f(p) = c - \frac{b^2}{4a}.$$
   Since $(x - p)^2 \ge 0$ for all real $x$, the minimum value $q$ is achieved uniquely when the squared term is zero, namely at $x = p$.
3. **Equivalence of the Two Perspectives:**
   Differentiating the vertex form $f(x) = a(x - p)^2 + q$ gives:
   $$f'(x) = 2a(x - p).$$
   Setting $f'(x) = 0$ immediately recovers $x = p$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Calculus Approach (Using the Derivative)
1. **Compute the first derivative:**
   $$f'(x) = \frac{d}{dx}[x^2 - 4x + 1] = 2x - 4.$$
2. **Find the critical point by setting $f'(x) = 0$:**
   $$2x - 4 = 0 \implies 2x = 4 \implies x = 2.$$
3. **Verify it is a minimum:**
   - **First derivative sign check:**
     - For $x < 2$: $f'(x) = 2x - 4 < 0$ (function is decreasing).
     - For $x > 2$: $f'(x) = 2x - 4 > 0$ (function is increasing).
     Since $f'$ changes from negative to positive, $x = 2$ is a strict local and global minimum.
   - **Second derivative test:**
     $$f''(x) = \frac{d}{dx}[2x - 4] = 2 > 0.$$
     Since $f''(x) = 2 > 0$ everywhere, the curve is strictly concave up, confirming a global minimum.
4. **Compute the minimum value:**
   $$f(2) = 2^2 - 4(2) + 1 = 4 - 8 + 1 = -3.$$
Thus, the minimum point found via calculus is:
$$V_{\text{calc}} = (2, -3).$$

---

### Step 2: Algebraic Approach (Completing the Square / Vertex Form)
1. Group the quadratic and linear terms:
   $$f(x) = (x^2 - 4x) + 1.$$
2. Complete the square on $x^2 - 4x$:
   $$x^2 - 4x = (x - 2)^2 - 2^2 = (x - 2)^2 - 4.$$
3. Substitute back into the function:
   $$f(x) = \big((x - 2)^2 - 4\big) + 1 = (x - 2)^2 - 3.$$
4. **Determine the vertex coordinates:**
   In the expression $f(x) = (x - 2)^2 - 3$:
   - For any real number $x$, $(x - 2)^2 \ge 0$.
   - The smallest possible value of $(x - 2)^2$ is $0$, which occurs if and only if $x - 2 = 0 \iff x = 2$.
   - When $x = 2$, $f(2) = 0 - 3 = -3$.
   - For all $x \neq 2$, $(x - 2)^2 > 0$, so $f(x) > -3$.
Therefore, the vertex (minimum point) found algebraically is:
$$V_{\text{geom}} = (2, -3).$$

---

### Step 3: Comparison and Explanation of Why Both Approaches Lead to the Same Point
- **Comparison:**
  Both methods produce the identical point:
  $$V = (2, -3).$$
- **Why They Must Agree:**
  1. **Geometric Reason:**
     A parabola opening upwards ($a = 1 > 0$) is symmetrical about its vertical axis of symmetry $x = p$. At the very bottom of the bowl (the vertex), the curve transitions smoothly from sloping downward to sloping upward. A smooth curve can only reverse its direction by having a momentary horizontal tangent line. Since the slope of the tangent line is given by the derivative, the vertex of a parabola is precisely the unique point where the tangent is horizontal ($f'(x) = 0$).
  2. **Algebraic Reason:**
     Differentiating the general vertex form $f(x) = a(x - p)^2 + q$ using the Chain Rule yields:
     $$f'(x) = 2a(x - p).$$
     Setting $f'(x) = 0$ requires $2a(x - p) = 0$. Since $a \neq 0$, the only solution is $x - p = 0 \iff x = p$.
     Thus, the zero of the derivative is algebraically forced to coincide with the center of the completed square.
  Calculus provides a universal language (the derivative) that generalizes this vertex-finding property to polynomials of any degree and non-polynomial functions where completing the square is impossible.

---

## 5. Why Each Step Is Valid
1. **The power rule** $\frac{d}{dx}[x^2 - 4x + 1] = 2x - 4$ is exact for quadratic polynomials.
2. **Completing the square $(x - 2)^2 - 4$** is an exact algebraic identity.
3. **The inequality $(x - 2)^2 \ge 0$** is an absolute axiom of ordered real fields.

---

## 6. Final Answer in Words
Using the derivative, setting $f'(x) = 2x - 4 = 0$ yields $x = 2$, and since $f''(2) = 2 > 0$, the function achieves a strict global minimum at $(2, -3)$. Using algebra, completing the square gives the vertex form $f(x) = (x - 2)^2 - 3$, which attains its minimum value $-3$ when the non-negative squared term $(x - 2)^2$ vanishes at $x = 2$. Both approaches lead to the exact same point $(2, -3)$ because the geometric vertex of a smooth parabola is the unique point where the slope of the tangent line is horizontal ($f'(x) = 0$).

---

## 7. Quick Verification
- Standard vertex formula check:
  $$p = -\frac{b}{2a} = -\frac{-4}{2(1)} = \frac{4}{2} = 2.$$
  $$q = c - \frac{b^2}{4a} = 1 - \frac{(-4)^2}{4(1)} = 1 - \frac{16}{4} = 1 - 4 = -3.$$
  Vertex is $(2, -3)$.
- Test symmetric points around $x = 2$:
  - At $x = 1$: $f(1) = 1 - 4 + 1 = -2$.
  - At $x = 3$: $f(3) = 9 - 12 + 1 = -2$.
  - At $x = 0$: $f(0) = 1$.
  - At $x = 4$: $f(4) = 16 - 16 + 1 = 1$.
  Symmetry $f(2 - h) = f(2 + h)$ is verified.

---

## 8. Common Mistakes to Avoid
- **Sign error in the linear equation:** Solving $2x - 4 = 0$ as $2x = -4 \implies x = -2$.
- **Mistaking the $y$-value for the vertex coordinate:** Stating the minimum is $2$ (which is the location) rather than $-3$ (which is the minimum value).
- **Arithmetic slip in completing the square:** Writing $(x - 2)^2 + 4$ instead of $(x - 2)^2 - 4$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Differentiating $f(x) = x^2 - 4x + 1$ gives $f'(x) = 2x - 4$, which equals zero at $x = 2$, identifying the minimum point as $(2, -3)$ because the second derivative is positive. Alternatively, completing the square rewrites the function in vertex form as $(x - 2)^2 - 3$, which reaches its lowest value of $-3$ when the squared term equals zero at $x = 2$. Both approaches yield the exact same point because the vertex of a smooth parabola is geometrically identical to the point where the tangent line flattens to a slope of zero.
