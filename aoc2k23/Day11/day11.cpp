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

set<int> brind, bcind;

ll distance(ll a, ll b, ll c, ll d, ll exp){
    ll ans = abs(a - c) + abs(b - d);

    ll rowis = 0; 
    ll colis = 0;

    for(int i = min(a, c); i <= max(a, c); i++){
        if(brind.find(i) != brind.end()){
            colis++;
        }
    }

    for(int i = min(b, d); i <= max(b, d); i++){
        if(bcind.find(i) != bcind.end()){
            rowis++;
        }
    }

    ans = ans + ((rowis + colis) * (exp - 1));

    return ans;
    

}


int main(){
    auto start = high_resolution_clock::now();
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    //code here

    ll n;
    cin >> n;
    
    vector< vector<char> > chart(n, vector<char>(n));

    rep(i, n){
        rep(j, n){
            cin >> chart[i][j];
        }
    }

    int brows = 0, bcols = 0;



    rep(i, n){
        set<char> rlol, clol;
        rep(j, n){
            rlol.insert(chart[i][j]);
            clol.insert(chart[j][i]);
        }
        if(rlol.size() == 1){
            brind.insert(i);
        }
        if(clol.size() == 1){
            bcind.insert(i);
        }
    }

    
    vector< pair<ll ,ll > > gals;

    rep(i, chart.size()){
        rep(j, chart[i].size()){
            if(chart[i][j] == '#'){
                gals.pb(mp(i, j));
            }
        }
    }
    ll ans1 = 0;
    ll ans2 = 0;
    rep(i, gals.size()){
        for(int j = i + 1; j < gals.size(); j++){
            ans1 += distance(gals[i].first, gals[i].second, gals[j].first, gals[j].second, 2);
            ans2 += distance(gals[i].first, gals[i].second, gals[j].first, gals[j].second, 1000000);
        }
    }
    cout << ans1 << endl;
    cout << ans2 << endl;

    auto stop = high_resolution_clock::now();
    auto dur = duration_cast<milliseconds>(stop - start);
    cerr << dur.count();
}