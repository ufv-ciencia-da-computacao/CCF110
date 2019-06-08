#include <stdio.h>

void result (double, double, char);

int main () {
  double num1, num2;
  char op;
  printf("(+) Soma\n(-) Subtracao\n(*) Multiplicacao\n(/) Divisao");
  scanf("%c", &op);
  printf("Digite 2 numeros: ");
  scanf("%lf %lf", &num1,&num2);
  return 0;
}

void result (double num1, double num2, char op) {
  switch (op) {
    case '+':
      printf("%lf\n", num1+num2);
      break;
    case '-':
      printf("%lf\n", num1-num2);
      break;
    case '*':
      printf("%lf\n", (num1*num2));
      break;
    case '/':
      printf("%lf\n", num1/num2);
      break;
    default:
      printf("Operacao nao compreendida\n");
      break;
  }
}

