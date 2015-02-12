#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int numero;
    char cadena[255];
    printf("Ingrese un numero:\n");
    scanf("%d", &numero);
    printf("ingrese su nombre:\n");
    fflush(stdin);
    scanf("%s", cadena);
    if(numero % 2 == 0) {
        printf("%s, ingresaste un valor par\n", cadena);
    } else {
        printf("%s, ingresaste un valor impar\n", cadena);
    }
    return 0;
}
