#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

void processCommand(uint8_t cmd) {
  char buffer[128];
  FILE* fin;
  
  switch(cmd) {
    case 0: // exit
      printf("Goodbye!\n");
      exit(0);
    case 1: // read public
      fin = fopen("/home/public.txt", "rt");
      fgets(buffer, sizeof(buffer), fin);
      fclose(fin);
      printf(buffer);
      break;
    case 2: // write public
      printf("Sorry, this has not been implemented yet.\n");
      break;       
    case 201: // read secret
      fin = fopen("/home/secret2.txt", "rt");
      fgets(buffer, sizeof(buffer), fin);
      fclose(fin);
      printf(buffer);
      break;
    case 202: // write secret
      printf("Sorry, this has not been implemented yet.\n");
      break;       
    default:
      printf("Unknown command: %d\n", cmd);
  }
}

void problem2() {
  char buffer[128];
  int command;  
  
  while (1) {
    printf("Select command:\n");
    gets(buffer);
    sscanf(buffer, "%d", &command);  
    if (command > 200)
      printf("You are not authorized to access this file!\n");
    else
      processCommand(command);   
  }    
}

int main() {
  printf("Available commands: \n 1 - read public file \n 2 - write public file \n 201 - read secret file \n 202 - write secret file \n 0 - exit \n");
  problem2();
}

