# Exercise 14: Rotation Matrices

## 1. Original Problem
The matrix for a rotation through an angle $\theta$ is:
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$
Compute $R(\alpha)R(\beta)$ and, using the angle-sum formulas for sine and cosine, show that:
$$R(\alpha)R(\beta) = R(\alpha + \beta)$$
Explain the result geometrically.

---

## 2. What We Are Trying to Find
We need to:
- Formulate the rotation matrices $R(\alpha)$ and $R(\beta)$ for angles $\alpha$ and $\beta$.
- Multiply the two matrices together using the standard row-by-column product rule.
- Apply the trigonometric angle-sum identities for sine and cosine to simplify all four entries of the product matrix.
- Prove algebraically that the product matrix matches $R(\alpha + \beta)$ in every entry.
- Give a clear geometric explanation of why rotating by $\beta$ and then by $\alpha$ is identical to a single rotation by $\alpha + \beta$.

---

## 3. Key Concepts and Theorems
1. **2D Rotation Matrix $R(\theta)$:**
   The standard matrix for a counterclockwise rotation by angle $\theta$ about the origin in $\mathbb{R}^2$ is:
   $$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$
2. **Trigonometric Angle-Sum Identities:**
   - **Cosine sum formula:**
     $$\cos(\alpha + \beta) = \cos\alpha \cos\beta - \sin\alpha \sin\beta$$
   - **Sine sum formula:**
     $$\sin(\alpha + \beta) = \sin\alpha \cos\beta + \cos\alpha \sin\beta$$
3. **Geometric Composition:**
   Applying linear transformation $T_2$ followed by linear transformation $T_1$ corresponds algebraically to multiplying their matrices $M_1 M_2$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Write Down the Matrices
$$R(\alpha) = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix}, \qquad R(\beta) = \begin{pmatrix} \cos\beta & -\sin\beta \\ \sin\beta & \cos\beta \end{pmatrix}$$

---

### Step 2: Multiply $R(\alpha)$ by $R(\beta)$
Set up the matrix product:
$$R(\alpha)R(\beta) = \begin{pmatrix} \cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha \end{pmatrix} \begin{pmatrix} \cos\beta & -\sin\beta \\ \sin\beta & \cos\beta \end{pmatrix}$$

Calculate each entry individually:

1. **Top-left entry $(1, 1)$:**
   $$(\text{Row 1 of } R(\alpha)) \cdot (\text{Column 1 of } R(\beta)) = (\cos\alpha)(\cos\beta) + (-\sin\alpha)(\sin\beta)$$
   $$= \cos\alpha \cos\beta - \sin\alpha \sin\beta$$

2. **Top-right entry $(1, 2)$:**
   $$(\text{Row 1 of } R(\alpha)) \cdot (\text{Column 2 of } R(\beta)) = (\cos\alpha)(-\sin\beta) + (-\sin\alpha)(\cos\beta)$$
   $$= -(\sin\alpha \cos\beta + \cos\alpha \sin\beta)$$

3. **Bottom-left entry $(2, 1)$:**
   $$(\text{Row 2 of } R(\alpha)) \cdot (\text{Column 1 of } R(\beta)) = (\sin\alpha)(\cos\beta) + (\cos\alpha)(\sin\beta)$$
   $$= \sin\alpha \cos\beta + \cos\alpha \sin\beta$$

4. **Bottom-right entry $(2, 2)$:**
   $$(\text{Row 2 of } R(\alpha)) \cdot (\text{Column 2 of } R(\beta)) = (\sin\alpha)(-\sin\beta) + (\cos\alpha)(\cos\beta)$$
   $$= \cos\alpha \cos\beta - \sin\alpha \sin\beta$$

---

### Step 3: Apply the Angle-Sum Formulas
Substitute the trigonometric identities into the four simplified expressions:
- For entries $(1, 1)$ and $(2, 2)$:
  $$\cos\alpha \cos\beta - \sin\alpha \sin\beta = \cos(\alpha + \beta)$$
- For entry $(2, 1)$:
  $$\sin\alpha \cos\beta + \cos\alpha \sin\beta = \sin(\alpha + \beta)$$
- For entry $(1, 2)$:
  $$-(\sin\alpha \cos\beta + \cos\alpha \sin\beta) = -\sin(\alpha + \beta)$$

Substituting these into the matrix yields:
$$R(\alpha)R(\beta) = \begin{pmatrix} \cos(\alpha + \beta) & -\sin(\alpha + \beta) \\ \sin(\alpha + \beta) & \cos(\alpha + \beta) \end{pmatrix}$$

