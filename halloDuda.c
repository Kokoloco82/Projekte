// halloDuda.c
/* 
    202205041117 antonius ehlen
    mein erstes kleines C Programm
*/

// importieren der Schnittstellendefinitionen zur Ein- und Ausgabe (auf den Bildschirm)
#include <stdio.h>

// Bennenen des Hauptproramms:
void main() {
    int a = 5, b = 7;
    //int b;
    //a = 5;
    //b = 7;
    printf("Hallo Duda in C!\n");
    if (a < b){
        printf("a ist kleiner als b\n");
    }
    else {
        printf("a ist GRÖßER als b\n");
    }
}

