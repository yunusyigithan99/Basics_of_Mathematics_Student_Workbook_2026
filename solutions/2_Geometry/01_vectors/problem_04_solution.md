# Problem 4 Solution: Dot Product and Perpendicularity

## 1. Original Problem
For the vectors
$$u = (1, 2, -1) \quad \text{and} \quad v = (2, -1, 3),$$
compute the dot product $u \cdot v$ and determine whether the vectors are perpendicular. Then find the real parameter $a$ so that the vector
$$w = (2, -1, a)$$
is perpendicular to $u$, and check the result.

---

## 2. What We Are Trying to Find
We need to:
1. Compute the dot product $u \cdot v$ using the standard algebraic definition.
2. Evaluate whether $u \cdot v = 0$ to decide whether $u$ and $v$ are orthogonal (perpendicular).
3. Set up the linear equation required for $w \perp u$, namely $w \cdot u = 0$.
4. Solve for the parameter $a$.
5. Verify the solution by plugging $a$ back into $w \cdot u$.

---

## 3. Key Concepts and Theorems
1. **Dot Product (Scalar Product) in $\mathbb{R}^3$:**
   For any vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$, their dot product is the sum of products of corresponding coordinates:
   $$u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3.$$
2. **Geometric Formula for the Dot Product:**
   $$u \cdot v = \|u\| \, \|v\| \cos \theta,$$
   where $\theta \in [0, \pi]$ is the angle between the two vectors.
3. **Orthogonality Criterion:**
   Two non-zero vectors $u$ and $v$ are perpendicular (orthogonal, denoted $u \perp v$) if and only if their angle is $\theta = \frac{\pi}{2}$ ($90^\circ$). Because $\cos(90^\circ) = 0$, this is algebraically equivalent to:
   $$u \perp v \iff u \cdot v = 0.$$
4. If $u \cdot v < 0$, the angle between them is obtuse ($\theta > 90^\circ$). If $u \cdot v > 0$, the angle is acute ($\theta < 90^\circ$).

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $u \cdot v$
Multiply corresponding components of $u = (1, 2, -1)$ and $v = (2, -1, 3)$ and sum:
$$u \cdot v = (1)(2) + (2)(-1) + (-1)(3) = 2 - 2 - 3 = -3.$$

### Step 2: Determine Whether $u$ and $v$ Are Perpendicular
Check the orthogonality criterion:
$$u \cdot v = -3 \neq 0.$$
Because the dot product is not zero (in fact, it is negative, indicating an obtuse angle), the vectors $u$ and $v$ are **not perpendicular**.

### Step 3: Find $a$ Such That $w \perp u$
The vector $w$ is defined as $w = (2, -1, a)$. For $w$ to be perpendicular to $u = (1, 2, -1)$, their dot product must vanish:
$$w \cdot u = 0.$$
Express the dot product algebraically:
$$w \cdot u = (2)(1) + (-1)(2) + (a)(-1) = 2 - 2 - a = -a.$$
Equating to zero:
$$-a = 0 \implies a = 0.$$

### Step 4: Check the Result
Substitute $a = 0$ back into $w$, giving $w = (2, -1, 0)$. Compute the dot product with $u$:
$$w \cdot u = (2)(1) + (-1)(2) + (0)(-1) = 2 - 2 + 0 = 0.$$
Since $w \cdot u = 0$, the vector $w = (2, -1, 0)$ is indeed strictly perpendicular to $u$.

---

## 5. Why Each Step Is Valid
1. **The dot product computation** sums three scalar multiplications, producing a single scalar invariant under coordinate rotations.
2. **The deduction that $u \not\perp v$** follows directly from the biconditional theorem $u \perp v \iff u \cdot v = 0$ for non-zero vectors.
3. **Setting $w \cdot u = 0$** converts the geometric requirement of perpendicularity into a straightforward linear algebraic equation in the single unknown $a$.

---

## 6. Final Answer in Words
The dot product is $u \cdot v = -3$, which means $u$ and $v$ are not perpendicular (they form an obtuse angle). For the vector $w = (2, -1, a)$ to be perpendicular to $u$, the parameter must be $a = 0$, producing the perpendicular vector $w = (2, -1, 0)$, whose dot product with $u$ is verified to be $0$.

---

## 7. Quick Verification
- Angle between $u$ and $v$:
  $$\|u\| = \sqrt{1^2 + 2^2 + (-1)^2} = \sqrt{6}, \quad \|v\| = \sqrt{2^2 + (-1)^2 + 3^2} = \sqrt{14}.$$
  $$\cos \theta = \frac{u \cdot v}{\|u\| \|v\|} = \frac{-3}{\sqrt{84}} \approx -0.3273 < 0 \implies \theta \approx 109.1^\circ \neq 90^\circ.$$
- Check $w \cdot u$ for $w = (2, -1, 0)$:
  $$\|w\| = \sqrt{4 + 1 + 0} = \sqrt{5}.$$
  $$\cos \angle(w, u) = \frac{w \cdot u}{\|w\| \|u\|} = \frac{0}{\sqrt{5}\sqrt{6}} = 0 \implies \angle(w, u) = 90^\circ.$$
  The verification is completely solid.

---

## 8. Common Mistakes to Avoid
- **Outputting a vector instead of a scalar:** Mistaking the dot product $u \cdot v$ for a cross product and writing coordinates instead of a single number.
- **Arithmetic sign drops:** Dropping the negative sign in $(-1)(3) = -3$ or $(-1)(a) = -a$.
- **Confusing condition for perpendicularity:** Setting $u \cdot v = 1$ instead of $u \cdot v = 0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
The dot product of $u$ and $v$ evaluates to $2 - 2 - 3 = -3$, which is non-zero, proving that the two vectors are not perpendicular. To make $w = (2, -1, a)$ perpendicular to $u$, we enforce the orthogonality condition $w \cdot u = 0$, which yields the linear equation $2 - 2 - a = 0$, giving $a = 0$. Plugging $a = 0$ back into $w$ gives $(2, -1, 0)$, whose dot product with $u$ is precisely zero, confirming perpendicularity.

