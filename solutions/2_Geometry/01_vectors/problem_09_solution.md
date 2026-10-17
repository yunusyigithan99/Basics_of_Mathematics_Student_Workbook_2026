# Problem 9 Solution: Cross Product as a Perpendicular Direction

## 1. Original Problem
For the vectors in $\mathbb{R}^3$:
$$u = (1, 2, 0) \quad \text{and} \quad v = (0, 1, 3),$$
compute the cross product $u \times v$. Use dot products to verify perpendicularity to both $u$ and $v$. Then compute $v \times u$, and compare the two results geometrically and algebraically.

---

## 2. What We Are Trying to Find
We are asked to:
1. Compute the cross product vector $u \times v$ using the formal $3 \times 3$ determinant expansion.
2. Check that $(u \times v) \cdot u = 0$ and $(u \times v) \cdot v = 0$.
3. Compute the reversed cross product $v \times u$.
4. Compare $u \times v$ with $v \times u$ to illustrate the anti-commutativity property of the cross product and connect it with the right-hand rule.

---

## 3. Key Concepts and Theorems
1. **Definition of Cross Product:**
   For $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ in $\mathbb{R}^3$, the cross product is given by the formal determinant:
   $$u \times v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} = (u_2 v_3 - u_3 v_2)\mathbf{i} - (u_1 v_3 - u_3 v_1)\mathbf{j} + (u_1 v_2 - u_2 v_1)\mathbf{k}.$$
2. **Orthogonality Property:**
   The vector $u \times v$ is orthogonal to both input vectors $u$ and $v$:
   $$(u \times v) \cdot u = 0 \quad \text{and} \quad (u \times v) \cdot v = 0.$$
3. **Anti-Commutativity:**
   Unlike scalar multiplication or the dot product, the cross product is not commutative; it is anti-commutative:
   $$v \times u = -(u \times v).$$
   Swapping the operands reverses the direction of the resulting normal vector according to the right-hand rule.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $u \times v$
Set up the determinant with unit basis vectors $\mathbf{i}, \mathbf{j}, \mathbf{k}$ in the first row, $u = (1, 2, 0)$ in the second row, and $v = (0, 1, 3)$ in the third row:
$$u \times v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 0 \\ 0 & 1 & 3 \end{vmatrix}.$$
Expand along the first row:
$$u \times v = \mathbf{i} \begin{vmatrix} 2 & 0 \\ 1 & 3 \end{vmatrix} - \mathbf{j} \begin{vmatrix} 1 & 0 \\ 0 & 3 \end{vmatrix} + \mathbf{k} \begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix}.$$
Evaluate each $2 \times 2$ minor determinant:
- $\mathbf{i}$-component: $(2)(3) - (0)(1) = 6 - 0 = 6$
- $\mathbf{j}$-component: $-\big((1)(3) - (0)(0)\big) = -(3 - 0) = -3$
- $\mathbf{k}$-component: $(1)(1) - (2)(0) = 1 - 0 = 1$

Combining these gives:
$$u \times v = (6, -3, 1).$$

### Step 2: Check Perpendicularity Using Dot Products
Check orthogonality with vector $u = (1, 2, 0)$:
$$(u \times v) \cdot u = (6)(1) + (-3)(2) + (1)(0) = 6 - 6 + 0 = 0.$$
Check orthogonality with vector $v = (0, 1, 3)$:
$$(u \times v) \cdot v = (6)(0) + (-3)(1) + (1)(3) = 0 - 3 + 3 = 0.$$
Both dot products are zero, which confirms that $(6, -3, 1)$ is perpendicular to both original vectors.

