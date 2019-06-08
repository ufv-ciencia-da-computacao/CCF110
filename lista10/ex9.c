#include <stdio.h>
#include <stdlib.h>

#define TAM_LIN 10
#define TAM_COL 5

void reprovaAprova(int *notas[]);

int main() {
  int notas[TAM_LIN][TAM_COL];
  for (int i = 0; i < TAM_LIN; i++) {
    for (int j = 0; j < TAM_COL; j++) {
      scanf("%d", notas[i][j]);
    }
  }

  reprovaAprova(notas);
  
  return 0;
}

void reprovaAprova(int *notas[]) {
  int soma = 0;
  for (int i = 0; i < TAM_LIN; i++) {
    for (int j = 0; j < TAM_COL; j++) {
      soma += notas[i][j];
      if (soma / TAM_LIN < 60) {
        printf("Reprovado\n");
      } else {
        printf("Aprovado\n");
      }
    }
  }
}