# Exercise 8: Inverse of a Transformation

## 1. Original Problem
The matrix:
$$S = \begin{pmatrix} 2 & 0 \\ 0 & \frac{1}{2} \end{pmatrix}$$
describes a scaling of the plane. Find $S^{-1}$ and explain geometrically what the inverse transformation does. Check the action of the pair $S, S^{-1}$ on one simple vector.

---

## 2. What We Are Trying to Find
We need to:
- Find the inverse matrix $S^{-1}$ algebraically.
- Describe the geometric effect of the forward transformation $S$ on the plane.
- Explain geometrically how the inverse transformation $S^{-1}$ undoes the effect of $S$.
- Select a simple concrete vector $\mathbf{v}$, apply $S$ to it, then apply $S^{-1}$ to the result, and demonstrate that the original vector is restored: $S^{-1}(S\mathbf{v}) = \mathbf{v}$.

---

## 3. Key Concepts and Theorems
1. **Geometric Meaning of Diagonal Matrices:**
   A diagonal matrix $D = \begin{pmatrix} d_1 & 0 \\ 0 & d_2 \end{pmatrix}$ scales coordinates independently along the coordinate axes:
   $$\begin{pmatrix} d_1 & 0 \\ 0 & d_2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} d_1 x \\ d_2 y \end{pmatrix}$$
2. **Inverse of an Axis Scaling:**
   If a transformation stretches an axis by a factor of $k$ ($k \neq 0$), its geometric inverse must compress that same axis by a factor of $\frac{1}{k}$.
   Therefore, the inverse of a diagonal matrix is obtained by inverting each non-zero diagonal entry:
   $$D^{-1} = \begin{pmatrix} \frac{1}{d_1} & 0 \\ 0 & \frac{1}{d_2} \end{pmatrix}$$
3. **Identity Action on Vectors:**
   For any vector $\mathbf{v}$, $(S^{-1}S)\mathbf{v} = I\mathbf{v} = \mathbf{v}$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Find the Inverse Matrix $S^{-1}$
Matrix $S = \begin{pmatrix} 2 & 0 \\ 0 & \frac{1}{2} \end{pmatrix}$ is diagonal.
- Compute the determinant:
  $$\det S = 2 \cdot \frac{1}{2} - 0 \cdot 0 = 1 - 0 = 1$$
- Since $\det S = 1 \neq 0$, the inverse exists.
- Inverting the diagonal entries:
  $$\frac{1}{2} \to \frac{1}{2}, \qquad \frac{1}{1/2} \to 2$$
Therefore:
$$S^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 2 \end{pmatrix}$$

---

### Step 2: Geometric Explanation of $S$ and $S^{-1}$
1. **What $S$ does to the plane:**
   - Any point $(x, y)$ is transformed into $\left(2x, \frac{1}{2}y\right)$.
   - The matrix doubles distances along the horizontal $x$-axis (a horizontal stretch by a factor of $2$).
   - Simultaneously, it cuts distances along the vertical $y$-axis in half (a vertical compression by a factor of $\frac{1}{2}$).
   - Notice that because $\det S = 1$, the total area of any geometric shape is preserved, even though its shape is elongated horizontally.

2. **What $S^{-1}$ does geometrically:**
   - The inverse transformation maps any point $(x', y')$ to $\left(\frac{1}{2}x', 2y'\right)$.
   - It compresses the horizontal $x$-axis by a factor of $\frac{1}{2}$, exactly canceling the horizontal stretch of $S$.
   - It stretches the vertical $y$-axis by a factor of $2$, exactly restoring the vertical compression of $S$.
   - Thus, $S^{-1}$ completely restores the original geometry of every figure in the plane.

---

### Step 3: Check the Action of $S$ and $S^{-1}$ on a Test Vector
Choose a simple test vector:
$$\mathbf{v} = \begin{pmatrix} 4 \\ 6 \end{pmatrix}$$

