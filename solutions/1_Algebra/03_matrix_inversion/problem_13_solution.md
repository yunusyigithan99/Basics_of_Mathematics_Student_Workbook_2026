# Exercise 13: Undoing a Composite Transformation

## 1. Original Problem
The matrices:
$$S = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}, \qquad H = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
describe nonuniform scaling and shear. For $T = HS$, find $T^{-1}$ in two ways:
1. first compute $T$, then its inverse,
2. use $(HS)^{-1} = S^{-1}H^{-1}$.

Compare the results. Additionally compute $H^{-1}S^{-1}$ and verify that the incorrect order gives a different matrix. Explain the rule: “when undoing a composition of operations, we undo them from the end.”

---

## 2. What We Are Trying to Find
We need to:
- Compute the composite transformation matrix $T = HS$.
- Invert $T$ directly using the $2 \times 2$ formula (Method 1).
- Invert $S$ and $H$ individually and multiply them in reverse order $S^{-1}H^{-1}$ (Method 2).
- Compare the two outcomes to confirm they match.
- Compute the un-reversed product $H^{-1}S^{-1}$ to prove empirically that order matters.
- Explain the geometric and algebraic intuition behind the fundamental rule: "undo from the end."

---

## 3. Key Concepts and Theorems
1. **Product Inversion Formula:**
   For any invertible matrices $A$ and $B$:
   $$(AB)^{-1} = B^{-1}A^{-1}$$
   Applied to $T = HS$:
   $$T^{-1} = (HS)^{-1} = S^{-1}H^{-1}$$
2. **The "Undo from the End" Principle:**
   When transformations are composed, the operator written closest to the vector acts first.
   In $T\mathbf{x} = H(S\mathbf{x})$, the vector is first scaled by $S$, and then sheared by $H$.
   To return to the original vector $\mathbf{x}$, one must undo the operations in reverse chronological order: first undo the shear (apply $H^{-1}$), and then undo the scale (apply $S^{-1}$).

---

## 4. Detailed Step-by-Step Solution

### Method 1: Compute $T$ First, Then Its Inverse
- **Compute $T = HS$:**
  $$T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1(2) + 1(0) & 1(0) + 1(1) \\ 0(2) + 1(0) & 0(0) + 1(1) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$$

- **Compute the determinant of $T$:**
  $$\det T = (2 \cdot 1) - (1 \cdot 0) = 2 - 0 = 2$$

- **Invert $T$ using the $2 \times 2$ formula:**
  $$T^{-1} = \frac{1}{2} \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & 1 \end{pmatrix}$$

---

### Method 2: Compute $T^{-1}$ via $S^{-1}H^{-1}$
- **Invert $S = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$:**
  $$S^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix}$$

- **Invert $H = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$:**
  $$H^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$

- **Multiply in reverse order ($S^{-1}H^{-1}$):**
  $$S^{-1}H^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2}(1) + 0 & \frac{1}{2}(-1) + 0 \\ 0 + 1(0) & 0 + 1(1) \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & 1 \end{pmatrix}$$

**Comparison:**
Both methods yield the exact same matrix $\begin{pmatrix} 1/2 & -1/2 \\ 0 & 1 \end{pmatrix}$.

---

### Step 3: Compute the Incorrect Order ($H^{-1}S^{-1}$)
Now multiply the inverses without reversing the order:
$$H^{-1}S^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1\left(\frac{1}{2}\right) + (-1)(0) & 1(0) + (-1)(1) \\ 0\left(\frac{1}{2}\right) + 1(0) & 0(0) + 1(1) \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -1 \\ 0 & 1 \end{pmatrix}$$

Compare this with the true inverse:
$$H^{-1}S^{-1} = \begin{pmatrix} \frac{1}{2} & -1 \\ 0 & 1 \end{pmatrix} \neq \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & 1 \end{pmatrix} = T^{-1}$$
Notice entry $(1, 2)$ is $-1$ instead of $-1/2$. The incorrect order completely fails to invert $T$!

