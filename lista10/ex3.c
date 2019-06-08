#include <stdio.h>
#include <stdlib.h>

int isPrime(int);

int main() {
  int num;
  scanf("%d", &num);

  printf(isPrime(num)==1 ? "E primo\n":"Nao E Primo\n");
  
  return 0;
}

int isPrime(int num) {
  int cont = 1;
  for (int i = 2; i <= num/2; i++) {
    if (num % i == 0) {
      cont++;
    }

    if (cont > 2) {
      return 0;
    }
  }  
  return 1;
}