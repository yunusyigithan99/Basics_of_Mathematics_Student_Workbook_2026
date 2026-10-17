# Problem 11 Solution: Decomposition into Parallel and Perpendicular Components

## 1. Original Problem
Decompose the 2D vector
$$u = (3, 4)$$
into two component vectors: one parallel to $v = (1, 2)$, denoted $u_{\parallel}$, and one perpendicular to $v$, denoted $u_{\perp}$.
Check that:
$$u = u_{\parallel} + u_{\perp} \quad \text{and} \quad u_{\perp} \cdot v = 0.$$
Explain why these are two logically independent checks of correctness.

---

## 2. What We Are Trying to Find
We need to:
1. Compute the parallel component $u_{\parallel} = \operatorname{proj}_v u$ using the projection formula.
2. Compute the perpendicular component $u_{\perp} = u - u_{\parallel}$.
3. Verify that the sum of the two components reconstructs $u$ exactly.
4. Verify that the dot product $u_{\perp} \cdot v = 0$.
5. Provide a clear explanation of why both checks are necessary and test different properties of the solution.

---

## 3. Key Concepts and Theorems
1. **Orthogonal Decomposition Theorem:**
   Given a non-zero vector $v \in \mathbb{R}^n$, any vector $u \in \mathbb{R}^n$ can be uniquely decomposed as:
   $$u = u_{\parallel} + u_{\perp},$$
   where $u_{\parallel}$ is in the subspace spanned by $v$ ($u_{\parallel} = c\,v$), and $u_{\perp}$ is orthogonal to $v$ ($u_{\perp} \cdot v = 0$).
2. **Formula for Parallel Component (Projection):**
   $$u_{\parallel} = \left(\frac{u \cdot v}{v \cdot v}\right) v.$$
3. **Formula for Perpendicular Component (Residual):**
   $$u_{\perp} = u - u_{\parallel}.$$
4. **Logically Independent Conditions:**
   - Property A (Reconstruction): $u_1 + u_2 = u$.
   - Property B (Directionality): $u_1$ is parallel to $v$, and $u_2$ is orthogonal to $v$.
   Neither property implies the other on its own.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Calculate $u \cdot v$ and $\|v\|^2$
For $u = (3, 4)$ and $v = (1, 2)$:
$$u \cdot v = (3)(1) + (4)(2) = 3 + 8 = 11,$$
$$v \cdot v = \|v\|^2 = 1^2 + 2^2 = 1 + 4 = 5.$$

### Step 2: Determine the Parallel Component $u_{\parallel}$
Apply the projection formula:
$$u_{\parallel} = \left(\frac{u \cdot v}{v \cdot v}\right) v = \frac{11}{5} (1, 2) = \left(\frac{11}{5}, \; \frac{22}{5}\right).$$

### Step 3: Determine the Perpendicular Component $u_{\perp}$
Subtract $u_{\parallel}$ from $u$:
$$u_{\perp} = u - u_{\parallel} = (3, 4) - \left(\frac{11}{5}, \; \frac{22}{5}\right) = \left(\frac{15}{5} - \frac{11}{5}, \; \frac{20}{5} - \frac{22}{5}\right) = \left(\frac{4}{5}, \; -\frac{2}{5}\right).$$

### Step 4: Perform Check 1 ($u = u_{\parallel} + u_{\perp}$)
Add the two calculated components together:
$$u_{\parallel} + u_{\perp} = \left(\frac{11}{5}, \; \frac{22}{5}\right) + \left(\frac{4}{5}, \; -\frac{2}{5}\right) = \left(\frac{11 + 4}{5}, \; \frac{22 - 2}{5}\right) = \left(\frac{15}{5}, \; \frac{20}{5}\right) = (3, 4) = u.$$
The sum reconstructs the original vector $u$ identically.

### Step 5: Perform Check 2 ($u_{\perp} \cdot v = 0$)
Take the dot product of $u_{\perp} = \left(\frac{4}{5}, -\frac{2}{5}\right)$ with $v = (1, 2)$:
$$u_{\perp} \cdot v = \left(\frac{4}{5}\right)(1) + \left(-\frac{2}{5}\right)(2) = \frac{4}{5} - \frac{4}{5} = 0.$$
The perpendicularity condition is confirmed.

