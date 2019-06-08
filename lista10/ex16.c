#include <stdio.h>
#include <stdbool.h>
#define TAM 10

void bubbleSort(int*);

int main () {
  int arr[TAM] = {1, 2, 0, 30, -50, 3, 25, 100, 2, -5};
  bubbleSort(arr);

  for (int i = 0; i < TAM; i++) {
    printf("%d ", arr[i]);
  }

  printf("\n");
  
  return 0;
}

void bubbleSort(int *arr) {
  bool trocado;
  do {
    trocado = false;
    for (int i = 0; i < TAM-1; i++) {
      if (arr[i] > arr[i+1]) {
        int aux = arr[i];
        arr[i] = arr[i+1];
        arr[i+1] = aux;
        trocado = true;
      }
    }
  } while (trocado);
}