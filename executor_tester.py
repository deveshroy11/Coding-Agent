from agent.executor import execute_cpp


code = """
#include <iostream>
using namespace std;

int main() {
    cout << 2 + 3;
    return 0;
}
"""

result = execute_cpp.invoke({"code": code})

print(result)