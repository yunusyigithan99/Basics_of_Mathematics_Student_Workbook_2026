# Exercise 6: Parameter and Invertibility

## 1. Original Problem
For the matrix:
$$A(t) = \begin{pmatrix} t & 1 \\ 2 & t \end{pmatrix}$$
find all values of $t$ for which the matrix is not invertible. Explain how your answer is related to the determinant being zero.

---

## 2. What We Are Trying to Find
We need to:
- Express the determinant of the parameterized matrix $A(t)$ as an algebraic function of the parameter $t$.
- Identify all values of $t$ that cause the matrix to lose its invertibility (become singular).
- Explain the fundamental mathematical connection between non-invertibility and a zero determinant.

---

## 3. Key Concepts and Theorems
1. **Determinant of a $2 \times 2$ Parameter Matrix:**
   $$\det A(t) = ad - bc = (t)(t) - (1)(2) = t^2 - 2$$
2. **Invertibility Theorem:**
   A square matrix is invertible if and only if its determinant is non-zero:
   $$A(t) \text{ is invertible} \iff \det A(t) \neq 0$$
   Consequently, the matrix is **not invertible** if and only if its determinant equals zero:
   $$A(t) \text{ is not invertible} \iff \det A(t) = 0$$
3. **Geometric and Algebraic Meaning of $\det A = 0$:**
   When the determinant is zero:
   - The matrix maps the 2D plane onto a 1-dimensional line, destroying information and losing injectivity.
   - The rows (and columns) become linearly dependent (parallel vectors).
   - The standard matrix inverse formula $A^{-1} = \frac{1}{\det A}\operatorname{adj}(A)$ fails due to division by zero.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Determinant of $A(t)$
Using the $2 \times 2$ determinant formula:
$$\det A(t) = \det\begin{pmatrix} t & 1 \\ 2 & t \end{pmatrix} = (t \cdot t) - (1 \cdot 2) = t^2 - 2$$

---

### Step 2: Set the Determinant Equal to Zero
To find the values of $t$ where the matrix is not invertible, set the determinant to zero:
$$\det A(t) = 0 \iff t^2 - 2 = 0$$

Solve this quadratic equation:
$$t^2 = 2 \implies t = \pm\sqrt{2}$$

Thus, there are two such values:
$$t_1 = \sqrt{2}, \qquad t_2 = -\sqrt{2}$$

---

### Step 3: Explain the Relation to the Zero Determinant
- **Why $\det A = 0$ implies non-invertibility:**
  If a matrix $A$ has an inverse $A^{-1}$, then by the multiplicative property of determinants:
  $$\det(A \cdot A^{-1}) = \det(I) \implies \det(A) \cdot \det(A^{-1}) = 1$$
  This identity requires that $\det(A) \neq 0$, because no real number multiplied by zero can equal $1$. Therefore, whenever $\det A(t) = 0$, an inverse matrix cannot exist mathematically.
- **Structural inspection at $t = \sqrt{2}$:**
  $$A(\sqrt{2}) = \begin{pmatrix} \sqrt{2} & 1 \\ 2 & \sqrt{2} \end{pmatrix}$$
  Notice that Row 2 is exactly $\sqrt{2}$ times Row 1:
  $$\sqrt{2} \cdot (\sqrt{2}, 1) = (2, \sqrt{2})$$
  The rows are linearly dependent, confirming that the matrix collapses the plane into a single line.

---

## 5. Why Each Step Is Valid
- **Characteristic Determinant Evaluation:** The determinant polynomial $t^2 - 2$ is a smooth continuous function of $t$, whose roots isolate the exact singular points of the matrix family.
- **Field Axioms:** The equation $t^2 = 2$ in $\mathbb{R}$ has exactly two distinct solutions: $+\sqrt{2}$ and $-\sqrt{2}$.

---

## 6. Final Answer in Words
The matrix $A(t)$ is not invertible for two values of the parameter: $t = \sqrt{2}$ and $t = -\sqrt{2}$. This happens because a matrix fails to be invertible if and only if its determinant equals zero; setting the determinant $t^2 - 2 = 0$ yields $t = \pm\sqrt{2}$, which makes the rows linearly dependent and collapses the area factor to zero.

---

## 7. Quick Verification
- **Testing $t = \sqrt{2}$:**
  $$\det A(\sqrt{2}) = (\sqrt{2})(\sqrt{2}) - (1)(2) = 2 - 2 = 0 \implies \text{Not invertible} \quad \checkmark$$
- **Testing $t = -\sqrt{2}$:**
  $$\det A(-\sqrt{2}) = (-\sqrt{2})(-\sqrt{2}) - (1)(2) = 2 - 2 = 0 \implies \text{Not invertible} \quad \checkmark$$
- **Testing a non-singular value (e.g., $t = 0$):**
  $$\det A(0) = (0)(0) - 2 = -2 \neq 0 \implies \text{Invertible} \quad \checkmark$$

---

## 8. Common Mistakes to Avoid
- **Forgetting the Negative Root:** Writing only $t = \sqrt{2}$ and forgetting that $(-\sqrt{2})^2 = 2$ also solves $t^2 = 2$.
- **Setting Entries to Zero Instead of the Determinant:** Mistakenly solving for entries being zero ($t = 0$) rather than setting the entire determinant expression $t^2 - 2 = 0$.
- **Sign Error in Determinant:** Computing $t^2 + 2 = 0$, which would yield no real solutions.

---

## 9. Classroom Presentation (3-Sentence Summary)
"The determinant of the parameterized matrix is $\det A(t) = t^2 - 2$. Because a square matrix is non-invertible if and only if its determinant is zero, we solve $t^2 - 2 = 0$, giving $t = \pm\sqrt{2}$. At these two values, the rows become linearly dependent multiples of each other, meaning the matrix collapses 2D space into a 1D line and cannot be inverted."

