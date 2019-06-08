#include <stdio.h>

void defTraingle(double, double, double);

int main() {
  double L1, L2, L3;
  scanf("%lf %lf %lf", &L1, &L2, &L3);
  defTraingle(L1, L2, L3);
  return 0;
}

void defTraingle(double L1, double L2, double L3) {
  if (L1 == L2 && L2 == L3) {
    printf("Equilatero\n");
  } else if (L1 == L2 || L1 == L3 || L2 == L3){
    printf("Isosceles\n");
  } else {
    printf("Escaleno\n");
  }
  
  
}