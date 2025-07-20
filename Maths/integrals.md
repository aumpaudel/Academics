# ∫ Integrals – Quick Notes (basics)
## ✅ What is an integral?
- Mathematical tool to find:

    - Area under a curve

    - Accumulated quantity (like total distance, work done, etc.)

## ✏️ Types of integrals
| Type                | What it does                        | Notation             |
| ------------------- | ----------------------------------- | -------------------- |
| Indefinite integral | Family of functions (no limits); +C | ∫ f(x) dx = F(x) + C |
| Definite integral   | Number (area between x=a and x=b)   | ∫ₐᵇ f(x) dx          |

## 📦 Basic properties
| Property         | Example                                        |
| ---------------- | ---------------------------------------------- |
| Linearity        | ∫ (af(x) + bg(x)) dx = a∫ f(x) dx + b∫ g(x) dx |
| Reversing limits | ∫ₐᵇ f(x) dx = – ∫ᵇₐ f(x) dx                    |
| Additivity       | ∫ₐᵇ f(x) dx + ∫ᵇᶜ f(x) dx = ∫ₐᶜ f(x) dx        |

## ⚡ Common methods of integration
| Method               | Idea                    | Example             |
| -------------------- | ----------------------- | ------------------- |
| Substitution         | Change variable         | ∫ cos(3x) dx → u=3x |
| Integration by parts | ∫ u·dv = u·v – ∫ v·du   | ∫ x·e^x dx          |
| Partial fractions    | Break rational function | ∫ (1/(x²–1)) dx     |

- (For CS, knowing the concept is enough — software often computes actual integral)

## 🔧 Definite integral & area
- ∫ₐᵇ f(x) dx = area under curve f(x) from x=a to x=b.

- If f(x) < 0 in interval, area counted negative → use modulus if you just want area.

## 🔢 Numerical integration (very relevant in CSE)
| Method           | When used                         |
| ---------------- | --------------------------------- |
| Trapezoidal rule | Approximate area using trapezoids |
| Simpson’s rule   | Use parabolas; more accurate      |

→ You’ll implement these in Numerical Methods subject.

## ✏️ Key formulas to remember (basics)
| Integral   | Result                   |   |     |
| ---------- | ------------------------ | - | --- |
| ∫ xⁿ dx    | (xⁿ⁺¹)/(n+1) + C, n ≠ –1 |   |     |
| ∫ e^x dx   | e^x + C                  |   |     |
| ∫ 1/x dx   | ln                       | x | + C |
| ∫ sin x dx | –cos x + C               |   |     |
| ∫ cos x dx | sin x + C                |   |     |

## ✅ Summary
- Integral = area under curve / accumulated quantity.

- Two types: definite (number) & indefinite (function).

- Important in CS for numerical methods, stats, graphics.

- Numerical methods help approximate integrals when no formula works.