#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

#define vvd vector<vector<double>>
#define vd vector<double>

using namespace std;

class probab_system{

    private:
        double p;
        vvd Exp, p_g;
    
    public:
    
        probab_system(double p_in){
            p = p_in;
            Exp.resize(5, vd(4, -1));
            p_g.resize(5, vd(4, -1));
        }

        void compute(){
            for(int i = 0; i <= 2; i++){
                Exp[4][i] = 1;
            }
            for(int j = 0; j <= 3; j++){
                Exp[j][3] = 0;
            }
            for(int i = 3; i >= 0; i--){
                for(int j = 2; j >= 0; j--){
                    p_g[i][j] = max(0.0, min(1.0, (Exp[i + 1][j] - Exp[i][j + 1])/(4 * p - p * Exp[i][j + 1] - Exp[i][j + 1] + Exp[i + 1][j])));
                    Exp[i][j] = (p_g[i][j] * p_g[i][j] * (4 * p + (1 - p) * Exp[i][j + 1]));
                    Exp[i][j] += (2 * p_g[i][j] * (1 - p_g[i][j]) * Exp[i][j + 1]);
                    Exp[i][j] += (1 - p_g[i][j]) * (1 - p_g[i][j]) * (Exp[i + 1][j]);
                }
            }
        }

        double solve(){
            vvd p_r(5, vd(4));
            for(int i = 0; i <= 2; i++){
                p_r[4][i] = 0;
            }
            for(int j = 0; j <= 3; j++){
                p_r[j][3] = 0;
            }

            p_r[3][2] = 1.0;

            for(int i = 3; i >= 0; i--){
                for(int j = 2; j >= 0; j--){
                    if(i == 3 && j == 2){
                        continue;
                    }
                    p_r[i][j] = p_g[i][j] * p_g[i][j] * (1 - p) * p_r[i][j + 1];
                    p_r[i][j] += 2 * p_g[i][j] * (1 - p_g[i][j]) * p_r[i][j + 1];
                    p_r[i][j] += (1 - p_g[i][j]) * (1 - p_g[i][j]) * p_r[i + 1][j];
                }
            }

            return p_r[0][0];
        }

};



int main(){

    // after iters between 0.2 and 0.3

    double xmin = 0.2269703, xmax = 0.2269759;
    double n = 1000000;
    double step = (xmax - xmin) / n;

    

    double mx, my  = -1;

    freopen("output.out", "w", stdout);
    for (int i = 0; i <= n; i++) {
        double x = xmin + i * step;
        probab_system tsys = probab_system(x);
        tsys.compute();
        double y = tsys.solve();
        if(y > my){
            mx = x;
            my = y;
        }
        //cout << fixed << setprecision(10) << x << " " << y << endl;
    }

    cout << fixed << setprecision(10) << mx << " " << my << endl;
    

}