import heapq
import time
from collections import deque

class AStarSolver:
    def __init__(self, environment, heuristic_fn):
        
        self.env = environment
        self.heuristic = heuristic_fn
        
        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.execution_time = 0

    def solve(self, start_state):
       
        start_time = time.time()
        
        
        initial_h = self.heuristic(start_state, self.env.goal_state)
        frontier = [(initial_h, 0, start_state, [start_state])]
        
       
        explored = {start_state: 0}
        
        self.nodes_expanded = 0
        self.max_frontier_size = 1

        while frontier:
            
            self.max_frontier_size = max(self.max_frontier_size, len(frontier))
            
            
            f, g, current_state, path = heapq.heappop(frontier)
            self.nodes_expanded += 1

            
            if self.env.goal_test(current_state):
                self.execution_time = time.time() - start_time
                return path, self.nodes_expanded, self.max_frontier_size, self.execution_time

            
            for action in self.env.get_actions(current_state):
                neighbor = self.env.get_successor(current_state, action)
                new_g = g + 1  
                
                
                if neighbor not in explored or new_g < explored[neighbor]:
                    explored[neighbor] = new_g
                    h = self.heuristic(neighbor, self.env.goal_state)
                    f_new = new_g + h
                    
                    heapq.heappush(frontier, (f_new, new_g, neighbor, path + [neighbor]))

        self.execution_time = time.time() - start_time
        return None, self.nodes_expanded, self.max_frontier_size, self.execution_time



class BFSSolver:
    def __init__(self, environment):
        self.env = environment

        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.execution_time = 0

    def solve(self, start_state):
        start_time = time.time()

        frontier = deque([(start_state, [start_state])])  # (state, path)
        explored = set([start_state])

        self.nodes_expanded = 0
        self.max_frontier_size = 1

        while frontier:
            self.max_frontier_size = max(self.max_frontier_size, len(frontier))

            current_state, path = frontier.popleft()
            self.nodes_expanded += 1

            if self.env.goal_test(current_state):
                self.execution_time = time.time() - start_time
                return path, self.nodes_expanded, self.max_frontier_size, self.execution_time

            for action in self.env.get_actions(current_state):
                neighbor = self.env.get_successor(current_state, action)

                if neighbor not in explored:
                    explored.add(neighbor)
                    frontier.append((neighbor, path + [neighbor]))

        self.execution_time = time.time() - start_time
        return None, self.nodes_expanded, self.max_frontier_size, self.execution_time

import time

class DFSSolver:
    def __init__(self, environment):
        self.env = environment

        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.execution_time = 0

    def solve(self, start_state):
        start_time = time.time()

        frontier = [(start_state, [start_state])]  # stack
        explored = set([start_state])

        self.nodes_expanded = 0
        self.max_frontier_size = 1

        while frontier:
            self.max_frontier_size = max(self.max_frontier_size, len(frontier))

            current_state, path = frontier.pop()  # LIFO
            self.nodes_expanded += 1

            if self.env.goal_test(current_state):
                self.execution_time = time.time() - start_time
                return path, self.nodes_expanded, self.max_frontier_size, self.execution_time

            for action in self.env.get_actions(current_state):
                neighbor = self.env.get_successor(current_state, action)

                if neighbor not in explored:
                    explored.add(neighbor)
                    frontier.append((neighbor, path + [neighbor]))

        self.execution_time = time.time() - start_time
        return None, self.nodes_expanded, self.max_frontier_size, self.execution_time


class GreedyBestFirstSolver:
    def __init__(self, environment, heuristic_fn):
        """
        Initializes the Greedy Best-First Search agent.
        Uses only h(n) as the evaluation function.
        """
        self.env = environment
        self.heuristic = heuristic_fn
        
        # Metrics for Empirical Validation 
        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.execution_time = 0

    def solve(self, start_state):
        """
        Executes Greedy Best-First Search.
        Returns: (path, nodes_expanded, max_frontier, execution_time)
        """
        start_time = time.time()
        
        # Priority Queue stores (h, current_state, path)
        # We ignore g(n) (step cost) for priority sorting.
        initial_h = self.heuristic(start_state, self.env.goal_state)
        frontier = [(initial_h, start_state, [start_state])]
        
        # Track visited states to prevent cycles [cite: 187-189]
        explored = set([start_state])
        
        self.nodes_expanded = 0
        self.max_frontier_size = 1

        while frontier:
            # Monitor peak memory usage [cite: 93]
            self.max_frontier_size = max(self.max_frontier_size, len(frontier))
            
            # Pop the node that appears closest to the goal (lowest h)
            h, current_state, path = heapq.heappop(frontier)
            self.nodes_expanded += 1

            # Goal Test [cite: 280-283]
            if self.env.goal_test(current_state):
                self.execution_time = time.time() - start_time
                return path, self.nodes_expanded, self.max_frontier_size, self.execution_time

            # Transition Model: Generating successor states [cite: 360-373]
            for action in self.env.get_actions(current_state):
                neighbor = self.env.get_successor(current_state, action)
                
                if neighbor not in explored:
                    explored.add(neighbor)
                    h_val = self.heuristic(neighbor, self.env.goal_state)
                    # Add to frontier based strictly on heuristic value
                    heapq.heappush(frontier, (h_val, neighbor, path + [neighbor]))

        self.execution_time = time.time() - start_time
        return None, self.nodes_expanded, self.max_frontier_size, self.execution_time