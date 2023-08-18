#include <stdio.h>

unsigned long long int recursiveFibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (n == 2) return 2;
    return recursiveFibonacci(n - 3) + recursiveFibonacci(n - 2);
}

int main() {
    int n = 10; // Replace with desired value of n
    printf("F(%d) = %llu\n", n, recursiveFibonacci(n));
    return 0;
}

