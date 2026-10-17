# Exercise 14: A Small Change in the Right-Hand Side

## 1. Original Problem
Compare the systems:
$$\text{System A: } \begin{cases} x + y = 2 \\ 2x - y = 1 \\ 3x = 3 \end{cases} \qquad \text{and} \qquad \text{System B: } \begin{cases} x + y = 2 \\ 2x - y = 1 \\ 3x = 3.1 \end{cases}$$
Check the consistency of each system and explain why a small change in one number can change the type of the system.

---

## 2. What We Are Trying to Find
We need to:
- Test System A for mathematical consistency (determine if solutions exist, and find them if so).
- Test System B for mathematical consistency.
- Compare the two systems, which differ by only a tiny perturbation ($0.1$) in a single constant on the right-hand side.
- Explain geometrically and algebraically why an overdetermined system (more equations than unknowns) is sensitive to changes in the constant vector.

---

## 3. Key Concepts and Theorems
1. **Overdetermined Linear Systems:**
   A linear system with more equations than variables ($m > n$, here $3$ equations and $2$ unknowns) is **overdetermined**.
   - An overdetermined system is typically **inconsistent** (no solution) unless the right-hand side happens to lie precisely within the column space of the coefficient matrix.
2. **Geometric Interpretation in $\mathbb{R}^2$:**
   Each equation represents a straight line.
   - For a system of 3 lines in the plane to have a common solution, all three lines must be **concurrent** (they must intersect at the exact same point).
   - If even one line is shifted by the smallest fraction, concurrency is destroyed: the three lines instead form a triangle, leaving no single point common to all three.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Analyze System A
$$\begin{cases} x + y = 2 & \text{(Equation 1)} \\ 2x - y = 1 & \text{(Equation 2)} \\ 3x = 3 & \text{(Equation 3)} \end{cases}$$

- **Solve Equations 1 and 2 first:**
  Add Equation 1 and Equation 2:
  $$(x + y) + (2x - y) = 2 + 1 \implies 3x = 3 \implies x = 1$$
  Substitute $x = 1$ into Equation 1:
  $$1 + y = 2 \implies y = 1$$
  The unique intersection of the first two lines is the point $(x, y) = (1, 1)$.

- **Test the point in Equation 3:**
  Substitute $x = 1$ into the third equation:
  $$3x = 3(1) = 3$$
  The equation gives $3 = 3$, which is completely satisfied!
  Notice that adding Equation 1 and Equation 2 mathematically generates Equation 3:
  $$\text{Eq}_1 + \text{Eq}_2 = \text{Eq}_3 \iff (x + y) + (2x - y) = 2 + 1 = 3x = 3$$

- **Conclusion for System A:**
  System A is **consistent** and has **exactly one solution**: $(x, y) = (1, 1)$.

---

### Step 2: Analyze System B
$$\begin{cases} x + y = 2 & \text{(Equation 1)} \\ 2x - y = 1 & \text{(Equation 2)} \\ 3x = 3.1 & \text{(Equation 3)} \end{cases}$$

- **Solve Equations 1 and 2 first:**
  As before, Equations 1 and 2 require:
  $$x = 1, \qquad y = 1$$
  This is the only point in the plane where the first two constraints are satisfied simultaneously.

- **Test the point in Equation 3:**
  Substitute $x = 1$ into the third equation:
  $$3x = 3(1) = 3 \neq 3.1$$
  We obtain the impossible contradiction:
  $$3 = 3.1 \quad \text{(False!)}$$

- **Conclusion for System B:**
  There is no point $(x, y)$ that can satisfy all three equations simultaneously.
  System B is **inconsistent** and has **no solution**.

---

### Step 3: Explain Why a Small Change Alters the System Type
1. **Algebraic Explanation:**
   In an overdetermined system ($3 \times 2$), the coefficient matrix $A = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 3 & 0 \end{pmatrix}$ has rank $2$, but it lives in a 3-dimensional target space $\mathbb{R}^3$.
   - The column space of $A$ is a 2-dimensional plane sitting inside $\mathbb{R}^3$.
   - The vector $\mathbf{b}_A = \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix}$ happens to lie **exactly on this 2D plane** because $(1, 1)^T$ maps to $(2, 1, 3)^T$.
   - However, perturbing the third component from $3$ to $3.1$ creates $\mathbf{b}_B = \begin{pmatrix} 2 \\ 1 \\ 3.1 \end{pmatrix}$, which is nudged **off the plane** into the 3rd dimension.
   - Because the target vector no longer lies in the column space, the augmented rank jumps to $3 > \operatorname{rank}(A) = 2$, instantly destroying consistency.

