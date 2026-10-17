# Exercise 7: Inverse of a Product

## 1. Original Problem
For the matrices:
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$$
compute $(AB)^{-1}$ and $B^{-1}A^{-1}$. Check that the results are the same and explain the meaning of the reversed order.

---

## 2. What We Are Trying to Find
We need to:
- Compute the matrix product $AB$ and then invert that product to find $(AB)^{-1}$.
- Invert matrices $A$ and $B$ individually, and then multiply them in reversed order: $B^{-1}A^{-1}$.
- Confirm that both calculation paths produce the exact same matrix.
- Explain the physical and algebraic meaning of reversing the order of factors when inverting a product.

---

## 3. Key Concepts and Theorems
1. **The Inverse of a Product Theorem (Order Reversal):**
   For any two invertible matrices $A$ and $B$ of the same size, the inverse of their product is the product of their inverses in **reverse order**:
   $$(AB)^{-1} = B^{-1}A^{-1}$$
2. **The "Socks and Shoes" Principle:**
   If you put on your socks first ($B$), then put on your shoes ($A$), to undo this action and return to your original state, you must take off your shoes first ($A^{-1}$), and then take off your socks ($B^{-1}$).
   Algebraically, multiplying $(AB)$ by $(B^{-1}A^{-1})$ allows the adjacent inner terms to cancel:
   $$(AB)(B^{-1}A^{-1}) = A(B B^{-1})A^{-1} = A I A^{-1} = A A^{-1} = I$$
   If you incorrectly multiply by $A^{-1}B^{-1}$, you get $(AB)(A^{-1}B^{-1})$, which cannot simplify because $B$ and $A^{-1}$ do not commute!

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $(AB)^{-1}$
- **First, compute the product $AB$:**
  $$AB = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 1(2) + 1(0) & 1(0) + 1(3) \\ 0(2) + 1(0) & 0(0) + 1(3) \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ 0 & 3 \end{pmatrix}$$

- **Second, compute the determinant of $AB$:**
  $$\det(AB) = (2 \cdot 3) - (3 \cdot 0) = 6 - 0 = 6$$

- **Third, invert $AB$ using the $2 \times 2$ formula:**
  $$(AB)^{-1} = \frac{1}{6} \begin{pmatrix} 3 & -3 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} \frac{3}{6} & -\frac{3}{6} \\ 0 & \frac{2}{6} \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \end{pmatrix}$$

---

### Step 2: Compute $B^{-1}A^{-1}$
- **Invert $A$:**
  $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \implies \det A = 1$.
  $$A^{-1} = \frac{1}{1}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$

- **Invert $B$:**
  $B = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ is a diagonal matrix. Inverting the diagonal entries:
  $$B^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{3} \end{pmatrix}$$

- **Multiply in reverse order ($B^{-1} A^{-1}$):**
  $$B^{-1}A^{-1} = \begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{3} \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2}(1) + 0 & \frac{1}{2}(-1) + 0 \\ 0 + \frac{1}{3}(0) & 0 + \frac{1}{3}(1) \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \end{pmatrix}$$

---

### Step 3: Compare Results
Comparing the two matrices:
$$(AB)^{-1} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{1}{3} \end{pmatrix} = B^{-1}A^{-1}$$
The two matrices are completely identical.

---

### Step 4: Explanation of the Reversed Order
Matrix multiplication represents the composition of geometric transformations.
- In the product $AB\mathbf{x} = A(B\mathbf{x})$, the transformation $B$ acts **first** on the vector, and $A$ acts **second**.
- To reverse this composite action, we must undo the operations in the exact reverse sequence: we must first undo what was done last (apply $A^{-1}$), and then undo what was done first (apply $B^{-1}$).
- Writing this in algebraic functional notation:
  $$(AB)^{-1} = B^{-1}A^{-1}$$
- If we didn't reverse the order, we would compute $A^{-1}B^{-1}$, which gives $\begin{pmatrix} 1/2 & -1/3 \\ 0 & 1/3 \end{pmatrix} \neq (AB)^{-1}$.

---

## 5. Why Each Step Is Valid
- **Cancellation of Adjacent Inverses:** $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I$ by associativity of matrix multiplication.
- **Uniqueness of the Matrix Inverse:** If a matrix $M$ satisfies $(AB)M = I$, then $M$ must be the unique inverse $(AB)^{-1}$.

---

## 6. Final Answer in Words
Computing $(AB)^{-1}$ directly gives the matrix with top row $1/2, -1/2$ and bottom row $0, 1/3$. Computing $B^{-1}A^{-1}$ produces the identical matrix, confirming that $(AB)^{-1} = B^{-1}A^{-1}$. The order of the factors must reverse because the last transformation applied ($A$) must be the first one undone ($A^{-1}$), allowing adjacent matrices to cancel into the identity.

---

## 7. Quick Verification
- **Testing the wrong order $A^{-1}B^{-1}$ to prove it fails:**
  $$A^{-1}B^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1/2 & 0 \\ 0 & 1/3 \end{pmatrix} = \begin{pmatrix} 1/2 & -1/3 \\ 0 & 1/3 \end{pmatrix} \neq (AB)^{-1}$$
  The top-right entry is $-1/3$ instead of $-1/2$. This verifies that order reversal is strictly necessary. $\checkmark$
- **Product check:**
  $$(AB)(B^{-1}A^{-1}) = \begin{pmatrix} 2 & 3 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1/2 & -1/2 \\ 0 & 1/3 \end{pmatrix} = \begin{pmatrix} 1 & -1 + 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I \quad \checkmark$$

---

## 8. Common Mistakes to Avoid
- **Assuming Inversion Distributes Without Order Reversal:** Writing $(AB)^{-1} = A^{-1}B^{-1}$. This is only true in the rare case where $A$ and $B$ commute.
- **Diagonal Inverse Slip:** Writing $B^{-1} = \begin{pmatrix} -2 & 0 \\ 0 & -3 \end{pmatrix}$ instead of taking reciprocals $1/2$ and $1/3$.
- **Negating the Diagonal Entries in $A^{-1}$:** Changing $+1$ to $-1$ on the main diagonal of $A^{-1}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Calculating $(AB)^{-1}$ and $B^{-1}A^{-1}$ both yield the exact same matrix $\begin{pmatrix}1/2&-1/2\\0&1/3\end{pmatrix}$, confirming that the inverse of a product is the product of the inverses in reverse order. Reversing the order is mathematically essential because in the product $AB$, the transformation $B$ acts first and $A$ acts second, so undoing the composition requires reversing $A$ first and then $B$. This ensures that when the product and its inverse are multiplied, the adjacent matrices $B$ and $B^{-1}$ cancel directly to the identity."

