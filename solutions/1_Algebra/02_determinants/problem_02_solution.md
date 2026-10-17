# Exercise 2: Determinant of a 3×3 Matrix

## 1. Original Problem
For the matrix:
$$A = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 4 \\ 2 & 1 & 5 \end{pmatrix}$$
compute $\det A$ using Sarrus' rule. Then perform one simple check using a chosen property of the determinant.

---

## 2. What We Are Trying to Find
We need to:
- Compute the determinant of a given $3 \times 3$ matrix using Sarrus' rule (diagonal diagonals scheme).
- Verify the computed determinant using an alternative property or method (such as Laplace expansion along the column with a zero).
- Show the complete algebraic steps clearly with every sign and operation explained.

---

## 3. Key Concepts and Theorems
1. **Sarrus' Rule (for $3 \times 3$ matrices only):**
   Copy the first two columns to the right of the matrix:
   $$\begin{matrix} 1 & 2 & -1 & 1 & 2 \\ 0 & 3 & 4 & 0 & 3 \\ 2 & 1 & 5 & 2 & 1 \end{matrix}$$
   - Add the products of the three downward diagonals:
     $$D_1 = (1)(3)(5) = 15, \quad D_2 = (2)(4)(2) = 16, \quad D_3 = (-1)(0)(1) = 0$$
   - Subtract the products of the three upward diagonals:
     $$U_1 = (2)(3)(-1) = -6, \quad U_2 = (1)(4)(1) = 4, \quad U_3 = (5)(0)(2) = 0$$
   $$\det A = (D_1 + D_2 + D_3) - (U_1 + U_2 + U_3)$$
2. **Laplace Expansion Check:**
   Expanding along a row or column with zero entries simplifies the computation to smaller $2 \times 2$ determinants:
   $$\det A = \sum_{j=1}^n (-1)^{i+j} a_{ij} M_{ij}$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute $\det A$ via Sarrus' Rule
Set up the diagonal products:

1. **Downward Diagonals (positive sign):**
   - First diagonal: $1 \cdot 3 \cdot 5 = 15$
   - Second diagonal: $2 \cdot 4 \cdot 2 = 16$
   - Third diagonal: $(-1) \cdot 0 \cdot 1 = 0$
   - Sum of downward diagonals:
     $$\Sigma_{\text{down}} = 15 + 16 + 0 = 31$$

2. **Upward Diagonals (negative sign):**
   - First upward diagonal: $2 \cdot 3 \cdot (-1) = -6$
   - Second upward diagonal: $1 \cdot 4 \cdot 1 = 4$
   - Third upward diagonal: $5 \cdot 0 \cdot 2 = 0$
   - Sum of upward diagonals:
     $$\Sigma_{\text{up}} = (-6) + 4 + 0 = -2$$

3. **Combine the Sums:**
   $$\det A = \Sigma_{\text{down}} - \Sigma_{\text{up}} = 31 - (-2) = 31 + 2 = 33$$

---

### Step 2: Verification Check via Laplace Expansion
To verify without repeating Sarrus, expand along the **first column**, which contains a convenient zero ($a_{21} = 0$):
$$\det A = a_{11} C_{11} + a_{21} C_{21} + a_{31} C_{31}$$
where $C_{ij} = (-1)^{i+j} M_{ij}$.

- **Term 1 ($a_{11} = 1$, row 1, col 1, sign $+$):**
  $$1 \cdot \det\begin{pmatrix} 3 & 4 \\ 1 & 5 \end{pmatrix} = 1 \cdot (3 \cdot 5 - 4 \cdot 1) = 1 \cdot (15 - 4) = 11$$
- **Term 2 ($a_{21} = 0$, row 2, col 1):**
  $$-0 \cdot \det\begin{pmatrix} 2 & -1 \\ 1 & 5 \end{pmatrix} = 0$$
- **Term 3 ($a_{31} = 2$, row 3, col 1, sign $+$):**
  $$2 \cdot \det\begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix} = 2 \cdot (2 \cdot 4 - (-1) \cdot 3) = 2 \cdot (8 + 3) = 2 \cdot 11 = 22$$

Summing the terms:
$$\det A = 11 + 0 + 22 = 33$$
Both methods match perfectly.

---

## 5. Why Each Step Is Valid
- **Sarrus' Rule Validity:** Sarrus' rule is the direct permutation expansion of the Leibniz determinant formula for $n=3$, enumerating all $3! = 6$ permutations (3 even and 3 odd).
- **Laplace Expansion Consistency:** The Laplace expansion theorem guarantees that expanding along any row or any column produces the identical determinant value.

---

## 6. Final Answer in Words
Using Sarrus' rule, the sum of the downward diagonal products is $31$ and the sum of the upward diagonal products is $-2$, giving a determinant of $31 - (-2) = 33$. Verifying this result by Laplace expansion along the first column yields $1(11) + 2(11) = 33$, confirming the calculation.

---

## 7. Quick Verification
- Sarrus' rule gave $\det A = 33$.
- Laplace expansion along column 1 gave $\det A = 33$.
- Row operation check ($R_3 \leftarrow R_3 - 2R_1$):
  Row 3 becomes $(0, -3, 7)$. Expanding along column 1 gives $1 \cdot [3(7) - 4(-3)] = 21 - (-12) = 33$. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Applying Sarrus to $4 \times 4$ Matrices:** Sarrus' rule works ONLY for $3 \times 3$ matrices. A $4 \times 4$ determinant has $4! = 24$ terms, while diagonal copying produces only 8 terms.
- **Sign Error on Upward Diagonals:** Forgetting that upward diagonals must be subtracted, or mishandling $-(-6) = +6$.
- **Index Misalignment when Copying Columns:** Misaligning columns when writing the two helper columns to the right.

---

## 9. Classroom Presentation (3-Sentence Summary)
"We evaluate the $3 \times 3$ determinant using Sarrus' rule by adding the three downward diagonal products to get $31$ and subtracting the three upward diagonal products, which sum to $-2$. This yields $\det A = 31 - (-2) = 33$. To verify the result quickly, we expand along the first column, where the zero eliminates one minor and confirms the exact value $11 + 22 = 33$."

