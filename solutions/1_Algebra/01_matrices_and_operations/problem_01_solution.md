# Exercise 1: Matrix Size and Entries

## 1. Problem Statement

Given the matrices:
$$A = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 4 & 5 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ -2 & 3 \\ 4 & 1 \end{pmatrix}$$

1. State the sizes of matrices $A$ and $B$.
2. Read off the entries $a_{12}$, $a_{23}$, $b_{21}$, and $b_{32}$.
3. Write the second row of $A$ and the first column of $B$ as vectors.

---

## 2. Theoretical Background and Concepts

### Matrix Dimensions ($m \times n$)
A matrix is a rectangular grid of numbers organized into rows (horizontal lines) and columns (vertical lines).
- The dimension or size of a matrix is written as $m \times n$ (read as "$m$ by $n$").
- $m$ denotes the **number of rows**.
- $n$ denotes the **number of columns**.
- *Memory aid:* Remember **RC** (Rows first, then Columns).

### Matrix Entry Indexing ($a_{ij}$)
Individual entries inside a matrix are denoted with subscripts, such as $a_{ij}$ or $b_{ij}$:
- The first index ($i$) indicates the **row** number (counted from top to bottom, starting at 1).
- The second index ($j$) indicates the **column** number (counted from left to right, starting at 1).
- Therefore, $a_{ij}$ refers to the entry located at the intersection of row $i$ and column $j$.

### Row Vectors and Column Vectors
- A **row vector** is a matrix consisting of a single row (size $1 \times n$).
- A **column vector** is a matrix consisting of a single column (size $m \times 1$).
- A row from an $m \times n$ matrix contains $n$ elements.
- A column from an $m \times n$ matrix contains $m$ elements.

---

## 3. Detailed Step-by-Step Solution

### Part 1: Determine the Sizes of $A$ and $B$

- **For Matrix $A$:**
  $$A = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 4 & 5 \end{pmatrix}$$
  - Count rows (horizontal lines):
    - Row 1: $\begin{pmatrix} 2 & -1 & 3 \end{pmatrix}$
    - Row 2: $\begin{pmatrix} 0 & 4 & 5 \end{pmatrix}$
    - Total rows: $m = 2$.
  - Count columns (vertical lines):
    - Column 1: $\begin{pmatrix} 2 \\ 0 \end{pmatrix}$
    - Column 2: $\begin{pmatrix} -1 \\ 4 \end{pmatrix}$
    - Column 3: $\begin{pmatrix} 3 \\ 5 \end{pmatrix}$
    - Total columns: $n = 3$.
  
  Therefore, matrix $A$ has size **$2 \times 3$**.

- **For Matrix $B$:**
  $$B = \begin{pmatrix} 1 & 0 \\ -2 & 3 \\ 4 & 1 \end{pmatrix}$$
  - Count rows (horizontal lines):
    - Row 1: $\begin{pmatrix} 1 & 0 \end{pmatrix}$
    - Row 2: $\begin{pmatrix} -2 & 3 \end{pmatrix}$
    - Row 3: $\begin{pmatrix} 4 & 1 \end{pmatrix}$
    - Total rows: $m = 3$.
  - Count columns (vertical lines):
    - Column 1: $\begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}$
    - Column 2: $\begin{pmatrix} 0 \\ 3 \\ 1 \end{pmatrix}$
    - Total columns: $n = 2$.

  Therefore, matrix $B$ has size **$3 \times 2$**.

---

### Part 2: Read Off the Specified Entries

Using the notation $\text{entry}_{(\text{row}, \text{column})}$:

1. **Entry $a_{12}$:**
   - Matrix $A$, row 1, column 2.
   - Row 1 is $\begin{pmatrix} 2 & -1 & 3 \end{pmatrix}$; the second entry is $-1$.
   - **$a_{12} = -1$**

2. **Entry $a_{23}$:**
   - Matrix $A$, row 2, column 3.
   - Row 2 is $\begin{pmatrix} 0 & 4 & 5 \end{pmatrix}$; the third entry is $5$.
   - **$a_{23} = 5$**

3. **Entry $b_{21}$:**
   - Matrix $B$, row 2, column 1.
   - Row 2 is $\begin{pmatrix} -2 & 3 \end{pmatrix}$; the first entry is $-2$.
   - **$b_{21} = -2$**

4. **Entry $b_{32}$:**
   - Matrix $B$, row 3, column 2.
   - Row 3 is $\begin{pmatrix} 4 & 1 \end{pmatrix}$; the second entry is $1$.
   - **$b_{32} = 1$**

---

### Part 3: Write the Specified Row and Column as Vectors

1. **Second row of $A$:**
   - The second row consists of the entries in row 2: $0, 4, 5$.
   - As a row vector ($1 \times 3$ matrix):
     $$\mathbf{r}_2 = \begin{pmatrix} 0 & 4 & 5 \end{pmatrix}$$
   - *(Note: In standard vector notation, it can also be expressed as $(0, 4, 5)$ or as a transposed column vector $\begin{pmatrix} 0 \\ 4 \\ 5 \end{pmatrix}^T$.)*

