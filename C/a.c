// a program for GCD of two numbers
#include <stdio.h>
int main(){
    int n1,n2,m;
    printf("Enter two number you are suppose to get their GCD\n");
    scanf("%d%d",&n1,&n2);
    for(int i=1;i<10;i++){
    if(n1%i==0 &&n2%i==0){
        m=i;
    }
}
printf("The GCD of %d and %d is %d",n1,n2 ,m);
return 0;
}