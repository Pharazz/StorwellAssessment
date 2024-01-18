#include <stdio.h>
#include <stdlib.h>

int bruteForce(int m, int n){
    //First we check m and n sizes
    //if m = n then we have one square and output mxm
    if (m == n){
        printf("%dx%d ", m, m);
        return 1;
    }
//--------------------------------------------
    //To decrease unnecessary recursion when the sidelength = 1
    //We compute the remaining squares in one go
    else if (m == 1){
        while (n > 0){
            printf("1x1 ");
            n-=1;
        }
        return 1;
    }
    else if (n == 1){
        while (m > 0){
            printf("1x1 ");
            m-=1;
        }
        return 1;
    }
//--------------------------------------------
    else if(m>n){
        printf("%dx%d ", n, n);
        return bruteForce(m-n, n);
    }
    else {
        printf("%dx%d ", m, m);
        return bruteForce(m, n-m);
    }
    return 0;
}

int main() {
    int m, n;
    printf("Cut paper into largest squares\n");
    printf("Enter dimension n\n");
    scanf("%d", &n);
    printf("Enter dimension m\n");
    scanf("%d", &m);
    printf("Rectangle of size %dx%d\n\n", m, n);
    printf("Solution:\n");
    bruteForce(m,n);
    printf("\nEnd\n");

    // Return 0 to indicate successful execution
    return 0;
}
