# Problem 15 Solution: Comparing Directions Using the Cosine of the Angle

## 1. Original Problem
Given the three vectors in $\mathbb{R}^3$:
$$a = (1, 2, 1), \qquad b = (2, 4, 2), \qquad c = (2, 0, 3).$$
For each distinct pair of vectors, compute the directional cosine:
$$\cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|}.$$
Order the pairs by increasing angle between the vectors. Explain why for $a$ and $b$ the computed value is exactly $1$ even though the vectors have different lengths.

---

## 2. What We Are Trying to Find
We need to:
1. Compute the lengths $\|a\|$, $\|b\|$, and $\|c\|$.
2. Calculate the dot products and directional cosines for all three pairs: $(a, b)$, $(a, c)$, and $(b, c)$.
3. Determine the angles $\theta$ in degrees and radians.
4. Order the pairs from smallest angle to largest angle.
5. Provide the geometric explanation of why $\cos\theta = 1$ occurs for vectors of different lengths.

---

## 3. Key Concepts and Theorems
1. **Cosine Formula for the Angle Between Two Vectors:**
   For any non-zero vectors $u$ and $v$:
   $$\cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|}, \quad \text{where } \theta \in [0, \pi].$$
2. **Monotonicity of Cosine:**
   The cosine function is strictly decreasing on the interval $[0, \pi]$. Therefore:
   $$\text{A larger value of } \cos \theta \iff \text{a smaller angle } \theta.$$
3. **Collinear Vectors with the Same Sense:**
   If $v = k\,u$ with scalar $k > 0$, then:
   $$\cos \theta = \frac{u \cdot (k\,u)}{\|u\| \, \|k\,u\|} = \frac{k (u \cdot u)}{k \|u\|^2} = \frac{\|u\|^2}{\|u\|^2} = 1.$$
   This corresponds to an angle of $\theta = 0^\circ$. The dot product normalized by the magnitudes measures purely the angle/direction, completely invariant under positive rescaling of either vector.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Euclidean Norms of $a$, $b$, and $c$
- For $a = (1, 2, 1)$:
  $$\|a\| = \sqrt{1^2 + 2^2 + 1^2} = \sqrt{1 + 4 + 1} = \sqrt{6}.$$
- For $b = (2, 4, 2)$:
  $$\|b\| = \sqrt{2^2 + 4^2 + 2^2} = \sqrt{4 + 16 + 4} = \sqrt{24} = 2\sqrt{6}.$$
- For $c = (2, 0, 3)$:
  $$\|c\| = \sqrt{2^2 + 0^2 + 3^2} = \sqrt{4 + 0 + 9} = \sqrt{13}.$$

### Step 2: Analyze Pair $(a, b)$
Compute the dot product:
$$a \cdot b = (1)(2) + (2)(4) + (1)(2) = 2 + 8 + 2 = 12.$$
Compute the cosine:
$$\cos \theta_{ab} = \frac{a \cdot b}{\|a\| \, \|b\|} = \frac{12}{\sqrt{6} \cdot \sqrt{24}} = \frac{12}{\sqrt{144}} = \frac{12}{12} = 1.$$
Angle:
$$\theta_{ab} = \arccos(1) = 0^\circ \text{ (or } 0 \text{ rad)}.$$

### Step 3: Analyze Pair $(a, c)$
Compute the dot product:
$$a \cdot c = (1)(2) + (2)(0) + (1)(3) = 2 + 0 + 3 = 5.$$
Compute the cosine:
$$\cos \theta_{ac} = \frac{a \cdot c}{\|a\| \, \|c\|} = \frac{5}{\sqrt{6} \cdot \sqrt{13}} = \frac{5}{\sqrt{78}} \approx \frac{5}{8.83176} \approx 0.5661.$$
Angle:
$$\theta_{ac} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 0.969 \text{ rad} \approx 55.52^\circ.$$

### Step 4: Analyze Pair $(b, c)$
Compute the dot product:
$$b \cdot c = (2)(2) + (4)(0) + (2)(3) = 4 + 0 + 6 = 10.$$
Compute the cosine:
$$\cos \theta_{bc} = \frac{b \cdot c}{\|b\| \, \|c\|} = \frac{10}{2\sqrt{6} \cdot \sqrt{13}} = \frac{10}{2\sqrt{78}} = \frac{5}{\sqrt{78}} \approx 0.5661.$$
Angle:
$$\theta_{bc} = \arccos\left(\frac{5}{\sqrt{78}}\right) \approx 0.969 \text{ rad} \approx 55.52^\circ.$$

