#include <stdio.h>

void impares(int);

int main() {
  impares(0);
  return 0;
}

void impares(int n) {
  if (n > 100) {
    printf("\n");
    return;
  } else {
    if (n % 3 == 0) {
      printf("%d ", n);
    }   
    impares(n+1);
  } 
}