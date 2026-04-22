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


class Path:
    def __init__(self, nodes, cost):
        self.nodes = nodes
        self.cost = cost


cities = [
    "Chicago", "Indianapolis", "Detroit", "Cleveland", "Columbus",
    "Buffalo", "Pittsburgh", "Syracuse", "Baltimore",
    "Philadelphia", "New York", "Boston", "Providence", "Portland"
]

index_map = {city: i for i, city in enumerate(cities)}

n = len(cities)
graph = [[0] * n for _ in range(n)]


def add_edge(a, b, cost):
    i, j = index_map[a], index_map[b]
    graph[i][j] = cost
    graph[j][i] = cost


add_edge("Chicago", "Indianapolis", 182)
add_edge("Chicago", "Detroit", 283)
add_edge("Chicago", "Cleveland", 345)
add_edge("Indianapolis", "Columbus", 176)
add_edge("Detroit", "Cleveland", 169)
add_edge("Detroit", "Buffalo", 256)
add_edge("Cleveland", "Buffalo", 189)
add_edge("Cleveland", "Pittsburgh", 134)
add_edge("Cleveland", "Columbus", 144)
add_edge("Columbus", "Pittsburgh", 185)
add_edge("Buffalo", "Pittsburgh", 215)
add_edge("Buffalo", "Syracuse", 150)
add_edge("Pittsburgh", "Baltimore", 247)
add_edge("Pittsburgh", "Philadelphia", 305)
add_edge("Syracuse", "Philadelphia", 254)
add_edge("Syracuse", "Boston", 312)
add_edge("Baltimore", "Philadelphia", 101)
add_edge("Philadelphia", "New York", 97)
add_edge("New York", "Providence", 181)
add_edge("New York", "Boston", 215)
add_edge("Boston", "Providence", 50)
add_edge("Boston", "Portland", 107)


def bfs(start, goal):
    start_idx = index_map[start]
    goal_idx = index_map[goal]

    frontier = Queue()
    frontier.push(Path([start_idx], 0))

    reached = set([start_idx])

    while not frontier.is_empty():
        node = frontier.pop()
        if node is None:
            continue

        last = node.nodes[-1]

        if last == goal_idx:
            print("Cost:", node.cost, "| Path:",
                  " -> ".join(cities[i] for i in node.nodes))
            return

        for neighbor in range(n):
            if graph[last][neighbor] != 0:
                if neighbor not in reached:
                    reached.add(neighbor)
                    new_path = node.nodes + [neighbor]
                    new_cost = node.cost + graph[last][neighbor]
                    frontier.push(Path(new_path, new_cost))

    print("Failure")


def dfs(current, goal, path, cost):
    path.append(current)

    if current == goal:
        print("Cost:", cost, "| Path:",
              " -> ".join(cities[i] for i in path))
        path.pop()
        return

    for neighbor in range(n):
        if graph[current][neighbor] != 0 and neighbor not in path:
            dfs(neighbor, goal, path, cost + graph[current][neighbor])

    path.pop()


start = "Syracuse"
goal = "Chicago"

print("--- BFS ---")
bfs(start, goal)

print("\n--- DFS ---")
dfs(index_map[start], index_map[goal], [], 0)