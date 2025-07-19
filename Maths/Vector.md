# Vector Algebra & 3D Geometry

## 1. Vector Fundamentals
- **Definition**: Entity with magnitude and direction
- **Representation**: →a = a₁î + a₂ĵ + a₃k̂

### Types of Vectors
1. **Null Vector (Zero Vector)**
   - Magnitude = 0
   - Direction undefined

2. **Unit Vector**
   - â = →a/|→a|
   - |â| = 1

3. **Equal Vectors**
   - Same magnitude
   - Same direction
   - Same physical quantity

4. **Position Vector**
   - Joins origin to point P
   - →r = xî + yĵ + zk̂

5. **Collinear/Parallel Vectors**
   - →a = k→b (k ≠ 0)
   - Directed segments are parallel

6. **Like Vectors** - Same direction  
7. **Unlike Vectors** - Opposite directions

## 2. Vector Operations

### Basic Operations
- **Between two points**: →AB = →B - →A
- **Orthogonal triad**: î, ĵ, k̂ (right-handed system)

### Vector Addition
- **Triangle/Parallelogram Law**
  - |→R|² = |→A|² + |→B|² + 2|→A||→B|cosθ

### Section Formulas
- **Internal Division**: (m→b + n→a)/(m+n)
- **External Division**: (m→b - n→a)/(m-n)
- **Midpoint**: (→a + →b)/2

### Angle Bisector
- →V = â₁ + â₂ (unit vectors)

## 3. Products of Vectors

### Dot Product (Scalar Product)
→a·→b = |→a||→b|cosθ

#### Properties:
1. Angle determination:
   - +ve → Acute angle
   - -ve → Obtuse angle
   - 0 → Perpendicular (90°)

2. →a·→a = |→a|²
3. Algebraic properties:
   - (→a + →b)² = |→a|² + |→b|² + 2→a·→b
   - (→a + →b)·(→a - →b) = |→a|² - |→b|²

### Projection
- **Length**: →a·(→b/|→b|) = |→a|cosθ
- **Vector**: [→a·(→b/|→b|)] × (→b/|→b|)

### Cross Product (Vector Product)
→a × →b = |→a||→b|sinθ n̂

#### Properties:
1. Anti-commutative: →a × →b = -→b × →a
2. Distributive over addition
3. Parallel vectors: →a × →b = 0 if →a∥→b
4. Matrix determinant form:
   $$ \begin{vmatrix} 
   î & ĵ & k̂ \\ 
   a₁ & a₂ & a₃ \\ 
   b₁ & b₂ & b₃ 
   \end{vmatrix} $$

### Geometric Applications
- **Area of parallelogram**: |→a × →b|
- **Area of triangle**: ½|→a × →b|

## 4. Triple Products

### Scalar Triple Product (STP)
[→a →b →c] = (→a × →b)·→c

#### Properties:
1. Cyclic permutation invariant
2. [→a →b →c] = -[→a →c →b]
3. Volume interpretation:
   - Parallelepiped: |[→a →b →c]|
   - Tetrahedron: |[→a →b →c]|/6

### Vector Triple Product
→a × (→b × →c) = (→a·→c)→b - (→a·→b)→c

## 5. Important Theorems

### Coplanarity
- Three vectors are coplanar ⇔ [→a →b →c] = 0
- Any two vectors are always coplanar

### Linear Dependence
- Four or more vectors are always linearly dependent
- Three points collinear ⇔ [→a →b →c] = 0

### Reciprocal System
For non-coplanar vectors →a, →b, →c:
- →a' = (→b × →c)/[→a →b →c]
- →a·→a' = 1, →a'·→b = 0, etc.

## 6. 3D Geometry Essentials
# 3D Geometry Essentials

## 1. Direction Cosines and Ratios

### For vector →v = xî + yĵ + zk̂:

**Direction Cosines (DCs):**
- l = cosα = x/√(x²+y²+z²)
- m = cosβ = y/√(x²+y²+z²)
- n = cosγ = z/√(x²+y²+z²)

**Direction Ratios (DRs):**  
Any scalar multiples of components (x,y,z)

### Key Properties:
1. l² + m² + n² = 1
2. cos²α + cos²β + cos²γ = 1
3. sin²α + sin²β + sin²γ = 2
4. A vector has unique DCs: (l,m,n)
5. A line has two DC sets: (l,m,n) and (-l,-m,-n)
6. DCs → components of unit vector  
   DRs → components of original vector

---

## 2. Equations of Lines

### Required:
- Point on line (→a)
- Parallel vector (→b)

