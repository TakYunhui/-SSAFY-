// 13976 - 타일 채우기 2
#include <iostream>
#include <cstring>
using namespace std;
using ull = unsigned long long;
const long long MOD = 1000000007;

struct Mat {
    long long a[2][2];
    Mat() { memset(a, 0, sizeof(a)); }
};

Mat mul(const Mat &X, const Mat &Y) {
    Mat Z;
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            __int128 sum = 0;
            for(int k = 0; k < 2; k++) {
                sum += (__int128)X.a[i][k] * Y.a[k][j];
            }
            Z.a[i][j] = (long long)(sum % MOD);
        }
    }
    return Z;
}

Mat matPow(Mat A, ull e) {
    Mat R;
    R.a[0][0] = R.a[1][1] = 1;  // 단위행렬
    while (e) {
        if (e & 1) R = mul(R, A);
        A = mul(A, A);
        e >>= 1;
    }
    return R;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ull N;
    cin >> N;

    if (N & 1ULL) {
        cout << 0 << "\n";
        return 0;
    }

    // N = 2k일 때
    ull k = N >> 1;

    if (k == 1ULL) {
        cout << 3 << "\n";
        return 0;
    }

    Mat A;
    A.a[0][0] = 4;
    A.a[0][1] = MOD - 1;
    A.a[1][0] = 1;
    A.a[1][1] = 0;

    Mat P = matPow(A, k - 1);

    long long fk = ( (P.a[0][0] * 3) % MOD + (P.a[0][1] * 1) % MOD ) % MOD;
    cout << fk << "\n";
    return 0;
}