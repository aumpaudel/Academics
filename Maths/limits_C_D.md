# 🔍 Limits, Continuity & Differentiability – Quick Notes

## ✅ What is a Limit?
- The value a function approaches as the input approaches some point.
- **Notation**:  
  `lim┬(x→a) f(x) = L`  
  *(For LaTeX-enabled platforms: `$$\lim_{x \to a} f(x) = L$$`)*

## 📦 Basic Properties of Limits
| Rule       | Formula                                      |
|------------|----------------------------------------------|
| **Sum**    | `lim [f(x) + g(x)] = lim f(x) + lim g(x)`    |
| **Product**| `lim [f(x) · g(x)] = lim f(x) · lim g(x)`    |
| **Quotient**| `lim f(x)/g(x) = lim f(x)/lim g(x)` *(if lim g(x) ≠ 0)* |

## ⚡ One-Sided Limits
- **LHL** (x → a⁻): Approach from left  
- **RHL** (x → a⁺): Approach from right  
- *Limit exists iff LHL = RHL*

## 🔄 Continuity
A function is **continuous at x = a** if:
1. `f(a)` exists (defined)
2. `lim┬(x→a) f(x)` exists
3. `lim┬(x→a) f(x) = f(a)`

📌 *Graphically*: No jumps, holes, or breaks.

## ✏️ Differentiability
- **Differentiable at x = a** if `f'(a)` exists.
- Key implications:
  - Differentiable ⇒ Continuous  
  - Continuous ⇏ Differentiable *(e.g., |x| at x=0)*

## 🔢 Common Limits
| Function                | Limit Value |
|-------------------------|-------------|
| `(sin x)/x` as x→0      | 1           |
| `(1 + 1/n)ⁿ` as n→∞     | e           |
| `(aˣ - 1)/x` as x→0     | ln(a)       |

### ⚙ L'Hôpital's Rule
For indeterminate forms (0/0 or ∞/∞):  
`lim┬(x→a) f(x)/g(x) = lim┬(x→a) f'(x)/g'(x)`  
*(LaTeX: `$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}`)*

## 📊 Visual Intuition
| Concept         | Visualization                  |
|-----------------|--------------------------------|
| **Continuous**  | Can draw without lifting pen   |
| **Differentiable** | Smooth curve (no sharp corners) |

## ✅ Summary
1. **Limit**: Approaching value
2. **Continuity**: No sudden jumps
3. **Differentiability**: Smooth slope exists
4. **Applications**: Optimization, Numerical Methods, Graphics

---

### Platform-Specific Notes:
- **GitHub**: Basic tables/math will render, but for LaTeX use `$$...$$` with math-enabled extensions.
- **VS Code**: Install [Markdown+Math](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath) for LaTeX support.
- **Obsidian**: Supports LaTeX natively with `$$`.
- **General**: All emojis, tables, and code blocks (` `` `) work universally.