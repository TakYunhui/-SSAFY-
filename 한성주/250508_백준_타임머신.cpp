// 11657 - 타임머신
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;
const ll INF = 1000000000LL;

struct Edge { int u, v; ll w; };

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<Edge> edges;
    edges.reserve(M);

    for(int i = 0; i < M; i++){
        int A, B; ll C;
        cin >> A >> B >> C;
        edges.push_back({A, B, C});
    }

    vector<ll> dist(N+1, INF);
    dist[1] = 0;

    // 벨만-포드
    for(int i = 1; i < N; i++){
        bool updated = false;
        for(auto &e : edges){
            if(dist[e.u] != INF && dist[e.v] > dist[e.u] + e.w){
                dist[e.v] = dist[e.u] + e.w;
                updated = true;
            }
        }
        if(!updated) break;
    }

    // 음수 사이클 검사
    for(auto &e : edges){
        if(dist[e.u] != INF && dist[e.v] > dist[e.u] + e.w){
            cout << -1 << "\n";
            return 0;
        }
    }

    // 2번~N번 도시로 가는 최단 시간 출력
    for(int city = 2; city <= N; city++){
        if(dist[city] == INF) 
            cout << -1 << "\n";
        else 
            cout << dist[city] << "\n";
    }
    return 0;
}