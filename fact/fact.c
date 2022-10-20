#include <stdio.h>

int factR(int n)
{
	if (n == 1)
		return 1;
	else
		return n * factR(n - 1);
}

int factI(int n)
{
	int		f = 1;

	for (int i = n; i > 1; i--)
		f *= i;

	return f;
}

int main()
{
	printf("%d\n", factR(5));
	printf("%d\n", factI(5));
}
