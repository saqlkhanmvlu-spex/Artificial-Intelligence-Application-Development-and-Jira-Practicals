from collections import deque
# Function to display puzzle state
def print_state(state):
    print(f"{state[0]} {state[1]} {state[2]}")
    print(f"{state[3]} {state[4]} {state[5]}")
    print(f"{state[6]} {state[7]} {state[8]}")
# Function to find possible next states
def get_neighbors(state):
    neighbors = []
    # Find position of blank tile
    blank_index = state.index(0)
    # Possible moves
    moves = {
        "Up": -3,
        "Down": 3,
        "Left": -1,
        "Right": 1
    }
    for move, position_change in moves.items():
        new_index = blank_index + position_change
        # Check valid moves
        if move == "Up" and blank_index < 3:
            continue
        if move == "Down" and blank_index > 5:
            continue
        if move == "Left" and blank_index % 3 == 0:
            continue
        if move == "Right" and blank_index % 3 == 2:
            continue
        # Create new state by swapping blank tile
        new_state = list(state)
        new_state[blank_index], new_state[new_index] = (
            new_state[new_index],
            new_state[blank_index]
        )
        neighbors.append((tuple(new_state), move))
    return neighbors
# BFS Function
def bfs(initial_state, goal_state):
    queue = deque()
    queue.append((initial_state, []))
    visited = set()
    visited.add(initial_state)
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        for neighbor, move in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [(move, neighbor)]))
    return None
# Main Program
initial_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal_state = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)
print("INITIAL STATE")
print_state(initial_state)
print("\nGOAL STATE")
print_state(goal_state)
solution = bfs(initial_state, goal_state)
if solution:
    print("\n SHORTEST SEQUENCE OF MOVES")
    for step, (move, state) in enumerate(solution, start=1):
        print(f"\nStep {step}: {move}")
        print_state(state)
    print("Goal reached successfully!")
    print("Total number of moves:", len(solution))
else:
    print("\nNo solution found.")
