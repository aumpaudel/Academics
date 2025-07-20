# 🔢 Permutations & Combinations – Quick Notes

## ✅ Permutations (Order Matters)
**Definition**: Arrangements of items where order is important.

### Key Formulas:
- **Factorial**:  
  `n! = n × (n-1) × ... × 1`  
  *(Total arrangements of n distinct items)*
  
- **Permutations (nPr)**:  
  `nPr = n! / (n-r)!`  
  *(Arrangements of r items from n)*

## 📦 Combinations (Order Doesn't Matter)
**Definition**: Selections of items where order is irrelevant.

### Key Formula:
- **Combinations (nCr)**:  
  `nCr = n! / (r!(n-r)!)`  
  *(Also written as (n choose r))*

## ⚡ Permutation vs Combination
| Feature          | Permutation | Combination |
|------------------|-------------|-------------|
| **Order Matters** | Yes         | No          |
| **Example**      | ABC ≠ BAC   | ABC = BAC   |

## 🧠 Special Properties
| Property                  | Formula              | Meaning                     |
|---------------------------|----------------------|-----------------------------|
| Base Cases                | nC0 = nCn = 1        | Choosing none/all           |
| Symmetry                  | nCr = nC(n-r)        | Complementary choices       |
| Pascal's Rule             | nCr + nC(r-1) = (n+1)Cr | Recursive relationship |

## ✏️ Practical Example
| Scenario                  | Calculation | Result |
|---------------------------|-------------|--------|
| Choose 2 students from 4  | 4C2         | 6      |
| Arrange 2 books from 4    | 4P2         | 12     |

## 🧩 With Repetition
- **Combinations with Repetition**:  
  `(n+r-1)Cr`  
  *Example*: 3 chocolates from 5 types = 7C3 = 35 ways

## 🧠 CS Applications
| Area                   | Use Case                          |
|------------------------|-----------------------------------|
| Algorithm Design       | Generating test cases             |
| Probability            | Calculating event probabilities   |
| Cryptography           | Password strength analysis       |
| Machine Learning       | Feature subset selection         |

## 📊 Coding Tips
| Technique               | When to Use                      |
|-------------------------|----------------------------------|
| Fix-and-recurse         | Generating permutations          |
| Inclusion-Exclusion     | "At least one" problems          |
| Modular Arithmetic      | Handling large numbers (10^9+7)  |

## ✅ Summary
1. **Permutations (nPr)**: Ordered arrangements
2. **Combinations (nCr)**: Unordered selections
3. **Key Applications**:  
   - Algorithm complexity analysis  
   - Combinatorial optimization  
   - Probability calculations

---