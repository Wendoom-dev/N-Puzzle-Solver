# 8-Puzzle Solver: Group 07

A comprehensive Python implementation of the classic **8-puzzle problem** featuring four search strategies, advanced heuristics, and an animated terminal-based visualization engine.

---

## 🤖 AI Attribution
This project was developed by **Group 07** with the assistance of **Google Gemini (AI)**. The AI was utilized for:
* Refactoring search algorithms for modularity and performance.
* Designing the terminal animation logic and grid rendering in `visualizer.py`.
* Debugging complex state-space edge cases and solvability logic.
* Final validation and empirical testing were conducted by the group members.

---

## 🧠 Algorithms & Performance

| Algorithm | Type | Optimal? | Complete? | Selection Criteria |
|:---|:---:|:---:|:---:|:---|
| **A\*** | Informed | ✅ Yes | ✅ Yes | $f(n) = g(n) + h(n)$ |
| **Greedy BFS** | Informed | ❌ No | ✅ Yes | $f(n) = h(n)$ |
| **BFS** | Uninformed | ✅ Yes | ✅ Yes | Layer-by-layer exploration |
| **DFS** | Uninformed | ❌ No | ✅ Yes | Depth-first exploration |

---

## 🚀 Heuristics

### 1. Manhattan Distance
Sum of the absolute horizontal and vertical differences between current tile positions and goal positions. It is both admissible and consistent.

### 2. Linear Conflict
An enhancement over Manhattan Distance that identifies tiles in their correct row/column but in reversed relative order. It adds a penalty of 2 for every such conflict.

---

## 📋 Module Overview

### `solver.py`
Contains the four core search classes. Each solver returns:
* `path`: Sequence of states from start to goal.
* `nodes_expanded`: Total states popped from the frontier.
* `max_frontier_size`: Peak memory usage (frontier size).
* `execution_time`: Total search time in seconds.

### `environment.py`
Implements the **Inversion Parity** check to ensure the puzzle is mathematically solvable before starting a search.

---

## 🎮 How to Run

1. **Ensure Python 3.7+ is installed.**
2. **Run the orchestrator:**
   ```bash
   python main.py
