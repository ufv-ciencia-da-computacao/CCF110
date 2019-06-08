#include <stdio.h>
#define TAM 15

int sum(int*);

int main() {
  int arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  printf("%d", sum(arr));
  return 0;
}

int sum(int *arr) {
  int soma = 0;
  for (int i = 0; i < TAM; i++) {
    soma += arr[i];
  }
  return soma;
}