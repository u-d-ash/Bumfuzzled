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
#include <stack>

#define ll long long
#define pb push_back
#define pf push_front
#define mp make_pair

#define vll vector<ll>
#define vvll vector< vector<ll> >
#define pll pair<ll, ll>
#define vpll vector< pair<ll, ll> >
#define vbool vector<bool>

#define INF 100000000000000000
#define MOD 1000000007

#define rep(i, n) for(int i = 0; i < n; ++i)
#define dbg(x) cerr << x << endl;

//author: @u_d_ash_

using namespace std;
using namespace std::chrono;

vector< vector<int> > grid(100, vector<int>(100));

void solvetc(){

    //code here

    rep(i, 100){
        string s;
        cin >> s;
        rep(j, 100){
            grid[i][j] = s[j] - '0';
        }
    }

    // dp[i][j] = min(i =1 , j, j + 1, i)

    vvll dp(100, vll(100, INF));
    dp[99][99] = grid[99][99];

    for(int i = 98; i >= 0; i--){
        dp[i][99] = dp[i + 1][99] + grid[i][99];
        dp[99][i] = dp[99][i + 1] + grid[99][i];
    }

    for(int i = 98; i >= 0; i--){
        for(int j = 98; j >= 0; j--){
            dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1]);
        }
    }
    cout << dp[0][0] << endl;


}

int main(){
    auto start = high_resolution_clock::now();
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    //freopen("input.in", "r", stdin);
    //freopen("output.out", "w", stdout);
    
    bool TC = false;

    ll t;
    
    if(TC){
        cin >> t;
    }else{
        t = 1;
    }

    while(t--){

        solvetc();

    }

    auto stop = high_resolution_clock::now();
    auto dur = duration_cast<milliseconds>(stop - start);
    cerr << dur.count();
}