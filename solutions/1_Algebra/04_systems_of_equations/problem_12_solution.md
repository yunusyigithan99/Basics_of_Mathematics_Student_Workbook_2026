# Exercise 12: Homogeneous System

## 1. Original Problem
Solve:
$$\begin{cases} x + 2y - z = 0 \\ 2x + 4y - 2z = 0 \\ x - y + 2z = 0 \end{cases}$$
Give all solutions in parametric form and explain why $(0, 0, 0)$ always satisfies a homogeneous system.

---

## 2. What We Are Trying to Find
We need to:
- Solve the given system of 3 linear equations in 3 variables with zero right-hand side (a homogeneous system).
- Use Gaussian elimination to identify pivot and free variables.
- Write down the complete solution set in clean vector parametric form.
- Provide a rigorous mathematical explanation for why the zero vector $\mathbf{x} = (0, 0, 0)$ is guaranteed to be a solution for every homogeneous linear system.

---

## 3. Key Concepts and Theorems
1. **Homogeneous Linear System:**
   A linear system is called **homogeneous** if its constant vector is the zero vector:
   $$A\mathbf{x} = \mathbf{0}$$
2. **The Trivial Solution:**
   Every homogeneous linear system is **always consistent**, because setting all variables to zero yields:
   $$A \cdot \mathbf{0} = \mathbf{0}$$
   The solution $\mathbf{x} = \mathbf{0}$ is called the **trivial solution**.
3. **Non-Trivial Solutions:**
   A homogeneous system has non-trivial (non-zero) solutions if and only if:
   $$\operatorname{rank}(A) < n \iff \det A = 0 \iff \text{at least one free variable exists}$$
   The solution set forms a linear subspace of $\mathbb{R}^n$ called the **nullspace (kernel)** of matrix $A$: $\operatorname{Null}(A)$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Set Up the Augmented Matrix
Write down the augmented matrix $[A \mid \mathbf{0}]$:
$$M_0 = \left(\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 2 & 4 & -2 & 0 \\ 1 & -1 & 2 & 0 \end{array}\right)$$

*(Note: In homogeneous systems, the zero column on the right never changes under any row operations, but we track it for completeness).*

---

### Step 2: Forward Elimination
1. **Eliminate Row 2 ($R_2 \leftarrow R_2 - 2R_1$):**
   $$(2, 4, -2 \mid 0) - 2(1, 2, -1 \mid 0) = (2 - 2, 4 - 4, -2 - (-2) \mid 0) = (0, 0, 0 \mid 0)$$
   *Inspection:* Row 2 reduces completely to zeros because Equation 2 was an exact duplicate ($2 \times$ Eq 1).

2. **Eliminate Row 3 ($R_3 \leftarrow R_3 - R_1$):**
   $$(1, -1, 2 \mid 0) - (1, 2, -1 \mid 0) = (1 - 1, -1 - 2, 2 - (-1) \mid 0) = (0, -3, 3 \mid 0)$$

The matrix becomes:
$$M_1 = \left(\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & -3 & 3 & 0 \end{array}\right)$$

---

