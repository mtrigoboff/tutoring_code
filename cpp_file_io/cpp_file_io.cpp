#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream    in("test.txt");
    char        line[256];

    if (in) {
        cout << "opened file" << endl;
        while (in.getline(line, 256))
            cout << "'" << line << "'" << endl;
    }
    else
        cout << "could not open file" << endl;
}