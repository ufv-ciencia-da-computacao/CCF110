#include <stdio.h>

int parImpar (int);

int main () {
  int num;
  scanf("%d", &num);
  int verifier = parImpar(num);
  if (verifier == 0) {
    printf("É par\n");
  } else {
    printf("É ímpar\n");
  }
  
  return 0;
}

int parImpar(int num) {
  if (num % 2 != 0) {
    return 1;
  }
  
  return 0;
}