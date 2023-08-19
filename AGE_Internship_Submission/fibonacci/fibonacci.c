#include <stdio.h>
#include <stdlib.h>

typedef enum TypeTag {
    ADD,
    MUL,
    SUB,
    FIBO
} TypeTag;

typedef struct Node {
    TypeTag type;
    int value;
    struct Node *left;
    struct Node *right;
} Node;

Node* makeFunc(TypeTag type) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->type = type;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void calc(Node* node);

int fibo(int n) {
    int fib[n+2];
    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i <= n; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }

    return fib[n];
}

int main() {
    Node *add = makeFunc(ADD);
    add->left = makeFunc(ADD);
    add->right = makeFunc(ADD);
    add->left->value = 10;
    add->right->value = 6;

    Node *mul = makeFunc(MUL);
    mul->left = makeFunc(ADD);
    mul->right = makeFunc(ADD);
    mul->left->value = 5;
    mul->right->value = 4;

    Node *sub = makeFunc(SUB);
    sub->left = mul;
    sub->right = add;

    Node *fiboNode = makeFunc(FIBO);
    fiboNode->left = makeFunc(ADD);
    fiboNode->left->left = makeFunc(ADD); // Create nodes for Fibonacci sequence calculation
    fiboNode->left->right = makeFunc(ADD);
    fiboNode->left->left->value = 0; // Set initial values for Fibonacci calculation
    fiboNode->left->right->value = 1;

    calc(add);
    calc(mul);
    calc(sub);
    calc(fiboNode);

    printf("add : %d\n", add->value);
    printf("mul : %d\n", mul->value);
    printf("sub : %d\n", sub->value);
    printf("fibo : %d\n", fiboNode->value);

    free(add);
    free(mul);
    free(sub);
    free(fiboNode);

    return 0;
}

void calc(Node* node) {
    if (node == NULL) {
        return;
    }

    if (node->type == ADD) {
        calc(node->left);
        calc(node->right);
        node->value = node->left->value + node->right->value;
    } else if (node->type == MUL) {
        calc(node->left);
        calc(node->right);
        node->value = node->left->value * node->right->value;
    } else if (node->type == SUB) {
        calc(node->left);
        calc(node->right);
        node->value = node->left->value - node->right->value;
    } else if (node->type == FIBO) {
        node->value = fibo(node->left->left->value);
    }
}

