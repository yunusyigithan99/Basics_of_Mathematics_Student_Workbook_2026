# Problem 06: Analysis of a Logarithmic Function

## 1. Original Problem
Analyze the domain, zero, and monotonicity of
$$f(x) = \ln x - x + 1.$$
Explain why the analysis must begin with the domain.

---

## 2. What We Are Trying to Find
We need to determine:
1. Why the mathematical analysis must start with finding the domain $D_f$.
2. The exact domain of definition $D_f$.
3. All real zeros (roots) satisfying $f(x) = 0$.
4. The first derivative $f'(x)$ and the intervals on which $f$ is strictly increasing or strictly decreasing, along with any global/local extrema.

---

## 3. Key Concepts and Theorems
1. **Natural Logarithm Domain Requirement:**
   The function $\ln(u)$ is defined in the real numbers if and only if its argument is strictly positive: $u > 0$.
2. **First Derivative Test for Monotonicity:**
   Let $f$ be continuous on an interval $I$ and differentiable on its interior:
   - If $f'(x) > 0$ for all $x \in \operatorname{int}(I)$, then $f$ is strictly increasing on $I$.
   - If $f'(x) < 0$ for all $x \in \operatorname{int}(I)$, then $f$ is strictly decreasing on $I$.
3. **Global Extrema and Uniqueness of Roots:**
   If a continuous function has a global maximum at $x_0$ with value $f(x_0) = 0$, and is strictly increasing for $x < x_0$ and strictly decreasing for $x > x_0$, then $f(x) < 0$ for all $x \neq x_0$. Thus, $x_0$ is the unique real root.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Why the analysis must begin with the domain
Every function rule $y = f(x)$ is meaningless without specifying the set of allowable inputs. Performing algebraic manipulations or computing derivatives before defining the domain leads to "phantom" critical points or zeros located outside the region where the original expression exists. For instance, algebraic formulas might formally produce negative values or zero, where $\ln x$ is completely undefined. Hence, the domain establishes the universal set of validity for all subsequent calculations.

### Step 2: Determine the domain
The expression $f(x) = \ln x - x + 1$ contains the linear polynomial $-x + 1$ (defined on all $\mathbb{R}$) and the logarithm $\ln x$.
The logarithm requires:
$$x > 0.$$
Therefore, the domain is:
$$D_f = (0, \infty).$$

### Step 3: Compute the first derivative and find critical points
Differentiating term by term with respect to $x$ on $D_f$:
$$f'(x) = \frac{d}{dx}(\ln x) - \frac{d}{dx}(x) + \frac{d}{dx}(1) = \frac{1}{x} - 1.$$
Bring the terms to a common denominator:
$$f'(x) = \frac{1 - x}{x}.$$
Set $f'(x) = 0$ to locate stationary points:
$$\frac{1 - x}{x} = 0 \iff 1 - x = 0 \iff x = 1.$$
Since $1 \in D_f = (0, \infty)$, $x = 1$ is the unique critical point.

### Step 4: Determine the sign of $f'(x)$ and monotonicity
Since the denominator $x$ is strictly positive for all $x \in (0, \infty)$, the sign of $f'(x)$ is completely determined by the numerator $1 - x$:
- **Interval $(0, 1)$:**
  For $0 < x < 1$, we have $1 - x > 0$, so $f'(x) > 0$.
  Consequently, $f(x)$ is **strictly increasing** on $(0, 1]$.
- **Interval $(1, \infty)$:**
  For $x > 1$, we have $1 - x < 0$, so $f'(x) < 0$.
  Consequently, $f(x)$ is **strictly decreasing** on $[1, \infty)$.

### Step 5: Characterize the extremum and find the zeros
At $x = 1$, the derivative changes sign from positive to negative. Hence, $f$ attains a **strict global maximum** at $x = 1$.
The value at this maximum is:
$$f(1) = \ln(1) - 1 + 1 = 0 - 1 + 1 = 0.$$
Because $f(1) = 0$ is the strict maximum value of the function on the entire domain $(0, \infty)$, we have:
$$f(x) < f(1) = 0 \quad \text{for all } x \in (0, \infty) \setminus \{1\}.$$
Therefore, $x = 1$ is the **only real zero** of the function.

---

## 5. Why Each Step Is Valid
- **Step 1:** The domain of an analytic expression is the largest subset of $\mathbb{R}$ where all component operations are well-defined; the logarithm is undefined for non-positive inputs.
- **Step 2:** The intersection of $(0, \infty)$ (from $\ln x$) and $(-\infty, \infty)$ (from $-x+1$) is $(0, \infty)$.
- **Step 3:** By linearity of the derivative and standard differentiation rules $(\ln x)' = 1/x$ and $(x)' = 1$.
- **Step 4:** On $(0, \infty)$, $x > 0$, so dividing $1 - x$ by a positive quantity preserves the sign of $1 - x$.
- **Step 5:** Because $f$ strictly increases up to $x = 1$ and strictly decreases thereafter, the function cannot cross or touch the horizontal line $y = 0$ at any other point.

---

## 6. Final Answer in Words
The analysis begins with the domain because operations like logarithms are restricted to positive arguments, and examining properties outside the domain is mathematically invalid. 
The domain of $f(x)$ is $D_f = (0, \infty)$. 
The function has a unique critical point at $x = 1$, which is a strict global maximum with value $f(1) = 0$. 
The function is strictly increasing on $(0, 1]$ and strictly decreasing on $[1, \infty)$. 
Because the global maximum value is $0$, the only zero of the function is $x = 1$.

---

## 7. Quick Verification
- **Test point $x = 0.5$ (in $(0, 1)$):**
  $f'(0.5) = \frac{1 - 0.5}{0.5} = \frac{0.5}{0.5} = 1 > 0$ (increasing).
  $f(0.5) = \ln(0.5) - 0.5 + 1 \approx -0.693 + 0.5 = -0.193 < 0$.
- **Test point $x = 2$ (in $(1, \infty)$):**
  $f'(2) = \frac{1 - 2}{2} = -\frac{1}{2} < 0$ (decreasing).
  $f(2) = \ln(2) - 2 + 1 \approx 0.693 - 1 = -0.307 < 0$.
Both test points confirm that the function is strictly negative away from $x = 1$ and obeys the calculated monotonicity signs.

---

## 8. Common Mistakes to Avoid
- **Forgetting the domain restriction:** Considering $x \le 0$, which is completely invalid for the real natural logarithm.
- **Solving $\ln x - x + 1 = 0$ purely algebraically:** Trying to isolate $x$ using elementary algebraic operations is impossible because it is a transcendental equation; monotonicity and the value at the critical point must be used instead.
- **Omitting the denominator when checking the sign of $f'(x)$:** While $x > 0$ here means the denominator does not affect the sign, omitting it as a habit can cause fatal errors in functions where the denominator changes sign.

---

## 9. Classroom Presentation (3-Sentence Summary)
We must first identify the domain as $(0, \infty)$ because the logarithm is undefined for non-positive inputs. Differentiating gives $f'(x) = (1 - x)/x$, which shows the function increases on $(0, 1]$ and decreases on $[1, \infty)$. This makes $x = 1$ a global maximum where $f(1) = 0$, proving that $x = 1$ is the function's only zero.
