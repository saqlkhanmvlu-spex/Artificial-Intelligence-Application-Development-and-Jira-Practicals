table = { 
('Green', 'No', 'No'): 'Move Forward', 
('Green', 'Yes', 'No'): 'Stop', 
('Red', 'No', 'No'): 'Stop', 
('Yellow', 'No', 'No'): 'Slow Down', 
('Green', 'No', 'Yes'): 'Pick Up Passenger', 
('Red', 'Yes', 'No'): 'Stop', 
('Yellow', 'Yes', 'No'): 'Stop', 
('Green', 'Yes', 'Yes'): 'Wait Until Road is Clear', 
('Yellow', 'No', 'Yes'): 'Slow Down and Pick Up Passenger', 
('Red', 'No', 'Yes'): 'Wait for Green Signal' 
} 
percepts = [] 
def taxi_agent(percept):
percepts.append(percept) 
action = table.get(percept, "Wait") 
return action 
print("Autonomous Taxi Table-Driven Agent") 
n = int(input("Enter number of percepts: ")) 
for i in range(n): 
print(f"\nPercept {i+1}") 
signal = input("Traffic Signal (Green/Yellow/Red): ").capitalize() obstacle = input("Obstacle Present? (Yes/No): ").capitalize() passenger = input("Passenger Request? (Yes/No): ").capitalize() percept = (signal, obstacle, passenger) 
action = taxi_agent(percept) 
print("Current Percept:", percept) 
print("Agent Action:", action) 
print("Saqlain Khan SO13") 
