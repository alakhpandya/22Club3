#include<stdio.h>

int main()
{
    int a = 5, b = 10, c;
    // printf("Result: %d", a < b);
    // if(0){
    if(1){
        printf("Success!");
    }
    else{
        printf("Failure!");
    }
    // while (-0.00035){
    while (1){
        printf("Guess a number: ");
        scanf("%d", &c);
        if (c == 25){
            printf("Correct Guess!");
            break;
        }
        printf("Wrong guess! Try again...\n");
    }
    return 0;
}