#include <iostream>
#include <cmath>

int main(int argc, char* argv[]){
	std::cout << static_cast<float>(1)/3 << std::endl;
	int top = std::ceil(float(1)/3);
	std::cout << top << std::endl;
	std::cout << static_cast<float>(1)/3 << std::endl;
}
