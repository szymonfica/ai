#include <iostream> 
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <random>

#define st first
#define nd second
#define BOOST ios_base::sync_with_stdio(0); cout.tie(0); cin.tie(0);
 
using namespace std;
 
typedef long long ll;
const int MXN = 1000000+10;

char tab[77][77];
bool used[30];

void clear_tab() {
    for(int i=1; i<=70; i++) {
        for(int j=1; j<=70; j++) {
            tab[i][j] = '.';
        }
    }
}

bool check(int x, int y, int k) {
    if(x+k-1 > 70 || y+k-1 > 70)
        return false;
    for(int i=x; i<x+k; i++) {
        for(int j=y; j<y+k; j++) {
            if(tab[i][j] != '.') {
                return false;
            }
        }
    }
    return true;
}

void insert(int x, int y, int k) {
    for(int i=x; i<x+k; i++) {
        for(int j=y; j<y+k; j++) {
            tab[i][j] = char('A' + k - 1);
        }
    }
}

int main() {
    BOOST


    for(int i=1; i<=70; i++) {
        for(int j=1; j<=70; j++) {
            tab[i][j] = '.';
        }
    }
    vector<int> V = {24, 23, 22, 21, 20, 19, 18,
                     17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6,
                     5, 4, 3, 2, 1};
    int left = 4900;
    for(int l=1; l<=24; l++) {
        int k = V[l-1];
        bool done = false;
        for(int i=1; i<=70 && !done; i++) {
            for(int j=1; j<=70 && !done; j++) {
                if(check(i, j, k)) {
                    insert(i, j, k);
                    left -= k * k;
                    done = true;
                    used[k] = true;
                }
            }
        }
    }  
    for(int i=1; i<=70; i++) {
        for(int j=1; j<=70; j++) {
            cout<< tab[i][j];
        }
        cout<< '\n';
    }
    cout<< left << '\n';
    for(int i=1; i<=24; i++) {
        if(!used[i]) {
            cout<< i << ' ';
        }
    }
    cout<< '\n';

    

    return 0;
}