#include<bits/stdc++.h>


using namespace std;

struct TraversalResult {
    vector<int> order;
    map<int, int> parent;
};

TraversalResult bfs_tree(map<int, vector<int>>& graph, int start) {
    vector<int> order;
    map<int, int> parent;
    set<int> visited;
    queue<int> q;

    q.push(start);
    visited.insert(start);
    parent[start] = -1; 

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);

        vector<int>& neighbors = graph[u];
        for (int v : neighbors) {
            if (visited.find(v) == visited.end()) {
                visited.insert(v);
                parent[v] = u;
                q.push(v);
            }
        }
    }
    return TraversalResult{order, parent};
}
TraversalResult dfs_tree(map<int, vector<int>>& graph, int start) {
    vector<int> order;
    map<int, int> parent;
    set<int> visited;
    stack<int> s;

    s.push(start);
    visited.insert(start);
    parent[start] = -1;

    while (!s.empty()) {
        int u = s.top();
        s.pop();
        order.push_back(u);
        vector<int> neighbors = graph[u];
        for (auto it = neighbors.rbegin(); it != neighbors.rend(); ++it) {
            int v = *it;
            if (visited.find(v) == visited.end()) {
                visited.insert(v);
                parent[v] = u;
                s.push(v);
            }
        }
    }
    return TraversalResult{order, parent};
}
void print_tree(map<int, int>& parent, map<int, string>& id_to_name, string title) {
    cout << "\n" << title << ":" << endl;
    
    for (const pair<const int, int>& item : parent) {
        int child = item.first;
        int par = item.second;

        string child_name = id_to_name[child];
        string par_name = (par == -1) ? "None" : id_to_name[par];
        
        cout << child_name << " <- " << par_name << endl;
    }
}

int main() {
    map<int, string> id_to_name;
    id_to_name[0] = "Raj";     id_to_name[1] = "Priya";   id_to_name[2] = "Aarav";
    id_to_name[3] = "Sunil";   id_to_name[4] = "Akash";   id_to_name[5] = "Neha_C";
    id_to_name[6] = "Neha_R";  id_to_name[7] = "Sneha";   id_to_name[8] = "Rahul";
    id_to_name[9] = "Maya";    id_to_name[10] = "Arjun_B";id_to_name[11] = "Pooja";
    id_to_name[12] = "Arjun_R";

    map<int, vector<int>> graph;
    graph[0] = {3, 5};
    graph[1] = {0, 2, 4};
    graph[2] = {5, 12};
    graph[3] = {0, 4, 7, 9};
    graph[4] = {3, 1};
    graph[5] = {4, 0, 7};
    graph[6] = {1, 2, 5, 8};
    graph[7] = {8, 5};
    graph[8] = {7, 5, 6, 11, 12};
    graph[9] = {10};
    graph[10] = {9, 11};
    graph[11] = {8, 10, 12};
    graph[12] = {6, 8};

    int start_id = 0;
    TraversalResult bfs_res = bfs_tree(graph, start_id);
    cout << "BFS Order:" << endl;
    for (int id : bfs_res.order) cout << id_to_name[id] << " ";
    cout << endl;
    print_tree(bfs_res.parent, id_to_name, "BFS Parent Tree");

    cout << "\n----------------------------\n";

    TraversalResult dfs_res = dfs_tree(graph, start_id);
    cout << "DFS Order:" << endl;
    for (int id : dfs_res.order) cout << id_to_name[id] << " ";
    cout << endl;
    print_tree(dfs_res.parent, id_to_name, "DFS Parent Tree");

    return 0;
}