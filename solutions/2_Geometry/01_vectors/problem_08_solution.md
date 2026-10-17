# Problem 8 Solution: Linear Combination and Checking the Result

## 1. Original Problem
Check whether the vector
$$w = (5, 1)$$
can be written as a linear combination of
$$u = (1, 1) \quad \text{and} \quad v = (2, -1),$$
in the form:
$$w = a\,u + b\,v.$$
If so, find the scalar coefficients $a$ and $b$, reconstruct $w$ from them, and explain the geometric meaning of the existence of such coefficients.

---

## 2. What We Are Trying to Find
We need to:
1. Formulate the vector equation $w = a\,u + b\,v$ as a $2 \times 2$ system of linear equations in unknowns $a$ and $b$.
2. Solve the linear system to find the exact values of $a$ and $b$.
3. Substitute $a$ and $b$ back into the linear combination to reconstruct $w$ and verify consistency.
4. Explain geometrically why any vector in $\mathbb{R}^2$ can be represented as a linear combination of two non-parallel vectors (basis property of $\mathbb{R}^2$).

---

## 3. Key Concepts and Theorems
1. **Linear Combination in $\mathbb{R}^2$:**
   A vector $w$ is a linear combination of $u$ and $v$ if there exist scalars $a, b \in \mathbb{R}$ such that:
   $$a \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} + b \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} w_1 \\ w_2 \end{pmatrix}.$$
2. **Basis of a Vector Space:**
   In a 2-dimensional space $\mathbb{R}^2$, any two non-zero vectors that are not parallel (i.e., linearly independent) span the entire plane and form a basis.
3. **Determinant Criterion for 2D Independence:**
   Two vectors $u = (u_1, u_2)$ and $v = (v_1, v_2)$ form a basis for $\mathbb{R}^2$ if and only if:
   $$\det \begin{pmatrix} u_1 & v_1 \\ u_2 & v_2 \end{pmatrix} = u_1 v_2 - u_2 v_1 \neq 0.$$
   When this determinant is non-zero, every vector $w \in \mathbb{R}^2$ has a unique representation $(a, b)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the System of Linear Equations
Write out the vector equation $w = a\,u + b\,v$ in coordinates:
$$a \begin{pmatrix} 1 \\ 1 \end{pmatrix} + b \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}.$$
This corresponds to the system of two scalar linear equations:
$$\begin{cases}
a + 2b = 5 & \text{(Equation 1)} \\
a - b = 1 & \text{(Equation 2)}
\end{cases}$$

### Step 2: Solve the Linear System
Subtract Equation 2 from Equation 1 to eliminate the variable $a$:
$$(a + 2b) - (a - b) = 5 - 1$$
$$3b = 4 \implies b = \frac{4}{3}.$$
Now substitute $b = \frac{4}{3}$ into Equation 2 to solve for $a$:
$$a = 1 + b = 1 + \frac{4}{3} = \frac{7}{3}.$$
Thus, the unique coefficients are $a = \frac{7}{3}$ and $b = \frac{4}{3}$.

### Step 3: Reconstruct $w$ from $a$ and $b$
Evaluate the linear combination $a\,u + b\,v$ using the found coefficients:
$$a\,u + b\,v = \frac{7}{3} \begin{pmatrix} 1 \\ 1 \end{pmatrix} + \frac{4}{3} \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} \frac{7}{3} \\ \frac{7}{3} \end{pmatrix} + \begin{pmatrix} \frac{8}{3} \\ -\frac{4}{3} \end{pmatrix} = \begin{pmatrix} \frac{7 + 8}{3} \\ \frac{7 - 4}{3} \end{pmatrix} = \begin{pmatrix} \frac{15}{3} \\ \frac{3}{3} \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix} = w.$$
The original vector $w = (5, 1)$ is successfully reconstructed.

### Step 4: Geometric Meaning of the Coefficients
- The vectors $u = (1, 1)$ and $v = (2, -1)$ point in two distinct, non-parallel directions.
- Their determinant is $\det \begin{pmatrix} 1 & 2 \\ 1 & -1 \end{pmatrix} = 1(-1) - 1(2) = -3 \neq 0$, proving they form a complete basis for the 2D plane $\mathbb{R}^2$.
- These two vectors define an oblique (non-orthogonal) coordinate grid across the plane.
- The coefficients $a = \frac{7}{3}$ and $b = \frac{4}{3}$ represent the coordinates of the target point $(5, 1)$ measured along these skewed axes: to reach $w$, we travel $\frac{7}{3}$ units along the vector $u$, and from that point travel $\frac{4}{3}$ units along the direction of vector $v$.

---

## 5. Why Each Step Is Valid
1. **Setting up the system** is valid because vector equality is defined by coordinate-wise equality in both components.
2. **Elimination by subtraction** is valid by elementary row operations, preserving the exact solution set.
3. **The uniqueness of $a$ and $b$** is guaranteed by the invertibility of the $2 \times 2$ coefficient matrix whose determinant is $-3 \neq 0$.

---

## 6. Final Answer in Words
Yes, $w = (5, 1)$ can be written as a linear combination of $u$ and $v$ with coefficients $a = \frac{7}{3}$ and $b = \frac{4}{3}$. Reconstructing $w$ gives $\frac{7}{3}(1, 1) + \frac{4}{3}(2, -1) = (5, 1)$. Geometrically, the existence and uniqueness of these coefficients means that $u$ and $v$ form a basis for $\mathbb{R}^2$, allowing any vector in the plane to be uniquely reached by walking along the directions of $u$ and $v$.

---

## 7. Quick Verification
- **Cramer's Rule Verification:**
  $$D = \begin{vmatrix} 1 & 2 \\ 1 & -1 \end{vmatrix} = -1 - 2 = -3.$$
  $$D_a = \begin{vmatrix} 5 & 2 \\ 1 & -1 \end{vmatrix} = -5 - 2 = -7 \implies a = \frac{D_a}{D} = \frac{-7}{-3} = \frac{7}{3}.$$
  $$D_b = \begin{vmatrix} 1 & 5 \\ 1 & 1 \end{vmatrix} = 1 - 5 = -4 \implies b = \frac{D_b}{D} = \frac{-4}{-3} = \frac{4}{3}.$$
  Cramer's Rule produces the exact same coefficients, confirming the calculation.

---

## 8. Common Mistakes to Avoid
- **Fraction arithmetic errors:** Adding $\frac{7}{3} + \frac{8}{3}$ incorrectly or failing to simplify $\frac{15}{3} = 5$.
- **Sign slips during elimination:** Writing $(2b) - (-b) = b$ instead of $3b$.
- **Thinking vectors in $\mathbb{R}^2$ must be perpendicular to span:** Forgetting that any two non-parallel vectors span $\mathbb{R}^2$, whether they are orthogonal or not.

---

## 9. Classroom Presentation (3-Sentence Summary)
Setting $w = au + bv$ produces a simple two-by-two linear system for the horizontal and vertical coordinates: $a + 2b = 5$ and $a - b = 1$. Solving by elimination yields the unique fractional coefficients $a = 7/3$ and $b = 4/3$, which perfectly reconstruct $(5, 1)$. Geometrically, because $u$ and $v$ point in different directions, they span the entire plane and serve as an oblique coordinate system where $a$ and $b$ represent the coordinates of $w$.