2. **Geometric Explanation in the Plane:**
   - In System A, the three lines $y = -x + 2$, $y = 2x - 1$, and $x = 1$ are **concurrent**: all three pass through the exact same point $(1, 1)$.
   - In System B, changing $3x = 3$ to $3x = 3.1$ shifts the vertical line from $x = 1$ to $x = 1.0333\dots$.
   - This slight shift means the vertical line no longer passes through the intersection of the other two lines. Instead, the three lines cross each other at three distinct points, forming a small triangle. Because there is no single point shared by all three lines, the system has no solution.

---

## 5. Why Each Step Is Valid
- **Rouché-Capelli Theorem:** For System A, $\operatorname{rank}(A) = \operatorname{rank}([A \mid b_A]) = 2$, so a unique solution exists. For System B, $\operatorname{rank}([A \mid b_B]) = 3 > \operatorname{rank}(A) = 2$, which mathematically mandates inconsistency.
- **Affine Linear Subspace Geometry:** Linear combinations are exact; changing a constant by any non-zero $\epsilon \neq 0$ shifts an affine hyperplane, breaking exact concurrency.

---

## 6. Final Answer in Words
System A is consistent with the unique solution $(x, y) = (1, 1)$, while System B is inconsistent and has no solution. A tiny change of $0.1$ in the third equation alters the system type because the system is overdetermined (3 equations for 2 unknowns). In System A, the three lines happen to be concurrent at the exact same point $(1, 1)$; shifting the third line by $0.1$ moves it off that intersection, creating a triangle of non-intersecting lines with no common point.

---

## 7. Quick Verification
- **Augmented matrix reduction for System A:**
  $$\left(\begin{array}{cc|c} 1 & 1 & 2 \\ 2 & -1 & 1 \\ 3 & 0 & 3 \end{array}\right) \xrightarrow{R_2 - 2R_1, \; R_3 - 3R_1} \left(\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & -3 & -3 \\ 0 & -3 & -3 \end{array}\right) \xrightarrow{R_3 - R_2} \left(\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & -3 & -3 \\ 0 & 0 & 0 \end{array}\right)$$
  Zero row $[0 \; 0 \mid 0] \implies$ Consistent! $\checkmark$
- **Augmented matrix reduction for System B:**
  $$\left(\begin{array}{cc|c} 1 & 1 & 2 \\ 2 & -1 & 1 \\ 3 & 0 & 3.1 \end{array}\right) \xrightarrow{R_2 - 2R_1, \; R_3 - 3R_1} \left(\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & -3 & -3 \\ 0 & -3 & -2.9 \end{array}\right) \xrightarrow{R_3 - R_2} \left(\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & -3 & -3 \\ 0 & 0 & 0.1 \end{array}\right)$$
  Row $[0 \; 0 \mid 0.1] \implies 0 = 0.1 \implies$ Inconsistent! $\checkmark$

---

## 8. Common Mistakes to Avoid
- **Assuming Overdetermined Systems Can Never Have Solutions:** Believing 3 equations with 2 unknowns is always inconsistent. As System A shows, if the equations are linearly dependent, a unique solution can exist.
- **Approximate Rounding in Pure Math:** Claiming that $3 \approx 3.1$ so the system is "almost solved". In linear algebra, consistency is strict: $3 \neq 3.1$ means strictly no solution.

---

## 9. Classroom Presentation (3-Sentence Summary)
"In System A, adding the first two equations gives $3x = 3$, meaning the third equation is consistent and the system has the unique solution $(1, 1)$. In System B, changing the right-hand side to $3.1$ creates the contradiction $3 = 3.1$, rendering the system inconsistent with no solution. Geometrically, this small change shifts the third line just enough so that the three lines no longer intersect at a single concurrent point, but instead form a triangle."

