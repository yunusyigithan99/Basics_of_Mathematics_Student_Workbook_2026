# Exercise 11: Parameter and Invertibility

## 1. Original Problem
For the matrix:
$$A(t) = \begin{pmatrix} 1 & t \\ t & 1 \end{pmatrix}$$
find all $t$ for which the matrix is invertible, and then give a formula for $A(t)^{-1}$. Explain what happens to this formula at the excluded values.

---

## 2. What We Are Trying to Find
We need to:
- Express the determinant of the symmetric parameter matrix $A(t)$ in terms of $t$.
- Determine all real values of $t$ for which $A(t)$ is invertible ($\det A(t) \neq 0$).
- Derive the general algebraic formula for the inverse matrix $A(t)^{-1}$ valid for those values.
- Explain the algebraic breakdown and geometric degeneracy that occurs at the specific excluded values where invertibility fails.

---

## 3. Key Concepts and Theorems
1. **Determinant and Invertibility Condition:**
   $$A(t) \text{ is invertible} \iff \det A(t) \neq 0$$
   For $A(t) = \begin{pmatrix} 1 & t \\ t & 1 \end{pmatrix}$, the determinant is:
   $$\det A(t) = 1(1) - (t)(t) = 1 - t^2$$
2. **Formula for the Inverse of a $2 \times 2$ Matrix:**
   $$A(t)^{-1} = \frac{1}{\det A(t)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{1 - t^2} \begin{pmatrix} 1 & -t \\ -t & 1 \end{pmatrix}$$
3. **Behavior at Singular Points:**
   At values where $\det A(t) = 0$, the scalar prefactor $\frac{1}{1 - t^2}$ involves division by zero. Structurally, the rows become linearly dependent.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Determinant of $A(t)$
Using the standard $ad - bc$ rule:
$$\det A(t) = (1 \cdot 1) - (t \cdot t) = 1 - t^2$$

---

### Step 2: Determine Values of $t$ for Invertibility
The matrix $A(t)$ is invertible if and only if its determinant is non-zero:
$$\det A(t) \neq 0 \iff 1 - t^2 \neq 0 \iff t^2 \neq 1 \iff t \neq 1 \quad \text{and} \quad t \neq -1$$

Thus, $A(t)$ is invertible for all real numbers except $t = 1$ and $t = -1$:
$$t \in \mathbb{R} \setminus \{-1, 1\}$$

---

### Step 3: Derive the Explicit Inverse Formula
For any $t \neq \pm 1$, use the $2 \times 2$ matrix inverse formula:
- Swap diagonal entries: $1 \leftrightarrow 1$ (remains $1$ and $1$).
- Negate off-diagonal entries: $t$ and $t$ become $-t$ and $-t$.
- Divide by the determinant $1 - t^2$.

This gives:
$$A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix} 1 & -t \\ -t & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{1 - t^2} & \frac{-t}{1 - t^2} \\ \frac{-t}{1 - t^2} & \frac{1}{1 - t^2} \end{pmatrix}$$

---

### Step 4: Explain What Happens at the Excluded Values
The excluded values are $t = 1$ and $t = -1$.

1. **At the algebraic formula level:**
   - At both $t = 1$ and $t = -1$, the denominator of the prefactor becomes $1 - (\pm 1)^2 = 1 - 1 = 0$.
   - Division by zero is undefined in mathematics; hence, the formula cannot evaluate to a valid matrix of real numbers.

2. **At the matrix structure level:**
   - **Case $t = 1$:**
     $$A(1) = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$$
     Both rows are identical ($R_1 = R_2$). The matrix has rank $1$. It collapses all vectors in $\mathbb{R}^2$ onto the line $y = x$.
   - **Case $t = -1$:**
     $$A(-1) = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$$
     The second row is the exact negative of the first row ($R_2 = -R_1$). The matrix again has rank $1$. It collapses all vectors in $\mathbb{R}^2$ onto the line $y = -x$.

In both excluded cases, the transformation squashes the 2-dimensional plane into a 1-dimensional line. Because multiple distinct input vectors are mapped to the same output vector, the mapping is non-injective and completely irreversible.

---

## 5. Why Each Step Is Valid
- **Factorization of the Determinant:** $1 - t^2 = (1 - t)(1 + t) = 0 \iff t = 1$ or $t = -1$ by the zero-product property of the field $\mathbb{R}$.
- **Smooth Family of Inverses:** For $t \in (-1, 1) \cup (-\infty, -1) \cup (1, \infty)$, the inverse is a smooth rational matrix-valued function with poles at $t = \pm 1$.

---

## 6. Final Answer in Words
The matrix $A(t)$ is invertible for all real numbers $t$ except $t = 1$ and $t = -1$ ($t \in \mathbb{R} \setminus \{-1, 1\}$). For any valid $t$, the inverse is given by $A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix} 1 & -t \\ -t & 1 \end{pmatrix}$. At the excluded values $t = \pm 1$, the formula fails due to division by zero, which corresponds to the rows becoming linearly dependent ($R_2 = \pm R_1$) and collapsing the 2D plane into a 1D line.

---

## 7. Quick Verification
- **Testing a valid value ($t = 0$):**
  $A(0) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$.
  Formula gives $A(0)^{-1} = \frac{1}{1-0}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$. Matches! $\checkmark$
- **Testing a non-trivial valid value ($t = 2$):**
  $A(2) = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$, $\det A(2) = 1 - 4 = -3$.
  $A(2)^{-1} = \frac{1}{-3}\begin{pmatrix} 1 & -2 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} -1/3 & 2/3 \\ 2/3 & -1/3 \end{pmatrix}$.
  Product check:
  $$\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} -1/3 & 2/3 \\ 2/3 & -1/3 \end{pmatrix} = \begin{pmatrix} -1/3 + 4/3 & 2/3 - 2/3 \\ -2/3 + 2/3 & 4/3 - 1/3 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$

---

## 8. Common Mistakes to Avoid
- **Forgetting $t = -1$:** Solving $1 - t^2 = 0$ as $t = 1$ and overlooking $t = -1$.
- **Negating the Diagonal Entries:** Writing $-1$ on the main diagonal instead of $-t$ on the off-diagonal.
- **Vague Description of Excluded Values:** Simply saying "it doesn't work" without explicitly mentioning division by zero and linear dependence of the rows.

---

## 9. Classroom Presentation (3-Sentence Summary)
"The determinant of this matrix is $\det A(t) = 1 - t^2$, which is non-zero whenever $t \neq \pm 1$, giving the inverse formula $A(t)^{-1} = \frac{1}{1 - t^2} \begin{pmatrix} 1 & -t \\ -t & 1 \end{pmatrix}$. At the excluded values $t = 1$ and $t = -1$, the determinant equals zero, causing the formula to fail due to division by zero. Structurally, when $t = 1$ the rows are identical, and when $t = -1$ the rows are opposite, which in both cases collapses the 2D plane onto a 1D line and destroys invertibility."

