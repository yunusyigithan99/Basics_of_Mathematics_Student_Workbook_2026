# Exercise 9: Composing Transformations

## 1. Original Problem
Let:
$$S = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}, \qquad R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$
The matrix $S$ describes nonuniform scaling, while $R$ describes a $90^\circ$ counterclockwise rotation.
For:
$$x = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
compute $RSx$ and $SRx$. Compare the results and explain geometrically why the order of these transformations matters.

---

## 2. What We Are Trying to Find
We need to:
- Compute the vector $RSx$, representing scaling first, followed by rotation.
- Compute the vector $SRx$, representing rotation first, followed by scaling.
- Compare the two resulting vectors to see if they are identical.
- Provide a geometric explanation for why changing the order of these two geometric operations produces completely different outcomes.

---

## 3. Key Concepts and Theorems
1. **Linear Transformations as Matrices:**
   A matrix acting on a vector represents a geometric mapping of the plane.
   - $S = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ maps $(x_1, x_2) \mapsto (2x_1, x_2)$, doubling the horizontal coordinate while keeping the vertical coordinate constant (horizontal stretch).
   - $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ maps $(x_1, x_2) \mapsto (-x_2, x_1)$, rotating any vector by $90^\circ$ counterclockwise around the origin.
2. **Composition Order:**
   In functional notation, $(f \circ g)(x) = f(g(x))$. Therefore, in matrix notation, the matrix closest to the vector acts **first**:
   - $RSx = R(S(x))$: first scale with $S$, then rotate with $R$.
   - $SRx = S(R(x))$: first rotate with $R$, then scale with $S$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $RSx$ (Scale first, then Rotate)
- **First, apply scaling matrix $S$ to vector $x$:**
  $$Sx = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2(1) + 0(2) \\ 0(1) + 1(2) \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \end{pmatrix}$$
  *Geometric effect:* The $x$-component is doubled from $1$ to $2$, while the $y$-component stays $2$.

- **Second, apply rotation matrix $R$ to the scaled vector $(Sx)$:**
  $$RSx = R(Sx) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 \\ 2 \end{pmatrix} = \begin{pmatrix} 0(2) + (-1)(2) \\ 1(2) + 0(2) \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \end{pmatrix}$$
  *Geometric effect:* The vector $(2, 2)$ is rotated $90^\circ$ counterclockwise into $(-2, 2)$.

---

### Step 2: Compute $SRx$ (Rotate first, then Scale)
- **First, apply rotation matrix $R$ to vector $x$:**
  $$Rx = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 0(1) + (-1)(2) \\ 1(1) + 0(2) \end{pmatrix} = \begin{pmatrix} -2 \\ 1 \end{pmatrix}$$
  *Geometric effect:* The original vector $(1, 2)$ is rotated $90^\circ$ counterclockwise into $(-2, 1)$.

- **Second, apply scaling matrix $S$ to the rotated vector $(Rx)$:**
  $$SRx = S(Rx) = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(-2) + 0(1) \\ 0(-2) + 1(1) \end{pmatrix} = \begin{pmatrix} -4 \\ 1 \end{pmatrix}$$
  *Geometric effect:* The new horizontal component ($-2$) is doubled to $-4$, while the vertical component ($1$) remains unchanged.

---

### Step 3: Compare Results
$$RSx = \begin{pmatrix} -2 \\ 2 \end{pmatrix}, \qquad SRx = \begin{pmatrix} -4 \\ 1 \end{pmatrix}$$
Clearly, $RSx \neq SRx$.

---

### Step 4: Geometric Explanation
The reason the order matters is that the scaling transformation $S$ is **nonuniform**: it acts exclusively along the original horizontal coordinate axis ($x$-axis) and leaves the vertical direction untouched.
1. In $RSx$, the vector's original horizontal coordinate ($1$) is doubled first (becoming $2$). Then, rotation moves this stretched coordinate into the vertical direction, producing $(-2, 2)$.
2. In $SRx$, rotation occurs first. This swaps the roles of the axes, sending the original vertical component ($2$) into the new horizontal position as $-2$. When $S$ subsequently stretches along the horizontal axis, it doubles this coordinate (which originally came from the $y$-axis!) from $-2$ to $-4$, resulting in $(-4, 1)$.
Because rotation changes the orientation of the vector relative to the fixed directional axis of the stretch, the order in which they are applied fundamentally changes the outcome.

---

## 5. Why Each Step Is Valid
- **Associativity of Matrix Multiplication:** $R(Sx) = (RS)x$ and $S(Rx) = (SR)x$. Evaluating sequentially as matrix-vector products corresponds directly to evaluating function composition.
- **Directionality of Linear Operators:** Matrix multiplication preserves linear combinations, but since nonuniform scaling has privileged directions (eigenvectors along the axes) that are rotated away by $R$, the operators do not commute: $RS \neq SR$.

---

## 6. Final Answer in Words
Computing the transformations gives $RSx = \begin{pmatrix} -2 \\ 2 \end{pmatrix}$ and $SRx = \begin{pmatrix} -4 \\ 1 \end{pmatrix}$. The results are different because scaling is direction-dependent. If we scale first, we stretch the original $x$-component; if we rotate first, the original $y$-component becomes the horizontal component, so the subsequent scaling doubles that component instead.

---

## 7. Quick Verification
- **Composite matrix method for $RS$:**
  $$RS = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 2 & 0 \end{pmatrix}$$
  Applying this matrix directly to $x$:
  $$(RS)x = \begin{pmatrix} 0 & -1 \\ 2 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 0(1) - 1(2) \\ 2(1) + 0(2) \end{pmatrix} = \begin{pmatrix} -2 \\ 2 \end{pmatrix} \quad \checkmark$$
- **Composite matrix method for $SR$:**
  $$SR = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix}$$
  Applying this matrix directly to $x$:
  $$(SR)x = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 0(1) - 2(2) \\ 1(1) + 0(2) \end{pmatrix} = \begin{pmatrix} -4 \\ 1 \end{pmatrix} \quad \checkmark$$
Both computation paths yield identical results, verifying the calculation.

---

## 8. Common Mistakes to Avoid
- **Reading the Order from Left to Right:** Applying $R$ first in $RSx$ because $R$ appears on the left. Remember: operations act right-to-left, closest to the vector first ($S$ acts first, then $R$).
- **Confusing Matrix Dimension with Vector Transformation:** Assuming all $2 \times 2$ geometric transformations must commute because they act on the same 2D plane.
- **Arithmetic Sign Errors in $R$:** Misplacing the negative sign in the rotation matrix ($r_{12} = -1$).

---

## 9. Classroom Presentation (3-Sentence Summary)
"When we apply the transformations, scaling first and then rotating gives $RSx = \begin{pmatrix}-2\\2\end{pmatrix}$, while rotating first and then scaling gives $SRx = \begin{pmatrix}-4\\1\end{pmatrix}$. This difference arises because scaling is directional, stretching only along the horizontal axis. Since rotation alters the orientation of the vector before the second transformation takes place, the order of composition directly dictates which physical component is stretched."

