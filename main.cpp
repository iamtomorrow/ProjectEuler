#include <iostream>

void GetSmallestPrimeFactor(int num);

int main( ) {
    std::cout << "Hello C++" << std::endl;

    GetSmallestPrimeFactor(10);
    std::cout << "Finished..." << std::endl;

    return 0;
}

void GetSmallestPrimeFactor(int num) {
    int factor = 0;
    for(int i = 0; i < num; i++) {
        if (num%i == 0) {
            factor = i;
        }
    }
    printf("FACTOR: ", factor);
}
