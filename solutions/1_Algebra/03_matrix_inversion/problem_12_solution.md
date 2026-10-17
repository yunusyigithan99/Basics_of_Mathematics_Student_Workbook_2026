# Exercise 12: Finding Inverses Without Starting from Scratch

## 1. Original Problem
It is known that:
$$A^{-1} = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}$$
Without finding $A$, compute:
$$(3A)^{-1}, \qquad (A^T)^{-1}, \qquad (A^2)^{-1}$$
Justify each result using the appropriate property.

---

## 2. What We Are Trying to Find
We are given the explicit inverse matrix $A^{-1}$, but we do NOT know matrix $A$ directly. We need to:
- Compute the inverse of the scaled matrix $3A$.
- Compute the inverse of the transposed matrix $A^T$.
- Compute the inverse of the squared matrix $A^2$.
- Perform all calculations strictly using algebraic properties of matrix inverses, without inverting $A^{-1}$ to recover $A$.

---

## 3. Key Concepts and Theorems
For any invertible $n \times n$ matrix $A$ and non-zero scalar $c \in \mathbb{R}$:
1. **Scalar Inverse Property:**
   $$(cA)^{-1} = \frac{1}{c} A^{-1}$$
   *Proof:* $(cA) \cdot \left(\frac{1}{c} A^{-1}\right) = \left(c \cdot \frac{1}{c}\right) (A A^{-1}) = 1 \cdot I = I$.
2. **Transpose Inverse Property (Commutativity of Transpose and Inverse):**
   $$(A^T)^{-1} = (A^{-1})^T$$
   *Proof:* Taking the transpose of $A A^{-1} = I$ gives $(A^{-1})^T A^T = I^T = I$.
3. **Power Inverse Property:**
   $$(A^k)^{-1} = (A^{-1})^k$$
   For $k = 2$:
   $$(A^2)^{-1} = (A \cdot A)^{-1} = A^{-1} A^{-1} = (A^{-1})^2$$

---

## 4. Detailed Step-by-Step Solution

We are given:
$$A^{-1} = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}$$

---

### Step 1: Compute $(3A)^{-1}$
- **Property applied:** $(cA)^{-1} = \frac{1}{c} A^{-1}$ with scalar $c = 3$.
- **Calculation:**
  $$(3A)^{-1} = \frac{1}{3} A^{-1} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix} = \begin{pmatrix} \frac{2}{3} & -\frac{1}{3} \\ -1 & \frac{2}{3} \end{pmatrix}$$
- **Justification:** Scaling a matrix by $3$ triples its action. To invert this scaling, every entry of the inverse transformation must be multiplied by the reciprocal $\frac{1}{3}$.

---

### Step 2: Compute $(A^T)^{-1}$
- **Property applied:** $(A^T)^{-1} = (A^{-1})^T$.
- **Calculation:**
  Transpose the known matrix $A^{-1}$ by swapping its off-diagonal entries:
  $$(A^T)^{-1} = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}^T = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}$$
- **Justification:** Transposition and inversion commute. The inverse of the transpose is simply the transpose of the given inverse matrix.

---

### Step 3: Compute $(A^2)^{-1}$
- **Property applied:** $(A^2)^{-1} = (A^{-1})^2 = A^{-1} \cdot A^{-1}$.
- **Calculation:**
  Multiply $A^{-1}$ by itself:
  $$(A^2)^{-1} = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}$$
  Calculate each entry:
  - Top-left $(1, 1)$: $2(2) + (-1)(-3) = 4 + 3 = 7$
  - Top-right $(1, 2)$: $2(-1) + (-1)(2) = -2 - 2 = -4$
  - Bottom-left $(2, 1)$: $-3(2) + 2(-3) = -6 - 6 = -12$
  - Bottom-right $(2, 2)$: $-3(-1) + 2(2) = 3 + 4 = 7$

  Assembling the result:
  $$(A^2)^{-1} = \begin{pmatrix} 7 & -4 \\ -12 & 7 \end{pmatrix}$$
