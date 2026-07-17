import heapq
graph = {
'Mumbai': [('Pune', 150), ('Hyderabad', 710)],
'Pune': [('Mumbai', 150), ('Bangalore', 840)],
'Hyderabad': [('Mumbai', 710), ('Bangalore', 570)],
'Bangalore': []
}
def ucs(start, goal):
queue = [(0, start, [start])]
visited = []
while queue:
cost, city, path = heapq.heappop(queue)
if city == goal:
return cost, path
if city not in visited:
visited.append(city)
for neighbor, distance in graph[city]:
heapq.heappush(
queue,
(
cost + distance,
neighbor,
path + [neighbor]
)
)
return None, None
cost, path = ucs("Mumbai", "Bangalore")
print("Least-cost path:")
print("Path:", " -> ".join(path))
print("Total Distance:", cost, "km")
