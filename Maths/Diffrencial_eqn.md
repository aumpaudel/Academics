# 🧮 Differential Equations – Quick Notes (basics)
## ✅ What is a differential equation?
- An equation involving:

    - a function y(x)

    - and its derivatives (e.g., dy/dx, d²y/dx²).

- It describes how a quantity changes.

## 🔹 Order & degree
| Term   | Meaning                                                          | Example                         |
| ------ | ---------------------------------------------------------------- | ------------------------------- |
| Order  | Highest derivative present                                       | d²y/dx² + dy/dx = 0 → order = 2 |
| Degree | Power of highest derivative (after clearing radicals, fractions) | (dy/dx)² + y = 0 → degree = 2   |


## 🛠 Types of differential equations
| Type              | Form                            | Example           |
| ----------------- | ------------------------------- | ----------------- |
| Ordinary DE (ODE) | Derivatives wrt single variable | dy/dx + y = x     |
| Partial DE (PDE)  | Derivatives wrt >1 variable     | ∂z/∂x + ∂z/∂y = 0 |

- In CSE, ODEs are more common.

## ✏️ Solution concepts
- General solution: Contains constants (C).

- Particular solution: Found by using initial/boundary conditions.

## 🔢 Basic first-order ODEs
### 1️⃣ Variable separable:
- dy/dx = f(x)·g(y)
    - → Separate: dy/g(y) = f(x) dx → Integrate.

### 2️⃣ Linear form:
- dy/dx + P(x)·y = Q(x)
    - → Use integrating factor (IF): e^(∫P(x) dx).

## 🔧 Applications (why it matters in CSE):
| Area                        | Example                                            |
| --------------------------- | -------------------------------------------------- |
| Numerical Methods           | Euler / Runge-Kutta methods solve ODEs numerically |
| Computer Graphics           | Animation curves, motion simulation                |
| AI / ML                     | Some optimization methods use gradient-based ODEs  |
| Physics engines (games, VR) | Simulate motion, rotation, collisions              |


## 📊 Numerical Methods basics (you’ll study in sem 5)
- When DE can't be solved analytically:

| Method           | Idea                                                  |
| ---------------- | ----------------------------------------------------- |
| Euler’s method   | Step-wise update: y\_{n+1} = y\_n + h·f(x\_n, y\_n)   |
| Runge-Kutta (RK) | More accurate; uses multiple slope estimates per step |


## 🔑 Key points to remember
- Differential equation ≠ just math: it models change.

- ODE vs PDE: single vs multiple variables.

- Degree & order help classify DE.

- Numerical solutions = backbone in CS simulations & AI.