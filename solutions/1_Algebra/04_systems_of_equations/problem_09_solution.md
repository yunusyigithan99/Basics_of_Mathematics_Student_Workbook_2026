# Exercise 9: A System from a Sum Condition

## 1. Original Problem
Find numbers $x, y$ satisfying:
$$x + y = 10, \qquad 2x + 5y = 32$$
Solve the system and explain geometrically why the solution is unique.

---

## 2. What We Are Trying to Find
We need to:
- Find the pair of real numbers $(x, y)$ that simultaneously satisfies both linear constraints.
- Solve the system algebraically using elimination or substitution.
- Convert both linear equations into geometric line equations in the Cartesian plane.
- Explain geometrically why the solution exists and why it is strictly unique.

---

## 3. Key Concepts and Theorems
1. **Linear Equations as Lines in $\mathbb{R}^2$:**
   Every linear equation $ax + by = c$ (with $(a, b) \neq (0, 0)$) defines a straight line in the 2D plane.
2. **Intersection of Two Lines:**
   - If two lines have **different slopes** ($m_1 \neq m_2$), they are not parallel.
   - In Euclidean plane geometry, any two distinct non-parallel straight lines must intersect at **exactly one unique point**.
   - The coordinates of this intersection point $(x_0, y_0)$ represent the unique solution to the system.
3. **Determinant Non-Zero Condition:**
   $$\det A = a_{11}a_{22} - a_{12}a_{21} \neq 0 \iff m_1 \neq m_2 \iff \text{Unique intersection}$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Solve the System Algebraically
Given equations:
$$\begin{cases} x + y = 10 & \text{(Equation 1)} \\ 2x + 5y = 32 & \text{(Equation 2)} \end{cases}$$

- **Eliminate $x$:**
  Multiply Equation 1 by $2$:
  $$2(x + y) = 2(10) \implies 2x + 2y = 20$$
  Subtract this from Equation 2:
  $$(2x + 5y) - (2x + 2y) = 32 - 20$$
  $$3y = 12 \implies y = \frac{12}{3} = 4$$

- **Solve for $x$:**
  Substitute $y = 4$ into Equation 1:
  $$x + 4 = 10 \implies x = 10 - 4 = 6$$

Thus, the algebraic solution is:
$$(x, y) = (6, 4)$$

---

### Step 2: Geometric Representation as Lines
Convert each equation into slope-intercept form ($y = mx + b$):

1. **First Line ($L_1: x + y = 10$):**
   $$y = -x + 10$$
   - Slope $m_1 = -1$
   - $y$-intercept $(0, 10)$
   - $x$-intercept $(10, 0)$

2. **Second Line ($L_2: 2x + 5y = 32$):**
   $$5y = -2x + 32 \implies y = -\frac{2}{5}x + \frac{32}{5} = -0.4x + 6.4$$
   - Slope $m_2 = -\frac{2}{5} = -0.4$
   - $y$-intercept $(0, 6.4)$
   - $x$-intercept $(16, 0)$

---

### Step 3: Explain Geometrically Why the Solution Is Unique
1. **Non-Parallelism of the Lines:**
   Compare the slopes of the two lines:
   $$m_1 = -1, \qquad m_2 = -0.4$$
   Because $-1 \neq -0.4$, the slopes are different ($m_1 \neq m_2$).
2. **Euclidean Axiom of Intersection:**
   In two-dimensional Euclidean geometry, two straight lines in the plane are either:
   - Parallel (same slope), in which case they either never meet or coincide everywhere, OR
   - Non-parallel (different slopes), in which case they must cross each other at **exactly one single point**.
3. **Geometric Conclusion:**
   Because line $L_1$ drops at a $45^\circ$ angle (slope $-1$) while line $L_2$ drops much more gently (slope $-0.4$), the lines cannot be parallel. They converge across the plane until they cross at the coordinates $(6, 4)$. Because two distinct straight lines can never bend back to cross a second time, this intersection point is strictly unique.

---

## 5. Why Each Step Is Valid
- **Linear Combination Invariance:** Multiplying Equation 1 by $2$ and subtracting it from Equation 2 is an affine projection that preserves the common point $(6, 4)$.
- **Uniqueness of Euclidean Intersections:** If two points $P \neq Q$ belonged to both lines, the line through $P$ and $Q$ would be unique, forcing the two lines to be identical, contradicting $m_1 \neq m_2$.

---

## 6. Final Answer in Words
The numbers satisfying the system are $x = 6$ and $y = 4$. Geometrically, each equation represents a straight line in the Cartesian plane: the first has slope $-1$ and the second has slope $-2/5$. Because their slopes are different, the lines are not parallel and must intersect at exactly one single point, $(6, 4)$, which geometrically guarantees that the solution is unique.

---

## 7. Quick Verification
- **Substitute into Equation 1:**
  $$6 + 4 = 10 \quad (10 = 10) \quad \checkmark$$
- **Substitute into Equation 2:**
  $$2(6) + 5(4) = 12 + 20 = 32 \quad (32 = 32) \quad \checkmark$$
- **Determinant verification:**
  $$\det A = \det\begin{pmatrix} 1 & 1 \\ 2 & 5 \end{pmatrix} = 1(5) - 1(2) = 5 - 2 = 3 \neq 0$$
  Since $\det A = 3 \neq 0$, the linear transformation is invertible, algebraically confirming uniqueness. $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Arithmetic Error in Subtraction:** Calculating $32 - 20 = 14$ instead of $12$.
- **Giving Only the Numbers Without Geometric Explanation:** Stating $(6, 4)$ but omitting the explanation regarding line slopes and non-parallel lines.
- **Confusing Normal Vectors with Slopes:** Stating that the normal vectors $(1, 1)$ and $(2, 5)$ are slopes; slopes are $-a/b$.

---

## 9. Classroom Presentation (3-Sentence Summary)
"By eliminating $x$ through subtracting $2(x+y=10)$ from $2x+5y=32$, we find $3y = 12$, which gives $y = 4$ and $x = 6$. Geometrically, the two equations define straight lines with slopes of $-1$ and $-0.4$. Because their slopes are different, the lines are not parallel and must cross at exactly one point in the plane, which proves that the solution $(6, 4)$ is unique."

