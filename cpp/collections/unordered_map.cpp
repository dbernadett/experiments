#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

namespace bob {
	class Person {
	public:
		Person(){};
		Person(string Name):name(Name){};
		string get_name(){
			return this->name;
		}
	private:
		string name;
	};

};

int main(int argc, char* argv[]) {
	auto hi = bob::Person("Hi");
	unordered_map<int, bob::Person> person_map;
	person_map[1] = hi;
	cout << person_map[1].get_name() << endl;
	string test = "Howdy!";
	cout << test[2] << " " << test.size() << endl;

}
