start = [3, 3, 0, 0]
goal = [0, 0, 3, 3]


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop() if self.items else None

    def is_empty(self):
        return len(self.items) == 0


def valid(state):
    if state[1] > 0 and state[0] > state[1]:
        return False
    if state[3] > 0 and state[2] > state[3]:
        return False
    if min(state) < 0 or max(state) > 3:
        return False
    if state[0] + state[2] != 3:
        return False
    if state[1] + state[3] != 3:
        return False
    return True


def steps(state, boat):
    moves = [(1,0),(0,1),(2,0),(0,2),(1,1)]
    children = []

    for m in moves:
        if boat == "left":
            new_state = [
                state[0] - m[0], state[1] - m[1],
                state[2] + m[0], state[3] + m[1]
            ]
        else:
            new_state = [
                state[0] + m[0], state[1] + m[1],
                state[2] - m[0], state[3] - m[1]
            ]

        if valid(new_state):
            children.append(new_state)

    return children


def dls(limit):
    stack = Stack()
    stack.push((start, "left", 0, [start]))

    total = 0

    while not stack.is_empty():
        state, boat, depth, path = stack.pop()
        total += 1

        if state == goal:
            return path, total

        if depth == limit:
            continue

        for child in steps(state, boat):
            new_boat = "right" if boat == "left" else "left"

            if child not in path:
                stack.push((child, new_boat, depth + 1, path + [child]))

    return "cutoff", total


def ids():
    depth = 0
    total_explored = 0

    while True:
        result, explored = dls(depth)
        total_explored += explored

        if result != "cutoff":
            return result, total_explored

        depth += 1


result, ids_total = ids()

print("states explored in IDS:", ids_total)

sol, dls_total = dls(3)

print("states explored in DLS with depth 3:", dls_total)
print("Solution path:", result)