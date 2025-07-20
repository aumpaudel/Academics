# ✏️ Derivatives – Quick Notes (Basics)

## ✅ What is a Derivative?
- Measures how a function changes as its input changes.
- Mathematically:  
  **`f'(x) = lim_(h→0) [f(x+h) − f(x)] / h`**  
  *(Rendered as a code block for clarity)*

## 📦 Interpretation
| Concept             | Meaning                                  |
|---------------------|------------------------------------------|
| `f'(x) > 0`         | Function is **increasing** at `x`        |
| `f'(x) < 0`         | Function is **decreasing** at `x`        |
| `f'(x) = 0`         | Critical point (possible max/min)        |
| **Derivative**      | Slope of tangent line (rate of change)   |

## 🛠 Basic Rules of Differentiation
| Rule           | Formula                                  |
|----------------|------------------------------------------|
| **Constant**   | `d/dx(c) = 0`                            |
| **Power**      | `d/dx(xⁿ) = n·xⁿ⁻¹`                      |
| **Sum**       | `d/dx(f ± g) = f' ± g'`                 |
| **Product**    | `d/dx(f·g) = f'·g + f·g'`               |
| **Quotient**   | `d/dx(f/g) = (f'·g − f·g') / g²`        |
| **Chain**      | `d/dx f(g(x)) = f'(g(x))·g'(x)`         |

## ✏️ Common Derivatives
| Function       | Derivative                               |
|----------------|------------------------------------------|
| `eˣ`           | `eˣ`                                     |
| `ln(x)`        | `1/x`                                    |
| `sin(x)`       | `cos(x)`                                 |
| `cos(x)`       | `−sin(x)`                                |
| `tan(x)`       | `sec²(x)`                                |

## 🔧 Higher-Order Derivatives
- `f''(x)`: Second derivative → **concavity**.
  - `f''(x) > 0` → **Convex** (local min).
  - `f''(x) < 0` → **Concave** (local max).

## 🔢 Numerical Differentiation
- Approximate when no analytic form:  
  **`f'(x) ≈ [f(x+h) − f(x)] / h`**  
  *(Small `h` for better accuracy)*

## ✅ Summary
1. Derivatives measure **rate of change**.
2. Core tools: **Product, Quotient, Chain Rules**.
3. Applications: Optimization, Physics, AI.