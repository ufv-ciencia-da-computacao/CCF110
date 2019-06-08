#include <stdio.h>

double medAritmetica(double, double, double);

int main() {
  double num1, num2, num3;

  scanf("%lf %lf %lf", &num1, &num2, &num3);
  printf("%.2lf\n", medAritmetica(num1, num2, num3));

  return 0;
}

double medAritmetica(double num1, double num2, double num3) {
  return (num1+num2+num3)/3;
}