'''
    Responsible for setting basic rules of environment like goal state, valid moves, solvability check etc.

    References : https://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable

'''
class Env:
    def __init__(self, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        
        self.goal_state = goal_state
        self.size = 3  

    def is_solvable(self, state):
        
        tiles = [t for t in state if t != 0]
        inversions = 0
        
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                if tiles[i] > tiles[j]:
                    inversions += 1
        
        
        return inversions % 2 == 0

    def get_actions(self, state):
        
        actions = []
        blank_idx = state.index(0)
        row, col = divmod(blank_idx, self.size)

         
        if row > 0: actions.append("Up")
         
        if row < self.size - 1: actions.append("Down")
        
        if col > 0: actions.append("Left")
        
        if col < self.size - 1: actions.append("Right")
        
        return actions

    def get_successor(self, state, action):
        
        state_list = list(state)
        blank_idx = state_list.index(0)
        
        if action == "Up":
            target_idx = blank_idx - self.size
        elif action == "Down":
            target_idx = blank_idx + self.size
        elif action == "Left":
            target_idx = blank_idx - 1
        elif action == "Right":
            target_idx = blank_idx + 1
        
        
        state_list[blank_idx], state_list[target_idx] = state_list[target_idx], state_list[blank_idx]
        return tuple(state_list)

    def goal_test(self, state):
        
        return state == self.goal_state