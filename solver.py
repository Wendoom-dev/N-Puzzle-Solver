import heapq
import time

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


class GreedyBestFirstSolver:
    def __init__(self, environment, heuristic_fn):
        """
        Initializes the Greedy Best-First Search agent.
        Uses f(n) = h(n) as the evaluation function.
        """
        self.grid_engine = environment
        self.est_cost_to_goal = heuristic_fn
        
        # Performance metrics for Empirical Validation
        self.total_nodes_visited = 0
        self.peak_frontier_size = 0
        self.search_duration = 0

    def solve(self, starting_layout):
        """
        Executes Greedy Search. 
        Returns: (solution_path, total_nodes_visited, peak_frontier_size, search_duration)
        """
        start_time = time.time()
        goal_state = self.grid_engine.goal_state
        
        # Priority Queue (Frontier) stores: (h_score, current_state, path)
        # Note: We ignore g(n) (path cost) for priority sorting.
        h_initial = self.est_cost_to_goal(starting_layout, goal_state)
        open_list = [(h_initial, starting_layout, [starting_layout])]
        
        # Track visited layouts to avoid cycles in the state space [cite: 131, 187-189].
        visited_configs = {starting_layout}
        
        self.total_nodes_visited = 0
        self.peak_frontier_size = 1

        while open_list:
            # Tracking max frontier for space complexity analysis [cite: 93, 488-491].
            self.peak_frontier_size = max(self.peak_frontier_size, len(open_list))
            
            # Pop the node that appears closest to the goal (lowest h).
            h, current_layout, solution_path = heapq.heappop(open_list)
            self.total_nodes_visited += 1

            # Goal Test [cite: 280-284]
            if self.grid_engine.goal_test(current_layout):
                self.search_duration = time.time() - start_time
                return solution_path, self.total_nodes_visited, self.peak_frontier_size, self.search_duration

            # Transition Model: Exploring successor nodes [cite: 360-373, 427].
            for action in self.grid_engine.get_actions(current_layout):
                successor_node = self.grid_engine.get_successor(current_layout, action)
                
                if successor_node not in visited_configs:
                    visited_configs.add(successor_node)
                    h_neighbor = self.est_cost_to_goal(successor_node, goal_state)
                    
                    # Push back to queue with only h as the priority.
                    heapq.heappush(open_list, (h_neighbor, successor_node, solution_path + [successor_node]))

        self.search_duration = time.time() - start_time
        return None, self.total_nodes_visited, self.peak_frontier_size, self.search_duration