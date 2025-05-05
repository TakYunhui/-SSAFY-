// 2637 - 장난감 조립
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<vector<pair<int,int>>> adj(N+1);
    vector<int> indegree(N+1, 0);

    for(int i = 0; i < M; i++){
        int X, Y, K;
        cin >> X >> Y >> K;
        adj[Y].push_back({X, K});
        indegree[X]++;
    }

    vector<vector<int>> dp(N+1, vector<int>(N+1, 0));
    queue<int> q;
    for(int i = 1; i <= N; i++){
        if(indegree[i] == 0){
            dp[i][i] = 1;
            q.push(i);
        }
    }

    while(!q.empty()){
        int u = q.front(); q.pop();
        for(auto &e : adj[u]){
            int v = e.first, k = e.second;
            for(int b = 1; b <= N; b++){
                dp[v][b] += dp[u][b] * k;
            }
            if(--indegree[v] == 0){
                q.push(v);
            }
        }
    }
    
    for(int b = 1; b <= N; b++){
        if(dp[N][b] > 0){
            cout << b << " " << dp[N][b] << "\n";
        }
    }
    return 0;
}
