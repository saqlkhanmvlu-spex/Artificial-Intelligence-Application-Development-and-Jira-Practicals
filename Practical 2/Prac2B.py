# Water Jug Problem using Depth-First Search (DFS)
def dfs(jug1, jug2, target):
stack = [((0, 0), [])] # (current_state, path)
visited = set()
while stack:
(x, y), path = stack.pop()
if (x, y) in visited:
continue
visited.add((x, y))
path = path + [(x, y)]
# Goal check
if x == target or y == target:
return path
next_states = [
(jug1, y), # Fill Jug 1
(x, jug2), # Fill Jug 2
(0, y), # Empty Jug 1
(x, 0), # Empty Jug 2
(x - min(x, jug2 - y), y + min(x, jug2 - y)), # Pour Jug1 -> Jug2
(x + min(y, jug1 - x), y - min(y, jug1 - x)) # Pour Jug2 -> Jug1
]
for state in next_states:
if state not in visited:
stack.append((state, path))
return None
# Main Program
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))
solution = dfs(jug1, jug2, target)
if solution:
print("\nGoal Achieved Successfully!")
print("Solution Path:")
for state in solution:
print(state)
else:
print("\nNo solution found.")
print("Saqlain Khan S013")
