# C++


#include <bits/stdc++.h>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int r;
    cin >> r; cin.ignore();
    int a;
    int b;
    int a_1;
    int b_1;
    cin >> a >> b >> a_1 >> b_1; cin.ignore();
    while(r--){
        if(a <= 0 or b<=0) break;
        b += floor(b_1 / 2);
        a += floor(a_1 / 2);
        b -= a_1;
        a -= b_1;
    }
    if(a>b) cout<<"A "<<a;
    else cout << "B "<<b;
}
