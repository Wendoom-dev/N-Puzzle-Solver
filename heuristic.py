def get_manhattan_distance(state, goal_state):
    
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:  
            
            curr_r, curr_c = divmod(i, 3)
            
            
            goal_idx = goal_state.index(tile)
            goal_r, goal_c = divmod(goal_idx, 3)
            
            
            distance += abs(curr_r - goal_r) + abs(curr_c - goal_c)
    return distance

def get_linear_conflict(state, goal_state):
    
    h_md = get_manhattan_distance(state, goal_state)
    conflicts = 0

    
    for r in range(3):
        
        row_tiles = []
        for c in range(3):
            tile = state[r * 3 + c]
            if tile != 0:
                row_tiles.append(tile)

        
        for i in range(len(row_tiles)):
            for j in range(i + 1, len(row_tiles)):
                tile_i = row_tiles[i]
                tile_j = row_tiles[j]
                
        
                target_row_i = goal_state.index(tile_i) // 3
                target_row_j = goal_state.index(tile_j) // 3
                
                if target_row_i == r and target_row_j == r:
                    
                    if goal_state.index(tile_i) > goal_state.index(tile_j):
                        conflicts += 1

    
    for c in range(3):
        col_tiles = []
        for r in range(3):
            tile = state[r * 3 + c]
            if tile != 0:
                col_tiles.append(tile)

        for i in range(len(col_tiles)):
            for j in range(i + 1, len(col_tiles)):
                tile_i = col_tiles[i]
                tile_j = col_tiles[j]
                
                target_col_i = goal_state.index(tile_i) % 3
                target_col_j = goal_state.index(tile_j) % 3
                
                if target_col_i == c and target_col_j == c:
                    if goal_state.index(tile_i) > goal_state.index(tile_j):
                        conflicts += 1

    
    return h_md + (2 * conflicts)