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

vector< vector<char> > matrix(140, vector<char>(140));

class number{

    public:
        int start_i, start_j, end_j, val;
        number(){
            start_i = 0;
            start_j = 0;
            end_j = 0;
            val = 0;
        } 

};

int main(){
    auto start = high_resolution_clock::now();
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    //code here
    ll n;
    cin >> n;

    vector< number > numbers;
    

    rep(i, n){
        rep(j, n){
            char x;
            cin >> x;
            matrix[i][j] = x;
        }
    }

    rep(i, n){
        int j = 0;
        while(j < n){

            if(isdigit(matrix[i][j])){
                number new_number = number();
                vector<int> numbervec;
                new_number.start_i = i;
                new_number.start_j = j;
                while(isdigit(matrix[i][j]) && j < n){
                    numbervec.pb(matrix[i][j] - '0');
                    j++;
                }
                new_number.end_j = j - 1;
                ll val = 0;
                rep(i, numbervec.size()){
                    val += (numbervec[i] * pow(10, numbervec.size() - i - 1));
                }
                new_number.val = val;
                numbers.push_back(new_number);
            }else{
                j++;
            }
        }
    }

    ll ans = 0;

    map< ll , vector<ll> > gear_map;

    rep(i, numbers.size()){
        number this_number = numbers[i];
        for(int i = this_number.start_i - 1; i <= this_number.start_i + 1; i++ ){
            for(int j = this_number.start_j - 1; j <= this_number.end_j + 1; j++){
                if(i >= 0 && i <= n - 1){
                    if(j >= 0 && j <= n - 1){
                        if(matrix[i][j] == '*'){
                            gear_map[n * i + j].pb(this_number.val);
                        }
                    }
                }
            }
        }

    }
    ans = 0;
    for(auto i : gear_map){
        if(i.second.size() == 2){
            ans += (i.second[0] * i.second[1]);
        }
    }

    cout << ans << endl;
    

    auto stop = high_resolution_clock::now();
    auto dur = duration_cast<milliseconds>(stop - start);
    cerr << dur.count();
}