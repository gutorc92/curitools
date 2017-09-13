#include<iostream>
#include<cmath>
#include<iomanip>

using namespace std;

int main(){
    
    int codPiece[2], quantityPiece[2];
    double valuePiece[2], total = 0;
    cin >> codPiece[0] >> quantityPiece[0] >> valuePiece[0];
    cin >> codPiece[1] >> quantityPiece[1] >> valuePiece[1];
    for(int i = 0; i < 2; i++){
            total += (quantityPiece[i] * valuePiece[i]);
    }
    cout.precision(2);
    cout << setiosflags (ios::fixed) << "VALOR A PAGAR: R$ " << total <<endl;
    return 1 ;
}

