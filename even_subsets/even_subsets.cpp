#include <iostream>
#include <string>

using namespace std;

void generateEvenSubsetR(unsigned int index, string subset, string s)
{
	if (index == s.size() && subset.size() % 2 == 0)
		cout << (subset.size() == 0 ? "-- empty set --" : subset) << endl;
	if (index == s.size())
		return;
	generateEvenSubsetR(index + 1, subset, s);
	generateEvenSubsetR(index + 1, subset + s[index], s);
}

void generateEvenSubset(string s)
{
	generateEvenSubsetR(0, "", s);
}

int main()
{
	generateEvenSubset("ABCDEF");
}