### Step 3: Rearrange into Row Echelon Form
Swap Row 2 and Row 3 ($R_2 \leftrightarrow R_3$) to push the zero row to the bottom:
$$M_2 = \left(\begin{array}{ccc|c} \mathbf{1} & 2 & -1 & 0 \\ 0 & \mathbf{-3} & 3 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

Divide Row 2 by $-3$ ($R_2 \leftarrow -\frac{1}{3}R_2$):
$$M_3 = \left(\begin{array}{ccc|c} \mathbf{1} & 2 & -1 & 0 \\ 0 & \mathbf{1} & -1 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

---

### Step 4: Identify Pivots and Free Variables
- **Pivots:**
  - Row 1 pivot is in Column 1 $\implies x$ is a pivot variable.
  - Row 2 pivot is in Column 2 $\implies y$ is a pivot variable.
- **Free Variable:**
  - Column 3 contains no pivot $\implies \mathbf{z}$ **is a free variable**.
  Assign $z = t$, where $t \in \mathbb{R}$.

---

### Step 5: Express Basic Variables in Terms of Parameter $t$
1. **From Row 2:**
   $$y - z = 0 \implies y = z \implies y = t$$
2. **From Row 1 (back-substitution):**
   $$x + 2y - z = 0$$
   Substitute $y = t$ and $z = t$:
   $$x + 2(t) - t = 0 \implies x + t = 0 \implies x = -t$$

---

### Step 6: Write the Parametric Solution
Collecting the variables:
$$\begin{cases} x = -t \\ y = t \\ z = t \end{cases} \qquad (t \in \mathbb{R})$$

In vector parametric form:
$$\begin{pmatrix} x \\ y \\ z \end{pmatrix} = t \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}, \qquad t \in \mathbb{R}$$
The solution set is a 1-dimensional subspace (a straight line through the origin in $\mathbb{R}^3$) spanned by the vector $(-1, 1, 1)$.

---

### Step 7: Explain Why $(0, 0, 0)$ Always Satisfies Any Homogeneous System
A general linear equation has the form:
$$a_1 x_1 + a_2 x_2 + \dots + a_n x_n = b$$
In a **homogeneous** system, the constant on the right-hand side is zero ($b = 0$):
$$a_1 x_1 + a_2 x_2 + \dots + a_n x_n = 0$$
When we evaluate the left-hand side at the point $(x_1, x_2, \dots, x_n) = (0, 0, \dots, 0)$:
$$a_1(0) + a_2(0) + \dots + a_n(0) = 0 + 0 + \dots + 0 = 0$$
Because multiplying any real number by zero always yields zero, the sum on the left-hand side is identically zero, which matches the right-hand side ($0 = 0$) for every single equation in the system.
In matrix notation:
$$A \mathbf{0} = \mathbf{0}$$
for any matrix $A$, because the zero vector is the identity element under vector addition. Therefore, the trivial solution $(0, 0, \dots, 0)$ is mathematically guaranteed to exist for all homogeneous systems.

Notice that in our parametric solution $\mathbf{x} = t(-1, 1, 1)^T$, choosing $t = 0$ immediately yields the trivial solution $(0, 0, 0)$.

---

## 5. Why Each Step Is Valid
- **Subspace Axiom for Homogeneous Systems:** The solution set $\operatorname{Null}(A) = \{\mathbf{x} \in \mathbb{R}^n \mid A\mathbf{x} = \mathbf{0}\}$ is closed under vector addition and scalar multiplication, meaning it is a vector subspace that must contain the origin $\mathbf{0}$.
- **Row Invariance:** Multiplying rows or subtracting rows never alters the zero column in the augmented block because $c \cdot 0 - d \cdot 0 = 0$.

---

## 6. Final Answer in Words
The homogeneous system has infinitely many solutions. In parametric vector form, the complete solution set is $\begin{pmatrix} x \\ y \\ z \end{pmatrix} = t \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$ for all $t \in \mathbb{R}$. The zero vector $(0, 0, 0)$ always satisfies every homogeneous system because substituting zero for every variable makes every term on the left side evaluate to zero, trivially matching the right side $0 = 0$.

---

## 7. Quick Verification
- **Substitute parametric vector into Equation 1:**
  $$(-t) + 2(t) - (t) = -t + 2t - t = 0 \quad \checkmark$$
- **Substitute into Equation 2:**
  $$2(-t) + 4(t) - 2(t) = -2t + 4t - 2t = 0 \quad \checkmark$$
- **Substitute into Equation 3:**
  $$(-t) - (t) + 2(t) = -2t + 2t = 0 \quad \checkmark$$
The equations hold identically for all $t \in \mathbb{R}$.

---

## 8. Common Mistakes to Avoid
- **Claiming the Only Solution is $(0, 0, 0)$:** Failing to recognize that the row of zeros produces a free variable $z = t$, resulting in non-trivial solutions.
- **Thinking a Homogeneous System Can Be Inconsistent:** A homogeneous system can NEVER be inconsistent. It always has at least the trivial solution $(0, 0, 0)$.
- **Sign Error in Back-Substitution:** Writing $x + t = 0 \implies x = t$ instead of $x = -t$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"Elimination reveals a row of zeros and leaves us with rank 2, making $z = t$ a free variable with $y = t$ and $x = -t$, which gives the parametric line of solutions $t\begin{pmatrix}-1\\1\\1\end{pmatrix}$. The point $(0, 0, 0)$ is always guaranteed to satisfy any homogeneous system because multiplying every coefficient by zero identically equals zero, matching the right-hand side. When $t = 0$ in our parametric formula, we recover this exact trivial zero solution."

