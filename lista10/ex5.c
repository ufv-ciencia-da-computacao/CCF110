#include <stdio.h>

double fahrToCelsius(double);
double fahrToKelvin(double);
double celsiusToFahr(double);
double celsiusToKelvin(double);
double kelvinToCelsius(double);
double kelvinToFahr(double);

int main () {

  double num;
  int op;
  printf("(1) Fahrenheit para Celsius\n(2) Fahrenheit para Kelvin\n(3) Celsius para Fahrenheit\n(4) Celsius para Kelvin\n(5) Kelvin para Celsius\n(6) Kelvin para Fahrenheit\nDigite um numero: ");
  scanf("%d", &op);

  printf("Digite um número: ");
  scanf("%lf", &num);
  switch (op) {
    case 1:
      printf("%.2lf\n", fahrToCelsius(num));
      break;
    case 2:
      printf("%.2lf\n", fahrToKelvin(num));
      break;
    case 3:
      printf("%.2lf\n", celsiusToFahr(num));
      break;
    case 4:
      printf("%.2lf\n", celsiusToKelvin(num));
      break;
    case 5:
      printf("%.2lf\n", kelvinToCelsius(num));
      break;
    case 6:
      printf("%.2lf\n", kelvinToFahr(num));
      break; 
    default:
      printf("Numero invalido\n");
      break;
  }

  return 0;
}

double fahrToCelsius(double num) {
  return (num-32) * (5./9);
}

double fahrToKelvin(double num) {
  return (num-32) * (5./9) + 273.15;
}

double celsiusToFahr(double num) {
  return (num * (9./5)) + 32;
}

double celsiusToKelvin(double num) {
  return (num + 273.15);
}

double kelvinToCelsius(double num) {
  return (num - 273.15);
}

double kelvinToFahr(double num) {
  return ((num - 273.15) * 9./5) + 32;
}