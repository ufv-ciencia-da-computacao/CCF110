#include <stdio.h>

int fib(int n);

int main() {
  for (int i = 1; i < 21; i++) {
    printf("fib(%d) = %d\n", i, fib(i));
  }
  
  return 0;
}

int fib(int n) {
  if (n == 1 || n == 2) {
    return 1;
  }
  return fib(n-1) + fib(n-2);
}