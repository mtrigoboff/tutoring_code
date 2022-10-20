#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* rev(char* str)
{
	int		right = strlen(str) - 1;
	char	temp;

	for (int left = 0; left < right; left++, right--) {
		temp = str[left];
		str[left] = str[right];
		str[right] = temp;
	}
	return str;
}

int main(int argc, char** argv)
{
	if (argc > 1)
		printf("%s\n", rev(argv[1]));
	else
		printf("call with one string argument\n");

	return 0;
}
