// Matrix Multiplication
#include <stdio.h>
int main(){
    // getting values in set A and B
    int A[3][3] , B[3][3], C[3][3];
    for(int i = 0; i<3; i++){
        for(int j = 0; j<3; j++){
            printf("A[%d][%d] ", i,j);
            scanf("%d", &A[i][j]);
        }    
    }
    for(int i = 0; i<3; i++){
        for(int j = 0; j<3; j++){
            printf("B[%d][%d] ", i,j);
            scanf("%d", &B[i][j]);
        }    
    }

    // Logic for multiplication
    // Yeah triple Loop
    for(int i = 0;i<3; i++){
        for(int j = 0; j<3; j++){
            C[i][j] = 0;
            for(int k = 0; k<3 ; k++){
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    for(int i = 0; i<3; i++){
        for(int j = 0; j<3; j++){
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    return 0;
}


