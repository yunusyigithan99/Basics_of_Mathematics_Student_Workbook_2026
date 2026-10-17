# Exercise 13: A Recurrence Written in Matrix Form

## 1. Original Problem
Let:
$$F = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$
Compute $F^2$, $F^3$, $F^4$, and $F^5$. Compare the numbers obtained with the sequence:
$$0, 1, 1, 2, 3, 5, 8, \dots$$
and describe the relationship you observe. Then compute:
$$F \begin{pmatrix} a \\ b \end{pmatrix}$$
and explain how this multiplication performs one recurrence step: it creates the sum of two consecutive terms and keeps one of them for the next step.

---

## 2. What We Are Trying to Find
We need to:
- Compute the matrix powers $F^2$, $F^3$, $F^4$, and $F^5$ by repeated matrix multiplication.
- Identify how the numbers inside these power matrices relate to the famous Fibonacci sequence ($0, 1, 1, 2, 3, 5, 8, \dots$).
- Multiply $F$ by an arbitrary 2-component vector $\begin{pmatrix} a \\ b \end{pmatrix}$.
- Explain the mechanism by which matrix multiplication executes a recurrence relation: updating the state by adding two terms while simultaneously carrying over one term as memory.

---

## 3. Key Concepts and Theorems
1. **The Fibonacci Sequence:**
   The Fibonacci sequence is defined by the initial conditions and recurrence:
   $$F_0 = 0, \quad F_1 = 1, \quad F_{n+1} = F_n + F_{n-1} \quad (n \ge 1)$$
   The sequence values are:
   $$F_0=0, \; F_1=1, \; F_2=1, \; F_3=2, \; F_4=3, \; F_5=5, \; F_6=8, \dots$$
2. **State-Space Representation of Recurrences:**
   A second-order linear recurrence $x_{k+1} = x_k + x_{k-1}$ requires two values of history to compute the next term. By defining a state vector $\mathbf{v}_k = \begin{pmatrix} x_k \\ x_{k-1} \end{pmatrix}$, the recurrence can be written as a first-order matrix system:
   $$\mathbf{v}_{k+1} = F \mathbf{v}_k$$
3. **Fibonacci Matrix Theorem:**
   For any integer $n \ge 1$:
   $$F^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}$$

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Successive Powers of $F$
Given $F^1 = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$:

- **Compute $F^2 = F \cdot F$:**
  $$F^2 = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1(1) + 1(1) & 1(1) + 1(0) \\ 1(1) + 0(1) & 1(1) + 0(0) \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$$

- **Compute $F^3 = F^2 \cdot F$:**
  $$F^3 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(1) & 2(1) + 1(0) \\ 1(1) + 1(1) & 1(1) + 1(0) \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix}$$

- **Compute $F^4 = F^3 \cdot F$:**
  $$F^4 = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 3(1) + 2(1) & 3(1) + 2(0) \\ 2(1) + 1(1) & 2(1) + 1(0) \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}$$

- **Compute $F^5 = F^4 \cdot F$:**
  $$F^5 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 5(1) + 3(1) & 5(1) + 3(0) \\ 3(1) + 2(1) & 3(1) + 2(0) \end{pmatrix} = \begin{pmatrix} 8 & 5 \\ 5 & 3 \end{pmatrix}$$

---

### Step 2: Compare with the Fibonacci Numbers
List the Fibonacci sequence:
$$F_0 = 0, \quad F_1 = 1, \quad F_2 = 1, \quad F_3 = 2, \quad F_4 = 3, \quad F_5 = 5, \quad F_6 = 8$$

Compare these with the entries of the power matrices:
- $F^1 = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} F_2 & F_1 \\ F_1 & F_0 \end{pmatrix}$
- $F^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} F_3 & F_2 \\ F_2 & F_1 \end{pmatrix}$
- $F^3 = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} F_4 & F_3 \\ F_3 & F_2 \end{pmatrix}$
- $F^4 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix} = \begin{pmatrix} F_5 & F_4 \\ F_4 & F_3 \end{pmatrix}$
- $F^5 = \begin{pmatrix} 8 & 5 \\ 5 & 3 \end{pmatrix} = \begin{pmatrix} F_6 & F_5 \\ F_5 & F_4 \end{pmatrix}$

**Relationship Observed:**
Every entry in $F^n$ is a Fibonacci number. Specifically:
$$F^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}$$

---

### Step 3: Compute $F \begin{pmatrix} a \\ b \end{pmatrix}$
Multiply matrix $F$ by the vector $\begin{pmatrix} a \\ b \end{pmatrix}$:
$$F \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} 1 \cdot a + 1 \cdot b \\ 1 \cdot a + 0 \cdot b \end{pmatrix} = \begin{pmatrix} a + b \\ a \end{pmatrix}$$

