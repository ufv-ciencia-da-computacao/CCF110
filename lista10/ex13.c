#include <stdio.h>
#include <math.h>

double modulusDistanceXYZ(double x, double y, double z);

int main () {
  double x1, x2;
  double y1, y2;
  double z1, z2;

  printf("Digite para x:\n");
  scanf("%lf %ld", &x1, &x2);
  printf("Digite para y:\n");
  scanf("%lf %ld", &y1, &y2);
  printf("Digite para z:\n");
  scanf("%lf %ld", &z1, &z2);

  printf("%lf\n", modulusDistanceXYZ(x2-x1, y2-y1, z2-z1));

  return 0;
}

double modulusDistanceXYZ(double x, double y, double z) {
  return sqrt(pow(x, 2) + pow(y,2) + pow(z, 2));
}