- **Justification:** By the product rule for inverses, $(A \cdot A)^{-1} = A^{-1} A^{-1}$. We simply multiply the known inverse matrix by itself.

---

## 5. Why Each Step Is Valid
- **Ring Inversion Axioms:** In any unital associative algebra, $(ab)^{-1} = b^{-1}a^{-1}$ and $(\lambda a)^{-1} = \lambda^{-1} a^{-1}$ are identities that depend solely on the properties of the elements and their inverses, completely bypassing the need to compute the base element $A$.
- **Dual Basis Action:** The transpose represents the adjoint operator on the dual space; its inverse is naturally the adjoint of the inverse operator.

---

## 6. Final Answer in Words
Without computing the original matrix $A$:
- $(3A)^{-1} = \frac{1}{3} A^{-1} = \begin{pmatrix} 2/3 & -1/3 \\ -1 & 2/3 \end{pmatrix}$, because scaling a matrix by $c$ scales its inverse by $1/c$.
- $(A^T)^{-1} = (A^{-1})^T = \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix}$, because transposition and inversion commute.
- $(A^2)^{-1} = (A^{-1})^2 = \begin{pmatrix} 7 & -4 \\ -12 & 7 \end{pmatrix}$, because inverting $A^2$ is equivalent to squaring $A^{-1}$.

---

## 7. Quick Verification
- **Reconstructing $A$ as an independent check:**
  Since $(A^{-1})^{-1} = A$:
  $\det(A^{-1}) = 2(2) - (-1)(-3) = 4 - 3 = 1$.
  $A = \frac{1}{1}\begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$.
  - Test $3A \cdot (3A)^{-1}$:
    $$\begin{pmatrix} 6 & 3 \\ 9 & 6 \end{pmatrix} \begin{pmatrix} 2/3 & -1/3 \\ -1 & 2/3 \end{pmatrix} = \begin{pmatrix} 4 - 3 & -2 + 2 \\ 6 - 6 & -3 + 4 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$
  - Test $A^T \cdot (A^T)^{-1}$:
    $$\begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 2 & -3 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 4 - 3 & -6 + 6 \\ 2 - 2 & -3 + 4 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$
  - Test $A^2 \cdot (A^2)^{-1}$:
    $$A^2 = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} 7 & 4 \\ 12 & 7 \end{pmatrix}$$
    $$\begin{pmatrix} 7 & 4 \\ 12 & 7 \end{pmatrix} \begin{pmatrix} 7 & -4 \\ -12 & 7 \end{pmatrix} = \begin{pmatrix} 49 - 48 & -28 + 28 \\ 84 - 84 & -48 + 49 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$
All three properties are fully verified!

---

## 8. Common Mistakes to Avoid
- **Multiplying $A^{-1}$ by 3 Instead of Dividing:** Writing $(3A)^{-1} = 3 A^{-1}$. The scalar must be inverted ($1/3$).
- **Re-inverting to Find $A$ First:** Spending time solving for $A$ when the problem explicitly says *"Without finding $A$"*.
- **Squaring Individual Entries:** Squaring entries to get $\begin{pmatrix} 4 & 1 \\ 9 & 4 \end{pmatrix}$ instead of computing the row-by-column product $A^{-1} \cdot A^{-1}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Instead of finding matrix $A$, we apply the fundamental properties of matrix inverses directly to $A^{-1}$. For scalar scaling, the factor inverts to give $(3A)^{-1} = \frac{1}{3}A^{-1} = \begin{pmatrix}2/3&-1/3\\-1&2/3\end{pmatrix}$, while for the transpose, the operations commute to give $(A^T)^{-1} = (A^{-1})^T = \begin{pmatrix}2&-3\\-1&2\end{pmatrix}$. Finally, inverting $A^2$ is identical to multiplying $A^{-1}$ by itself, which produces $(A^{-1})^2 = \begin{pmatrix}7&-4\\-12&7\end{pmatrix}$."

