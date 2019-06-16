#include <stdio.h>

void quadrado(int, int);

int main() {
  quadrado(3, 3);
  return 0;
}

void quadrado(int rep, int n) {
  static int i = 0;
  if (n <= 0) {
    return;
  } else if (rep <= 0) { 
    printf("\n");
    i++;
    quadrado(n-1+i, n-1);
  } else {
    printf("* ");
    quadrado(rep-1, n);
  } 
}