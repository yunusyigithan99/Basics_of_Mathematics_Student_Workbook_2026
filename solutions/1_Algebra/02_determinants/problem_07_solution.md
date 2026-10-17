# Exercise 7: Using Properties Instead of Recomputing

## 1. Original Problem
Suppose that for a $3 \times 3$ matrix, $\det A = -4$. Compute:
$$\det(2A), \qquad \det(A^T), \qquad \det(A^2), \qquad \det(-A)$$
Justify each answer using the appropriate property.

---

## 2. What We Are Trying to Find
We are given that $A$ is an $n \times n$ matrix with $n = 3$ and that its determinant is $\det A = -4$. We need to compute:
- The determinant of the scaled matrix $2A$.
- The determinant of the transposed matrix $A^T$.
- The determinant of the squared matrix $A^2$.
- The determinant of the negated matrix $-A$.
Each calculation must be fully justified by quoting the general theorem/property for $n \times n$ determinants.

---

## 3. Key Concepts and Theorems
For any $n \times n$ matrix $A$ and scalar $c \in \mathbb{R}$:
1. **Scalar Multiplication Property:**
   Multiplying an entire $n \times n$ matrix by a scalar $c$ scales every one of its $n$ rows by $c$. Therefore:
   $$\det(cA) = c^n \det A$$
   *(Crucial note: The exponent $n$ equals the dimension of the matrix!)*
2. **Transpose Invariance Property:**
   Transposing a matrix does not change its determinant:
   $$\det(A^T) = \det A$$
3. **Multiplicative Property (Determinant of a Product):**
   The determinant of a product of matrices equals the product of their determinants:
   $$\det(AB) = \det A \cdot \det B \implies \det(A^k) = (\det A)^k$$
4. **Negation Property:**
   Negation is scalar multiplication by $c = -1$:
   $$\det(-A) = \det((-1)A) = (-1)^n \det A$$

---

## 4. Detailed Step-by-Step Solution

Given data:
- Matrix size: $n = 3$
- Known determinant: $\det A = -4$

---

### Step 1: Compute $\det(2A)$
- **Property used:** $\det(cA) = c^n \det A$ with scalar $c = 2$ and dimension $n = 3$.
- **Calculation:**
  $$\det(2A) = 2^3 \cdot \det A = 8 \cdot (-4) = -32$$
- **Justification:** Multiplying matrix $A$ by $2$ doubles all 3 rows. Since each doubled row factors out a $2$ from the determinant, the total factor introduced is $2 \cdot 2 \cdot 2 = 2^3 = 8$.

---

### Step 2: Compute $\det(A^T)$
- **Property used:** $\det(A^T) = \det A$.
- **Calculation:**
  $$\det(A^T) = \det A = -4$$
- **Justification:** Transposing swaps rows and columns. In the Leibniz formula, swapping rows and columns corresponds to summing over inverse permutations, which have identical signs, leaving the determinant invariant.

---

### Step 3: Compute $\det(A^2)$
- **Property used:** $\det(A^2) = \det(A \cdot A) = (\det A)^2$.
- **Calculation:**
  $$\det(A^2) = (-4)^2 = 16$$
- **Justification:** The determinant is completely multiplicative over matrix products. Squaring the matrix squares its volume scaling factor.

---

### Step 4: Compute $\det(-A)$
- **Property used:** $\det(-A) = (-1)^n \det A$ with dimension $n = 3$.
- **Calculation:**
  $$\det(-A) = (-1)^3 \cdot \det A = (-1) \cdot (-4) = 4$$
- **Justification:** Negating matrix $A$ multiplies each of the 3 rows by $-1$. Factoring $-1$ out of all three rows gives $(-1)^3 = -1$, which flips the sign of $-4$ to $+4$.

---

## 5. Why Each Step Is Valid
- **Multilinearity with Respect to Rows:** The determinant is linear in each row independently. When an $n \times n$ matrix is multiplied by $c$, every row is scaled, producing $n$ independent factors of $c$.
- **Homomorphism Property:** The determinant function $\det: \operatorname{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$ is a group homomorphism, guaranteeing $\det(A^k) = (\det A)^k$.

---

## 6. Final Answer in Words
For the given $3 \times 3$ matrix with $\det A = -4$:
- $\det(2A) = 2^3(-4) = -32$
- $\det(A^T) = -4$
- $\det(A^2) = (-4)^2 = 16$
- $\det(-A) = (-1)^3(-4) = 4$

---

## 7. Quick Verification
- Check with a simple diagonal matrix $A = \operatorname{diag}(-4, 1, 1)$, which has size $3 \times 3$ and $\det A = (-4)(1)(1) = -4$:
  - $2A = \operatorname{diag}(-8, 2, 2) \implies \det(2A) = (-8)(2)(2) = -32 \quad \checkmark$
  - $A^T = A \implies \det(A^T) = -4 \quad \checkmark$
  - $A^2 = \operatorname{diag}(16, 1, 1) \implies \det(A^2) = (16)(1)(1) = 16 \quad \checkmark$
  - $-A = \operatorname{diag}(4, -1, -1) \implies \det(-A) = (4)(-1)(-1) = 4 \quad \checkmark$
All concrete checks match the theoretical values perfectly.

---

## 8. Common Mistakes to Avoid
- **Forgetting the Matrix Dimension in Scalar Scaling:** Writing $\det(2A) = 2 \det A = -8$ instead of $2^3 \det A = -32$. A scalar pulls out to the power of the matrix size $n$.
- **Assuming $\det(-A) = -\det A$ Always:** For $n = 3$, $(-1)^3 = -1$, but for an even dimension like $n = 2$ or $n = 4$, $\det(-A) = + \det A$. Always check whether $n$ is even or odd!
- **Squaring the Sign Incorrectly in $A^2$:** Writing $(-4)^2 = -16$. A real number squared is always non-negative.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Because $A$ is a $3 \times 3$ matrix, pulling out a scalar requires raising it to the third power, which gives $\det(2A) = 2^3(-4) = -32$ and $\det(-A) = (-1)^3(-4) = 4$. Transposition leaves the determinant completely unchanged, so $\det(A^T) = -4$. Finally, because the determinant of a product is the product of determinants, squaring the matrix gives $\det(A^2) = (-4)^2 = 16$."

