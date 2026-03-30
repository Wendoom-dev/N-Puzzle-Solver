import os
import time

'''
    This file is responsible for showing the simulation of the search algorithms we have used. It was developed with assistance of Google Gemini (AI) particularly for animations and grid layouts to ensure readibility and smooth simulation

'''
class PuzzleVisualizer:
    def __init__(self, pause_duration=0.5):
        
        self.pause_duration = pause_duration

    def clear_screen(self):
        
        os.system('cls' if os.name == 'nt' else 'clear')

    def render_grid(self, grid_layout):
        
        print("+---+---+---+")
        for i in range(0, 9, 3):
            row = grid_layout[i:i+3]
            
            formatted_row = [str(tile) if tile != 0 else " " for tile in row]
            print(f"| {formatted_row[0]} | {formatted_row[1]} | {formatted_row[2]} |")
            print("+---+---+---+")

    def animate_solution(self, solution_sequence, stats=None):
       
        if not solution_sequence:
            print("No solution path found to visualize.")
            return

        total_steps = len(solution_sequence) - 1
        
        for step, layout in enumerate(solution_sequence):
            self.clear_screen()
            print("=== N-Puzzle Solver: Solution Replay ===")
            print(f"Step: {step} / {total_steps}")
            print("----------------------------------------")
            
            self.render_grid(layout)
            
            if stats:
                print("\n--- Live Search Metrics ---")
                print(f"Algorithm: {stats.get('algo', 'N/A')}")
                print(f"Heuristic: {stats.get('heuristic', 'N/A')}")
                print(f"Nodes Visited: {stats.get('nodes', 0)}")
                print(f"Time Taken: {stats.get('time', 0.0):.4f} seconds")
            
            time.sleep(self.pause_duration)

        print("\nGoal State Reached successfully!")

    def display_comparison_table(self, results_data):
        
        print("\n" + "="*50)
        print(f"{'Algorithm':<15} | {'Heuristic':<15} | {'Nodes':<8} | {'Time (s)':<8}")
        print("-" * 50)
        for entry in results_data:
            print(f"{entry['algo']:<15} | {entry['heuristic']:<15} | {entry['nodes']:<8} | {entry['time']:<8.4f}")
        print("="*50 + "\n")