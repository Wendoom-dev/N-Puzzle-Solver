#  8-Puzzle Solver

> A Python implementation of the classic **8-puzzle problem** using **A\***, **BFS**, and **DFS** search algorithms — with pluggable heuristics and a clean environment model.

---

##  Project Structure

```
8-puzzle-solver/
├── environment.py   # Puzzle environment: state transitions, goal test, solvability
├── heuristic.py     # Heuristic functions for A* (Manhattan Distance, Linear Conflict)
└── solver.py        # Search algorithms: A*, BFS, DFS
```

---

##  Algorithms Implemented

| Algorithm | Optimal? | Complete? | Heuristic Used |
|:---|:---:|:---:|:---|
| A\* + Manhattan Distance | ✅ | ✅ | `get_manhattan_distance` |
| A\* + Linear Conflict | ✅ | ✅ | `get_linear_conflict` |
| BFS (Breadth-First Search) | ✅ | ✅ | None |
| DFS (Depth-First Search) | ❌ | ✅ | None |

---

##  Getting Started

### Prerequisites

- Python 3.7+
- No external dependencies (uses only Python standard library)

### Run the Solver

```python
from environment import Env
from heuristic import get_manhattan_distance, get_linear_conflict
from solver import AStarSolver, BFSSolver, DFSSolver

# Define the environment
env = Env()  # Default goal: (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Define a scrambled start state
start = (1, 2, 3, 4, 0, 5, 7, 8, 6)

# Check solvability first
if not env.is_solvable(start):
    print("This puzzle configuration is unsolvable.")
else:
    # --- A* with Manhattan Distance ---
    solver = AStarSolver(env, get_manhattan_distance)
    path, nodes, frontier_size, time_taken = solver.solve(start)

    print(f"Solution Length : {len(path) - 1} moves")
    print(f"Nodes Expanded  : {nodes}")
    print(f"Max Frontier    : {frontier_size}")
    print(f"Time Taken      : {time_taken:.4f}s")
```

---

##  Heuristics

### Manhattan Distance
Calculates the sum of horizontal and vertical distances of each tile from its goal position. Admissible and consistent.

### Linear Conflict
An enhancement over Manhattan Distance. Adds a penalty when two tiles are in their correct row or column but in reversed order — forcing extra moves to resolve. Always `≥` Manhattan Distance, resulting in fewer nodes expanded.

```
Linear Conflict = Manhattan Distance + 2 × (number of conflicts)
```

---

##  Module Overview

### `environment.py`

| Method | Description |
|:---|:---|
| `is_solvable(state)` | Checks solvability using inversion parity |
| `get_actions(state)` | Returns valid moves: `Up`, `Down`, `Left`, `Right` |
| `get_successor(state, action)` | Returns the resulting state after an action |
| `goal_test(state)` | Returns `True` if the state equals the goal |

### `heuristic.py`

| Function | Description |
|:---|:---|
| `get_manhattan_distance(state, goal)` | Sum of tile distances from goal positions |
| `get_linear_conflict(state, goal)` | Manhattan Distance + linear conflict penalty |

### `solver.py`

| Class | Description |
|:---|:---|
| `AStarSolver(env, heuristic_fn)` | Informed search using `f(n) = g(n) + h(n)` |
| `BFSSolver(env)` | Uninformed breadth-first search |
| `DFSSolver(env)` | Uninformed depth-first search |

All solvers return the same 4-tuple from `.solve(start_state)`:

```python
path, nodes_expanded, max_frontier_size, execution_time = solver.solve(start)
```

| Return Value | Type | Description |
|:---|:---|:---|
| `path` | `list` or `None` | Sequence of states from start → goal |
| `nodes_expanded` | `int` | Total nodes popped from the frontier |
| `max_frontier_size` | `int` | Peak frontier size during search |
| `execution_time` | `float` | Time taken in seconds |

---

##  State Representation

The puzzle is represented as a **9-tuple** of integers, where `0` is the blank tile.

```
Goal State:          Example Scrambled State:
 1 | 2 | 3            1 | 2 | 3
-----------          -----------
 4 | 5 | 6            4 |   | 5
-----------          -----------
 7 | 8 |              7 | 8 | 6

(1, 2, 3, 4, 5, 6, 7, 8, 0)    (1, 2, 3, 4, 0, 5, 7, 8, 6)
```

---

##  License

This project is open source and available under the [MIT License](LICENSE).
