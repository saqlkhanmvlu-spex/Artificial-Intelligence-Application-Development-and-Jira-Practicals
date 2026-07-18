import heapq
# Graph: city and distance to connected cities
graph = {
    'Arad': [('Zerind',75), ('Sibiu',140), ('Timisoara',118)],
    'Zerind': [('Arad',75), ('Oradea',71)],
    'Oradea': [('Zerind',71), ('Sibiu',151)],
    'Sibiu': [('Arad',140), ('Oradea',151), ('Fagaras',99), ('Rimnicu Vilcea',80)],
    'Timisoara': [('Arad',118), ('Lugoj',111)],
    'Lugoj': [('Timisoara',111), ('Mehadia',70)],
    'Mehadia': [('Lugoj',70), ('Drobeta',75)],
    'Drobeta': [('Mehadia',75), ('Craiova',120)],
    'Craiova': [('Drobeta',120), ('Rimnicu Vilcea',146), ('Pitesti',138)],
    'Rimnicu Vilcea': [('Sibiu',80), ('Craiova',146), ('Pitesti',97)],
    'Fagaras': [('Sibiu',99), ('Bucharest',211)],
    'Pitesti': [('Rimnicu Vilcea',97), ('Craiova',138), ('Bucharest',101)],
    'Bucharest': []
}
# Heuristic: straight-line distance to Bucharest
heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0
}
def astar(start, goal):
    queue = []
    # queue contains: f_cost, g_cost, city, path
    heapq.heappush(queue, (heuristic[start], 0, start, [start]))
    visited = set()
    while queue:
        f_cost, g_cost, city, path = heapq.heappop(queue)
        if city == goal:
            return g_cost, path
        if city not in visited:
            visited.add(city)
            for neighbor, distance in graph[city]:
                new_g = g_cost + distance
                new_f = new_g + heuristic[neighbor]


                heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))
    return None, []
cost, path = astar('Arad', 'Bucharest')
print("Shortest path using A* Search:")
print("Path:", " -> ".join(path))
print("Total Cost:", cost)
print("Saqlain Khan S013")
