# Matrices

## Definition
- A matrix **A** of order m×n is denoted as `[aᵢⱼ]ₘₓₙ` where:
  - `i` = row index (1 ≤ i ≤ m)
  - `j` = column index (1 ≤ j ≤ n)
  - `aᵢⱼ` = element at i-th row and j-th column

---

## Types of Matrices

1. **Row Matrix**: Matrix with only 1 row (order 1×n)
   - Example: `[1 2 3]`

2. **Column Matrix**: Matrix with only 1 column (order m×1)
   - Example: `[1; 2; 3]`

3. **Null Matrix (Zero Matrix)**: All elements are 0 (denoted by O)
   - Example: `[0 0; 0 0]`

4. **Square Matrix**: Number of rows = columns (m = n)
   - Example: `[1 2; 3 4]`

5. **Diagonal Matrix**: 
   - Square matrix where non-zero elements only appear on main diagonal
   - `tr(A)` = sum of diagonal elements
   - Example: `diag(1, 2, 3)`

6. **Scalar Matrix**: 
   - Diagonal matrix with identical diagonal elements
   - Example: `[5 0; 0 5]`

7. **Identity Matrix (Iₙ)**: 
   - Scalar matrix with diagonal elements = 1
   - Example: `I₂ = [1 0; 0 1]`

8. **Triangular Matrix**:
   - **Upper Triangular**: All elements below diagonal = 0
   - **Lower Triangular**: All elements above diagonal = 0

9. **Horizontal Matrix**: More columns than rows (m < n)

10. **Vertical Matrix**: More rows than columns (n < m)

11. **Transpose Matrix (Aᵀ)**: Rows and columns interchanged

12. **Orthogonal Matrix**:
    - Satisfies AAᵀ = I
    - Proper: |A| = +1 (pure rotation)
    - Improper: |A| = -1 (rotation + reflection)

13. **Singular Matrix**: Determinant |A| = 0

14. **Non-Singular Matrix**: Determinant |A| ≠ 0

15. **Skew-Symmetric Matrix**: Aᵀ = -A

16. **Symmetric Matrix**: Aᵀ = A

17. **Idempotent Matrix**: A² = A

18. **Involutory Matrix**: A² = I

---

## Matrix Algebra

### 1. Comparable Matrices
- Two matrices A (m×n) and B (k×p) are comparable if m = k and n = p

### 2. Equal Matrices
- A = B if aᵢⱼ = bᵢⱼ for all i,j

### 3. Scalar Multiplication
- kA = [kaᵢⱼ] for scalar k

### 4. Addition/Subtraction
- Defined only for comparable matrices
- **Properties**:
  - Commutative: A + B = B + A
  - Non-commutative subtraction: A - B ≠ B - A
  - Associative: (A + B) + C = A + (B + C)
  - Distributive: k(A ± B) = kA ± kB
  - Commutative scalar: kA = Ak

### 5. Matrix Multiplication
- For A (m×n) and B (n×p), product C = AB is m×p
- Element cᵢⱼ = Σ(aᵢₖbₖⱼ) for k=1 to n

---

## Matrix Properties

1. Non-commutative multiplication: AB ≠ BA in general
2. Distributive over addition:
   - A(B ± C) = AB ± AC
   - (B ± C)A = BA ± CA
3. Binomial expansion: (A + B)² = A² + AB + BA + B²
4. Identity property: AI = IA = A
5. Power of identity: Iⁿ = I
6. Power of matrix: A² = AA
7. Associative multiplication: A(BC) = (AB)C
8. Scalar multiplication: k(AB) = (kA)B = A(kB)
9. Diagonal matrix operations:
   - A ± B = diag(a₁ ± b₁, a₂ ± b₂)
   - AB = diag(a₁b₁, a₂b₂)
   - Aⁿ = diag(a₁ⁿ, a₂ⁿ)
10. Trace properties:
    - tr(λA) = λtr(A)
    - tr(A ± B) = tr(A) ± tr(B)
    - tr(AB) = tr(BA)
11. Null matrix: OA = AO = O
12. Binomial theorem: (I + A)ⁿ = ΣⁿCr Aʳ
13. Transpose properties:
    - (Aᵀ)ᵀ = A
    - (A + B)ᵀ = Aᵀ + Bᵀ
    - (kA)ᵀ = kAᵀ
    - (AB)ᵀ = BᵀAᵀ

---

## Elementary Transformations

1. Row/column interchange: Rᵢ ↔ Rⱼ or Cᵢ ↔ Cⱼ
2. Transpose: A → Aᵀ
3. Row/column addition: Rᵢ → Rᵢ ± Rⱼ or Cᵢ → Cᵢ ± Cⱼ
4. Scalar multiplication: Rᵢ → kRᵢ or Cᵢ → kCᵢ
5. Linear combination: Rᵢ → Rᵢ + kRⱼ or Cᵢ → Cᵢ + kCⱼ