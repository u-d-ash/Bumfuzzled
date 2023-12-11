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

vector< vector<int> > luls(140, vector<int>(140, 0));

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    //code here
    ll n;
    cin >> n;

    vector< vector<char> > chart(n, vector<char>(n));

    ll si, sj;

    rep(i, n){
        rep(j, n){
            cin >> chart[i][j];
            if(chart[i][j] == 'S'){
                si = i;
                sj = j;
                chart[i][j] = '-';
            }
            
        }
    }

    int ci = si;
    int cj = sj + 1;

    bool runmode = true;
    bool plus = true;

    ll steps = 0;
    while(true){

        char x = chart[ci][cj];
        luls[ci][cj] = 1;
        steps++;

        if(runmode && plus){

            if(x == '-'){
                cj++;
            }else if(x == 'J'){
                plus = false;
                runmode = false;
                ci--;
            }else if(x == '7'){
                plus = true;
                runmode = false;
                ci++;
            }else{
                cout << "Err at " << ci << " " << cj << endl;
                break;
            }

        }else if(runmode && !plus){

            if(x == '-'){
                cj--;
            }else if(x == 'F'){
                plus = true;
                runmode = false;
                ci++;
            }else if(x == 'L'){
                plus = false;
                runmode = false;
                ci--;
            }else{
                cout << "Err at " << ci << " " << cj << endl;
                break;
            }

        }else if(!runmode && !plus){

            if(x == '|'){
                ci--;
            }else if(x == 'F'){
                runmode = true;
                plus = true;
                cj++;
            }else if(x == '7'){
                runmode = true;
                plus = false;
                cj--;
            }else{
                cout << "Err at " << ci << " " << cj << endl;
                break;
            }

        }else if(!runmode && plus){

            if(x == '|'){
                ci++;
            }else if(x == 'J'){
                runmode = true;
                plus = false;
                cj--;
            }else if(x == 'L'){
                runmode = true;
                plus = true;
                cj++;
            }else{
                cout << "Err at " << ci << " " << cj << endl;
                break;
            }

        }

        if(ci == si){
            if(cj == sj){
                break;
            }
        }

    }

    cout << steps/2 << endl;

    rep(i, n){
        rep(j, n){
            cout << luls[i][j];

        }
        cout << endl;
    }
    
    ll count = 0;

    rep(i, n){
        bool open = 0;
        rep(j, n){
            if(luls[i][j] == 1){
                if((chart[i][j] == 'F' || chart[i][j] == '7') || chart[i][j] == '|'){

                    open = 1 - open;

                }
            }else{
                if(open){
                    count++;
                }
            }
        }
    }

    cout << count << endl;


}