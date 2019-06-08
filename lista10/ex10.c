#include <stdio.h>

double meterToInches(double);
double inchesToFt(double);

int main () {
  int op;
  double meters;
  printf("(1) Metro para Polegada\n(2) Metro para Pés\n");
  scanf("%d", &op);
  printf("Digite um numero: ");
  scanf("%lf", &meters);

  switch (op) {
    case 1:
      printf("%.3lf\n", meterToInches(meters));
      break;
    case 2:
      printf("%.3lf\n", inchesToFt(meterToInches(meters)));
    default:
      break;
  }
  return 0;
}

double meterToInches(double meters) {
  return meters * 39.37;
}

double inchesToFt(double inches) {
  return inches/12;
}