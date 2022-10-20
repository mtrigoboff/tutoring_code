int main()
{
	int		init_ia2[3][2] = { {1, 2}, {3, 4}, {5, 6} };
	int		ia2[3][2];
	int		n = 1;

	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 2; j++)
			ia2[i][j] = n++;
	return 0;

}