2. **First column of $B$:**
   - The first column consists of the entries in column 1: $1, -2, 4$.
   - As a standard column vector ($3 \times 1$ matrix):
     $$\mathbf{c}_1 = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}$$
   - *(Note: In transpose notation, it can also be expressed as $\begin{pmatrix} 1 & -2 & 4 \end{pmatrix}^T$.)*

---

## 4. Summary of Results

| Question | Target | Value / Representation |
| :--- | :--- | :--- |
| **Sizes** | Size of $A$ | $2 \times 3$ |
| | Size of $B$ | $3 \times 2$ |
| **Entries** | $a_{12}$ | $-1$ |
| | $a_{23}$ | $5$ |
| | $b_{21}$ | $-2$ |
| | $b_{32}$ | $1$ |
| **Vectors** | Row 2 of $A$ | $\mathbf{r}_2 = \begin{pmatrix} 0 & 4 & 5 \end{pmatrix}$ |
| | Column 1 of $B$ | $\mathbf{c}_1 = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}$ |

---

## 5. Verification and Consistency Checks

1. **Total Element Count:**
   - For $A$: $2 \text{ rows} \times 3 \text{ columns} = 6 \text{ entries}$. Counting the elements in $A$: $\{2, -1, 3, 0, 4, 5\}$ (6 elements total). Consistent.
   - For $B$: $3 \text{ rows} \times 2 \text{ columns} = 6 \text{ entries}$. Counting the elements in $B$: $\{1, 0, -2, 3, 4, 1\}$ (6 elements total). Consistent.

2. **Index Boundaries:**
   - In $A$ ($2 \times 3$), valid indices must satisfy $1 \le i \le 2$ and $1 \le j \le 3$.
     - $a_{12}$: $i = 1 \le 2$, $j = 2 \le 3$. (Valid)
     - $a_{23}$: $i = 2 \le 2$, $j = 3 \le 3$. (Valid)
   - In $B$ ($3 \times 2$), valid indices must satisfy $1 \le i \le 3$ and $1 \le j \le 2$.
     - $b_{21}$: $i = 2 \le 3$, $j = 1 \le 2$. (Valid)
     - $b_{32}$: $i = 3 \le 3$, $j = 2 \le 2$. (Valid)

3. **Vector Length and Dimension Compatibility:**
   - The second row of $A$ has 3 components, matching the column dimension of $A$ ($n = 3$).
   - The first column of $B$ has 3 components, matching the row dimension of $B$ ($m = 3$).
# Exercise 1: Matrix Size and Entries

## 1. Problem Statement

Given the matrices:
$$A = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 4 & 5 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ -2 & 3 \\ 4 & 1 \end{pmatrix}$$

1. State the sizes of matrices $A$ and $B$.
2. Read off the entries $a_{12}$, $a_{23}$, $b_{21}$, and $b_{32}$.
3. Write the second row of $A$ and the first column of $B$ as vectors.

---

## 2. Theoretical Background and Concepts

### Matrix Dimensions ($m \times n$)
A matrix is a rectangular grid of numbers organized into rows (horizontal lines) and columns (vertical lines).
- The dimension or size of a matrix is written as $m \times n$ (read as "$m$ by $n$").
- $m$ denotes the **number of rows**.
- $n$ denotes the **number of columns**.
- *Memory aid:* Remember **RC** (Rows first, then Columns).

### Matrix Entry Indexing ($a_{ij}$)
Individual entries inside a matrix are denoted with subscripts, such as $a_{ij}$ or $b_{ij}$:
- The first index ($i$) indicates the **row** number (counted from top to bottom, starting at 1).
- The second index ($j$) indicates the **column** number (counted from left to right, starting at 1).
- Therefore, $a_{ij}$ refers to the entry located at the intersection of row $i$ and column $j$.

### Row Vectors and Column Vectors
- A **row vector** is a matrix consisting of a single row (size $1 \times n$).
- A **column vector** is a matrix consisting of a single column (size $m \times 1$).
- A row from an $m \times n$ matrix contains $n$ elements.
- A column from an $m \times n$ matrix contains $m$ elements.

---

## 3. Detailed Step-by-Step Solution

### Part 1: Determine the Sizes of $A$ and $B$

- **For Matrix $A$:**
  $$A = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 4 & 5 \end{pmatrix}$$
  - Count rows (horizontal lines):
    - Row 1: $\begin{pmatrix} 2 & -1 & 3 \end{pmatrix}$
    - Row 2: $\begin{pmatrix} 0 & 4 & 5 \end{pmatrix}$
    - Total rows: $m = 2$.
  - Count columns (vertical lines):
    - Column 1: $\begin{pmatrix} 2 \\ 0 \end{pmatrix}$
    - Column 2: $\begin{pmatrix} -1 \\ 4 \end{pmatrix}$
    - Column 3: $\begin{pmatrix} 3 \\ 5 \end{pmatrix}$
    - Total columns: $n = 3$.
  
  Therefore, matrix $A$ has size **$2 \times 3$**.

