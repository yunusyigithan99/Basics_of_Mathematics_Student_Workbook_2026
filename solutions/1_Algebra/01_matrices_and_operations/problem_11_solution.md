# Exercise 11: When Do Matrices Commute?

## 1. Original Problem
Given:
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$
Find the conditions on $a, b, c, d$ under which $AB = BA$. Describe the general form of all such matrices $B$.

---

## 2. What We Are Trying to Find
We need to:
- Compute the matrix products $AB$ and $BA$ in terms of the unknown parameters $a, b, c, d$.
- Set the two resulting matrices equal to each other ($AB = BA$) to form a system of algebraic equations.
- Solve this system for the variables $a, b, c, d$.
- Write out the general form of any matrix $B$ that commutes with $A$ and interpret its structure.

---

## 3. Key Concepts and Theorems
1. **Commutativity of Matrices:**
   Two square matrices $A$ and $B$ commute if and only if $AB = BA$.
2. **Matrix Equality:**
   Two matrices of identical size are equal if and only if all four corresponding entries are equal:
   $$\begin{pmatrix} x_1 & x_2 \\ x_3 & x_4 \end{pmatrix} = \begin{pmatrix} y_1 & y_2 \\ y_3 & y_4 \end{pmatrix} \iff x_1 = y_1, \; x_2 = y_2, \; x_3 = y_3, \; x_4 = y_4$$
3. **The Commutant (Centralizer) of a Matrix:**
   The set of all matrices that commute with a given matrix $A$ forms a linear subspace (and a subalgebra) containing at least all scalar multiples of the identity ($aI$) and polynomials in $A$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Product $AB$
Multiply $A$ by $B$:
$$AB = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$
- Top-left entry: $1 \cdot a + 1 \cdot c = a + c$
- Top-right entry: $1 \cdot b + 1 \cdot d = b + d$
- Bottom-left entry: $0 \cdot a + 1 \cdot c = c$
- Bottom-right entry: $0 \cdot b + 1 \cdot d = d$

Thus:
$$AB = \begin{pmatrix} a + c & b + d \\ c & d \end{pmatrix}$$

---

### Step 2: Compute the Product $BA$
Multiply $B$ by $A$:
$$BA = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
- Top-left entry: $a \cdot 1 + b \cdot 0 = a$
- Top-right entry: $a \cdot 1 + b \cdot 1 = a + b$
- Bottom-left entry: $c \cdot 1 + d \cdot 0 = c$
- Bottom-right entry: $c \cdot 1 + d \cdot 1 = c + d$

Thus:
$$BA = \begin{pmatrix} a & a + b \\ c & c + d \end{pmatrix}$$

---

### Step 3: Equate Corresponding Entries
For $AB = BA$, we equate the matrices entry-by-entry:
$$\begin{pmatrix} a + c & b + d \\ c & d \end{pmatrix} = \begin{pmatrix} a & a + b \\ c & c + d \end{pmatrix}$$

This gives four scalar equations:
1. **Entry $(1,1)$:** $a + c = a \implies c = 0$
2. **Entry $(1,2)$:** $b + d = a + b \implies d = a$
3. **Entry $(2,1)$:** $c = c$ (always true for any $c$)
4. **Entry $(2,2)$:** $d = c + d \implies c = 0$

---

### Step 4: Deduce the Conditions and General Form
From Equations (1) and (4), we must have:
$$c = 0$$
From Equation (2), we must have:
$$d = a$$
There are no constraints on $b$; it can be any arbitrary real number. Likewise, $a$ can be any arbitrary real number.

Substituting $c = 0$ and $d = a$ back into matrix $B$ yields the general form:
$$B = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}, \qquad \text{where } a, b \in \mathbb{R}$$

Notice that we can decompose this general matrix as:
$$B = \begin{pmatrix} a & 0 \\ 0 & a \end{pmatrix} + \begin{pmatrix} 0 & b \\ 0 & 0 \end{pmatrix} = a \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + b \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = a I + b(A - I)$$
This shows that every matrix that commutes with $A$ is an upper-triangular matrix with equal diagonal entries, which is a linear combination of the identity matrix $I$ and the shear matrix $(A - I)$.

---

## 5. Why Each Step Is Valid
- **Matrix Equality Definition:** Two matrices are identical if and only if each coordinate entry matches; this transforms a single matrix equation into an exact system of four linear equations.
- **Algebraic Cancellation:** Subtracting $a$ from both sides of $a + c = a$ yields $c = 0$ by the additive group properties of $\mathbb{R}$.
- **Consistency of the System:** Both the $(1,1)$ and $(2,2)$ entries independently require $c = 0$, proving that the system of equations is completely consistent.

---

## 6. Final Answer in Words
For matrices $A$ and $B$ to commute ($AB = BA$), two conditions must hold simultaneously: $c = 0$ and $d = a$, while $a$ and $b$ can be any real numbers. The general form of all such matrices $B$ is an upper-triangular matrix of the form $\begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$, having identical diagonal entries and zero in the bottom-left position.

---

## 7. Quick Verification
Let us choose concrete values, say $a = 3$ and $b = 5$, giving $B = \begin{pmatrix} 3 & 5 \\ 0 & 3 \end{pmatrix}$.
- Compute $AB$:
  $$AB = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 3 & 5 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 1(3) + 1(0) & 1(5) + 1(3) \\ 0(3) + 1(0) & 0(5) + 1(3) \end{pmatrix} = \begin{pmatrix} 3 & 8 \\ 0 & 3 \end{pmatrix}$$
- Compute $BA$:
  $$BA = \begin{pmatrix} 3 & 5 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 3(1) + 5(0) & 3(1) + 5(1) \\ 0(1) + 3(0) & 0(1) + 3(1) \end{pmatrix} = \begin{pmatrix} 3 & 8 \\ 0 & 3 \end{pmatrix}$$
Since $AB = BA = \begin{pmatrix} 3 & 8 \\ 0 & 3 \end{pmatrix}$, the condition is verified. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Assuming Only Multiples of Identity Commute:** Concluding that $B$ must simply be $aI$ (i.e., assuming $b$ must be $0$). In fact, any value of $b$ commutes because the upper-right entry of $A$ allows coupling with $b$.
- **Overlooking Equation $(1,2)$:** Forgetting to equate the top-right entries ($b+d = a+b$), which is the crucial step establishing that the diagonal entries must be equal ($d = a$).
- **Writing $c$ as Arbitrary:** Missing the requirement $c = 0$ from the top-left equation.

---

## 9. Classroom Presentation (3-Sentence Summary)
"By computing the products $AB$ and $BA$ in terms of parameters $a, b, c, d$ and equating corresponding entries, we obtain the constraints $c = 0$ and $d = a$. This means that any matrix commuting with $A$ must be upper-triangular with equal numbers along its main diagonal. Consequently, all commuting matrices take the general form $B = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$, which represents a 2-dimensional subspace spanned by the identity matrix and $A$ itself."

