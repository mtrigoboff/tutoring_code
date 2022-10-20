#include <iostream>

using namespace std;

struct Student
{
	string		name;
	float		gpa;
	int			age;
};

int main()
{
	Student		s1;

	s1.name = "Albert";
	s1.gpa = 3.21;
	s1.age = 28;

	cout << s1.name << ' ' << s1.gpa << ' ' << s1.age << endl;

	return 0;
}
