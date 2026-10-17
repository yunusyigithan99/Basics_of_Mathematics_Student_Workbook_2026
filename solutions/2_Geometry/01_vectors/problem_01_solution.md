# Problem 1 Solution: Vector Operations and Their Meaning

## 1. Original Problem
For the vectors
$$u = (2, -1, 3) \quad \text{and} \quad v = (-1, 4, 2)$$
compute:
$$u + v, \qquad u - v, \qquad 3u - 2v.$$
Then verify that
$$(u + v) - v = u,$$
and explain geometrically what adding two vectors means.

---

## 2. What We Are Trying to Find
We are asked to:
1. Calculate the vector sum $u + v$ component by component.
2. Calculate the vector difference $u - v$ component by component.
3. Compute the linear combination $3u - 2v$ by performing scalar multiplications followed by vector subtraction.
4. Verify the algebraic identity $(u + v) - v = u$ explicitly using the calculated coordinates.
5. Provide a clear geometric interpretation of vector addition (the triangle/head-to-tail rule and parallelogram rule).

---

## 3. Key Concepts and Theorems
1. **Vector Addition in $\mathbb{R}^3$:**
   Given two vectors $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$, their sum is formed by adding corresponding components:
   $$u + v = (u_1 + v_1, \; u_2 + v_2, \; u_3 + v_3).$$
2. **Vector Subtraction in $\mathbb{R}^3$:**
   Subtracting $v$ from $u$ is equivalent to subtracting corresponding coordinates:
   $$u - v = (u_1 - v_1, \; u_2 - v_2, \; u_3 - v_3).$$
3. **Scalar Multiplication:**
   Multiplying a vector by a real number $c \in \mathbb{R}$ scales each coordinate by $c$:
   $$c\,u = (c\,u_1, \; c\,u_2, \; c\,u_3).$$
4. **Geometric Interpretation of Addition:**
   Geometrically, a vector represents a translation or displacement in space. Placing the initial point (tail) of vector $v$ at the terminal point (head) of vector $u$, the sum $u + v$ is the directed line segment connecting the tail of $u$ directly to the head of $v$ (the triangle law). Alternatively, if both originate from the same point, $u + v$ forms the main diagonal of the parallelogram spanned by $u$ and $v$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $u + v$
Add corresponding components of $u = (2, -1, 3)$ and $v = (-1, 4, 2)$:
$$u + v = \big(2 + (-1), \; -1 + 4, \; 3 + 2\big) = (1, 3, 5).$$

### Step 2: Compute $u - v$
Subtract each component of $v$ from the corresponding component of $u$:
$$u - v = \big(2 - (-1), \; -1 - 4, \; 3 - 2\big) = (3, -5, 1).$$

### Step 3: Compute $3u - 2v$
First, scale $u$ by $3$ and $v$ by $2$:
$$3u = 3 \cdot (2, -1, 3) = (6, -3, 9),$$
$$2v = 2 \cdot (-1, 4, 2) = (-2, 8, 4).$$
Now subtract $2v$ from $3u$:
$$3u - 2v = \big(6 - (-2), \; -3 - 8, \; 9 - 4\big) = (8, -11, 5).$$

### Step 4: Verify that $(u + v) - v = u$
Take our result $u + v = (1, 3, 5)$ and subtract $v = (-1, 4, 2)$:
$$(u + v) - v = \big(1 - (-1), \; 3 - 4, \; 5 - 2\big) = (2, -1, 3).$$
Comparing this with the original vector $u = (2, -1, 3)$, we see:
$$(u + v) - v = u.$$
The identity holds exactly.

### Step 5: Geometric Meaning of Vector Addition
A vector represents a displacement in space. When we add vector $v$ to vector $u$:
- **Triangle / Head-to-Tail Rule:** Starting from an arbitrary origin point $O$, we translate along vector $u$ to point $P$. Then, starting from point $P$, we perform a second displacement along vector $v$ to reach point $Q$. The sum vector $u + v$ represents the net resultant displacement directly from the initial point $O$ to the final point $Q$.
- **Parallelogram Rule:** If vectors $u$ and $v$ originate from the common initial point $O$, they define two adjacent sides of a parallelogram. The vector sum $u + v$ corresponds to the directed diagonal of this parallelogram starting from the shared tail $O$.

---

## 5. Why Each Step Is Valid
1. **Componentwise addition and subtraction** are valid because the vector space $\mathbb{R}^3$ is defined with standard coordinate-wise operations inherited from real number arithmetic.
2. **Scalar multiplication before subtraction** follows standard algebraic order of operations, where scaling distributes across coordinates.
3. **The cancellation $(u + v) - v = u$** is valid by the group properties of vector spaces: $(u + v) - v = u + (v - v) = u + \mathbf{0} = u$, proving that vector subtraction is the exact inverse operation of vector addition.

---

## 6. Final Answer in Words
The sum of the vectors is $u + v = (1, 3, 5)$, the difference is $u - v = (3, -5, 1)$, and the linear combination is $3u - 2v = (8, -11, 5)$. The identity $(u + v) - v = u$ is confirmed because $(1, 3, 5) - (-1, 4, 2) = (2, -1, 3) = u$. Geometrically, adding two vectors corresponds to chaining displacements head-to-tail, yielding the total net translation between the initial and terminal points.

---

## 7. Quick Verification
- **Coordinate check for linear combination:**
  $$(3u - 2v) + 2v = (8, -11, 5) + (-2, 8, 4) = (6, -3, 9) = 3(2, -1, 3) = 3u.$$
  This matches $3u$ perfectly.
- **Difference check:**
  $$(u - v) + v = (3, -5, 1) + (-1, 4, 2) = (2, -1, 3) = u.$$
  Both cross-checks confirm that no arithmetic errors occurred.

---

## 8. Common Mistakes to Avoid
- **Sign errors during subtraction:** Forgetting that subtracting a negative coordinate produces addition, e.g., writing $2 - (-1) = 1$ instead of $2 + 1 = 3$.
- **Mixing coordinates:** Adding an $x$-coordinate to a $y$-coordinate across different axes.
- **Confusing vector addition with scalar addition:** Vectors cannot be added by just summing all six coordinates into a single scalar number; the result must remain a 3-dimensional vector.

---

## 9. Classroom Presentation (3-Sentence Summary)
To calculate vector sums and linear combinations, we perform standard arithmetic operations component by component along each coordinate axis. Subtracting vector $v$ from the sum $u + v$ cancels out the displacement of $v$, recovering vector $u$ exactly. Geometrically, vector addition represents sequential translations in space following the head-to-tail rule, producing the net resultant displacement.

