dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

explored = 0


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def serialize(state):
    s = ""
    for i in range(3):
        for j in range(3):
            s += str(state[i][j])
    return s


def dfs(state, depth, visited, limit, goal):
    global explored
    explored += 1

    if state == goal:
        print("Goal found at depth:", depth)
        return True

    if depth >= limit:
        return False

    key = serialize(state)
    visited.add(key)

    x, y = find_blank(state)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            new_key = serialize(new_state)

            if new_key not in visited:
                if dfs(new_state, depth + 1, visited, limit, goal):
                    return True

    visited.remove(key)
    return False


goal = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

start = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

visited = set()
depth_limit = 100

found = dfs(start, 0, visited, depth_limit, goal)

print("States explored by DFS:", explored)

if not found:
    print("Goal not found within depth limit")