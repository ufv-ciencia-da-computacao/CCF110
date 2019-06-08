#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <regex.h>

bool isValidCPF(char[]); 

int main() {
  char userCpf[11];
  bool isValid;
  printf("Digite seu CPF sem pontos: ");
  scanf("%s", userCpf);
  printf(isValidCPF(userCpf) ? "E Valido\n": "Nao E Valido\n");
  
  return 0;
}

bool isValidCPF(char cpf[11]) {
  int cpfInt[11];
  int weight[10] = {11, 10, 9, 8, 7, 6, 5, 4, 3, 2};
  int sum = 0; 
  
  for (int i = 0; cpf[i] != '\0'; i++) cpfInt[i] = cpf[i] - 48;

  for (int i = 0, j = 1; i < 8, j < 10; i++, j++) sum += cpfInt[i] * weight[j];

  if (sum % 11 < 2 && cpfInt[9] != 0 || cpfInt[9] != (11 - sum % 11)) {
    return false;
  }
  
  sum=0;

  for (int i = 0; i < 10; i++) sum += cpfInt[i] * weight[i];

  if (sum % 11 < 2 && cpfInt[10] != 0 || cpfInt[10] != (11 - sum % 11)) {
    return false;
  }

  return true;
}