#include <stdio.h>

int isPositiveNegative(int);

int main() {
  int num;
  scanf("%d", &num);
  printf(isPositiveNegative(num) != 1 ? "Negativo\n":"Positivo\n");
  return 0;
}

int isPositiveNegative(int num){
  return num < 0  ? 0 : 1;
}