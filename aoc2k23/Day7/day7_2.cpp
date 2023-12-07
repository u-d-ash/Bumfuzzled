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

map<char, int> vals;

struct hand{

    string cards;
    ll bid;

    hand(string c, ll b){
        this -> cards = c;
        this -> bid = b;
    }
};

int category(string s){
    set<char> charset;
    map<char, int> charmap;
    rep(i, s.length()){
        charset.insert(s[i]);
        charmap[s[i]]++;
    }
    if(charmap['J'] == 0){
        if(charset.size() == 1){
            return 6;
        }else if(charset.size() == 2){
            for(auto i : charmap){
                if(i.second == 1){
                    return 5;
                }else if(i.second == 2){
                    return 4;
                }else if(i.second == 3){
                    return 4;
                }else if(i.second == 4){
                    return 5;
                }
            }
        }else if(charset.size() == 3){
            for(auto i : charmap){
                if(i.second == 2){
                    return 2;
                }else if(i.second == 3){
                    return 3;
                }
            }
        }else if(charset.size() == 4){
            return 1;
        }else if(charset.size() == 5){
            return 0;
        }
    }else{
        if(charset.size() == 1){
            // all Js
            return 6;
        }else if(charset.size() == 2){
            // J and something else... can be treated as 5 of a kind
            return 6;
        }else if(charset.size() == 3){
            if(charmap['J'] == 1){
                for(auto i : charmap){
                    if(i.second == 3){
                        return 5;
                    }else if(i.second == 2){
                        return 4;
                    }
                }
            }else if(charmap['J'] == 2){
                return 5;
            }else if(charmap['J'] == 3){
                return 5;
            }
        }else if(charset.size() == 4){
            return 3;
        }else if(charset.size() == 5){
            return 1;
        }
    }
    
}

bool comparator(const hand& lh, const hand& rh){
    string lstring = lh.cards;
    string rstring = rh.cards;
    int lcat = category(lstring);
    int rcat = category(rstring);
    if(lcat < rcat){
        return true;
    }else if(lcat > rcat){
        return false;
    }else{
        rep(i, 5){
            if(vals[lstring[i]] < vals[rstring[i]]){
                return true;
            }else if(vals[lstring[i]] > vals[rstring[i]]){
                return false;
            }
        }
        return false;
    }

}

int main(){
    auto start = high_resolution_clock::now();
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    //code here

    vector<hand> vec;

    vals['A'] = 13;
    vals['K'] = 12;
    vals['Q'] = 11;
    vals['J'] = 1;
    vals['T'] = 10;

    for(int i = 2; i <= 9; i++){
        vals['0' + i] = i;
    }

    rep(i, 1000){
        string s;
        ll bind;
        cin >> s >> bind;
        vec.pb(hand(s, bind));
    }

    sort(vec.begin(), vec.end(), &comparator);
    ll answer = 0;
    rep(i, vec.size()){
        cout << i << endl;
        answer += (vec[i].bid * (i + 1));
    }
    cout << answer << endl;

    auto stop = high_resolution_clock::now();
    auto dur = duration_cast<milliseconds>(stop - start);
    cerr << dur.count();
}