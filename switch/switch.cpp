#include <iostream>

using namespace std;

int main()
{
	int		n;

	cout << "> ";
	cin >> n;

	switch (n) {
		case 1:
			cout << "1 is OK" << endl;
			break;
		case 2:
			cout << "2 is OK" << endl;
			break;
		case 3:
			cout << "3 is OK" << endl;
			break;
		case 4:
			cout << "4 is OK" << endl;
			break;
		default:
			cout << "Wrong number!" << endl;
			break;
	}

	return 0;
}
