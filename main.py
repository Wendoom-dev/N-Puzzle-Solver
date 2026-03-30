import sys
from environment import Env
from heuristic import get_manhattan_distance, get_linear_conflict
from solver import AStarSolver, BFSSolver, DFSSolver, GreedyBestFirstSolver
from visualizer import PuzzleVisualizer

def get_user_input():
    print("\n--- Group 07: 8-Puzzle Solver Configuration ---")
    print("Enter the initial state (9 numbers, 0 for blank, e.g., '1 2 3 4 0 5 7 8 6'):")
    try:
        user_input = input(">> ").strip().split()
        if len(user_input) != 9:
            raise ValueError("Input must contain exactly 9 numbers.")
        starting_layout = tuple(map(int, user_input))
        if sorted(starting_layout) != list(range(9)):
            raise ValueError("Input must contain all numbers from 0 to 8 exactly once.")
        return starting_layout
    except ValueError as e:
        print(f"Invalid Input: {e}")
        return None

def main():
    # 1. Initialize Engine & Visualizer
    GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    grid_engine = Env(goal_state=GOAL)
    viz_tool = PuzzleVisualizer(pause_duration=0.6)

    # 2. Setup Starting Layout
    starting_layout = get_user_input()
    if not starting_layout:
        return

    # 3. L2 Requirement: Solvability Check
    if not grid_engine.is_solvable(starting_layout):
        print("\n[!] Error: This configuration is mathematically unsolvable.")
        print("Reason: Inversion parity constraints prevent reaching the goal.")
        return

    # 4. Algorithm Selection Menu
    print("\n--- Select Search Algorithm ---")
    print("1. Breadth-First Search (BFS) - Uninformed")
    print("2. Depth-First Search (DFS) - Uninformed")
    print("3. A* Search - Informed")
    print("4. Greedy Best-First Search - Informed")
    choice = input(">> ")

    search_agent = None
    algo_name = ""
    h_name = "None"

    # --- Uninformed Searches ---
    if choice == '1':
        search_agent = BFSSolver(grid_engine)
        algo_name = "BFS"
    elif choice == '2':
        search_agent = DFSSolver(grid_engine)
        algo_name = "DFS"

    # --- Informed Searches (Require Heuristic) ---
    elif choice in ['3', '4']:
        print("\nSelect Heuristic Function:")
        print("a. Manhattan Distance (L1 Baseline)")
        print("b. Linear Conflict (L2 Advanced)")
        h_choice = input(">> ").lower()
        
        h_func = get_linear_conflict if h_choice == 'b' else get_manhattan_distance
        h_name = "Linear Conflict" if h_choice == 'b' else "Manhattan Distance"
        
        if choice == '3':
            search_agent = AStarSolver(grid_engine, h_func)
            algo_name = "A*"
        else:
            search_agent = GreedyBestFirstSolver(grid_engine, h_func)
            algo_name = "Greedy Best-First"

    else:
        print("Invalid Selection.")
        return

    # 5. Execute Search and Capture Empirical Metrics
    print(f"\n[i] Running {algo_name} search...")
    solution_path, expanded_count, peak_memory, time_elapsed = search_agent.solve(starting_layout)

    # 6. Visualization & Reporting
    if solution_path:
        outcome_metrics = {
            "algo": algo_name,
            "heuristic": h_name,
            "nodes": expanded_count,
            "time": time_elapsed
        }
        
        # Trigger the animation of the solution sequence
        viz_tool.animate_solution(solution_path, outcome_metrics)
        
        # Final Summary for Empirical Validation (D3, Section 5)
        print("\n--- Final Performance Metrics ---")
        print(f"Algorithm Used:      {algo_name}")
        print(f"Heuristic Used:      {h_name}")
        print(f"Path Length (Cost):  {len(solution_path) - 1}")
        print(f"Nodes Expanded:      {expanded_count}")
        print(f"Max Frontier Size:   {peak_memory}")
        print(f"Computation Time:    {time_elapsed:.5f} seconds")
    else:
        print(f"\n[!] {algo_name} failed to find a solution.")

if __name__ == "__main__":
    main()