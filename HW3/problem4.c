#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

void problem4() {
  FILE *fin;
  char *input;
  uint64_t length = 256;
  char *secret;

  secret = malloc(length);
  fin = fopen("/home/secret4.txt", "rt");
  fgets(secret, length, fin);
  fclose(fin);

  printf("Please enter your guess:\n");
  input = malloc(length);
  gets(input);
  if (strcmp(secret, input) == 0)
    printf("Congratulations, you have guessed the secret!\n");
  else {
    printf("Your guess was ");
    printf(input);
    printf("\n");
  }
}

int main() {
  problem4();
}

