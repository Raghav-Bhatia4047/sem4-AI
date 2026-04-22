import random   
l = ["000", "001", "010", "011", "100", "101", "110", "111"]
n = random.choice(l)

move = 1
suck = 2
cost = 0

L = ["Dirty", "Clean"]
rules = {
    ('A', 'Dirty'): 'SUCK',
    ('A', 'Clean'): 'MOVE_RIGHT',

    ('B', 'Dirty'): 'SUCK',
    ('B', 'Clean'): 'random',

    ('C', 'Dirty'): 'SUCK',
    ('C', 'Clean'): 'MOVE_LEFT'
}

loca = ['A', 'B', 'C']
a = random.choice([0, 1, 2])

Env = {
    'A': L[int(n[0])],
    'B': L[int(n[1])],
    'C': L[int(n[2])]
}

visited = {tile: False for tile in loca}

print("Initial Environment:", Env)

while True:
    location = loca[a]
    status = Env[location]
    visited[location] = True

    print(f"\nLocation: {location} is {status}")
    action = rules[(location, status)]
    if action == 'random':
        if a == 0:
            action = 'MOVE_RIGHT'
        elif a == 2:
            action = 'MOVE_LEFT'
        else:
            action = random.choice(['MOVE_RIGHT', 'MOVE_LEFT'])
    print("Action:", action)
    if action == 'SUCK':
        cost += suck
        Env[location] = 'Clean'
    elif action == 'MOVE_RIGHT':
        if a < 2:
            cost += move
            a += 1
    elif action == 'MOVE_LEFT':
        if a > 0:
            cost += move
            a -= 1
    if all(v == 'Clean' for v in Env.values()) and all(visited.values()):
        break

print("\nFinal Environment:", Env)
print("Total Cost:", cost)
