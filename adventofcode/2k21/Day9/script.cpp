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

vector< vector<bool> > vis(100, vector<bool>(100, false));

vector< vector<int> > grid(100, vector<int>(100));

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void flood(int x, int y, ll &c){
    vis[x][y] = 1;
    c += 1;
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >= 0 && nx < 100 && ny >= 0 && ny < 100){
            if(!vis[nx][ny] and grid[nx][ny] != 9){
                flood(nx, ny, c);
            }
        }
    }
}

void solvetc(){

    //code here

    vector<ll> sizes;

    rep(i, 100){
        rep(j, 100){
            cin >> grid[i][j];
        }
    }

    for(int i = 0; i < 100; i++){
        for(int j = 0; j < 100; j++){
            bool r = true;
            for(int k = 0; k < 4; k++){
                int nx = i + dx[k];
                int ny = j + dy[k];
                if(nx >= 0 && nx < 100 && ny >= 0 && ny < 100){
                    if(grid[i][j] >= grid[nx][ny]){
                        r = false;
                        break;
                    }
                }
            }
            if(r){
                ll c = 0;
                flood(i, j, c);
                sizes.push_back(c);
            }
        }
    }

    sort(sizes.rbegin(), sizes.rend());
    cout << sizes[0] * sizes[1] * sizes[2] << endl;

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