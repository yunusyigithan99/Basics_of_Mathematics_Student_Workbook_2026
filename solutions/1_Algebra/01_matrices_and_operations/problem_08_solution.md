# Exercise 8: Row Operations and Their Reversibility

## 1. Original Problem
For the matrix:
$$A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & 1 \\ -1 & 1 & 3 \end{pmatrix}$$
perform, in order:
1. $R_2 \leftarrow R_2 - 2R_1$,
2. $R_3 \leftarrow R_3 + R_1$,
3. interchange $R_2$ and $R_3$.

Write the matrix after each step. Then, for each of the three operations, state an operation that reverses it.

---

## 2. What We Are Trying to Find
We need to:
- Apply three elementary row operations sequentially to matrix $A$, showing the resulting matrix after each individual modification.
- Identify and formulate the exact inverse operation that cancels each row operation and restores the matrix to its prior state.
- Demonstrate that elementary row operations are completely reversible and do not lose information.

---

## 3. Key Concepts and Theorems
1. **Elementary Row Operations (EROs):**
   There are three types of elementary row operations:
   - **Type 1 (Replacement/Addition):** Add a multiple of one row to another row ($R_i \leftarrow R_i + cR_j$).
   - **Type 2 (Scaling):** Multiply a row by a non-zero scalar ($R_i \leftarrow cR_i$, $c \neq 0$).
   - **Type 3 (Swap/Interchange):** Swap two rows ($R_i \leftrightarrow R_j$).
2. **Reversibility (Invertibility):**
   Every elementary row operation is reversible:
   - The reverse of $R_i \leftarrow R_i + cR_j$ is $R_i \leftarrow R_i - cR_j$.
   - The reverse of $R_i \leftarrow cR_i$ is $R_i \leftarrow \frac{1}{c}R_i$.
   - The reverse of $R_i \leftrightarrow R_j$ is swapping the same two rows back: $R_i \leftrightarrow R_j$.
3. **Equivalence of Linear Systems:**
   Because row operations are reversible, applying them to an augmented matrix transforms a system of linear equations into an equivalent system having the exact same solution set.

---

## 4. Detailed Step-by-Step Solution

We start with the initial matrix:
$$A = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & 1 \\ -1 & 1 & 3 \end{pmatrix}$$

---

### Step 1: Perform $R_2 \leftarrow R_2 - 2R_1$
We keep Row 1 and Row 3 unchanged. We compute the new Row 2 entry-by-entry:
- First entry: $2 - 2(1) = 2 - 2 = 0$
- Second entry: $4 - 2(2) = 4 - 4 = 0$
- Third entry: $1 - 2(-1) = 1 + 2 = 3$

The matrix after Step 1 is:
$$A^{(1)} = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ -1 & 1 & 3 \end{pmatrix}$$

**Inverse Operation:**
To undo subtracting $2R_1$, we add $2R_1$ back to Row 2:
$$R_2 \leftarrow R_2 + 2R_1$$

---

### Step 2: Perform $R_3 \leftarrow R_3 + R_1$
Starting from $A^{(1)}$, we keep Row 1 and Row 2 unchanged and update Row 3:
- First entry: $-1 + 1 = 0$
- Second entry: $1 + 2 = 3$
- Third entry: $3 + (-1) = 2$

The matrix after Step 2 is:
$$A^{(2)} = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 3 & 2 \end{pmatrix}$$

**Inverse Operation:**
To undo adding $R_1$, we subtract $R_1$ from Row 3:
$$R_3 \leftarrow R_3 - R_1$$

---

### Step 3: Interchange $R_2$ and $R_3$ ($R_2 \leftrightarrow R_3$)
Starting from $A^{(2)}$, swap the positions of the second and third rows:
- The new Row 2 becomes the old Row 3: $(0, 3, 2)$
- The new Row 3 becomes the old Row 2: $(0, 0, 3)$

The matrix after Step 3 is:
$$A^{(3)} = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix}$$

**Inverse Operation:**
To undo swapping Row 2 and Row 3, we simply swap them again:
$$R_2 \leftrightarrow R_3$$

---

## 5. Why Each Step Is Valid
- **Linear Combination of Equations:** In Step 1 and Step 2, adding multiples of Row 1 to other rows is valid because it represents adding valid linear equations together, preserving the underlying relations between variables.
- **Row Permutation:** In Step 3, changing the vertical order of equations does not change which values of variables satisfy the equations.
- **Matrix Invertibility:** Each row operation corresponds algebraically to multiplying on the left by an invertible elementary matrix $E$, ensuring no dimension loss or irreversible distortion occurs.

---

## 6. Final Answer in Words
After the first operation ($R_2 \leftarrow R_2 - 2R_1$), the matrix becomes $\begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ -1 & 1 & 3 \end{pmatrix}$, whose reverse operation is $R_2 \leftarrow R_2 + 2R_1$. After the second operation ($R_3 \leftarrow R_3 + R_1$), the matrix becomes $\begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 3 & 2 \end{pmatrix}$, whose reverse operation is $R_3 \leftarrow R_3 - R_1$. After interchanging rows 2 and 3, the final matrix is $\begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix}$ (which is in upper-triangular echelon form), and its reverse operation is swapping rows 2 and 3 again ($R_2 \leftrightarrow R_3$).

---

## 7. Quick Verification
- **Testing the reverse of Step 3 on $A^{(3)}$:**
  Swap $R_2$ and $R_3$:
  $$\begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix} \xrightarrow{R_2 \leftrightarrow R_3} \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ 0 & 3 & 2 \end{pmatrix} = A^{(2)} \quad \checkmark$$
- **Testing the reverse of Step 2 on $A^{(2)}$:**
  Subtract $R_1$ from $R_3$:
  $$\begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ 0 - 1 & 3 - 2 & 2 - (-1) \end{pmatrix} = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 0 & 3 \\ -1 & 1 & 3 \end{pmatrix} = A^{(1)} \quad \checkmark$$
- **Testing the reverse of Step 1 on $A^{(1)}$:**
  Add $2R_1$ to $R_2$:
  $$\begin{pmatrix} 1 & 2 & -1 \\ 0 + 2(1) & 0 + 2(2) & 3 + 2(-1) \\ -1 & 1 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 2 & -1 \\ 2 & 4 & 1 \\ -1 & 1 & 3 \end{pmatrix} = A \quad \checkmark$$
Every step successfully returns to the original matrix!

---

## 8. Common Mistakes to Avoid
- **Arithmetic Sign Slip with Negative Entries:** In Step 1, subtracting $2(-1)$ from $1$ gives $1 - (-2) = 3$, not $-1$.
- **Altering the Source Row:** Erroneously changing Row 1 while computing $R_2 - 2R_1$. The source row ($R_1$) must remain completely unchanged.
- **Applying Next Operations to the Original Matrix:** Applying Step 2 or Step 3 to the initial matrix $A$ instead of the sequentially updated matrices $A^{(1)}$ and $A^{(2)}$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"We sequentially apply Gaussian row operations to eliminate the leading entries in the first column, producing an upper-triangular echelon matrix $\begin{pmatrix} 1 & 2 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix}$. Each of these elementary operations is completely reversible: subtracting a row is reversed by adding it, and swapping rows is reversed by swapping them back. This guaranteed reversibility is the core reason why Gaussian elimination simplifies linear systems without altering their solutions."

