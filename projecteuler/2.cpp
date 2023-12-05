#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <chrono>
#include <cstring>

#define INF 10000000000
#define MOD 1000000007

#define ll long long
#define pb push_back
#define pf push_front
#define mp make_pair

#define rep(i, n) for(int i = 0; i < n; ++i)
#define dbg(x) cerr << x << endl;

//author: @u_d_ash_

using namespace std;
using namespace std::chrono;

vector<ll> fib(1000000000, 0);

int main(){
    auto start = high_resolution_clock::now();
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    //code here

    fib[1] = 1;
    fib[2] = 2;

    ll x = 3;
    ll ans = 2; //need to count the 2 as well !
    while(true){

        fib[x] = fib[x - 1] + fib[x - 2];
        if(fib[x] >= 4000000){
            break;
        }
        if(fib[x] % 2 == 0){
            ans += fib[x];
        }
        x++;

    }

    cout << ans << endl;

    auto stop = high_resolution_clock::now();
    auto dur = duration_cast<milliseconds>(stop - start);
    cerr << dur.count();
}