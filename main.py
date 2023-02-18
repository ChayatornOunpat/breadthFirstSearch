from collections import deque

def bfs(grid, start, end):
    # Create a queue for BFS and mark the starting point as visited
    queue = deque([(start, [start])])
    visited = set([start])
    
    # Define possible moves on the grid as 4-directional (up, right, down, left)
    moves = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    
    # Start the BFS loop
    while queue:
        # Dequeue the next point from the queue and check if it's the end point
        current, path = queue.popleft()
        if current == end:
            return path
        
        # Generate next possible moves and enqueue them if they haven't been visited
        for move in moves:
            next_pos = (current[0] + move[0], current[1] + move[1])
            if (0 <= next_pos[0] < len(grid) and 
                0 <= next_pos[1] < len(grid[0]) and 
                grid[next_pos[0]][next_pos[1]] != "#" and 
                next_pos not in visited):
                visited.add(next_pos)
                next_path = path + [next_pos]
                queue.append((next_pos, next_path))
    
    # If end point was not found, return None
    return None


grid = [
    ['#','#','#','#','.','#'],
    ['.','.','.','.','.','.'],
    ['.','#','.','.','.','.'],
    ['.','.','.','.','#','.'],
    ['.','.','#','.','.','.'],
    ['.','.','.','.','#','#']
]
start = (5,0)
end = (0,4)


if __name__ == "__main__":
    print(bfs(grid,start,end))