### Step 6: Explain Why the Two Checks Are Independent
These two verification steps test fundamentally different aspects of the decomposition:
1. **The sum check ($u_{\parallel} + u_{\perp} = u$) tests completeness:** It confirms that no part of the original vector was lost or miscalculated during coordinate subtraction. However, infinitely many pairs of vectors sum to $u$ (for example, $(1, 0) + (2, 4) = (3, 4)$), none of which are necessarily orthogonal to $v$.
2. **The orthogonality check ($u_{\perp} \cdot v = 0$) tests geometric orientation:** It verifies that $u_{\perp}$ forms a strict $90^\circ$ angle with the reference direction $v$. However, infinitely many vectors are orthogonal to $v$ (any multiple of $(2, -1)$), but very few of them will sum with $u_{\parallel}$ to yield $u$.

Because one check tests **conservation of vector magnitude/components** and the other tests **geometric angle/orthogonality**, neither implies the other. Satisfying both simultaneously proves beyond doubt that the decomposition is correct.

---

## 5. Why Each Step Is Valid
1. **The projection ratio $\frac{11}{5}$** scales $v$ by the exact amount required so that the difference vector is perpendicular to $v$.
2. **Fractional subtraction with common denominators** preserves exact rational precision without rounding errors.
3. **The scalar product evaluation** confirms orthogonality since $\cos(90^\circ) = 0$.

---

## 6. Final Answer in Words
The parallel component of $u$ along $v$ is $u_{\parallel} = \left(\frac{11}{5}, \frac{22}{5}\right)$, and the perpendicular component is $u_{\perp} = \left(\frac{4}{5}, -\frac{2}{5}\right)$. Their sum is $\left(\frac{11}{5} + \frac{4}{5}, \frac{22}{5} - \frac{2}{5}\right) = (3, 4) = u$, and their dot product is $\left(\frac{4}{5}\right)(1) + \left(-\frac{2}{5}\right)(2) = 0$. These two checks are independent because the first ensures the components correctly reconstruct the original vector, while the second verifies that the geometric angle between $u_{\perp}$ and $v$ is strictly $90^\circ$.

---

## 7. Quick Verification
- **Check parallelism of $u_{\parallel}$:**
  $$u_{\parallel} = \left(\frac{11}{5}, \frac{22}{5}\right) = \frac{11}{5}(1, 2) = \frac{11}{5} v.$$
  Since $u_{\parallel}$ is an explicit scalar multiple of $v$, it is strictly parallel to $v$.
- **Pythagorean Length Invariance:**
  $$\|u\|^2 = 3^2 + 4^2 = 25.$$
  $$\|u_{\parallel}\|^2 = \left(\frac{11}{5}\right)^2 + \left(\frac{22}{5}\right)^2 = \frac{121 + 484}{25} = \frac{605}{25} = \frac{121}{5} = 24.2.$$
  $$\|u_{\perp}\|^2 = \left(\frac{4}{5}\right)^2 + \left(-\frac{2}{5}\right)^2 = \frac{16 + 4}{25} = \frac{20}{25} = \frac{4}{5} = 0.8.$$
  $$\|u_{\parallel}\|^2 + \|u_{\perp}\|^2 = 24.2 + 0.8 = 25 = \|u\|^2.$$
  The Pythagorean identity holds perfectly.

---

## 8. Common Mistakes to Avoid
- **Denominator squared error:** Dividing $u \cdot v$ by $\|v\| = \sqrt{5}$ instead of $\|v\|^2 = 5$.
- **Arithmetic sign in $u_{\perp}$:** Calculating $4 - \frac{22}{5} = \frac{20 - 22}{5} = -\frac{2}{5}$, but forgetting the minus sign.
- **Relying only on the sum check:** Simply verifying that $u_{\parallel} + u_{\perp} = u$ without checking whether $u_{\perp}$ is actually perpendicular to $v$.

---

## 9. Classroom Presentation (3-Sentence Summary)
Projecting $u = (3, 4)$ onto $v = (1, 2)$ yields the parallel component $u_{\parallel} = (11/5, 22/5)$, and subtracting this from $u$ gives the perpendicular component $u_{\perp} = (4/5, -2/5)$. We verify correctness by confirming that their sum reconstitutes $(3, 4)$ and that the dot product $u_{\perp} \cdot v$ is zero. These two checks are logically independent because the first confirms conservation of the vector, while the second guarantees that the geometric orientation is strictly perpendicular.