---

### Step 4: Explanation of the Recurrence Step
Let $a$ represent the current term of a recurrence (say $x_k$) and $b$ represent the previous term ($x_{k-1}$):
$$\begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} x_k \\ x_{k-1} \end{pmatrix}$$
Multiplying by $F$ yields:
$$F \begin{pmatrix} x_k \\ x_{k-1} \end{pmatrix} = \begin{pmatrix} x_k + x_{k-1} \\ x_k \end{pmatrix} = \begin{pmatrix} x_{k+1} \\ x_k \end{pmatrix}$$
This reveals the dual role of matrix $F$:
1. **The top row $(1, 1)$:** Computes the new term $x_{k+1} = x_k + x_{k-1}$ by summing the two inputs.
2. **The bottom row $(1, 0)$:** Acts as a memory register by shifting the current term $x_k$ down into the "previous term" slot while discarding the obsolete $x_{k-1}$.
Thus, a single matrix multiplication steps the entire recurrence forward by one time step.

---

## 5. Why Each Step Is Valid
- **Matrix Multiplication Distributivity:** The top row operation $1 \cdot a + 1 \cdot b$ directly encodes the linear recurrence relation defining Fibonacci numbers.
- **Cascading Powers:** By associativity, $F^n \begin{pmatrix} F_1 \\ F_0 \end{pmatrix} = F(F(\dots(F\mathbf{v}_0))) = \begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix}$. Applying the matrix $n$ times advances the sequence by $n$ steps.

---

## 6. Final Answer in Words
The powers of $F$ are $F^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, $F^3 = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix}$, $F^4 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}$, and $F^5 = \begin{pmatrix} 8 & 5 \\ 5 & 3 \end{pmatrix}$. The entries correspond exactly to the Fibonacci sequence, where $F^n$ contains $F_{n+1}$ in the top-left, $F_n$ on the off-diagonals, and $F_{n-1}$ in the bottom-right. The matrix-vector product $F\begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} a+b \\ a \end{pmatrix}$ executes one step of the recurrence by calculating the sum of the two terms in the first row and shifting the primary term into the memory position in the second row.

---

## 7. Quick Verification
- **Determinant verification (Cassini's Identity):**
  - $\det(F) = 1(0) - 1(1) = -1$
  - Using the determinant power property $\det(F^n) = (\det F)^n = (-1)^n$:
    - For $n=2$: $\det(F^2) = 2(1) - 1(1) = 1 = (-1)^2 \quad \checkmark$
    - For $n=3$: $\det(F^3) = 3(1) - 2(2) = -1 = (-1)^3 \quad \checkmark$
    - For $n=4$: $\det(F^4) = 5(2) - 3(3) = 1 = (-1)^4 \quad \checkmark$
    - For $n=5$: $\det(F^5) = 8(3) - 5(5) = -1 = (-1)^5 \quad \checkmark$
  This verifies Cassini's famous identity: $F_{n+1}F_{n-1} - F_n^2 = (-1)^n$.
- **Vector step test with base values $(F_1, F_0) = (1, 0)$:**
  $$F \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1+0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} F_2 \\ F_1 \end{pmatrix} \quad \checkmark$$

---

## 8. Common Mistakes to Avoid
- **Offsetting Fibonacci Indices:** Forgetting that $F_0 = 0$, which causes mislabeling the entries (e.g., calling $F_1$ the first entry instead of $F_2$).
- **Miscalculating Off-Diagonal Entries in $F^2$:** Adding entries incorrectly when multiplying $1 \cdot 1 + 1 \cdot 0$.
- **Viewing Matrix Powers as Mere Arithmetic:** Overlooking the profound structural insight that raising a companion matrix to power $n$ computes the $n$-th step of a recurrence in logarithmic time ($O(\log n)$ via binary exponentiation).

---

## 9. Classroom Presentation (3-Sentence Summary)
"Raising the matrix $F = \begin{pmatrix}1&1\\1&0\end{pmatrix}$ to successive powers produces matrices whose entries are consecutive Fibonacci numbers, yielding $F^n = \begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}$. When we multiply $F$ by a vector $\begin{pmatrix}a\\b\end{pmatrix}$, we get $\begin{pmatrix}a+b\\a\end{pmatrix}$, showing how the top row generates the next Fibonacci number by addition while the bottom row preserves the current number as history. This proves that linear algebra can encode and solve recursive sequences through matrix multiplication."

