#include <vector>

using namespace std;

void dfs(int node, vector<vector<int>> adj, vector<int>& visited) {
    visited[node] = 1;

    for(auto neigh : adj) {
        if(!visited[neigh])
            dfs(neigh, adj, visited);
    }
}


int main () {
    int edges[3][2] = {{0,1}, {1, 2}, {3, 4}};

    int n = 5;
    int l; cin >> l;
    vector<vector<int>> con;
    
    for(int i = 0; i < edges.Length; i++) {
        con[i[0]].push_back(i[1]);
        con[i[1]].push_back(i[0]);
    }
    
    vector<int> visited;
    int res = 0;
    for(int i = 0; i < n; i++) {
        if(!visited[i]) {
            dfs(i, con, visited);
            res++;
        }
    }

     cout << res << endl;       

    return 0;
}