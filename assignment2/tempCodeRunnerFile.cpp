#include <bits/stdc++.h>
using namespace std;

vector<vector<int> > goal;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int explored = 0;

void find_blank(const vector<vector<int> >& state, int &x, int &y) {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (state[i][j] == 0) {
                x = i;
                y = j;
                return;
            }
}

string serialize(const vector<vector<int> >& state) {
    string s = "";
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            s += char(state[i][j] + '0');
    return s;
}

bool dfs(vector<vector<int> > state, int depth, set<string> &visited, int limit) {
    explored++;

    if (state == goal) {
        cout << "Goal found at depth: " << depth << endl;
        return true;
    }

    if (depth >= limit)
        return false;

    string key = serialize(state);
    visited.insert(key);

    int x, y;
    find_blank(state, x, y);

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
            vector<vector<int> > new_state = state;
            swap(new_state[x][y], new_state[nx][ny]);
            string new_key = serialize(new_state);

            if (visited.count(new_key) == 0) {
                if (dfs(new_state, depth + 1, visited, limit))
                    return true;
            }
        }
    }

    visited.erase(key);
    return false;
}

int main() {
    goal.resize(3, vector<int>(3));
    int val = 0;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++) {
            goal[i][j] = val;
            val++;
        }

    vector<vector<int> > start(3, vector<int>(3));
    start[0][0] = 7; start[0][1] = 2; start[0][2] = 4;
    start[1][0] = 5; start[1][1] = 0; start[1][2] = 6;
    start[2][0] = 8; start[2][1] = 3; start[2][2] = 1;

    set<string> visited;
    int depth_limit = 100;

    bool found = dfs(start, 0, visited, depth_limit);

    cout << "States explored by DFS: " << explored << endl;

    if (!found)
        cout << "Goal not found within depth limit" << endl;

    return 0;
}