By definition of the rotation matrix for an arbitrary angle, this is precisely:
$$R(\alpha)R(\beta) = R(\alpha + \beta)$$

---

### Step 4: Geometric Explanation
- When we apply the matrix product $(R(\alpha)R(\beta))\mathbf{x} = R(\alpha)(R(\beta)\mathbf{x})$ to any vector $\mathbf{x} \in \mathbb{R}^2$, the transformation proceeds in two stages:
  1. $R(\beta)$ rotates the vector around the origin by an angle $\beta$.
  2. $R(\alpha)$ takes that already-rotated vector and rotates it further by an additional angle $\alpha$ in the same direction.
- In Euclidean geometry, rotating an object about the origin by angle $\beta$ and immediately rotating the result by angle $\alpha$ simply accumulates the total angular displacement to $\alpha + \beta$.
- Therefore, the composite transformation is a single pure rotation through angle $\alpha + \beta$. Since a linear map on $\mathbb{R}^2$ has a unique matrix representation, the algebraic product $R(\alpha)R(\beta)$ must equal $R(\alpha + \beta)$.
- Moreover, since $\alpha + \beta = \beta + \alpha$, rotation matrices in 2D commute: $R(\alpha)R(\beta) = R(\beta)R(\alpha)$.

---

## 5. Why Each Step Is Valid
- **Linear Representation of Isometries:** Planar rotations preserve lengths and angles (they are orthogonal transformations with determinant $+1$), so the composition of two rotations is itself an isometry with determinant $+1$ (a pure rotation).
- **Exact Trigonometric Equivalence:** The angle-sum identities are exact geometric theorems derived from the unit circle, guaranteeing that the algebraic matrix entries match the definition of $R(\alpha + \beta)$ without approximation.

---

## 6. Final Answer in Words
Multiplying the rotation matrices $R(\alpha)$ and $R(\beta)$ and simplifying the entries using the trigonometric sum identities for sine and cosine produces the matrix $\begin{pmatrix} \cos(\alpha+\beta) & -\sin(\alpha+\beta) \\ \sin(\alpha+\beta) & \cos(\alpha+\beta) \end{pmatrix}$, which is exactly $R(\alpha + \beta)$. Geometrically, this expresses the intuitive fact that rotating a vector counterclockwise by angle $\beta$ and then rotating it further by angle $\alpha$ is identical to a single rotation through the combined angle $\alpha + \beta$.

---

## 7. Quick Verification
- **Testing with specific angles ($\alpha = 90^\circ = \frac{\pi}{2}$, $\beta = 90^\circ = \frac{\pi}{2}$):**
  $$R(90^\circ) = \begin{pmatrix} \cos 90^\circ & -\sin 90^\circ \\ \sin 90^\circ & \cos 90^\circ \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
  Compute the product:
  $$R(90^\circ)R(90^\circ) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$$
  Formula prediction:
  $$R(90^\circ + 90^\circ) = R(180^\circ) = \begin{pmatrix} \cos 180^\circ & -\sin 180^\circ \\ \sin 180^\circ & \cos 180^\circ \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} \quad \checkmark$$
- **Determinant property:**
  $\det(R(\alpha)) = \cos^2\alpha + \sin^2\alpha = 1$.
  $\det(R(\alpha)R(\beta)) = \det(R(\alpha))\det(R(\beta)) = 1 \cdot 1 = 1 = \det(R(\alpha+\beta)) \quad \checkmark$

---

## 8. Common Mistakes to Avoid
- **Sign Error on the Off-Diagonal Sine:** Forgetting the minus sign on the top-right entry when evaluating $(1, 2)$, leading to a mistaken positive sign.
- **Misremembering the Cosine Sum Identity:** Thinking $\cos(\alpha+\beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$ with a plus sign instead of a minus sign.
- **Assuming Commutativity Holds for All 3D Rotations:** While 2D rotation matrices commute ($R(\alpha)R(\beta) = R(\beta)R(\alpha)$), rotations in three dimensions around different axes do not commute in general.

---

## 9. Classroom Presentation (3-Sentence Summary)
"By carrying out the row-by-column multiplication of $R(\alpha)$ and $R(\beta)$, the entries naturally group into the classical angle-sum formulas for cosine and sine, yielding the rotation matrix $R(\alpha+\beta)$. Geometrically, this confirms that performing two successive rotations by angles $\beta$ and $\alpha$ simply accumulates the total rotation angle to $\alpha+\beta$. This elegant calculation shows that the abstract algebra of matrix multiplication perfectly mirrors the physical reality of composing planar rotations."

