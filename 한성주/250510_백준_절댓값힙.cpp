// 11286 - 절댓값 힙
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// 절댓값이 작은 순, 같으면 실제 값이 작은 순으로 정렬하는 비교 함수
struct AbsCompare {
    bool operator()(int a, int b) const {
        int absA = abs(a), absB = abs(b);
        if (absA != absB) 
            return absA > absB;   // 절댓값이 작은 쪽이 우선
        return a > b;              // 절댓값이 같다면 값이 작은 쪽이 우선
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    priority_queue<int, vector<int>, AbsCompare> heap;

    while (N--) {
        int x;
        cin >> x;
        if (x != 0) {
            heap.push(x);
        } else {
            if (heap.empty()) {
                cout << "0\n";
            } else {
                cout << heap.top() << "\n";
                heap.pop();
            }
        }
    }

    return 0;
}
