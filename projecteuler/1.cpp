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

ll sum(ll n){
    return (n * (n + 1))/2;
}


int main(){
    auto start = high_resolution_clock::now();
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    //code here

    // add multiples of three, five remove of fifteen

    //3 * k < 1000 -> k = 333
    //5 * k < 1000 -> k = 199
    //15 * k < 1000 -> k = 66

    ll ans = (3 * sum(333) + 5 * sum(199) - (15 * sum(66)));
    cout << ans << endl;


    auto stop = high_resolution_clock::now();
    auto dur = duration_cast<milliseconds>(stop - start);
    cerr << dur.count();
}