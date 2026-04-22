class Queue:
    def __init__(self):
        self.data = []
        self.front = 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.data[self.front]
            self.front += 1
            return item
        return None

    def is_empty(self):
        return self.front >= len(self.data)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

explored = 0


def serialize(state):
    s = ""
    for i in range(3):
        for j in range(3):
            s += str(state[i][j])
    return s


def bfs(start, goal):
    global explored

    q = Queue()
    visited_depth = {}

    start_key = serialize(start)
    visited_depth[start_key] = 0
    q.push((start, 0))

    while not q.is_empty():
        curr = q.pop()
        if curr is None:
            continue

        state, depth = curr
        explored += 1

        if state == goal:
            print("Goal found at depth:", depth)
            return depth

        x = y = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    x, y = i, j

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                key = serialize(new_state)

                if key not in visited_depth or visited_depth[key] > depth + 1:
                    visited_depth[key] = depth + 1
                    q.push((new_state, depth + 1))

    return -1


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

depth = bfs(start, goal)

print("States explored by optimized BFS:", explored)

if depth == -1:
    print("Goal not found.")