- **For Matrix $B$:**
  $$B = \begin{pmatrix} 1 & 0 \\ -2 & 3 \\ 4 & 1 \end{pmatrix}$$
  - Count rows (horizontal lines):
    - Row 1: $\begin{pmatrix} 1 & 0 \end{pmatrix}$
    - Row 2: $\begin{pmatrix} -2 & 3 \end{pmatrix}$
    - Row 3: $\begin{pmatrix} 4 & 1 \end{pmatrix}$
    - Total rows: $m = 3$.
  - Count columns (vertical lines):
    - Column 1: $\begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}$
    - Column 2: $\begin{pmatrix} 0 \\ 3 \\ 1 \end{pmatrix}$
    - Total columns: $n = 2$.

  Therefore, matrix $B$ has size **$3 \times 2$**.

---

### Part 2: Read Off the Specified Entries

Using the notation $\text{entry}_{(\text{row}, \text{column})}$:

1. **Entry $a_{12}$:**
   - Matrix $A$, row 1, column 2.
   - Row 1 is $\begin{pmatrix} 2 & -1 & 3 \end{pmatrix}$; the second entry is $-1$.
   - **$a_{12} = -1$**

2. **Entry $a_{23}$:**
   - Matrix $A$, row 2, column 3.
   - Row 2 is $\begin{pmatrix} 0 & 4 & 5 \end{pmatrix}$; the third entry is $5$.
   - **$a_{23} = 5$**

3. **Entry $b_{21}$:**
   - Matrix $B$, row 2, column 1.
   - Row 2 is $\begin{pmatrix} -2 & 3 \end{pmatrix}$; the first entry is $-2$.
   - **$b_{21} = -2$**

4. **Entry $b_{32}$:**
   - Matrix $B$, row 3, column 2.
   - Row 3 is $\begin{pmatrix} 4 & 1 \end{pmatrix}$; the second entry is $1$.
   - **$b_{32} = 1$**

---

### Part 3: Write the Specified Row and Column as Vectors

1. **Second row of $A$:**
   - The second row consists of the entries in row 2: $0, 4, 5$.
   - As a row vector ($1 \times 3$ matrix):
     $$\mathbf{r}_2 = \begin{pmatrix} 0 & 4 & 5 \end{pmatrix}$$
   - *(Note: In standard vector notation, it can also be expressed as $(0, 4, 5)$ or as a transposed column vector $\begin{pmatrix} 0 \\ 4 \\ 5 \end{pmatrix}^T$.)*

2. **First column of $B$:**
   - The first column consists of the entries in column 1: $1, -2, 4$.
   - As a standard column vector ($3 \times 1$ matrix):
     $$\mathbf{c}_1 = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}$$
   - *(Note: In transpose notation, it can also be expressed as $\begin{pmatrix} 1 & -2 & 4 \end{pmatrix}^T$.)*

---

## 4. Summary of Results

| Question | Target | Value / Representation |
| :--- | :--- | :--- |
| **Sizes** | Size of $A$ | $2 \times 3$ |
| | Size of $B$ | $3 \times 2$ |
| **Entries** | $a_{12}$ | $-1$ |
| | $a_{23}$ | $5$ |
| | $b_{21}$ | $-2$ |
| | $b_{32}$ | $1$ |
| **Vectors** | Row 2 of $A$ | $\mathbf{r}_2 = \begin{pmatrix} 0 & 4 & 5 \end{pmatrix}$ |
| | Column 1 of $B$ | $\mathbf{c}_1 = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}$ |

---

## 5. Verification and Consistency Checks

1. **Total Element Count:**
   - For $A$: $2 \text{ rows} \times 3 \text{ columns} = 6 \text{ entries}$. Counting the elements in $A$: $\{2, -1, 3, 0, 4, 5\}$ (6 elements total). Consistent.
   - For $B$: $3 \text{ rows} \times 2 \text{ columns} = 6 \text{ entries}$. Counting the elements in $B$: $\{1, 0, -2, 3, 4, 1\}$ (6 elements total). Consistent.

2. **Index Boundaries:**
   - In $A$ ($2 \times 3$), valid indices must satisfy $1 \le i \le 2$ and $1 \le j \le 3$.
     - $a_{12}$: $i = 1 \le 2$, $j = 2 \le 3$. (Valid)
     - $a_{23}$: $i = 2 \le 2$, $j = 3 \le 3$. (Valid)
   - In $B$ ($3 \times 2$), valid indices must satisfy $1 \le i \le 3$ and $1 \le j \le 2$.
     - $b_{21}$: $i = 2 \le 3$, $j = 1 \le 2$. (Valid)
     - $b_{32}$: $i = 3 \le 3$, $j = 2 \le 2$. (Valid)

3. **Vector Length and Dimension Compatibility:**
   - The second row of $A$ has 3 components, matching the column dimension of $A$ ($n = 3$).
   - The first column of $B$ has 3 components, matching the row dimension of $B$ ($m = 3$).