# Exercise 15: Combining Determinant Properties

## 1. Original Problem
Let $A$ and $B$ be invertible $2 \times 2$ matrices with:
$$\det A = -2, \qquad \det B = 3$$
Without finding the entries of the matrices, compute:
$$\det\left(B^{-1} A^T B\right)$$
State the determinant properties you use in order and explain why the factors involving $B$ eventually cancel.

---

## 2. What We Are Trying to Find
We need to:
- Compute the determinant of the composite matrix expression $B^{-1} A^T B$ strictly using determinant properties, without knowing the individual numerical entries of $A$ or $B$.
- State each determinant theorem applied in the exact sequence of the calculation.
- Explain mathematically and geometrically why the factors involving matrix $B$ cancel out completely, leaving the result dependent only on matrix $A$.

---

## 3. Key Concepts and Theorems
1. **Multiplicative Property (Determinant of a Product):**
   For any square matrices $X$ and $Y$ of the same size:
   $$\det(XY) = \det X \cdot \det Y$$
   By induction, for three matrices:
   $$\det(XYZ) = \det X \cdot \det Y \cdot \det Z$$
2. **Determinant of an Inverse Matrix:**
   If $B$ is invertible, then:
   $$\det(B^{-1}) = \frac{1}{\det B}$$
3. **Determinant of a Transpose Matrix:**
   Transposing a matrix does not change its determinant:
   $$\det(A^T) = \det A$$
4. **Commutativity of Scalar Multiplication:**
   Because determinants are scalar numbers in $\mathbb{R}$, their numerical multiplication is commutative:
   $$\frac{1}{\det B} \cdot \det A \cdot \det B = \det A \cdot \left(\frac{1}{\det B} \cdot \det B\right) = \det A \cdot 1 = \det A$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Apply the Product Property
Using the multiplicative property of determinants on the product of the three matrices $B^{-1}$, $A^T$, and $B$:
$$\det\left(B^{-1} A^T B\right) = \det(B^{-1}) \cdot \det(A^T) \cdot \det(B)$$

---

### Step 2: Apply the Inverse Property to $B^{-1}$
Because matrix $B$ is invertible and $\det B = 3 \neq 0$, the determinant of its inverse is the reciprocal of $\det B$:
$$\det(B^{-1}) = \frac{1}{\det B} = \frac{1}{3}$$

---

### Step 3: Apply the Transpose Property to $A^T$
Transposition does not change the determinant:
$$\det(A^T) = \det A = -2$$

---

### Step 4: Substitute and Cancel the Factors of $B$
Substitute the evaluated scalar terms back into the product expression:
$$\det\left(B^{-1} A^T B\right) = \left(\frac{1}{\det B}\right) \cdot (\det A) \cdot (\det B) = \frac{1}{3} \cdot (-2) \cdot 3$$

Because multiplication of real numbers is commutative, rearrange the scalar factors:
$$\det\left(B^{-1} A^T B\right) = (-2) \cdot \left(\frac{1}{3} \cdot 3\right) = (-2) \cdot 1 = -2$$

---

### Step 5: Explanation of Why the Factors Involving $B$ Cancel
- **Algebraic Explanation:**
  The matrix expression involves both $B$ and $B^{-1}$. When applying the determinant map, these become reciprocal real numbers: $\det(B^{-1}) = \frac{1}{\det B}$. Because scalar numbers commute under multiplication, $\left(\frac{1}{\det B}\right) \cdot \det B = 1$. The noncommutativity of the matrices ($B$ and $B^{-1}$ are separated by $A^T$) disappears once converted into scalar determinants.
- **Geometric Explanation (Similarity / Conjugation):**
  The transformation $B^{-1} A^T B$ represents the linear operator $A^T$ expressed in a new coordinate system defined by the change-of-basis matrix $B$.
  - First, $B$ maps the coordinates, scaling oriented volume by a factor of $\det B = 3$.
  - Next, $A^T$ acts, scaling volume by a factor of $\det(A^T) = -2$.
  - Finally, $B^{-1}$ changes coordinates back to the original frame, scaling volume by $\frac{1}{\det B} = \frac{1}{3}$.
  The initial expansion/distortion introduced by $B$ is completely and precisely undone by its inverse $B^{-1}$. Therefore, changing the basis cannot alter the intrinsic volume-scaling factor of the core transformation.

---

## 5. Why Each Step Is Valid
- **Homomorphism Axiom:** The determinant map $\det: \operatorname{GL}_2(\mathbb{R}) \to \mathbb{R}^\times$ is a group homomorphism. For any group homomorphism $\phi$, $\phi(b^{-1} a b) = \phi(b)^{-1} \phi(a) \phi(b) = \phi(a)$ because the target group $\mathbb{R}^\times$ is abelian.
- **Invariance of Characteristic Polynomial:** The matrix $B^{-1} A^T B$ is similar to $A^T$, and similar matrices always have identical determinants, traces, and eigenvalues.

---

## 6. Final Answer in Words
The determinant of $B^{-1} A^T B$ is $-2$. In order, we apply: (1) the product rule to split the determinant into $\det(B^{-1}) \cdot \det(A^T) \cdot \det(B)$, (2) the inverse rule $\det(B^{-1}) = 1/\det B$, and (3) the transpose rule $\det(A^T) = \det A$. The terms involving $B$ cancel because the determinant converts the operations into ordinary real numbers where multiplication is commutative, allowing $\frac{1}{3}$ and $3$ to multiply to $1$, geometrically reflecting that changing basis does not alter volume scaling.

---

## 7. Quick Verification
- **Testing with concrete matrices:**
  Let $A = \begin{pmatrix} -2 & 0 \\ 0 & 1 \end{pmatrix} \implies \det A = -2$, $A^T = A$.
  Let $B = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} \implies \det B = 3$, $B^{-1} = \begin{pmatrix} 1/3 & 0 \\ 0 & 1 \end{pmatrix}$.
  Compute $B^{-1} A^T B$:
  $$B^{-1} A^T B = \begin{pmatrix} 1/3 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} -2/3 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 0 \\ 0 & 1 \end{pmatrix}$$
  The determinant is $(-2)(1) - (0)(0) = -2$. Matches! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Attempting to Multiply Matrices without Entries:** Spending time trying to solve for unknown entries $a, b, c, d$ instead of applying pure determinant properties.
- **Forgetting that Transpose Preserves Determinant:** Incorrectly assuming $A^T$ requires an extra minus sign or inversion.
- **Thinking Matrices Cancel Directly ($B^{-1} B = I$):** Writing $B^{-1} A^T B = B^{-1} B A^T = A^T$. Matrix multiplication is NOT commutative, so $B$ cannot jump over $A^T$. The cancellation happens ONLY at the scalar determinant level!

---

## 9. Classroom Presentation (3-Sentence Summary)
"Using the product rule, the expression splits into the product of scalar determinants: $\det(B^{-1}) \cdot \det(A^T) \cdot \det(B)$. Since $\det(B^{-1}) = \frac{1}{\det B}$ and $\det(A^T) = \det A$, the expression simplifies to $\frac{1}{3} \cdot (-2) \cdot 3 = -2$. The factors involving $B$ cancel out completely because the determinant maps matrices to real numbers where multiplication is commutative, reflecting the geometric fact that a change of basis never alters the intrinsic volume scaling of a transformation."

