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

int dx[8] = {0, 0, 1, 1, 1, -1, -1, -1};
int dy[8] = {1, -1, 0, -1, 1, 0, 1, -1};

ll flashes = 0;

void printgrid(vector< vector<int> > &grid){
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            cout << grid[i][j];
        }
        cout << endl;
    }
}

void run_iteration(vector< vector<int> > &grid){
    queue< pair<int, int> > flashline;
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            if(grid[i][j] == 9){
                flashline.push(mp(i, j));
                grid[i][j] = 0;
                flashes++;
            }else{
                grid[i][j]++;
            }
        }
    }
    while(flashline.size() != 0){
        auto curr = flashline.front();
        flashline.pop();
        int x = curr.first;
        int y = curr.second;
        //cout << x << " " << y << endl;
        for(int k = 0; k < 8; k++){
            int nx = x + dx[k];
            int ny = y + dy[k];
            if(nx >= 0 && nx < 10 && ny >= 0 && ny < 10){
                if(grid[nx][ny] == 9){
                    flashline.push(mp(nx, ny));
                    grid[nx][ny] = 0;
                    flashes++;
                }else if(grid[nx][ny] != 0){
                    grid[nx][ny] += 1;
                }
            }
        }
    }
}

void solvetc(){

    //code here

    vector< vector<int> > grid(10, vector<int>(10));

    for(int i = 0; i < 10; i++){
        string s;
        cin >> s;
        for(int j = 0; j < 10; j++){
            grid[i][j] = s[j] - '0';
        }
    }
    int steps = 0;
    while(true){
        int iflash = flashes;
        run_iteration(grid);
        steps++;
        int fflash = flashes;
        if(fflash - iflash == 100){
            break;
        }
    }
    
    cout << steps << endl;
    cout << flashes << endl;

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