# Exercise 9: Matrix Equation

## 1. Original Problem
Given:
$$A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$$
Solve the equation $AX = B$ for $X$. Before calculating, decide on which side of the equation $A^{-1}$ must be used. Then check the result by computing $AX$.

---

## 2. What We Are Trying to Find
We need to:
- Determine the correct algebraic side (left versus right) to multiply by $A^{-1}$ in order to isolate the unknown matrix $X$.
- Compute the inverse matrix $A^{-1}$.
- Calculate the solution matrix $X$ using matrix multiplication.
- Check the solution by explicitly calculating the product $AX$ to confirm it reproduces matrix $B$.

---

## 3. Key Concepts and Theorems
1. **Side Dependency in Matrix Equations (Noncommutativity):**
   Because matrix multiplication is generally noncommutative ($MN \neq NM$), you cannot simply "divide by $A$."
   - In the equation $AX = B$, matrix $A$ appears on the **left** of $X$.
   - To eliminate $A$, we must multiply both sides by $A^{-1}$ **from the left**:
     $$A^{-1}(AX) = A^{-1}B \implies (A^{-1}A)X = A^{-1}B \implies IX = A^{-1}B \implies X = A^{-1}B$$
   - Multiplying from the right would give $(AX)A^{-1} = B A^{-1}$, which does NOT isolate $X$ because $A$ and $X$ cannot be swapped.
2. **Inverting a Unitriangular Shear Matrix:**
   For $A = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$, the determinant is $1$ and the inverse is simply $A^{-1} = \begin{pmatrix} 1 & -k \\ 0 & 1 \end{pmatrix}$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Decide Which Side to Multiply by $A^{-1}$
In the equation:
$$AX = B$$
The unknown matrix $X$ is multiplied by $A$ on the left.
To cancel $A$ into the identity matrix $I$, $A^{-1}$ must be positioned immediately adjacent to $A$. Therefore:
$$\mathbf{A^{-1} \text{ must be applied from the LEFT.}}$$

Setting up the algebraic derivation:
$$A^{-1}(AX) = A^{-1}B$$
$$(A^{-1}A)X = A^{-1}B$$
$$I X = A^{-1}B$$
$$X = A^{-1}B$$

---

### Step 2: Compute $A^{-1}$
For matrix $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$:
$$\det A = (1 \cdot 1) - (2 \cdot 0) = 1 - 0 = 1$$
Using the $2 \times 2$ formula (swap diagonal, negate off-diagonal, divide by 1):
$$A^{-1} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$$

---

### Step 3: Compute $X = A^{-1}B$
Multiply $A^{-1}$ by $B = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$:
$$X = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$$

Calculate each entry:
- **Top-left $(1, 1)$:** $1(3) + (-2)(2) = 3 - 4 = -1$
- **Top-right $(1, 2)$:** $1(1) + (-2)(4) = 1 - 8 = -7$
- **Bottom-left $(2, 1)$:** $0(3) + 1(2) = 0 + 2 = 2$
- **Bottom-right $(2, 2)$:** $0(1) + 1(4) = 0 + 4 = 4$

Assembling the solution matrix:
$$X = \begin{pmatrix} -1 & -7 \\ 2 & 4 \end{pmatrix}$$

---

### Step 4: Check by Computing $AX$
Multiply matrix $A$ by our solution matrix $X$:
$$AX = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -1 & -7 \\ 2 & 4 \end{pmatrix}$$

Calculate each entry:
- **Top-left $(1, 1)$:** $1(-1) + 2(2) = -1 + 4 = 3$
- **Top-right $(1, 2)$:** $1(-7) + 2(4) = -7 + 8 = 1$
- **Bottom-left $(2, 1)$:** $0(-1) + 1(2) = 0 + 2 = 2$
- **Bottom-right $(2, 2)$:** $0(-7) + 1(4) = 0 + 4 = 4$

Assembling the product:
$$AX = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} = B$$
The product matches matrix $B$ exactly, confirming the solution!

---

## 5. Why Each Step Is Valid
- **Ring Multiplication Properties:** Matrix multiplication is associative ($A^{-1}(AX) = (A^{-1}A)X$) and distributes over matrix addition, but lacks commutativity, requiring strict preservation of factor position.
- **Bijective Inversion:** Multiplying by an invertible matrix is an equivalence transformation; it neither introduces extraneous solutions nor loses valid solutions.

---

## 6. Final Answer in Words
To isolate $X$ in the equation $AX = B$, matrix $A^{-1}$ must be multiplied from the left, yielding $X = A^{-1}B$. Computing $A^{-1} = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$ and performing the multiplication yields the solution matrix $X = \begin{pmatrix} -1 & -7 \\ 2 & 4 \end{pmatrix}$. Computing $AX$ reproduces $B = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$, confirming that the result is correct.

---

## 7. Quick Verification
- **Testing the incorrect right-hand multiplication ($B A^{-1}$) to show the distinction:**
  $$B A^{-1} = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 3 & -6 + 1 \\ 2 & -4 + 4 \end{pmatrix} = \begin{pmatrix} 3 & -5 \\ 2 & 0 \end{pmatrix} \neq X$$
  Multiplying $A$ by this wrong matrix gives:
  $$\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & -5 \\ 2 & 0 \end{pmatrix} = \begin{pmatrix} 7 & -5 \\ 2 & 0 \end{pmatrix} \neq B$$
  This directly confirms that left multiplication is the only mathematically valid option. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Multiplying on the Right:** Calculating $X = B A^{-1}$ instead of $A^{-1}B$. In matrix algebra, $A^{-1}B \neq B A^{-1}$.
- **Writing $X = B / A$:** Matrix division does not exist as a mathematical notation because it fails to specify whether the inverse acts from the left or right.
- **Sign Error in $A^{-1}$:** Forgetting to change the sign of $2$ to $-2$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"In the matrix equation $AX = B$, because $A$ multiplies $X$ on the left, we must multiply both sides by $A^{-1}$ from the left to isolate $X = A^{-1}B$. Computing the inverse gives $A^{-1} = \begin{pmatrix}1&-2\\0&1\end{pmatrix}$, and multiplying it by $B$ produces the solution $X = \begin{pmatrix}-1&-7\\2&4\end{pmatrix}$. Multiplying $A$ by this resulting matrix reproduces $B$, proving our solution is correct and highlighting that multiplication side matters strictly."