### Step 3: Compute $v \times u$
Set up the determinant with $v$ in row 2 and $u$ in row 3:
$$v \times u = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 0 & 1 & 3 \\ 1 & 2 & 0 \end{vmatrix}.$$
Expand along row 1:
$$v \times u = \mathbf{i} \begin{vmatrix} 1 & 3 \\ 2 & 0 \end{vmatrix} - \mathbf{j} \begin{vmatrix} 0 & 3 \\ 1 & 0 \end{vmatrix} + \mathbf{k} \begin{vmatrix} 0 & 1 \\ 1 & 2 \end{vmatrix}.$$
Evaluate each component:
- $\mathbf{i}$-component: $(1)(0) - (3)(2) = 0 - 6 = -6$
- $\mathbf{j}$-component: $-\big((0)(0) - (3)(1)\big) = -(0 - 3) = 3$
- $\mathbf{k}$-component: $(0)(2) - (1)(1) = 0 - 1 = -1$

Thus:
$$v \times u = (-6, 3, -1).$$

### Step 4: Compare the Results
Comparing the two vectors:
$$v \times u = (-6, 3, -1) = -(6, -3, 1) = -(u \times v).$$
- **Algebraically:** Swapping rows 2 and 3 in the determinant multiplies the determinant by $-1$, proving anti-commutativity.
- **Geometrically:** Both vectors lie on the exact same perpendicular line to the plane spanned by $u$ and $v$ and have the exact same length ($\sqrt{6^2 + (-3)^2 + 1^2} = \sqrt{46}$). However, they point in opposite directions along that normal line, conforming to the right-hand rule when fingers curl from the first argument to the second.

---

## 5. Why Each Step Is Valid
1. **The formal determinant expansion** correctly computes the vector cross product defined in $\mathbb{R}^3$.
2. **The middle term's negative sign ($-\mathbf{j}$)** corresponds to the cofactor sign $(-1)^{1+2} = -1$ in Laplace expansion.
3. **The property $u \times v = -(v \times u)$** holds universally because swapping two rows of any determinant inverts the sign of the determinant.

---

## 6. Final Answer in Words
The cross product is $u \times v = (6, -3, 1)$. Taking the dot product of this vector with $u$ gives $6 - 6 + 0 = 0$, and with $v$ gives $0 - 3 + 3 = 0$, proving it is perpendicular to both. The reversed cross product is $v \times u = (-6, 3, -1) = -(u \times v)$. The two resulting vectors have the same magnitude and lie on the same normal line, but point in opposite directions due to the anti-commutative nature of the cross product.

---

## 7. Quick Verification
- **Length calculation:**
  $$\|u \times v\| = \sqrt{6^2 + (-3)^2 + 1^2} = \sqrt{36 + 9 + 1} = \sqrt{46}.$$
  $$\|u\| = \sqrt{1^2 + 2^2 + 0^2} = \sqrt{5}, \qquad \|v\| = \sqrt{0^2 + 1^2 + 3^2} = \sqrt{10}.$$
  $$u \cdot v = 1(0) + 2(1) + 0(3) = 2.$$
- **Lagrange's Identity:**
  $$\|u \times v\|^2 = \|u\|^2 \|v\|^2 - (u \cdot v)^2 = (5)(10) - (2)^2 = 50 - 4 = 46.$$
  Since $(\sqrt{46})^2 = 46$, Lagrange's Identity holds exactly!

---

## 8. Common Mistakes to Avoid
- **Forgetting the minus sign on the $\mathbf{j}$-component:** Writing $+\mathbf{j}(1 \cdot 3 - 0 \cdot 0) = +3\mathbf{j}$ instead of $-3\mathbf{j}$.
- **Assuming commutativity:** Writing $u \times v = v \times u$, forgetting that cross product is anti-commutative.
- **Applying cross product in $\mathbb{R}^2$:** Cross product produces a 3D vector and is defined exclusively in 3-dimensional space (and 7 dimensions).

---

## 9. Classroom Presentation (3-Sentence Summary)
Using the standard determinant formula, the cross product of $u$ and $v$ evaluates to $(6, -3, 1)$. We confirm that this vector is orthogonal to the inputs by checking that its dot products with both $u$ and $v$ equal zero. Reversing the order yields $v \times u = (-6, 3, -1)$, illustrating that the cross product is anti-commutative and that swapping inputs inverts the vector's direction via the right-hand rule.

