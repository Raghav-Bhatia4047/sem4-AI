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


class TraversalResult:
    def __init__(self):
        self.order = []
        self.parent = {}


def bfs_tree(graph, start):
    res = TraversalResult()
    visited = set()
    q = Queue()

    q.push(start)
    visited.add(start)
    res.parent[start] = -1

    while not q.is_empty():
        u = q.pop()
        if u is None:
            continue

        res.order.append(u)

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                res.parent[v] = u
                q.push(v)

    return res


def dfs_tree(graph, start):
    res = TraversalResult()
    visited = set()
    stack = []

    stack.append(start)
    visited.add(start)
    res.parent[start] = -1

    while stack:
        u = stack.pop()
        res.order.append(u)

        for v in reversed(graph[u]):
            if v not in visited:
                visited.add(v)
                res.parent[v] = u
                stack.append(v)

    return res


def print_tree(parent, id_to_name, title):
    print("\n" + title + ":")

    for child, par in parent.items():
        child_name = id_to_name[child]
        par_name = "None" if par == -1 else id_to_name[par]
        print(child_name, "<-", par_name)


id_to_name = {
    0: "Raj", 1: "Priya", 2: "Aarav",
    3: "Sunil", 4: "Akash", 5: "Neha_C",
    6: "Neha_R", 7: "Sneha", 8: "Rahul",
    9: "Maya", 10: "Arjun_B", 11: "Pooja",
    12: "Arjun_R"
}

graph = {
    0: [3, 5],
    1: [0, 2, 4],
    2: [5, 12],
    3: [0, 4, 7, 9],
    4: [3, 1],
    5: [4, 0, 7],
    6: [1, 2, 5, 8],
    7: [8, 5],
    8: [7, 5, 6, 11, 12],
    9: [10],
    10: [9, 11],
    11: [8, 10, 12],
    12: [6, 8]
}

start_id = 0

bfs_res = bfs_tree(graph, start_id)

print("BFS Order:")
print(" ".join(id_to_name[i] for i in bfs_res.order))

print_tree(bfs_res.parent, id_to_name, "BFS Parent Tree")

print("\n----------------------------\n")

dfs_res = dfs_tree(graph, start_id)

print("DFS Order:")
print(" ".join(id_to_name[i] for i in dfs_res.order))

print_tree(dfs_res.parent, id_to_name, "DFS Parent Tree")