import sys
from environment import Env
from heuristic import get_manhattan_distance, get_linear_conflict
from solver import AStarSolver
from visualizer import PuzzleVisualizer

def get_user_input():
    """
    Collects the initial 8-puzzle configuration from the user [cite: 251-261].
    Expected format: 9 numbers (0-8) separated by spaces.
    """
    print("\n--- Group 07: 8-Puzzle Solver Configuration ---")
    print("Enter the initial state (9 numbers, 0 for blank, e.g., '1 2 3 4 0 5 7 8 6'):")
    try:
        user_input = input(">> ").strip().split()
        if len(user_input) != 9:
            raise ValueError("Input must contain exactly 9 numbers.")
        
        starting_layout = tuple(map(int, user_input))
        
        # Validate that all numbers 0-8 are present [cite: 206-207]
        if sorted(starting_layout) != list(range(9)):
            raise ValueError("Input must contain all numbers from 0 to 8 exactly once.")
            
        return starting_layout
    except ValueError as e:
        print(f"Invalid Input: {e}")
        return None

def main():
    # 1. Initialize the Core Engine [cite: 101-111, 133-138]
    # Goal state defined in D1: (1, 2, 3, 4, 5, 6, 7, 8, 0) [cite: 50-57, 294-297]
    GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    grid_engine = Env(goal_state=GOAL)
    viz_tool = PuzzleVisualizer(pause_duration=0.6)

    # 2. Get the Starting Layout [cite: 251-252]
    starting_layout = get_user_input()
    if not starting_layout:
        return

    # 3. L2 Requirement: Solvability Detection 
    # Uses Inversion Parity to ensure the configuration is reachable [cite: 236-244, 414-416].
    if not grid_engine.is_solvable(starting_layout):
        print("\n[!] Error: This configuration is mathematically unsolvable.")
        print("Reason: Inversion parity constraints prevent reaching the goal [cite: 226-231, 385].")
        return

    print("\n--- Search Configuration ---")
    print("1. A* Search (Informed)")
    # Space for BFS, DFS, and Greedy to be added by teammates
    choice = input("Select an algorithm (currently only 1 is active): ")

    if choice == '1':
        print("\nSelect Heuristic")
        print("a. Manhattan Distance (L1 Baseline) ")
        print("b. Linear Conflict (L2 Advanced) ")
        h_choice = input(">> ").lower()
        
        # Select the heuristic function to be passed to the search agent
        h_func = get_linear_conflict if h_choice == 'b' else get_manhattan_distance
        h_name = "Linear Conflict" if h_choice == 'b' else "Manhattan Distance"
        
        # Initialize the Search Agent
        search_agent = AStarSolver(grid_engine, h_func)
        
        print(f"\n[i] Starting A* search with {h_name}...")
        
        # 4. Execute Search and Capture Metrics for Empirical Validation
        # Returns path, expanded count, max memory/frontier, and time
        solution_path, expanded_count, peak_memory, time_elapsed = search_agent.solve(starting_layout)

        if solution_path:
            # 5. Trigger Visualization
            # Formulate the stats dictionary for the UI overlay
            outcome_metrics = {
                "algo": "A* Search",
                "heuristic": h_name,
                "nodes": expanded_count,
                "time": time_elapsed
            }
            
            viz_tool.animate_solution(solution_path, outcome_metrics)
            
            # Display final summary for the report
            print("\n--- Empirical Validation Summary ---")
            print(f"Total Moves to Goal: {len(solution_path) - 1}")
            print(f"Nodes Expanded (Time Complexity Proxy): {expanded_count}")
            print(f"Max Frontier Size (Space Complexity Proxy): {peak_memory}")
            print(f"Total Computation Time: {time_elapsed:.5f} seconds")
        else:
            print("Search failed to find a solution path.")

if __name__ == "__main__":
    main()