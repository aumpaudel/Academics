# 🧩 Sets, Relations & Functions – Quick Notes

## ✅ Sets
**Definition**: Collection of well-defined distinct objects.  
**Example**:  
`A = {1, 2, 3}`

### 📦 Notation & Operations
| Symbol | Meaning          |
|--------|------------------|
| `∈`    | Belongs to       |
| `⊆`    | Subset           |
| `∪`    | Union            |
| `∩`    | Intersection     |
| `A'`   | Complement       |
| `A-B`  | Set difference   |

### ✏️ Key Properties
- **Union Size**:  
  `n(A∪B) = n(A) + n(B) - n(A∩B)`  
- **Cartesian Product**:  
  `n(A×B) = n(A) · n(B)`

### 🧠 CS Applications
| Area          | Use Case                     |
|---------------|------------------------------|
| DBMS          | Relations = sets of tuples   |
| Programming   | `HashSet`, `Set` data types  |
| Algorithms    | Tracking unique elements     |

---

## 🔗 Relations
**Definition**: Subset of `A×B` (Cartesian product).  
**Example**:  
If `A = {1,2}`, `B = {x,y}`, then:  
`A×B = {(1,x), (1,y), (2,x), (2,y)}`  
A relation `R` could be:  
`R = {(1,x), (2,y)}`

### 📊 Types of Relations
| Property       | Meaning                                                                 |
|----------------|-------------------------------------------------------------------------|
| Reflexive      | `(a,a) ∈ R` ∀ `a∈A`                                                    |
| Symmetric      | `(a,b) ∈ R ⇒ (b,a) ∈ R`                                                |
| Transitive     | `(a,b) ∈ R` & `(b,c) ∈ R ⇒ (a,c) ∈ R`                                  |
| Equivalence    | Reflexive + Symmetric + Transitive                                      |

### 🧠 CS Applications
| Area            | Use Case                               |
|-----------------|----------------------------------------|
| Databases       | Tables as relations                    |
| Graph Theory    | Edges represent relation pairs         |
| State Machines  | Transitions modeled as relations       |

---

## ➡️ Functions
**Definition**: Special relation where each `a∈A` maps to exactly one `b∈B`.  
**Notation**:  
`f: A → B`  
**Example**:  
`f(x) = x²`

### 📦 Function Types
| Type            | Meaning                                      |
|-----------------|----------------------------------------------|
| Injective       | Distinct inputs → distinct outputs          |
| Surjective      | Every `b∈B` is mapped by some `a∈A`         |
| Bijective       | Both injective & surjective (invertible)     |

### 🔑 Domain & Codomain
- **Domain**: Input set (`A`)
- **Codomain**: Possible outputs (`B`)
- **Range**: Actual outputs (`⊆ B`)

### 🧠 CS Applications
| Area                  | Example                          |
|-----------------------|----------------------------------|
| Hash Tables           | Keys → array indices             |
| Functional Programming| Function composition            |
| Databases             | Key-value mappings               |

---

## ✅ Summary
1. **Sets**: Fundamental collections with operations (union, intersection)
2. **Relations**: Subsets of Cartesian products with special properties
3. **Functions**: Mappings with uniqueness constraints

**Foundations for**:
- Database systems
- Graph algorithms
- Automata theory

---

### Formatting Notes:
1. **Math Notation**: Uses Unicode symbols (`∈`, `⊆`, `⇒`) for broad compatibility
2. **Tables**: Standard Markdown syntax (works everywhere)
3. **LaTeX Alternative**: For platforms supporting LaTeX (e.g., Obsidian, VS Code with plugins), replace:
   - `n(A∪B)` with `$$|A \cup B| = |A| + |B| - |A \cap B|$$`
4. **Code Blocks**: Used for set definitions for clarity
5. **Emojis**: Retained for visual organization (supported in most modern editors)

**Compatible with**: GitHub, GitLab, VS Code, Obsidian, and most Markdown viewers.