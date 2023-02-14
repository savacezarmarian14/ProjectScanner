#include <stdio.h>
#include <pthread.h>

int a = 0;

void *Add1(void *arg) {
    a = a + 1;
    pthread_exit(NULL);
}

void *Add2(void *arg) {
    a = a + 2;
    pthread_exit(NULL);
}

void *Add3(void *arg) {
    a = a + 3;
    pthread_exit(NULL);
}

void *Add4(void *arg) {
    a = a + 4;
    pthread_exit(NULL);
}

void *Add5(void *arg) {
    a = a + 5;
    pthread_exit(NULL);
}

void *Add6(void *arg) {
    a = a + 6;
    pthread_exit(NULL);
}

void *Add7(void *arg) {
    a = a + 7;
    pthread_exit(NULL);
}

void *Add8(void *arg) {
    a = a + 8;
    pthread_exit(NULL);
}

void *Add9(void *arg) {
    a = a + 9;
    pthread_exit(NULL);
}

void *Add10(void *arg) {
    a = a + 10;
    pthread_exit(NULL);
}

int main(int argc, char *argv[]) {
    return 0;
}
