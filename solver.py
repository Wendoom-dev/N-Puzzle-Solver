'''
    Implementation of 4 search Strategies - A*, BFS, DFS and Greedy Search 
    
    Storing paths for proper visualisation

    References: https://www.geeksforgeeks.org/artificial-intelligence/8-puzzle-problem-in-ai/, https://www.datacamp.com/tutorial/a-star-algorithm, https://www.geeksforgeeks.org/dsa/a-search-algorithm/
'''
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

        frontier = deque([(start_state, [start_state])])  
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

        frontier = [(start_state, [start_state])]  
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
        
        self.env = environment
        self.heuristic = heuristic_fn
        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.execution_time = 0

    def solve(self, start_state):

        start_time = time.time()

        initial_h = self.heuristic(start_state, self.env.goal_state)
        frontier = [(initial_h, start_state, [start_state])]

        explored = set([start_state])
        self.nodes_expanded = 0
        self.max_frontier_size = 1

        while frontier:
            self.max_frontier_size = max(self.max_frontier_size, len(frontier))

            h, current_state, path = heapq.heappop(frontier)
            self.nodes_expanded += 1

            if self.env.goal_test(current_state):
                self.execution_time = time.time() - start_time
                return path, self.nodes_expanded, self.max_frontier_size, self.execution_time

            for action in self.env.get_actions(current_state):
                neighbor = self.env.get_successor(current_state, action)

                if neighbor not in explored:
                    explored.add(neighbor)
                    h_val = self.heuristic(neighbor, self.env.goal_state)

                    heapq.heappush(frontier, (h_val, neighbor, path + [neighbor]))

        self.execution_time = time.time() - start_time
        return None, self.nodes_expanded, self.max_frontier_size, self.execution_time