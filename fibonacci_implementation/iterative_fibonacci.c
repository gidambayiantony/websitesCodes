#include <stdio.h>

unsigned long long int iterativeFibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (n == 2) return 2;

    unsigned long long int prev3 = 0;
    unsigned long long int prev2 = 1;
    unsigned long long int prev1 = 2;
    unsigned long long int current;

    for (int i = 3; i <= n; i++) {
        current = prev1 + prev2;
        prev3 = prev2;
        prev2 = prev1;
        prev1 = current;
    }

    return current;
}

int main() {
    int n = 10; // Replace with desired value of n
    printf("F(%d) = %llu\n", n, iterativeFibonacci(n));
    return 0;
}

