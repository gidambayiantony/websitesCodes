#include <stdio.h>

unsigned long long int memo[100];

unsigned long long int memoizedFibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (n == 2) return 2;

    if (memo[n] != 0) {
        return memo[n];
    }

    memo[n] = memoizedFibonacci(n - 3) + memoizedFibonacci(n - 2);
    return memo[n];
}

int main() {
    int n = 10; // Replace with desired value of n
    printf("F(%d) = %llu\n", n, memoizedFibonacci(n));
    return 0;
}

