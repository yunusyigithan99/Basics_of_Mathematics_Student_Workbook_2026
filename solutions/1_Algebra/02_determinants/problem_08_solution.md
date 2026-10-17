# Exercise 8: Determinant of a Product

## 1. Original Problem
Let $A$ and $B$ be square matrices such that:
$$\det A = 3, \qquad \det B = -5$$
Compute $\det(AB)$, $\det(BA)$ and, if it exists, $\det(A^{-1}B)$. Explain why the first two results are equal even though usually $AB \neq BA$.

---

## 2. What We Are Trying to Find
We need to:
- Calculate the determinant of the matrix product $AB$.
- Calculate the determinant of the reversed product $BA$.
- Check whether $A^{-1}$ exists, and if so, calculate $\det(A^{-1}B)$.
- Explain how $\det(AB)$ and $\det(BA)$ can be identical even when the matrix products $AB$ and $BA$ are completely different matrices.

---

## 3. Key Concepts and Theorems
1. **Multiplicative Property of Determinants:**
   For any square matrices $A$ and $B$ of the same size:
   $$\det(AB) = \det A \cdot \det B$$
2. **Determinant of an Inverse Matrix:**
   If $\det A \neq 0$, then $A$ is invertible, and:
   $$\det(A^{-1}) = \frac{1}{\det A}$$
3. **Commutativity of Scalar Multiplication:**
   While matrix multiplication is noncommutative ($AB \neq BA$ in general), multiplication of ordinary real numbers is commutative:
   $$\text{For } x, y \in \mathbb{R}: \quad x \cdot y = y \cdot x$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $\det(AB)$
Using the multiplicative property of determinants:
$$\det(AB) = \det A \cdot \det B$$
Substitute the given numerical values:
$$\det(AB) = 3 \cdot (-5) = -15$$

---

### Step 2: Compute $\det(BA)$
Using the multiplicative property in reversed order:
$$\det(BA) = \det B \cdot \det A$$
Substitute the given numerical values:
$$\det(BA) = (-5) \cdot 3 = -15$$

---

### Step 3: Check Existence and Compute $\det(A^{-1}B)$
- **Existence check:**
  Since $\det A = 3 \neq 0$, matrix $A$ is invertible, which guarantees that $A^{-1}$ exists.
- **Compute the determinant:**
  Using the product and inverse properties:
  $$\det(A^{-1}B) = \det(A^{-1}) \cdot \det B = \left(\frac{1}{\det A}\right) \cdot \det B$$
  Substitute the numerical values:
  $$\det(A^{-1}B) = \frac{1}{3} \cdot (-5) = -\frac{5}{3}$$

---

### Step 4: Explanation of Why $\det(AB) = \det(BA)$
The apparent paradox arises from confusing matrix objects with scalar numbers:
- In the world of matrices, $AB$ and $BA$ are generally distinct matrices ($AB \neq BA$) because the geometric order of transformations matters.
- However, the determinant is a function that maps a matrix to a single **real number** (a scalar).
- When we take determinants, $\det(AB) = (\det A)(\det B)$ and $\det(BA) = (\det B)(\det A)$. Here, $\det A = 3$ and $\det B = -5$ are simply ordinary real numbers.
- Because multiplication of real numbers is commutative ($3 \cdot (-5) = -5 \cdot 3 = -15$), the scalar values must be identical:
  $$\det(AB) = \det(BA) = -15$$
Thus, even though the transformations differ, their net scaling of oriented volume is identical.

---

## 5. Why Each Step Is Valid
- **Cauchy-Binet Formula:** The determinant product formula $\det(AB) = \det A \det B$ is an algebraic identity established by the Cauchy-Binet theorem.
- **Inverse Determinant Relation:** From $A A^{-1} = I$, taking determinants gives $\det(A)\det(A^{-1}) = \det(I) = 1$. Since $\det A = 3 \neq 0$, division by $\det A$ is completely valid, yielding $\det(A^{-1}) = 1/3$.

---

## 6. Final Answer in Words
The determinant of $AB$ is $-15$, and the determinant of $BA$ is $-15$. Because $\det A = 3 \neq 0$, the inverse $A^{-1}$ exists, and the determinant of $A^{-1}B$ is $-\frac{5}{3}$. The products $AB$ and $BA$ have equal determinants because the determinant converts matrices into real numbers, and the multiplication of real numbers is commutative.

---

## 7. Quick Verification
- **Ratio check:**
  $$\det(A) \cdot \det(A^{-1}B) = 3 \cdot \left(-\frac{5}{3}\right) = -5 = \det(B) \quad \checkmark$$
- **Associative grouping check:**
  $$\det(A \cdot A^{-1} \cdot B) = \det(I \cdot B) = \det(B) = -5 \quad \checkmark$$

---

## 8. Common Mistakes to Avoid
- **Claiming $A^{-1}B$ Does Not Exist:** Forgetting to check $\det A \neq 0$ and prematurely assuming an inverse cannot be evaluated.
- **Assuming $AB = BA$ Because Their Determinants Match:** Wrongly deducing that two matrices must be identical simply because they have the same determinant. (For instance, $\begin{pmatrix}1&0\\0&1\end{pmatrix}$ and $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ both have determinant $1$, but they are not equal).
- **Inverting the Fraction:** Writing $\det(A^{-1}) = \det A = 3$ instead of $\frac{1}{3}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"By applying the product rule for determinants, we find that $\det(AB) = 3(-5) = -15$ and $\det(BA) = (-5)(3) = -15$. Because $\det A$ is non-zero, the inverse matrix exists, giving $\det(A^{-1}B) = \frac{1}{3}(-5) = -\frac{5}{3}$. Even though $AB$ and $BA$ are usually different matrices, their determinants are identical because the determinant maps them to real numbers, where scalar multiplication is strictly commutative."

