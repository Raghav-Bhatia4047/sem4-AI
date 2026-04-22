class Queue:
    def __init__(self):
        self.data = []
        self.front = 0

    def append(self, item):
        self.data.append(item)

    def popleft(self):
        item = self.data[self.front]
        self.front += 1
        return item

    def is_empty(self):
        return self.front >= len(self.data)


class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, priority, item):
        self.data.append((priority, item))
        self.data.sort(key=lambda x: x[0])

    def pop(self):
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0


cities = [
    "Chicago", "Indianapolis", "Detroit", "Cleveland", "Columbus",
    "Buffalo", "Pittsburgh", "Syracuse", "Baltimore",
    "Philadelphia", "New York", "Boston", "Providence", "Portland"
]

N = len(cities)
graph = [[0] * N for _ in range(N)]


def add_edge(a, b, cost):
    i, j = cities.index(a), cities.index(b)
    graph[i][j] = cost
    graph[j][i] = cost


edges = [
    ("Chicago","Indianapolis",182), ("Chicago","Detroit",283), ("Chicago","Cleveland",345),
    ("Indianapolis","Columbus",176),
    ("Detroit","Cleveland",169), ("Detroit","Buffalo",256),
    ("Cleveland","Buffalo",189), ("Cleveland","Pittsburgh",134), ("Cleveland","Columbus",144),
    ("Columbus","Pittsburgh",185),
    ("Buffalo","Pittsburgh",215), ("Buffalo","Syracuse",150),
    ("Pittsburgh","Baltimore",247), ("Pittsburgh","Philadelphia",305),
    ("Syracuse","Philadelphia",254), ("Syracuse","Boston",312),
    ("Baltimore","Philadelphia",101),
    ("Philadelphia","New York",97),
    ("New York","Providence",181), ("New York","Boston",215),
    ("Boston","Providence",50), ("Boston","Portland",107)
]

for e in edges:
    add_edge(*e)


heuristic = [0,180,280,340,400,500,450,600,520,510,560,700,650,780]


class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost


def bfs(start, goal):
    start, goal = cities.index(start), cities.index(goal)

    frontier = Queue()
    frontier.append((start, [start]))

    reached = {start}
    explored = 0

    while not frontier.is_empty():
        node, path = frontier.popleft()
        explored += 1

        if node == goal:
            return explored

        for n in range(N):
            if graph[node][n] != 0 and n not in reached:
                reached.add(n)
                frontier.append((n, path + [n]))

    return explored


def dfs(start, goal):
    start, goal = cities.index(start), cities.index(goal)
    explored = 0

    def dfs_util(node, path):
        nonlocal explored
        explored += 1

        if node == goal:
            return True

        for n in range(N):
            if graph[node][n] != 0 and n not in path:
                if dfs_util(n, path + [n]):
                    return True

        return False

    dfs_util(start, [])
    return explored


def best_first_search(start, goal):
    start, goal = cities.index(start), cities.index(goal)

    node = Node(start, None, 0)

    frontier = PriorityQueue()
    frontier.push(heuristic[start], node)

    reached = {start: node}
    explored = 0

    while not frontier.is_empty():
        _, node = frontier.pop()
        explored += 1

        if node.state == goal:
            return explored

        for n in range(N):
            if graph[node.state][n] != 0:
                child_cost = node.path_cost + graph[node.state][n]
                child = Node(n, node, child_cost)

                if n not in reached or child_cost < reached[n].path_cost:
                    reached[n] = child
                    frontier.push(heuristic[n], child)

    return explored


start_city = "Syracuse"
goal_city = "Chicago"

print("BFS explored nodes:", bfs(start_city, goal_city))
print("DFS explored nodes:", dfs(start_city, goal_city))
print("Best First explored nodes:", best_first_search(start_city, goal_city))