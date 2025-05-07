// 1300 - K번째 수
#include <iostream>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N, K;
    cin >> N >> K;

    ll low = 1, high = N * N;
    while (low < high) {
        ll mid = (low + high) / 2;
        ll cnt = 0;
        for (ll i = 1; i <= N; i++) {
            ll add = mid / i;
            if (add > N) add = N;
            cnt += add;
            if (cnt >= K) break;
        }
        if (cnt < K)
            low = mid + 1;
        else
            high = mid;
    }

    cout << low << "\n";
    return 0;
}