---

### Step 4: Explain the Rule "Undo from the End"
Consider a vector $\mathbf{x}$ undergoing the transformation:
$$\mathbf{x} \xrightarrow{\text{Step 1: Apply } S} \mathbf{y} = S\mathbf{x} \xrightarrow{\text{Step 2: Apply } H} \mathbf{z} = H\mathbf{y} = T\mathbf{x}$$
Now suppose you are standing at the final state $\mathbf{z}$ and wish to return to $\mathbf{x}$:
1. The last action performed on the vector was the shear $H$. Therefore, before you can touch the scaling, you must first undo the shear by applying $H^{-1}$. This takes you from $\mathbf{z}$ back to $\mathbf{y}$:
   $$\mathbf{y} = H^{-1}\mathbf{z}$$
2. Now that the shear is stripped away, the vector is back in its scaled state $\mathbf{y} = S\mathbf{x}$. You can now undo the original scaling by applying $S^{-1}$:
   $$\mathbf{x} = S^{-1}\mathbf{y} = S^{-1}(H^{-1}\mathbf{z})$$
This demonstrates that the inverse transformation must be the composition $(S^{-1} \circ H^{-1})$, which in matrix notation is $S^{-1}H^{-1}$. If you tried to scale first ($S^{-1}$), you would be scaling a sheared shape along the wrong axes, distorting the figure further rather than restoring it.

---

## 5. Why Each Step Is Valid
- **Cancellation of Inner Terms:** $(HS)(S^{-1}H^{-1}) = H(S S^{-1})H^{-1} = H I H^{-1} = H H^{-1} = I$.
- **Non-Commutative Shear-Scaling Interaction:** In $T$, scaling affects the horizontal shear factor ($2 \times 1$). In $H^{-1}S^{-1}$, the inverse shear acts before the scale is reduced, producing an erroneous unscaled shear entry of $-1$.

---

## 6. Final Answer in Words
Computing $T^{-1}$ both by inverting $T = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$ directly and by calculating $S^{-1}H^{-1}$ yields the identical matrix $\begin{pmatrix} 1/2 & -1/2 \\ 0 & 1 \end{pmatrix}$. Computing the incorrect order $H^{-1}S^{-1}$ gives $\begin{pmatrix} 1/2 & -1 \\ 0 & 1 \end{pmatrix}$, which is not the inverse. The rule "undo from the end" reflects the fact that in a sequence of operations, the last transformation applied must be undone first to peel back each layer of distortion in reverse order.

---

## 7. Quick Verification
- **Testing $T(S^{-1}H^{-1})$:**
  $$\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1/2 & -1/2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2(1/2) + 0 & 2(-1/2) + 1(1) \\ 0 & 0 + 1(1) \end{pmatrix} = \begin{pmatrix} 1 & -1 + 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$
- **Testing $T(H^{-1}S^{-1})$ with the wrong order:**
  $$\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1/2 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -2 + 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \neq I$$
  This rigorously confirms that $H^{-1}S^{-1}$ fails to invert $T$. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Multiplying in Forward Order:** Writing $(HS)^{-1} = H^{-1}S^{-1}$. As demonstrated, this fails to cancel the terms and produces an incorrect entry.
- **Transposing Instead of Inverting $H$:** Writing $H^{-1} = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ (which is $H^T$). The inverse of a shear has a negative shear entry: $\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Both by inverting the combined matrix $T = \begin{pmatrix}2&1\\0&1\end{pmatrix}$ and by computing the reversed product $S^{-1}H^{-1}$, we obtain the identical inverse matrix $\begin{pmatrix}1/2&-1/2\\0&1\end{pmatrix}$. In contrast, multiplying in the wrong order gives $H^{-1}S^{-1} = \begin{pmatrix}1/2&-1\\0&1\end{pmatrix}$, which fails because it tries to scale before the shear has been removed. This illustrates the fundamental principle that to undo a composition of transformations, you must always undo the last operation first."

