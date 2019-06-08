#include <stdio.h>
#include <stdlib.h>
#define TAM 6

int *changingMoney(double, double[]);

int main () {
  double change[TAM] = {0.5, 0.20, 0.10, 0.05, 0.02, 0.01};
  double received;
  double price;
  int *result;

  scanf("%lf %lf", &received, &price);
  result = changingMoney(received - price+0.001, change);
  
  for (int i = 0; i < TAM; i++) {
    printf("%d moeda(s) de %.2lf\n", result[i], change[i]);
  }
  
  return 0;
}

int *changingMoney(double num, double change[]) {
  int *changeResult = (int*) calloc(0, TAM * sizeof(int));
  int i=0;
  while (i < TAM) {
    changeResult[i] = (int)(num/change[i]);
    num -= changeResult[i] * change[i];
    i++;
  }
  return changeResult;
}