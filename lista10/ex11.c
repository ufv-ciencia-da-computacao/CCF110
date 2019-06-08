#include <stdio.h>

double triangleArea(double, double , double);

int main () {
  double L1, L2, L3;
  scanf("%lf %lf %lf", &L1, &L2, &L3);
  printf("Triangle Area: %lf\n", triangleArea(L1, L2, L3));
  return 0;
}

double triangleArea (double L1, double L2, double L3) {
  return (L1+L2+L3)/2;
}

