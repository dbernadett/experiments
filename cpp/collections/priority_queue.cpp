#include <iostream>
#include <string>
#include <queue>

using namespace std;

using q=priority_queue<int, vector<int>, greater<int> >;

int main(int argc, char* argv[]){
	q pq;
	pq.push(1);
	pq.push(5);
	pq.push(7);
	cout << pq.top() << endl;
	
}
