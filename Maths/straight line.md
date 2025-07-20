# 📐 Straight Lines – Quick Notes (2D Geometry)

## ✅ Line Fundamentals
### Core Equations:
1. **General Form**:  
   `ax + by + c = 0`  
2. **Slope-Intercept**:  
   `y = mx + c`  
   *(m = slope, c = y-intercept)*

### 📦 Key Concepts
| Term       | Formula/Meaning               |
|------------|-------------------------------|
| **Slope (m)** | `(y₂ - y₁)/(x₂ - x₁)`       |
| **x-intercept** | Set `y=0`, solve for `x`    |
| **y-intercept** | Set `x=0`, solve for `y`    |

---

## ✏️ Line Equation Forms
| Form           | Equation                      | When to Use                 |
|----------------|-------------------------------|-----------------------------|
| **Point-Slope**  | `y - y₁ = m(x - x₁)`        | Known point + slope         |
| **Two-Point**    | `(y-y₁)/(x-x₁) = (y₂-y₁)/(x₂-x₁)` | Two known points       |
| **Intercept**    | `x/a + y/b = 1`             | Known x & y intercepts      |

---

## 🔍 Important Relationships
1. **Parallel Lines**: Same slope (`m₁ = m₂`)  
2. **Perpendicular Lines**:  
   `m₁ × m₂ = -1`  
   *(or slopes are negative reciprocals)*  
3. **Angle Between Lines**:  
   `tanθ = |(m₁ - m₂)/(1 + m₁m₂)|`

---

## 🧠 CS Applications
| Area            | Use Case                      |
|-----------------|-------------------------------|
| Computer Graphics | Line drawing (Bresenham's algorithm) |
| Game Development | Collision detection (hitboxes) |
| UI/UX Design    | Rendering buttons/div borders  |
| Data Visualization | Plotting trendlines          |

---

## 📊 Worked Examples
### Example 1: Find slope  
Given points `A(2, 3)` and `B(5, 11)`:  
`m = (11 - 3)/(5 - 2) = 8/3`

### Example 2: Equation from two points  
Given `A(1, 2)` and `B(3, 6)`:  
1. Find slope: `m = (6-2)/(3-1) = 2`  
2. Use point-slope: `y - 2 = 2(x - 1)` → `y = 2x`

---

## ✅ Summary
1. **Slope (`m`)** defines steepness and direction.  
2. **Forms**: Choose based on given data (points/slopes/intercepts).  
3. **Applications**: Essential for graphics, games, and visual computing.

---