1. **Apply the forward transformation $S$:**
   $$\mathbf{w} = S\mathbf{v} = \begin{pmatrix} 2 & 0 \\ 0 & \frac{1}{2} \end{pmatrix} \begin{pmatrix} 4 \\ 6 \end{pmatrix} = \begin{pmatrix} 2(4) + 0(6) \\ 0(4) + \frac{1}{2}(6) \end{pmatrix} = \begin{pmatrix} 8 \\ 3 \end{pmatrix}$$
   *Inspection:* The $x$-component doubled ($4 \to 8$) and the $y$-component halved ($6 \to 3$).

2. **Apply the inverse transformation $S^{-1}$ to $\mathbf{w}$:**
   $$S^{-1}\mathbf{w} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 8 \\ 3 \end{pmatrix} = \begin{pmatrix} \frac{1}{2}(8) + 0(3) \\ 0(8) + 2(3) \end{pmatrix} = \begin{pmatrix} 4 \\ 6 \end{pmatrix}$$

Comparing the final output with the initial vector:
$$S^{-1}(S\mathbf{v}) = \begin{pmatrix} 4 \\ 6 \end{pmatrix} = \mathbf{v}$$
The original vector is completely restored.

---

## 5. Why Each Step Is Valid
- **Diagonal Decoupling:** Diagonal operators act on orthogonal Cartesian coordinates without cross-axis coupling, allowing each coordinate's scale factor to be inverted independently in $\mathbb{R}$.
- **Identity Invariance:** Multiplying by $S^{-1}S = I$ leaves any vector in $\mathbb{R}^2$ invariant because the identity operator fixes all points.

---

## 6. Final Answer in Words
The inverse matrix is $S^{-1} = \begin{pmatrix} 1/2 & 0 \\ 0 & 2 \end{pmatrix}$. Geometrically, while $S$ doubles horizontal lengths and halves vertical lengths, $S^{-1}$ reverses this action by halving horizontal lengths and doubling vertical lengths. Applying $S$ to the vector $\begin{pmatrix} 4 \\ 6 \end{pmatrix}$ produces $\begin{pmatrix} 8 \\ 3 \end{pmatrix}$, and subsequently applying $S^{-1}$ returns the vector back to $\begin{pmatrix} 4 \\ 6 \end{pmatrix}$.

---

## 7. Quick Verification
- **Matrix product check:**
  $$S S^{-1} = \begin{pmatrix} 2 & 0 \\ 0 & 1/2 \end{pmatrix} \begin{pmatrix} 1/2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 2(1/2) & 0 \\ 0 & (1/2)(2) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$
- **Determinant product check:**
  $\det(S) \cdot \det(S^{-1}) = 1 \cdot 1 = 1$. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Negating Instead of Inverting:** Writing $S^{-1} = \begin{pmatrix} -2 & 0 \\ 0 & -1/2 \end{pmatrix}$. An inverse scaling requires reciprocals ($1/k$), not negatives.
- **Inverting the Position of Entries:** Swapping the positions of $2$ and $1/2$ instead of taking reciprocals in place.
- **Forgetting the Vector Test:** Providing only the matrix $S^{-1}$ without demonstrating the step-by-step vector action on a chosen test vector.

---

## 9. Classroom Presentation (3-Sentence Summary)
"The forward matrix $S$ scales the plane by doubling the horizontal coordinate and halving the vertical coordinate. Its inverse $S^{-1} = \begin{pmatrix}1/2&0\\0&2\end{pmatrix}$ undoes this transformation by halving the horizontal coordinate and doubling the vertical coordinate. Testing this pair on the vector $\begin{pmatrix}4\\6\end{pmatrix}$ transforms it to $\begin{pmatrix}8\\3\end{pmatrix}$ and immediately back to $\begin{pmatrix}4\\6\end{pmatrix}$, confirming that the inverse restores the original point."