### Forms:
1. **Vector Form**:  
   →r = →a + λ→b

2. **Cartesian Form**:  
   (x-x₁)/a = (y-y₁)/b = (z-z₁)/c = λ

3. **Symmetric Form**:  
   x = x₁ + λa  
   y = y₁ + λb  
   z = z₁ + λc

4. **3D Parametric Form**:  
   →r = (x₁+λa)î + (y₁+λb)ĵ + (z₁+λc)k̂

---

## 3. Angle Bisectors

### Important Concepts:
1. **Internal Angle Bisector**:  
   →r = â + b̂

2. **External Angle Bisector**:  
   →r = â - b̂

3. **Acute/Obtuse Determination**:
   - If →a·→b > 0:  
     â + b̂ → acute  
     â - b̂ → obtuse
   - If →a·→b < 0:  
     â + b̂ → obtuse  
     â - b̂ → acute

---

## 4. Lines in 3D Space

### Types of Lines:
1. **Coplanar Lines**:
   - Intersecting
   - Parallel
   - Coincident

2. **Non-Coplanar (Skew Lines)**:
   - Neither parallel nor intersecting

### Checking for Skew Lines:
1. Take points P(λ) on L₁, Q(μ) on L₂
2. Solve vector PQ = →0
3. If no solution exists → skew lines

### Shortest Distance Between Skew Lines:
$$ d = \frac{|(\vec{a}-\vec{b})·(\vec{m}×\vec{n})|}{|\vec{m}×\vec{n}|} $$

**Matrix Forms**:
- Numerator: 
  $$\begin{vmatrix} 
  a₁-b₁ & a₂-b₂ & a₃-b₃ \\ 
  m₁ & m₂ & m₃ \\ 
  n₁ & n₂ & n₃ 
  \end{vmatrix}$$
  
- Denominator: 
  $$\begin{vmatrix} 
  î & ĵ & k̂ \\ 
  m₁ & m₂ & m₃ \\ 
  n₁ & n₂ & n₃ 
  \end{vmatrix}$$

### Coplanarity Condition:
$$\begin{vmatrix} 
a₁-b₁ & a₂-b₂ & a₃-b₃ \\ 
m₁ & m₂ & m₃ \\ 
n₁ & n₂ & n₃ 
\end{vmatrix} = 0$$

---

## 5. Planes in 3D Space

### Equation Forms:
1. **Using Point and Normal**:
   - Vector: (→r - →a)·→n = 0
   - Cartesian: a(x-x₁) + b(y-y₁) + c(z-z₁) = 0

2. **Using Two Vectors**:
   - [→r - →a, →b, →c] = 0
   - Parametric: →r = →a + λ→b + μ→c

3. **Intercept Form**:  
   x/α + y/β + z/γ = 1  
   (α,β,γ = intercepts)

### Relative Positions:
- **Coincident**: a₁/a₂ = b₁/b₂ = c₁/c₂ = d₁/d₂
- **Parallel**: a₁/a₂ = b₁/b₂ = c₁/c₂ ≠ d₁/d₂
- **Intersecting**: Ratios unequal

---

## 6. Key Results

### Angle Between Planes:
$$ cosθ = \frac{\vec{n₁}·\vec{n₂}}{|\vec{n₁}||\vec{n₂}|} $$

### Point-Plane Relations:
1. **Same Side**:  
   (ax₁+by₁+cz₁-d)(ax₂+by₂+cz₂-d) > 0

2. **Opposite Sides**:  
   (ax₁+by₁+cz₁-d)(ax₂+by₂+cz₂-d) < 0

3. **Distance from Point**:  
   $$ d = \frac{|ax₁+by₁+cz₁-d|}{\sqrt{a²+b²+c²}} $$

4. **Foot of Perpendicular**:  
   $$ \frac{x-x₁}{a} = \frac{y-y₁}{b} = \frac{z-z₁}{c} = -\frac{(ax₁+by₁+cz₁-d)}{a²+b²+c²} $$

### Angle Bisector Planes:
$$ \frac{a₁x+b₁y+c₁z-d₁}{\sqrt{a₁²+b₁²+c₁²}} = ±\frac{a₂x+b₂y+c₂z-d₂}{\sqrt{a₂²+b₂²+c₂²}} $$

**Sign Convention**:
- +ve → Obtuse when n₁·n₂ > 0
- -ve → Acute when n₁·n₂ > 0

---

## 7. Special Cases

### Family of Planes:
p₁ + λp₂ = 0

### Unsymmetric Line Form:
Intersection of two planes p₁ = 0 and p₂ = 0
