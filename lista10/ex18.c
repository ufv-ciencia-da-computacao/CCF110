#include <stdio.h>
#define TAM 5

void div3(int*);

int main() {
  int arr = {3, 6, 7, 9, 11, 12, 15, 16, 17, 21};
  div3(arr);
  return 0;
}

void div3(int *arr) {
  for (int i = 0; i < TAM; i++) {
    if (arr[i] % 3 == 0) {
      printf("%d ", arr[i]);
    }
  }
  printf("\n");
}