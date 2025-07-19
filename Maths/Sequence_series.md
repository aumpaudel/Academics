# Sequences & Series

## Basic Definitions
- **Sequence**: Ordered set of numbers separated by commas  
  Example: `1, 3, 5, 7,...`
- **Series**: Sum of sequence terms separated by +  
  Example: `1 + 3 + 5 + 7 + ...`
- **Progression**: Sequence/Series with a fixed pattern

---

## Arithmetic Progression (AP)

### Key Formulas
- **General term**:  
  `aₙ = a + (n-1)d`  
  Where:  
  `a` = first term, `d` = common difference  
  Behavior:  
  - `d > 0`: Increasing  
  - `d < 0`: Decreasing  
  - `d = 0`: Constant

- **Sum of first n terms**:  
  `Sₙ = n/2 [2a + (n-1)d]` or `n/2 (a + aₙ)`

- **Property**: If `m⋅aₙ = n⋅aₘ` ⇒ `aₘ₊ₙ = 0`

### Properties
1. **Scalar multiplication**:  
   - AP × k ⇒ new difference = k×d  
   - AP ÷ k ⇒ new difference = d/k

2. **Three-term condition**:  
   If a, b, c are in AP ⇒ `2b = a + c`

3. **Linear general term**:  
   `aₙ = dn + c` (where d = common difference)

4. **Quadratic sum**:  
   `Sₙ = An² + Bn` ⇒ `d = 2A`

5. **Term relations**:  
   - `d = aₙ - aₙ₋₁`  
   - `aₙ = Sₙ - Sₙ₋₁`

6. **Symmetric sums**:  
   `a₁ + aₙ = a₂ + aₙ₋₁ = ... = constant`

### Term Selection
| Terms | Format |
|-------|--------|
| 3 terms | `a-d, a, a+d` |
| 5 terms | `a-2d, a-d, a, a+d, a+2d` |
| 4 terms | `a-3d, a-d, a+d, a+3d` |

### Arithmetic Mean (AM)
- **Between two numbers**:  
  `AM = (a + b)/2`

- **Inserting n AMs between a and b**:  
  Common difference `d = (b - a)/(n + 1)`  
  AMs: `a + d, a + 2d, ..., a + nd`

- **Sum of n AMs**:  
  `Sum = n(a + b)/2`

---

## Geometric Progression (GP)

### Key Formulas
- **General term**:  
  `aₙ = arⁿ⁻¹`

- **Sum of first n terms**:  
    - `Sₙ = a(1 - rⁿ)/(1 - r) (if |r| < 1)`
    - `a(rⁿ - 1)/(r - 1) (if |r| > 1)`

- **Infinite series**:  
`S∞ = a/(1 - r)` (only if |r| < 1)

### Geometric Mean (GM)
- **Between two numbers**:  
`GM = √(ab)`

- **Inserting n GMs between a and b**:  
Common ratio `r = (b/a)^(1/(n+1))`  
GMs: `ar, ar², ..., arⁿ`

- **Product property**:  
`G₁ × G₂ × ... × Gₙ = (GM)ⁿ`

### Properties
- Three-term condition:  
If a, b, c in GP ⇒ `b² = ac`

---

## Harmonic Progression (HP)

### Key Formulas
- **General term**:  
`aₙ = 1/[a + (n-1)d]` (Reciprocal of AP)

- **No general sum formula exists**

### Harmonic Mean (HM)
- **Between two numbers**:  
`HM = 2ab/(a + b)`

- **Inserting n HMs between a and b**:  
For reciprocal sequence `1/a, 1/a₁, ..., 1/b`,  
difference `d = [(1/b) - (1/a)]/(n + 1)`

---

## AM-GM-HM Relationships

### For two numbers a, b:
- `AM = (a + b)/2`
- `GM = √(ab)`
- `HM = 2ab/(a + b)`
**Key relations**:
1. `AM × HM = GM² = ab`
2. `AM ≥ GM ≥ HM` (Equality when a = b)

### Ratio property:
If `AM/GM = m/n` ⇒  
`a/b = [m ± √(m² - n²)] / [m ∓ √(m² - n²)]`

---

## Arithmetic-Geometric Progression (AGP)

### Structure:
- AP: `a, a+d, a+2d,...`  
  GP: `b, br, br²,...`  
  AGP: `ab, (a+d)br, (a+2d)br²,...`

### Sum formulas:
- **Finite sum**: Complex (see original notes)
- **Infinite sum** (|r| < 1):  
  `S∞ = ab/(1 - r) + dbr/(1 - r)²`

---

## Special Series Formulas

1. **Sum of first n natural numbers**:  
   `Σk = n(n + 1)/2`

2. **Sum of squares**:  
   `Σk² = n(n + 1)(2n + 1)/6`

3. **Sum of cubes**:  
   `Σk³ = [n(n + 1)/2]²`

4. **Telescoping series**:  
   `Σ(1/k - 1/(k+1)) = 1 - 1/(n+1)`

5. **Product series**:  
   `Σk(k+1) = Σk² + Σk`  
   `= n(n+1)(n+2)/3`