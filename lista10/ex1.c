#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct eq2grau {
  float a, b, c, x1, x2, delta;
};
typedef struct eq2grau Eq2Grau;

Eq2Grau solveEq2Grau(Eq2Grau);

int main () {
  Eq2Grau equacao;

  scanf("%f %f %f", &equacao.a, &equacao.b, &equacao.c);
  equacao = solveEq2Grau(equacao);

  printf("Delta: %f\nRaízes: (x1)= %f (x2)= %f\n", equacao.delta, equacao.x1, equacao.x2);

  return 0;
}

Eq2Grau solveEq2Grau(Eq2Grau eq) {
  eq.delta = ((eq.b*eq.b) - (4*eq.a*eq.c));
  eq.x1 = (((-1 * eq.b) + sqrt(eq.delta))/(2*eq.a));
  eq.x2 = (((-1 * eq.b) - sqrt(eq.delta))/(2*eq.a));

  return eq;
}