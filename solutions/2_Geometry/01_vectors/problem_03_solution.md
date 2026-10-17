# Problem 3 Solution: Vector Normalization

## 1. Original Problem
For the 2D vector
$$v = (3, 4),$$
find a unit vector $e$ with the same direction and orientation. Check that $\|e\| = 1$, reconstruct $v$ in the form $v = \|v\|e$, and explain what changes during normalization and what remains unchanged.

---

## 2. What We Are Trying to Find
We need to:
1. Calculate the Euclidean norm (magnitude) $\|v\|$.
2. Construct the unit vector $e$ in the direction of $v$ via the normalization formula $e = \frac{v}{\|v\|}$.
3. Verify by direct computation that the length of $e$ is strictly equal to $1$.
4. Reconstruct the original vector by multiplying the unit vector $e$ by the scalar magnitude $\|v\|$.
5. Explain conceptually what geometric properties change (magnitude) and what properties stay the same (direction and orientation) during normalization.

---

## 3. Key Concepts and Theorems
1. **Vector Length (Euclidean Norm in $\mathbb{R}^2$):**
   For any vector $v = (x, y)$, its length is:
   $$\|v\| = \sqrt{x^2 + y^2}.$$
2. **Unit Vector and Normalization:**
   A unit vector is any vector with length equal to $1$. Given any non-zero vector $v \neq \mathbf{0}$, dividing the vector by its own length produces a unit vector pointing in the same direction:
   $$e = \frac{v}{\|v\|} = \left(\frac{x}{\|v\|}, \; \frac{y}{\|v\|}\right).$$
3. **Decomposition into Magnitude and Direction:**
   Every non-zero vector can be factored uniquely into a product of a positive scalar (its length) and a unit vector (its pure directional information):
   $$v = \|v\| e.$$
4. **Homogeneity of Norms:**
   For any scalar $c \in \mathbb{R}$ and vector $v$, $\|c\,v\| = |c| \, \|v\|$. When $c = \frac{1}{\|v\|} > 0$, we have:
   $$\|e\| = \left\| \frac{1}{\|v\|} v \right\| = \frac{1}{\|v\|} \|v\| = 1.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Length of $v$
Given $v = (3, 4)$, we compute:
$$\|v\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5.$$
The length of vector $v$ is $5$.

### Step 2: Construct the Unit Vector $e$
Divide each coordinate of $v$ by the scalar length $\|v\| = 5$:
$$e = \frac{v}{\|v\|} = \frac{1}{5}(3, 4) = \left(\frac{3}{5}, \; \frac{4}{5}\right) = (0.6, \; 0.8).$$

### Step 3: Verify That $\|e\| = 1$
Calculate the Euclidean norm of the normalized vector $e$:
$$\|e\| = \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2} = \sqrt{\frac{9}{25} + \frac{16}{25}} = \sqrt{\frac{25}{25}} = \sqrt{1} = 1.$$
The condition $\|e\| = 1$ is verified.

### Step 4: Reconstruct $v$ in the Form $v = \|v\|e$
Multiply the unit vector $e$ by the magnitude $\|v\| = 5$:
$$\|v\| e = 5 \cdot \left(\frac{3}{5}, \; \frac{4}{5}\right) = \left(5 \cdot \frac{3}{5}, \; 5 \cdot \frac{4}{5}\right) = (3, 4) = v.$$
The original vector $v$ is recovered.

### Step 5: What Changes and What Remains Unchanged
- **What changes:**
  The **magnitude (length)** changes. The original vector has length $\|v\| = 5$, whereas the normalized vector has length $\|e\| = 1$. The scale factor applied is $\frac{1}{5}$.
- **What remains unchanged:**
  The **direction** (the infinite straight line on which the vector lies) and the **orientation** (the forward sense along that line, pointing into the first quadrant) remain completely identical. Because the scaling factor $\frac{1}{5} > 0$ is positive, the angle with the positive $x$-axis remains $\theta = \arctan(4/3) \approx 53.13^\circ$.

---

## 5. Why Each Step Is Valid
1. **Division by $\|v\|$** is valid because $\|v\| = 5 \neq 0$ (the zero vector cannot be normalized).
2. **Multiplying by positive scalar $\frac{1}{5}$** preserves the sign and ratio of the components, ensuring the slope $\frac{y}{x} = \frac{4/5}{3/5} = \frac{4}{3}$ is unchanged.
3. **The norm calculation** uses exact fraction arithmetic ($\frac{9}{25} + \frac{16}{25} = 1$), avoiding rounding issues.

---

## 6. Final Answer in Words
The unit vector in the direction of $v = (3, 4)$ is $e = \left(\frac{3}{5}, \frac{4}{5}\right)$ or $(0.6, 0.8)$. Its length is verified to be $\|e\| = 1$. Multiplying this unit vector by the scalar magnitude $5$ reconstructs $v = 5\left(\frac{3}{5}, \frac{4}{5}\right) = (3, 4)$. Normalization scales the length of the vector to $1$ while leaving its spatial direction and positive orientation completely unchanged.

---

## 7. Quick Verification
- Compute the angle $\theta$ for both vectors:
  $$\tan \theta_v = \frac{4}{3}, \qquad \tan \theta_e = \frac{4/5}{3/5} = \frac{4}{3}.$$
  Since both vectors lie in the first quadrant ($x > 0, y > 0$), they have the exact same angle $\theta \approx 0.9273\text{ rad} \approx 53.13^\circ$.
- Dot product of $v$ and $e$:
  $$v \cdot e = 3 \cdot \frac{3}{5} + 4 \cdot \frac{4}{5} = \frac{9 + 16}{5} = \frac{25}{5} = 5 = \|v\|.$$
  Since $v \cdot e = \|v\| \|e\| \cos(0^\circ) = 5 \cdot 1 \cdot 1 = 5$, the vectors are perfectly collinear and co-directed.

---

## 8. Common Mistakes to Avoid
- **Subtracting 1 instead of dividing:** Thinking that to make the length 1, one should subtract $4$ from the components. Normalization requires scalar division (multiplication by $\frac{1}{\|v\|}$), not subtraction.
- **Normalizing coordinates independently:** Dividing $x$ by $x$ and $y$ by $y$ to get $(1, 1)$, whose length is $\sqrt{2} \neq 1$. Both components must be divided by the common norm $\|v\|$.
- **Forgetting that $\|v\|e$ must equal $v$:** Miscalculating fractions so that the product no longer returns the original coordinates.

---

## 9. Classroom Presentation (3-Sentence Summary)
To normalize the vector $v = (3, 4)$, we first compute its length using the Pythagorean theorem, which gives $\|v\| = \sqrt{3^2 + 4^2} = 5$. Dividing each coordinate by $5$ produces the unit vector $e = (3/5, 4/5)$, whose norm is verified to be exactly $1$. Normalization separates a vector into its pure directional carrier of unit length and its scalar magnitude, leaving the line of action and orientation untouched.

