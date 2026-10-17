# Exercise 14: A Matrix That Is Its Own Inverse (Involutory Matrix)

## 1. Original Problem
Assume that a square matrix $A$ satisfies:
$$A^2 = I$$
Show that:
$$A^{-1} = A$$
Then give an example of a $2\times2$ matrix different from $I$ and $-I$ that satisfies this condition, and verify it by multiplication.

---

## 2. What We Are Trying to Find
We need to:
- Formally prove that any matrix whose square is the identity matrix is its own inverse ($A^{-1} = A$).
- Construct a concrete $2 \times 2$ matrix $A$ that is neither the identity matrix $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ nor the negative identity matrix $-I = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$, yet satisfies $A^2 = I$.
- Verify the constructed example by explicit matrix multiplication.

---

## 3. Key Concepts and Theorems
1. **Involutory Matrix:**
   A matrix $A$ is called **involutory** (an involution) if it equals its own inverse:
   $$A = A^{-1} \iff A^2 = I$$
2. **Definition of the Inverse:**
   By definition, if two square matrices $X$ and $Y$ satisfy $XY = I$ and $YX = I$, then $Y$ is the unique inverse of $X$.
   Setting $X = A$ and $Y = A$, the equation $A \cdot A = I$ immediately proves that $A$ is its own inverse.
3. **Geometric Meaning of Involutions:**
   Involutory transformations represent geometric operations that return to the starting position when applied twice. The most common examples are **reflections** (e.g., reflecting across an axis or across a diagonal line) and $180^\circ$ spatial half-turns.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Prove That $A^2 = I \implies A^{-1} = A$
We are given that:
$$A^2 = I$$
By definition of matrix powers, $A^2 = A \cdot A$. Therefore:
$$A \cdot A = I$$

There are two equally rigorous ways to conclude that $A^{-1} = A$:
- **Direct definition:** The inverse $A^{-1}$ is defined as the unique matrix that, when multiplied by $A$, yields $I$. Since $A$ multiplied by $A$ produces $I$, $A$ fulfills the definition of $A^{-1}$:
  $$A^{-1} = A$$
- **Algebraic cancellation:** Multiply both sides of $A \cdot A = I$ by $A^{-1}$ on the left:
  $$A^{-1}(A \cdot A) = A^{-1} I$$
  Using associativity of matrix multiplication:
  $$(A^{-1} A) A = A^{-1}$$
  Substitute $A^{-1}A = I$:
  $$I A = A^{-1} \implies A = A^{-1}$$
This completes the mathematical proof.

---

### Step 2: Construct an Example Different from $I$ and $-I$
To find a non-trivial involution in $\mathbb{R}^{2 \times 2}$, consider a **reflection across the $x$-axis**.
A reflection across the $x$-axis keeps the $x$-coordinate unchanged and negates the $y$-coordinate:
$$(x, y) \mapsto (x, -y)$$
In matrix form, this is represented by:
$$A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
Observe that:
- $A \neq I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$
- $A \neq -I = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$

*(Alternative valid examples include the reflection across the line $y=x$, given by $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, or reflection across the $y$-axis $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$.)*

---

### Step 3: Verify the Example by Matrix Multiplication
Multiply matrix $A$ by itself:
$$A^2 = A \cdot A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

Calculate each entry:
- **Top-left $(1, 1)$:** $1(1) + 0(0) = 1 + 0 = 1$
- **Top-right $(1, 2)$:** $1(0) + 0(-1) = 0 + 0 = 0$
- **Bottom-left $(2, 1)$:** $0(1) + (-1)(0) = 0 + 0 = 0$
- **Bottom-right $(2, 2)$:** $0(0) + (-1)(-1) = 0 + 1 = 1$

Assembling the product matrix:
$$A^2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$$
The matrix squares to the identity, confirming that $A = A^{-1}$.

---

## 5. Why Each Step Is Valid
- **Uniqueness of Inverses in Groups:** In the general linear group $\operatorname{GL}_n(\mathbb{R})$, every element has a unique two-sided inverse; showing $A \cdot A = I$ uniquely identifies $A^{-1}$ as $A$.
- **Idempotence of Paired Reflections:** Reflecting a point across a mirror line twice returns the point to its original position: $R \circ R = \text{id}$.

---

## 6. Final Answer in Words
If $A^2 = I$, multiplying both sides by $A^{-1}$ yields $(A^{-1}A)A = A^{-1}$, which simplifies directly to $A = A^{-1}$, proving that $A$ is its own inverse. A non-trivial example different from $\pm I$ is the reflection matrix $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$. Computing $A \cdot A$ produces the identity matrix $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, verifying that $A^2 = I$ and $A^{-1} = A$.

---

## 7. Quick Verification
- **Determinant check:**
  $\det(A^2) = (\det A)^2 = \det(I) = 1 \implies \det A = \pm 1$.
  For our example $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, $\det A = 1(-1) - 0 = -1$.
  Using the $2 \times 2$ inverse formula:
  $$A^{-1} = \frac{1}{-1}\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = A \quad \checkmark$$
- **Alternative example check ($y=x$ reflection):**
  $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$

---

## 8. Common Mistakes to Avoid
- **Providing $I$ or $-I$ as the Example:** The problem explicitly instructs that the example must be *"different from $I$ and $-I$"*.
- **Assuming $A^2 = I \implies A = \pm I$ for Matrices:** Confusing matrix algebra with scalar algebra (where $x^2 = 1 \implies x = \pm 1$). Matrices can satisfy $A^2 = I$ without being equal to $\pm I$.
- **Circular Reasoning in the Proof:** Assuming $A = A^{-1}$ to prove $A = A^{-1}$, instead of starting from $A^2 = I$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Starting from the condition $A^2 = I$, we write $A \cdot A = I$ and multiply both sides by $A^{-1}$, which immediately proves that $A = A^{-1}$. While in scalar numbers $x^2 = 1$ only allows $\pm 1$, in matrix algebra geometric reflections provide infinite solutions, such as the reflection matrix $A = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$. Squaring this matrix gives $\begin{pmatrix}1&0\\0&1\end{pmatrix}$, proving that applying a reflection twice returns every point to its original position."

