table = { 
('A', 'Dirty'): 'Suck', 
('A', 'Clean'): 'Right', 
('B', 'Dirty'): 'Suck', 
('B', 'Clean'): 'Left', 
('C', 'Dirty'): 'Suck', 
('C', 'Clean'): 'Backward', 
('D', 'Dirty'): 'Suck', 
('D', 'Clean'): 'Forward' 
} 
sequence_table = { 
(('A', 'Dirty'), ('A', 'Clean')): 'Right', 
(('A', 'Clean'), ('B', 'Dirty')): 'Suck', 
(('B', 'Dirty'), ('B', 'Clean')): 'Left', 
(('B', 'Clean'), ('A', 'Dirty')): 'Suck', 
(('C', 'Dirty'), ('C', 'Clean')): 'Backward',
(('C', 'Clean'), ('A', 'Dirty')): 'Suck', 
(('D', 'Dirty'), ('D', 'Clean')): 'Forward', 
(('C', 'Clean'), ('C', 'Dirty')): 'Suck' 
} 
percepts = [] 
def table_driven_agent(percept): 
percepts.append(percept) 
if tuple(percepts) in sequence_table: 
return sequence_table[tuple(percepts)] 
return table.get(percept, "NoOp") 
print("Vacuum Cleaner Table-Driven Agent") n = int(input("Enter number of percepts: ")) 
for i in range(n): 
print(f"\nPercept {i+1}") 
location = input("Enter Location (A/B/C/D): ").upper() status = input("Enter Status (Clean/Dirty): ").capitalize() 
percept = (location, status) 
action = table_driven_agent(percept) 
print("Percept History :", percepts) 
print("Agent Action :", action) 
print("Saqlain Khan SO13") 
