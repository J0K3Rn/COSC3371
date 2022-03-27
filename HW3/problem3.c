#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

void safe_gets(char *buffer, int size) {
  char *temp_buffer = malloc(65536);
  int8_t length;

  do {
    printf("[less than %d characters]: ", size);
    gets(temp_buffer);
    length = strlen(temp_buffer);
  } while (length >= size);
  
  strcpy(buffer, temp_buffer);
  free(temp_buffer);
}  

void problem3() {
  char command[12];
  char dataset[12];
  char buffer[256];
  char *filename;
  
  printf("Enter dataset name (secret or public):\n");
  gets(dataset);
  
  switch(dataset[0]) {
    case 's':
      printf("You are not authorized to use this dataset!\n");
      return;
    case 'p':
      printf("Access granted to the public dataset!\n");
      break;
    default:
      printf("Unknown dataset!\n");
      return;
  }
    
  while (1) {
    printf("Enter command (read, write, or exit):\n");
    safe_gets(command, 12);
    
    switch(command[0]) {
      case 'r': // read
        switch(dataset[0]) {
          case 's':
            filename = "/home/secret3.txt";
            break;
          case 'p':
            filename = "/home/public.txt";
            break;
        }
        FILE* fin = fopen(filename, "rt");
        fgets(buffer, sizeof(buffer), fin);
        fclose(fin);
        printf(buffer);
        break;
        
      case 'w': // write
        printf("Sorry, this has not been implemented yet.\n");
        break;       
         
      case 'e': // exit
        printf("Goodbye!\n");
        return;
   
      default:
        printf("Unknown command!\n");
    }       
  }    
}

int main() {
  problem3();
}

