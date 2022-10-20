#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* toUpper(char* low)
{
	int		lgth = strlen(low);
	char* up = malloc(lgth + 1);
	char* lowPtr = low;
	char* upPtr = up;

	if (!up)
		return NULL;

	while (*lowPtr != '\0')
		*upPtr++ = *lowPtr++ - 32;

	*upPtr = '\0';
	return up;
}

int main()
{
	char* low = "abc";
	char* up;

	up = toUpper(low);
	if (!up)
		return -1;

	printf("%s\n", up);
	free(up);

	return 0;
}
