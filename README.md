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

### `main.py`
The orchestrator of the application. It handles:
* **User Interface**: Console-based menu for inputting puzzle states and selecting algorithms.
* **Input Validation**: Ensures the entered state is a valid 3x3 permutation of numbers 0-8.
* **Execution Flow**: Coordinates between the environment, solvers, and the visualizer.

### `solver.py`
Contains the four core search classes (BFS, DFS, A*, Greedy). Each solver returns:
* **Path**: The sequence of states from start to goal.
* **Nodes Expanded**: Total states popped from the frontier (Time Complexity).
* **Max Frontier Size**: Peak memory usage during the search (Space Complexity).
* **Execution Time**: Total search time in seconds.

### `environment.py`
Defines the rules of the 8-puzzle world:
* **Move Logic**: Calculates valid sliding actions (Up, Down, Left, Right).
* **State Transitions**: Generates successor states by swapping tiles with the blank space.
* **Solvability**: Implements **Inversion Parity** to prevent searching for mathematically impossible goals.

### `heuristic.py`
Contains the "intelligence" for informed search:
* **Manhattan Distance**: Basic $L_1$ distance metric for tile displacements.
* **Linear Conflict**: Advanced heuristic that adds penalties for tiles blocking each other in their target rows or columns.

### `visualizer.py`
Manages the terminal-based user experience:
* **Animation**: Replays the solution path frame-by-frame.
* **Metric Overlay**: Displays real-time search data (nodes visited, current step) during the replay.
* **Comparison UI**: Renders tables to compare performance across different algorithms.
---

## 🎮 How to Run

1. **Ensure Python 3.7+ is installed.**
2. **Run the orchestrator:**
   ```bash
   python main.py
