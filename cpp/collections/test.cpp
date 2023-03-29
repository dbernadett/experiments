#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <unordered_set>
#include <unordered_map>
using namespace std;

struct ST {
    int x;
    int y;
    size_t operator()(const ST& st) const noexcept {
        size_t hash = st.x + 10 * st.y;
        return hash;
    };
};

namespace std {
    template<> struct hash<ST>
    {
        std::size_t operator()(const ST& p) const noexcept
        {
            return p(p);
        }
    };
}

void printstr(const string & s){
    cout << s << endl;
}


int main(int argv, char* args[]){
    pair<int, int> p({3,2});
    cout << p.first << endl;
    unordered_set<ST> up;
    unordered_set<string> uss;
    unordered_map<string, string> um{{"k", "v"}};
    cout << um["c"] << endl;

    string hello_world = "Hello World";
    const string bob = "god aweful";
    vector<int> gmap{ 10, 20, 5, 2, 3, 7 };
    priority_queue<int, vector<int>, greater<int>> pg = priority_queue<int, vector<int>, greater<int>>();
    for (int i = 0; i < gmap.size(); i++){
        pg.push(gmap[i]);
    }
    int a = pg.top();
    cout << a << endl;

    printstr(bob);
    cout << hello_world << endl;
}