### Step 5: Order the Pairs by Increasing Angle
Arranging by increasing $\theta$ (or equivalently, by decreasing $\cos \theta$):
1. **Pair $(a, b)$:** $\theta_{ab} = 0^\circ$ ($\cos \theta = 1$).
2. **Pair $(a, c)$ and Pair $(b, c)$ (tied):** $\theta_{ac} = \theta_{bc} \approx 55.52^\circ$ ($\cos \theta = \frac{5}{\sqrt{78}} \approx 0.5661$).

### Step 6: Explain Why $\cos \theta_{ab} = 1$ Despite Different Lengths
- Notice that $b = (2, 4, 2) = 2(1, 2, 1) = 2a$.
- The vector $b$ is a scalar multiple of $a$ with a positive constant $k = 2$.
- The ratio $\frac{u \cdot v}{\|u\| \|v\|}$ is mathematically constructed to isolate **directional alignment** from **magnitude**:
  $$\frac{u \cdot v}{\|u\| \|v\|} = \left(\frac{u}{\|u\|}\right) \cdot \left(\frac{v}{\|v\|}\right) = e_u \cdot e_v.$$
- Since both vectors point along the exact same line in space with the exact same forward orientation, their unit direction vectors are identical: $e_a = e_b$.
- The dot product of a unit vector with itself is always $e_a \cdot e_a = \|e_a\|^2 = 1^2 = 1$.
- Thus, the cosine is $1$ because the angle between co-directional vectors is $0^\circ$, completely independent of how long each vector is.

---

## 5. Why Each Step Is Valid
1. **The Cauchy-Schwarz inequality** guarantees that $\left|\frac{u \cdot v}{\|u\| \|v\|}\right| \le 1$, with equality to $+1$ holding if and only if $v = k\,u$ for some positive scalar $k > 0$.
2. **Factoring $b = 2a$** explains why pairs $(a, c)$ and $(b, c)$ produce the exact same angle: replacing $a$ with $2a$ doubles both the numerator and the denominator, leaving the ratio invariant.
3. **The inverse cosine function** is strictly decreasing on $[-1, 1]$, making the angle ordering well-defined.

---

## 6. Final Answer in Words
The directional cosines are $\cos \theta_{ab} = 1$, $\cos \theta_{ac} = \frac{5}{\sqrt{78}} \approx 0.5661$, and $\cos \theta_{bc} = \frac{5}{\sqrt{78}} \approx 0.5661$. Ordered by increasing angle:
$$\theta_{ab} = 0^\circ < \theta_{ac} = \theta_{bc} \approx 55.52^\circ.$$
The cosine for pair $(a, b)$ equals $1$ because $b = 2a$ points in the exact same direction as $a$. The normalization divides out the vector lengths, leaving only the relative angle, which is $0^\circ$.

---

## 7. Quick Verification
- Check with unit vectors:
  $$e_a = \frac{1}{\sqrt{6}}(1, 2, 1), \quad e_b = \frac{1}{2\sqrt{6}}(2, 4, 2) = \frac{1}{\sqrt{6}}(1, 2, 1) = e_a.$$
  $$e_a \cdot e_b = e_a \cdot e_a = 1 \implies \theta_{ab} = 0^\circ.$$
- Unit vector $e_c = \frac{1}{\sqrt{13}}(2, 0, 3)$.
  $$e_a \cdot e_c = \frac{1}{\sqrt{78}}\big(1(2) + 2(0) + 1(3)\big) = \frac{5}{\sqrt{78}}.$$
  $$e_b \cdot e_c = e_a \cdot e_c = \frac{5}{\sqrt{78}}.$$
  The calculations are completely verified.

---

## 8. Common Mistakes to Avoid
- **Thinking $\cos \theta = 1$ means equal vectors:** Concluding that $a = b$. The cosine measures direction, not length.
- **Inverting the ordering:** Sorting by increasing cosine rather than increasing angle (since larger cosine means smaller angle).
- **Neglecting to simplify $\sqrt{6}\sqrt{24} = \sqrt{144} = 12$:** Leading to complicated expressions instead of recognizing the exact integer 1.

---

## 9. Classroom Presentation (3-Sentence Summary)
Computing $(u \cdot v) / (\|u\| \|v\|)$ for the three pairs yields $\cos \theta_{ab} = 1$, while both $(a, c)$ and $(b, c)$ yield $5/\sqrt{78} \approx 0.5661$. Ordering by increasing angle gives $\theta_{ab} = 0^\circ$ first, followed by the tied angles $\theta_{ac} = \theta_{bc} \approx 55.52^\circ$. The cosine for $a$ and $b$ is exactly $1$ because $b = 2a$ shares the exact same spatial direction as $a$, and dividing by vector lengths normalizes away their differing magnitudes.

