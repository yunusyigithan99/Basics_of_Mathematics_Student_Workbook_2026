# Problem 2 Solution: Distance as the Length of a Vector

## 1. Original Problem
The points in $\mathbb{R}^3$ are given by
$$A = (1, 2, 3) \quad \text{and} \quad B = (4, -2, 6).$$

1. Construct the displacement vector $\overrightarrow{AB}$.
2. Compute its Euclidean length (norm) $\|\overrightarrow{AB}\|$.
3. Compute the distance $d(A, B)$ between the points using the Cartesian distance formula.
4. Explain why both calculations give the exact same result.

---

## 2. What We Are Trying to Find
We need to:
1. Find the components of the vector directed from point $A$ to point $B$.
2. Calculate the magnitude (length) of this vector using the Euclidean norm formula.
3. Calculate the distance between points $A$ and $B$ using the 3D distance formula.
4. Provide the conceptual reasoning showing that distance between two geometric points is fundamentally identical to the norm of their connecting displacement vector.

---

## 3. Key Concepts and Theorems
1. **Displacement Vector Connecting Two Points:**
   Given initial point $A = (x_A, y_A, z_A)$ and terminal point $B = (x_B, y_B, z_B)$, the displacement vector $\overrightarrow{AB}$ is found by subtracting the coordinates of the initial point from the terminal point:
   $$\overrightarrow{AB} = B - A = (x_B - x_A, \; y_B - y_A, \; z_B - z_A).$$
2. **Euclidean Norm (Vector Length):**
   The length (magnitude) of a vector $v = (v_1, v_2, v_3)$ in $\mathbb{R}^3$ is given by the Pythagorean theorem in three dimensions:
   $$\|v\| = \sqrt{v_1^2 + v_2^2 + v_3^2}.$$
3. **Cartesian Distance Formula:**
   The straight-line distance $d(A, B)$ between points $A$ and $B$ in $\mathbb{R}^3$ is:
   $$d(A, B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}.$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Construct the Vector $\overrightarrow{AB}$
Subtract the coordinates of the starting point $A(1, 2, 3)$ from the endpoint $B(4, -2, 6)$:
$$\overrightarrow{AB} = (4 - 1, \; -2 - 2, \; 6 - 3) = (3, -4, 3).$$

### Step 2: Compute the Length of $\overrightarrow{AB}$
Apply the Euclidean norm definition to the component vector $(3, -4, 3)$:
$$\|\overrightarrow{AB}\| = \sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{9 + 16 + 9} = \sqrt{34}.$$
Since $34 = 2 \times 17$ has no square factors, the exact length is $\sqrt{34}$ (approximately $5.831$).

### Step 3: Compute Distance Using the Coordinate Formula
Directly substitute the coordinates of points $A$ and $B$ into the 3D Euclidean distance formula:
$$d(A, B) = \sqrt{(4 - 1)^2 + (-2 - 2)^2 + (6 - 3)^2} = \sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{9 + 16 + 9} = \sqrt{34}.$$

### Step 4: Explain Why Both Calculations Give the Same Result
Comparing the two formulas reveals that they are identical:
- The vector components $(v_1, v_2, v_3)$ of $\overrightarrow{AB}$ are defined precisely as the coordinate differences along each axis:
  $$v_1 = x_B - x_A, \quad v_2 = y_B - y_A, \quad v_3 = z_B - z_A.$$
- The length formula for a vector sums the squares of its components and extracts the square root:
  $$\|\overrightarrow{AB}\| = \sqrt{v_1^2 + v_2^2 + v_3^2}.$$
- Substituting the definitions of $v_1, v_2, v_3$ into the norm expression reproduces the point distance formula line for line:
  $$d(A, B) = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = \|\overrightarrow{AB}\|.$$
Geometrically, distance is simply the magnitude of the displacement required to travel straight from $A$ to $B$.

---

## 5. Why Each Step Is Valid
1. **Subtracting $A$ from $B$** correctly defines the directed translation vector originating at $A$ and terminating at $B$.
2. **Squaring each component** eliminates negative signs (such as $(-4)^2 = 16$), properly measuring the non-negative physical spatial extent along each orthogonal coordinate axis.
3. **The 3D Pythagorean theorem** is valid because the Cartesian coordinate axes $x$, $y$, and $z$ are mutually perpendicular.

---

## 6. Final Answer in Words
The displacement vector is $\overrightarrow{AB} = (3, -4, 3)$, and its Euclidean length is $\|\overrightarrow{AB}\| = \sqrt{34}$. The distance between the points using the coordinate distance formula is also $d(A, B) = \sqrt{34}$. Both calculations yield the identical result because the Cartesian distance formula is simply the algebraic definition of the length of the difference vector between the two points.

---

## 7. Quick Verification
- Reverse vector $\overrightarrow{BA} = A - B = (1 - 4, 2 - (-2), 3 - 6) = (-3, 4, -3)$.
- Its length is $\|\overrightarrow{BA}\| = \sqrt{(-3)^2 + 4^2 + (-3)^2} = \sqrt{9 + 16 + 9} = \sqrt{34}$.
- Since $\|\overrightarrow{AB}\| = \|\overrightarrow{BA}\| = d(A, B) = \sqrt{34}$, distance is symmetric and strictly non-negative, confirming consistency.

---

## 8. Common Mistakes to Avoid
- **Subtracting in reverse order:** Writing $A - B$ instead of $B - A$ when constructing $\overrightarrow{AB}$. While this gives the same length, the direction of the vector is inverted.
- **Sign error when squaring negative numbers:** Writing $(-4)^2 = -16$ instead of $+16$. Length is always the sum of non-negative squared terms.
- **Forgetting the square root:** Stating that the distance is $34$ (the squared distance) instead of $\sqrt{34}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
We construct the vector $\overrightarrow{AB}$ by subtracting the coordinates of point $A$ from point $B$, yielding $(3, -4, 3)$. Calculating the Euclidean norm of this vector gives $\sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{34}$, which matches the coordinate distance formula step for step. This demonstrates that geometric distance between any two points is fundamentally the length of the displacement vector connecting them.

