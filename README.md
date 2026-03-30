```markdown
# 8-Puzzle Solver: Group 07

> A comprehensive Python implementation of the classic **8-puzzle problem** featuring four search strategies, advanced heuristics, and an animated terminal-based visualization engine.

---

## 🛠 Project Structure

```text
8-puzzle-solver/
├── environment.py   # Puzzle engine: state transitions, goal test, and inversion parity
├── heuristic.py     # Heuristic logic: Manhattan Distance and Linear Conflict
├── solver.py        # Search Agents: A*, BFS, DFS, and Greedy Best-First Search
├── visualizer.py    # UI Engine: Terminal animation and performance tables
└── main.py          # Orchestrator: User input and algorithm execution
```

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

### 1. Manhattan Distance ($L_1$ Baseline)
Calculated as the sum of the absolute horizontal and vertical differences between current tile positions and their goal positions. It is both admissible and consistent.

### 2. Linear Conflict (Advanced)
An enhancement of Manhattan Distance that identifies tiles in their correct row/column but in reversed relative order. It adds a penalty of 2 for every such conflict, significantly reducing the number of nodes expanded in A*.

---

## 📋 Module Overview

### `solver.py`
Contains the four core search classes. Each solver returns a standardized 4-tuple:
* `path`: The sequence of states from start to goal.
* `nodes_expanded`: Total states popped from the frontier (Time Complexity proxy).
* `max_frontier_size`: Peak memory usage (Space Complexity proxy).
* `execution_time`: Total search time in seconds.

### `environment.py`
Implements the **Inversion Parity** check to ensure the puzzle is mathematically solvable before starting a search, preventing infinite loops in unsolvable configurations.

---

## 🎮 How to Run

1. **Ensure Python 3.7+ is installed.**
2. **Run the orchestrator:**
   ```bash
   python main.py
   ```
3. **Follow the prompts** to enter your 9-digit initial state (e.g., `1 2 3 4 0 5 7 8 6`) and select your desired algorithm and heuristic.

---

## 📚 References
* [8-Puzzle Problem in AI (GeeksforGeeks)](https://www.geeksforgeeks.org/artificial-intelligence/8-puzzle-problem-in-ai/)
* [A* Search Algorithm Tutorial (DataCamp)](https://www.datacamp.com/tutorial/a-star-algorithm)
* [Solvability of the 8-Puzzle (Math StackExchange)](https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable)
```

