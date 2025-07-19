# Determinants (△)

## Value of Matrix
- Denoted by |A|

## Minor & Co-factor
- **Minor (Mᵢⱼ)**: Remove the i-th row and j-th column, then find the determinant of the remaining matrix.
- **Co-factor (Cᵢⱼ)**: Cᵢⱼ = (-1)ⁱ⁺ʲ Mᵢⱼ  
- **Determinant Expansion**: |A| = a₁₁C₁₁ + a₁₂C₁₂ + ...  

## Properties of Determinants
1. a₃₁C₁₁ + a₃₂C₁₂ + a₃₃C₁₃ = 0  
2. |A| = |Aᵀ|  
3. |I| = 1  
4. |AB| = |A||B|  
5. |Aⁿ| = |A|ⁿ  
6. If |AB| = 0, then |A| = 0 or |B| = 0 (or both).  
7. |kA|ₙ = kⁿ|A|  
8. Scalar multiplication affects only one row/column.  
9. |O|ₙ = 0 (Zero matrix)  
10. |diag(a₁, a₂, a₃)| = a₁ × a₂ × a₃  
11. Swapping two rows/columns changes the sign of △.  
12. If two rows/columns are identical, △ = 0.  
13. If a row/column is all zeros, △ = 0.  
14. **Split Determinant**:  
    $$ \begin{vmatrix} a+x & p & q \\ b+y & r & s \\ c+z & t & u \end{vmatrix} = \begin{vmatrix} a & p & q \\ b & r & s \\ c & t & u \end{vmatrix} + \begin{vmatrix} x & p & q \\ y & r & s \\ z & t & u \end{vmatrix} $$  
15. **Vandermonde-like Determinants**:  
    $$ \begin{vmatrix} 1 & 1 & 1 \\ a & b & c \\ a² & b² & c² \end{vmatrix} = (a-b)(b-c)(c-a) $$  
    (Also holds for transposed and variants with bc, ca, ab).  
16. **Higher-order Vandermonde**:  
    $$ \begin{vmatrix} 1 & 1 & 1 \\ a & b & c \\ a³ & b³ & c³ \end{vmatrix} = (a-b)(b-c)(c-a)(a+b+c) $$  
17. **Cyclic Determinant**:  
    $$ \begin{vmatrix} a & b & c \\ b & c & a \\ c & a & b \end{vmatrix} = 3abc - a³ - b³ - c³ $$  
18. **Skew-Symmetric Matrix**: Determinant of an odd-order skew-symmetric matrix is always 0.

## Multiplication of Two Determinants
- Possible only for same-order determinants.  
  Methods:  
  - Row-to-Row (R→R)  
  - Column-to-Column (C→C)  
  - Row-to-Column (R→C)  
  - Column-to-Row (C→R)  

## Differentiation of Determinants
For △ = |A|:  
$$ \frac{d△}{dx} = \begin{vmatrix} C_1' & C_2 & C_3 \end{vmatrix} + \begin{vmatrix} C_1 & C_2' & C_3 \end{vmatrix} + \begin{vmatrix} C_1 & C_2 & C_3' \end{vmatrix} $$  
(Similarly for rows or integration/summation).

---

# System of Linear Equations
Given:  
$$ a₁x + b₁y + c₁z = d₁ $$  
$$ a₂x + b₂y + c₂z = d₂ $$  
$$ a₃x + b₃y + c₃z = d₃ $$  
Matrix form: **AX = B**, solution: **X = A⁻¹B**.

## 1. Cramer’s Rule
- $$ x = \frac{△₁}{△}, \ y = \frac{△₂}{△}, \ z = \frac{△₃}{△} $$  
  Where:  
  - △ = |A|  
  - △₁ = Replace 1st column of A with B.  
  - △₂ = Replace 2nd column of A with B.  
  - △₃ = Replace 3rd column of A with B.  

### Solution Types:
- **Non-Homogeneous (dᵢ ≠ 0)**:  
  - **Unique**: △ ≠ 0.  
  - **Infinite**: △ = △₁ = △₂ = △₃ = 0.  
  - **No Solution**: △ = 0 but any △ᵢ ≠ 0.  
- **Homogeneous (dᵢ = 0)**:  
  - **Trivial (x=y=z=0)**: △ ≠ 0.  
  - **Non-Trivial**: △ = 0.  

## 2. Rank Method
- **Echelon Form**:  
  - Leading 1 in each row.  
  - Zeroes below leading 1.  
- **Rank(A)**: Number of non-zero rows in echelon form.  
- **Augmented Matrix [A|B]**:  
  - **Unique Solution**: rank(A) = rank([A|B]) = n.  
  - **No Solution**: rank(A) ≠ rank([A|B]).  
  - **Infinite Solutions**: rank(A) = rank([A|B]) < n.  

---

# Adjoint & Inverse Properties
1. **A·adj(A) = |A|Iₙ**  
2. **|adj(A)| = |A|ⁿ⁻¹**  
3. **adj(AB) = adj(B)adj(A)**  
4. **A⁻¹ = adj(A)/|A|** (if |A| ≠ 0)  
5. **Inverse of Diagonal Matrix**: diag(1/a, 1/b, 1/c).  

---

# Matrix Polynomial & Eigenvalues
- **Characteristic Equation**: |A - λI| = 0.  
- **Cayley-Hamilton Theorem**: A matrix satisfies its own characteristic equation.  

---

# Applications
1. **Area of Triangle**:  
   For points (a₁,b₁), (a₂,b₂), (a₃,b₃):  
   $$ \text{Area} = \frac{1}{2} \begin{vmatrix} a₁ & b₁ & 1 \\ a₂ & b₂ & 1 \\ a₃ & b₃ & 1 \end{vmatrix} $$  

2. **Volume of Tetrahedron**:  
   For points (aᵢ,bᵢ,cᵢ), i=1,2,3,4:  
   $$ \text{Volume} = \frac{1}{6} \begin{vmatrix} a₁ & b₁ & c₁ & 1 \\ a₂ & b₂ & c₂ & 1 \\ a₃ & b₃ & c₃ & 1 \\ a₄ & b₄ & c₄ & 1 \end{vmatrix} $$  