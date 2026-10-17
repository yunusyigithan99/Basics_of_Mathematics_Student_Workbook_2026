# Exercise 9: Area and the Determinant

## 1. Original Problem
The vectors:
$$u = \begin{pmatrix} 3 \\ 1 \end{pmatrix}, \qquad v = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$$
span a parallelogram. Compute its area using a determinant. Then reverse the order of the vectors and explain what changes in the determinant and what does not change in the area.

---

## 2. What We Are Trying to Find
We need to:
- Compute the geometric area of the parallelogram formed by the two vectors $u$ and $v$ using a $2 \times 2$ determinant.
- Compute the determinant when the vectors are placed in reverse order.
- Contrast the mathematical concepts of **oriented (signed) area** and **geometric (absolute) area**.
- Explain why the sign changes when the order is reversed while the physical area remains unchanged.

---

## 3. Key Concepts and Theorems
1. **Geometric Interpretation of the $2 \times 2$ Determinant:**
   If vectors $u = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}$ and $v = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$ form the adjacent sides of a parallelogram, the determinant of the matrix formed by placing them as columns (or rows) gives the **signed (oriented) area** of the parallelogram:
   $$\det\begin{pmatrix} u & v \end{pmatrix} = \det\begin{pmatrix} u_1 & v_1 \\ u_2 & v_2 \end{pmatrix}$$
2. **Geometric (Absolute) Area:**
   Physical area cannot be negative. Therefore, the geometric area is the **absolute value** of the determinant:
   $$\text{Area} = \left| \det\begin{pmatrix} u & v \end{pmatrix} \right|$$
3. **Orientation and Column Swaps:**
   - A positive determinant indicates that sweeping from the first vector to the second vector follows a **counterclockwise** direction (a right-handed orientation).
   - Reversing the order swaps the columns, multiplying the determinant by $-1$ and reversing the orientation to clockwise.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Determinant with Order $(u, v)$
Form the matrix $M_1 = \begin{pmatrix} u & v \end{pmatrix}$ with $u$ as the first column and $v$ as the second column:
$$M_1 = \begin{pmatrix} 3 & 1 \\ 1 & 4 \end{pmatrix}$$

Compute the determinant:
$$\det M_1 = (3 \cdot 4) - (1 \cdot 1) = 12 - 1 = 11$$

---

### Step 2: Compute the Geometric Area
The geometric area is the absolute value of the determinant:
$$\text{Area} = |\det M_1| = |11| = 11$$

---

### Step 3: Compute the Determinant with Reversed Order $(v, u)$
Form the matrix $M_2 = \begin{pmatrix} v & u \end{pmatrix}$ with $v$ as the first column and $u$ as the second column:
$$M_2 = \begin{pmatrix} 1 & 3 \\ 4 & 1 \end{pmatrix}$$

Compute the determinant:
$$\det M_2 = (1 \cdot 1) - (3 \cdot 4) = 1 - 12 = -11$$

---

### Step 4: Explain What Changes and What Does Not Change
1. **What changes in the determinant:**
   - The value changes from $+11$ to $-11$.
   - Swapping the column positions reverses the **sign** of the determinant.
   - Geometrically, this sign change reflects a reversal of **orientation**: rotating from $u$ to $v$ is counterclockwise ($+$), while rotating from $v$ to $u$ is clockwise ($-$).
2. **What does not change in the area:**
   - The physical geometric area is given by the magnitude:
     $$\text{Area} = |\det M_2| = |-11| = 11$$
   - The physical parallelogram itself is completely identical; changing which side we name first does not shrink, stretch, or alter the shape of the surface.
   - Therefore, the **area remains strictly $11$**.

---

## 5. Why Each Step Is Valid
- **Cross-Product Magnitude Equivalence:** In 3D space, embedding vectors as $(3, 1, 0)$ and $(1, 4, 0)$ yields $u \times v = (0, 0, 11\mathbf{k})$. The length $\|u \times v\| = 11$ represents the area, while the z-component gives the determinant.
- **Orientation Reversal Invariance:** Area is a measure on Euclidean space and is inherently invariant under rigid reflections and coordinate re-indexings.

---

## 6. Final Answer in Words
The area of the parallelogram spanned by vectors $u$ and $v$ is $11$. When the order of the vectors is reversed, the determinant changes from $11$ to $-11$ because the two columns are swapped, reversing the rotational orientation. However, the geometric area does not change because area is the absolute value of the determinant, remaining equal to $11$.

---

## 7. Quick Verification
- **Base $\times$ Height Geometry Check:**
  - Length of base vector $u$: $\|u\| = \sqrt{3^2 + 1^2} = \sqrt{10}$.
  - Unit normal to $u$: $n = \frac{1}{\sqrt{10}}\begin{pmatrix} -1 \\ 3 \end{pmatrix}$.
  - Height $h$ is the projection of $v$ onto $n$:
    $$h = |v \cdot n| = \frac{|1(-1) + 4(3)|}{\sqrt{10}} = \frac{|-1 + 12|}{\sqrt{10}} = \frac{11}{\sqrt{10}}$$
  - $\text{Area} = \text{base} \times \text{height} = \sqrt{10} \times \frac{11}{\sqrt{10}} = 11$. Matches perfectly! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Reporting a Negative Area:** Writing that the area is $-11$ when vectors are reversed. Area is always non-negative; you must take the absolute value.
- **Setting Up the Matrix as Rows Instead of Columns:** While $\det(M^T) = \det(M)$ means row setup gives the same number in this case, conceptually the vectors should be treated consistently as columns.
- **Confusing Perimeter with Area:** Attempting to sum the vector lengths.

---

## 9. Classroom Presentation (3-Sentence Summary)
"The area of the parallelogram is given by the absolute value of the determinant of the vectors, which evaluates to $|3(4) - 1(1)| = 11$. Reversing the order of the vectors swaps the columns, flipping the determinant's sign from $+11$ to $-11$ to reflect a change from counterclockwise to clockwise orientation. However, because geometric area is strictly a positive magnitude, the physical area remains unchanged at $11$."

