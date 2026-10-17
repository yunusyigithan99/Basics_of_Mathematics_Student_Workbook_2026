# Problem 5 Solution: Angle Between Vectors

## 1. Original Problem
Given the vectors in $\mathbb{R}^3$:
$$u = (1, 1, 0) \quad \text{and} \quad v = (1, 0, 1),$$

1. Use the sign of the dot product $u \cdot v$ to predict the type of angle (acute, right, or obtuse).
2. Compute the exact angle between the vectors in radians and degrees.
3. Compare the calculated result with the initial prediction.

---

## 2. What We Are Trying to Find
We are asked to:
1. Calculate the scalar product $u \cdot v$ and determine whether its sign is positive, zero, or negative to classify the angle type qualitatively before calculating.
2. Calculate the lengths $\|u\|$ and $\|v\|$.
3. Evaluate $\cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|}$ and invert the cosine to find the exact angle $\theta$.
4. Check that the quantitative angle matches the qualitative prediction.

---

## 3. Key Concepts and Theorems
1. **Geometric Formula for Dot Product:**
   For non-zero vectors $u$ and $v$,
   $$u \cdot v = \|u\| \, \|v\| \cos \theta \implies \cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|},$$
   where $\theta \in [0, \pi]$ is the interior angle between the vectors.
2. **Qualitative Classification by Sign:**
   Since lengths $\|u\| > 0$ and $\|v\| > 0$ are always strictly positive:
   - If $u \cdot v > 0 \iff \cos \theta > 0 \iff 0 \le \theta < \frac{\pi}{2}$ ($0^\circ \le \theta < 90^\circ$), the angle is **acute**.
   - If $u \cdot v = 0 \iff \cos \theta = 0 \iff \theta = \frac{\pi}{2}$ ($\theta = 90^\circ$), the angle is **right** (orthogonal).
   - If $u \cdot v < 0 \iff \cos \theta < 0 \iff \frac{\pi}{2} < \theta \le \pi$ ($90^\circ < \theta \le 180^\circ$), the angle is **obtuse**.
3. **Special Cosine Values:**
   Recall from standard trigonometry that $\cos\left(\frac{\pi}{3}\right) = \cos(60^\circ) = \frac{1}{2}$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $u \cdot v$ and Predict Angle Type
Evaluate the dot product of $u = (1, 1, 0)$ and $v = (1, 0, 1)$:
$$u \cdot v = (1)(1) + (1)(0) + (0)(1) = 1 + 0 + 0 = 1.$$
Since $u \cdot v = 1 > 0$, the cosine of the angle between them must be strictly positive:
$$\cos \theta > 0.$$
Therefore, we predict that the angle between $u$ and $v$ is **acute** (strictly between $0^\circ$ and $90^\circ$).

### Step 2: Compute the Lengths of $u$ and $v$
Calculate the Euclidean norm for each vector:
$$\|u\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{1 + 1 + 0} = \sqrt{2},$$
$$\|v\| = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{1 + 0 + 1} = \sqrt{2}.$$

### Step 3: Compute the Angle $\theta$
Substitute $u \cdot v = 1$, $\|u\| = \sqrt{2}$, and $\|v\| = \sqrt{2}$ into the angle formula:
$$\cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|} = \frac{1}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2}.$$
Since the geometric angle between two vectors lies in the interval $[0, \pi]$, we solve:
$$\theta = \arccos\left(\frac{1}{2}\right) = \frac{\pi}{3} \text{ radians} = 60^\circ.$$

### Step 4: Compare with the Prediction
The exact value obtained is $\theta = 60^\circ$ (or $\pi/3$ rad). Since $0^\circ < 60^\circ < 90^\circ$, this is indeed an acute angle. The quantitative computation confirms our qualitative prediction derived from the sign of the dot product.

---

## 5. Why Each Step Is Valid
1. **Predicting by sign** is valid because the norm factors in the denominator of $\cos \theta = \frac{u \cdot v}{\|u\| \|v\|}$ are strictly positive real numbers, meaning $\operatorname{sgn}(\cos \theta) = \operatorname{sgn}(u \cdot v)$.
2. **Computing the norms** uses standard Euclidean distance from the origin.
3. **Inverting the cosine function** over $[0, \pi]$ is well-defined because $\cos$ is strictly decreasing and bijective on $[0, \pi]$.

---

## 6. Final Answer in Words
Because the dot product $u \cdot v = 1$ is positive, the angle is predicted to be acute. Computing the lengths $\|u\| = \sqrt{2}$ and $\|v\| = \sqrt{2}$ gives $\cos \theta = \frac{1}{2}$, which yields an exact angle of $\theta = \frac{\pi}{3}$ radians (or $60^\circ$). This confirms that the angle is acute, in complete agreement with the sign prediction.

---

## 7. Quick Verification
- **Law of Cosines on the vector triangle:**
  Construct the difference vector $w = u - v = (1 - 1, 1 - 0, 0 - 1) = (0, 1, -1)$.
  Its squared length is $\|u - v\|^2 = 0^2 + 1^2 + (-1)^2 = 2$.
  By the Law of Cosines:
  $$\|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2\|u\|\|v\|\cos\theta \implies 2 = 2 + 2 - 2(\sqrt{2})(\sqrt{2})\cos\theta \implies 2 = 4 - 4\cos\theta \implies 4\cos\theta = 2 \implies \cos\theta = \frac{1}{2}.$$
  This confirms $\theta = 60^\circ$ independently.

---

## 8. Common Mistakes to Avoid
- **Omitting the denominator:** Computing $u \cdot v = 1$ and mistakenly concluding that $\cos \theta = 1$ (which would imply $\theta = 0^\circ$). One must always divide by the product of the magnitudes $\|u\| \|v\|$.
- **Unit confusion:** Mixing up radians and degrees (e.g., stating the angle is $\pi/3$ degrees).
- **Misidentifying the sign of the dot product:** Multiplying $0 \times 1 = 1$ instead of $0$.

---

## 9. Classroom Presentation (3-Sentence Summary)
First, we find the dot product $u \cdot v = 1$, which is positive, immediately indicating that the angle between the two vectors must be acute. Next, dividing this dot product by the product of their lengths, $\sqrt{2} \cdot \sqrt{2} = 2$, yields $\cos \theta = 1/2$. Inverting the cosine gives an exact angle of $\pi/3$ radians or $60^\circ$, which perfectly validates our initial qualitative prediction.

