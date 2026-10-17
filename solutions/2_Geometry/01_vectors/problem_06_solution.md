# Problem 6 Solution: Projection and Perpendicular Component

## 1. Original Problem
Find the orthogonal vector projection of
$$u = (4, 2)$$
onto the direction of
$$v = (1, 1).$$
Then compute the residual (perpendicular component) vector
$$r = u - \operatorname{proj}_v u$$
and verify that $r \cdot v = 0$. Explain this result geometrically.

---

## 2. What We Are Trying to Find
We need to:
1. Calculate the scalar factor $\frac{u \cdot v}{\|v\|^2}$ determining how far along $v$ the shadow of $u$ falls.
2. Find the vector projection $\operatorname{proj}_v u$.
3. Compute the residual vector $r = u - \operatorname{proj}_v u$.
4. Verify by scalar multiplication that $r \cdot v = 0$.
5. Give the geometric interpretation of orthogonal decomposition into parallel and perpendicular components.

---

## 3. Key Concepts and Theorems
1. **Orthogonal Projection of a Vector:**
   The projection of vector $u$ onto the non-zero vector $v$ is the vector along the line spanned by $v$ obtained by dropping a perpendicular from the tip of $u$:
   $$\operatorname{proj}_v u = \left(\frac{u \cdot v}{v \cdot v}\right) v = \left(\frac{u \cdot v}{\|v\|^2}\right) v.$$
2. **Orthogonal Decomposition:**
   Any vector $u$ can be uniquely written as the sum of two orthogonal components:
   $$u = u_{\parallel} + u_{\perp},$$
   where $u_{\parallel} = \operatorname{proj}_v u$ is parallel to $v$, and $u_{\perp} = r = u - \operatorname{proj}_v u$ is perpendicular to $v$.
3. **Orthogonality of the Residual:**
   By algebraic linearity of the dot product:
   $$r \cdot v = \left(u - \frac{u \cdot v}{v \cdot v} v\right) \cdot v = u \cdot v - \left(\frac{u \cdot v}{v \cdot v}\right)(v \cdot v) = u \cdot v - u \cdot v = 0.$$
   This guarantees that $r$ is always perpendicular to $v$.

---

## 4. Detailed Step-by-Step Solution

### Step 1: Compute the Dot Products $u \cdot v$ and $v \cdot v$
For $u = (4, 2)$ and $v = (1, 1)$:
$$u \cdot v = (4)(1) + (2)(1) = 4 + 2 = 6,$$
$$v \cdot v = \|v\|^2 = 1^2 + 1^2 = 1 + 1 = 2.$$

### Step 2: Compute the Projection Vector $\operatorname{proj}_v u$
Substitute into the projection formula:
$$\operatorname{proj}_v u = \left(\frac{u \cdot v}{v \cdot v}\right) v = \left(\frac{6}{2}\right) (1, 1) = 3 (1, 1) = (3, 3).$$
The parallel component of $u$ along $v$ is $(3, 3)$.

### Step 3: Compute the Residual Vector $r$
Subtract the projection from $u$:
$$r = u - \operatorname{proj}_v u = (4, 2) - (3, 3) = (4 - 3, \; 2 - 3) = (1, -1).$$

### Step 4: Verify That $r \cdot v = 0$
Compute the dot product of $r = (1, -1)$ and $v = (1, 1)$:
$$r \cdot v = (1)(1) + (-1)(1) = 1 - 1 = 0.$$
Because the dot product is exactly zero, $r$ is strictly orthogonal to $v$.

### Step 5: Geometric Interpretation
Geometrically, consider $u$ and $v$ originating from the origin $(0, 0)$:
- The vector $v = (1, 1)$ defines a line $y = x$.
- The projection $\operatorname{proj}_v u = (3, 3)$ is the "orthogonal shadow" cast by $u$ onto the line $y = x$. It represents the point on that line that is closest to the tip of $u = (4, 2)$.
- The residual vector $r = (1, -1)$ connects the tip of the shadow $(3, 3)$ to the tip of the vector $(4, 2)$. By construction, dropping an orthogonal line from $(4, 2)$ to $y = x$ meets the line at right angles ($90^\circ$).
- Therefore, $r$ represents the perpendicular altitude dropped from $u$ onto the direction $v$, confirming why $r \cdot v = 0$.

---

## 5. Why Each Step Is Valid
1. **The projection formula** minimizes the Euclidean distance $\|u - c\,v\|$ over all scalars $c \in \mathbb{R}$, which occurs precisely when the error vector is orthogonal to $v$.
2. **Computing $r = u - \operatorname{proj}_v u$** isolates the complementary perpendicular component because $u = \operatorname{proj}_v u + r$.
3. **The identity $r \cdot v = 0$** follows directly from the linearity of the inner product over real vector spaces.

---

## 6. Final Answer in Words
The projection of $u = (4, 2)$ onto $v = (1, 1)$ is $\operatorname{proj}_v u = (3, 3)$. The perpendicular residual vector is $r = (1, -1)$. The dot product is $r \cdot v = (1)(1) + (-1)(1) = 0$, verifying that $r$ is orthogonal to $v$. Geometrically, this decomposes $u$ into the closest point on the line spanned by $v$ and the perpendicular vector connecting that line to $u$.

---

## 7. Quick Verification
- **Reconstruction:**
  $$\operatorname{proj}_v u + r = (3, 3) + (1, -1) = (3 + 1, 3 - 1) = (4, 2) = u.$$
- **Collinearity of projection with $v$:**
  $$\operatorname{proj}_v u = (3, 3) = 3(1, 1) = 3v,$$
  which is clearly parallel to $v$.
- **Pythagorean Theorem Check:**
  $$\|u\|^2 = 4^2 + 2^2 = 20,$$
  $$\|\operatorname{proj}_v u\|^2 = 3^2 + 3^2 = 18,$$
  $$\|r\|^2 = 1^2 + (-1)^2 = 2.$$
  Since $\|\operatorname{proj}_v u\|^2 + \|r\|^2 = 18 + 2 = 20 = \|u\|^2$, the decomposition forms a right triangle whose hypotenuse is $u$.

---

## 8. Common Mistakes to Avoid
- **Dividing by $\|v\|$ instead of $\|v\|^2$:** The scalar projection (length of projection) has $\|v\|$ in the denominator, but the *vector* projection onto $v$ has $\|v\|^2 = v \cdot v$ in the denominator to balance the magnitude of $v$.
- **Projecting in the wrong direction:** Projecting $v$ onto $u$ instead of $u$ onto $v$.
- **Arithmetic sign in residual:** Calculating $u - \operatorname{proj}_v u = (4 - 3, 2 - 3)$ as $(1, 1)$ instead of $(1, -1)$.

---

## 9. Classroom Presentation (3-Sentence Summary)
To find the projection of $u$ onto $v$, we calculate the scalar ratio $(u \cdot v) / (v \cdot v) = 6/2 = 3$, giving the parallel component $\operatorname{proj}_v u = 3(1, 1) = (3, 3)$. Subtracting this from $u$ yields the residual vector $r = (4, 2) - (3, 3) = (1, -1)$, which represents the perpendicular component. Taking the dot product of $r$ with $v$ gives $1 - 1 = 0$, confirming that dropping an orthogonal shadow decomposes any vector into perfectly perpendicular parts.

