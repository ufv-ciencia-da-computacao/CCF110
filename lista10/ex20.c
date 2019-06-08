#include <stdio.h>
#define TAM 20

double squareSum(double*);

int main() {
  double arr[TAM];
  for (int i = 0; i < TAM; i++) {
    scanf("%lf", &arr[i]);
  }

  printf("%lf\n", squareSum(arr));
  
  return 0;
}

double squareSum(double* arr) {
  double sum=0;

  for (int i = 0; i < TAM; i++) {
    sum += arr[i]*arr[i];
  }
  return sum;
}