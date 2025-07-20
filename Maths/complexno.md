# 🔮 Complex Numbers – Quick Notes

## ✅ What is a Complex Number?
**Definition**:  
`z = a + ib`  
where:  
- `a` = Real part (`Re(z)`)  
- `b` = Imaginary part (`Im(z)`)  
- `i` = √(-1) *(imaginary unit)*

## 📦 Types of Complex Numbers
| Type                | Example      |
|---------------------|--------------|
| Purely Real         | `3`          |
| Purely Imaginary    | `0 + 4i`     |
| Complex             | `2 + 5i`     |

## 🔧 Basic Operations
| Operation      | Formula                          |
|---------------|----------------------------------|
| **Addition**   | `(a+ib) + (c+id) = (a+c) + i(b+d)` |
| **Subtraction**| `(a+ib) - (c+id) = (a-c) + i(b-d)` |
| **Multiplication**| `(a+ib)(c+id) = (ac-bd) + i(ad+bc)` *(using i² = -1)* |
| **Conjugate**  | `z̄ = a - ib`                    |

## ✏️ Modulus & Argument
| Term         | Formula                     |
|--------------|-----------------------------|
| **Modulus**  | `\|z\| = √(a² + b²)`        |
| **Argument** | `θ = tan⁻¹(b/a)` *(in radians)* |

## 📊 Polar Form
`z = r(cosθ + isinθ)`  
where:  
- `r = \|z\|` *(magnitude)*  
- `θ = arg(z)` *(angle)*

## ⚡ Euler's Formula
`e^(iθ) = cosθ + isinθ`  
Thus:  
`z = re^(iθ)`  
*(Used in rotations and wave equations)*

## 🧠 Applications in CS/Engineering
| Field               | Use Case                     |
|---------------------|------------------------------|
| Computer Graphics   | 2D rotations via multiplication |
| Signal Processing   | Fourier Transforms (e^(iωt))  |
| Control Systems     | Pole-zero analysis           |
| Quantum Computing   | State representations        |

## 🧩 Complex Division
To divide `(a+ib)/(c+id)`:  
1. Multiply numerator & denominator by conjugate `(c-id)`  
2. Result:  
   `[(ac+bd) + i(bc-ad)] / (c²+d²)`

### ✏️ Example Calculations
**Modulus of z = 3 + 4i**:  
`\|z\| = √(3² + 4²) = 5`

**Conjugate**:  
`z̄ = 3 - 4i`

## ✅ Summary
1. **Form**: `a + ib` with `i² = -1`
2. **Visualization**:  
   - Modulus → Distance from origin  
   - Argument → Angle with real axis
3. **Key Tools**:  
   - Polar form (`re^(iθ)`)  
   - Conjugates for simplification
4. **Applications**: Graphics, signal processing, physics simulations

---

