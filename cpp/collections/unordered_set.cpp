#include <string>
#include <unordered_set>
#include <iostream>

using namespace std;
int main(int argc, char* argv[]){
	unordered_set<string> us;
	us.insert("Hello world");
	us.erase("Hello world");
	cout << (us.end() == us.find("Hello world")) << endl;
	cout << us.empty() << endl;
}
