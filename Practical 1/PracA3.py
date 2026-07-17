table = { 
('Yes', 'No', 'No'): 'Attack Enemy', 
('Yes', 'Yes', 'No'): 'Use Health Kit', 
('Yes', 'No', 'Yes'): 'Reload Weapon', 
('No', 'No', 'No'): 'Explore Map', 
('No', 'Yes', 'No'): 'Search for Health Pack', 
('No', 'No', 'Yes'): 'Search for Ammo', 
('Yes', 'Yes', 'Yes'): 'Retreat', 
('No', 'Yes', 'Yes'): 'Find Safe Zone', 
('No', 'No', 'Yes'): 'Collect Ammo Crate', 
('Yes', 'No', 'No'): 'Eliminate Enemy' 
} 
percepts = [] 
def gaming_agent(percept): 
percepts.append(percept) 
action = table.get(percept, "Wait") 
return action 
print("Gaming Table-Driven Agent") 
n = int(input("Enter number of percepts: ")) 
for i in range(n): 
print(f"\nPercept {i+1}") 
enemy = input("Enemy Nearby? (Yes/No): ").capitalize() health = input("Health Low? (Yes/No): ").capitalize() ammo = input("Ammo Low? (Yes/No): ").capitalize() percept = (enemy, health, ammo)
action = gaming_agent(percept) 
print("Current Percept:", percept) 
print("Agent Action:", action) 
print("Saqlain Khan SO13") 
