# 🧩 Binomial Theorem – Quick Notes

## ✅ Statement
For any positive integer n:  
`(a + b)ⁿ = Σₖ₌₀ⁿ (n choose k) aⁿ⁻ᵏbᵏ`  
where:  
`(n choose k) = n! / (k!(n-k)!)` *(binomial coefficient)*

## ✏️ General Term
`Tₖ₊₁ = (n choose k) aⁿ⁻ᵏbᵏ`  
*(k ranges from 0 to n)*

## 📦 Key Features
- **Number of terms**: Always `n + 1`  
- **Symmetry**: `(n choose k) = (n choose n-k)`  
- **Middle term(s)**:  
  - Even n: Single middle term  
  - Odd n: Two equal middle terms  

## 🧠 Special Cases
| Case          | Expansion Pattern          |
|---------------|----------------------------|
| `(1 + x)ⁿ`    | All terms positive         |
| `(1 - x)ⁿ`    | Alternating signs (+/-)    |

## ⚡ Important Properties
| Property                      | Result                   |
|-------------------------------|--------------------------|
| Sum of all coefficients       | `2ⁿ` (set a=b=1)        |
| Sum of even-powered coefficients | `2ⁿ⁻¹` (when n>0)    |

## 🧠 CS Applications
| Area               | Use Case                                |
|--------------------|-----------------------------------------|
| Algorithm Design   | Analyzing recursive cases              |
| Probability        | Modeling Bernoulli trials              |
| Machine Learning   | Binomial distributions                 |
| Competitive Coding | Efficient large-number computations    |

## ✏️ Worked Example
**Expand (x + 2)³**:  
<br> = (3 choose 0)x³ + (3 choose 1)x²·2 + (3 choose 2)x·2² + (3 choose 3)2³
<br> = 1·x³ + 3·x²·2 + 3·x·4 + 1·8
<br> = x³ + 6x² + 12x + 8

## 📊 Approximation Technique
For `|x| << 1`:  
`(1 + x)ⁿ ≈ 1 + nx`  
*(Useful for quick estimates)*

## ✅ Summary
1. **Core Formula**: `(a+b)ⁿ` expansion via binomial coefficients  
2. **Combinatorial Meaning**: `(n choose k)` counts k-element subsets  
3. **Applications**:  
   - Probability theory  
   - Algorithm analysis  
   - Statistical modeling  

---