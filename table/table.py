# in the format specifiers:
#    < means left justify
#    ^ means center
#    > means right justify

hdrs = [['track',			'price',		'currency',		'total',	'rating'],
		['-----',			'-----',		'--------',		'-----',	'------']
	   ]
table = [['Facebook',		0.0,			'USD',			2974676,	3.5],
		 ['Instagram',		0.0,			'USD',			2161558,	4.5],
		 ['Clash of Clans',	0.0,			'USD',			2130805,	4.5],
		 ['Fruit Ninja',	1.99,			'USD',			698516,		4.5]
		]

for hdr in hdrs:
	print(f'{hdr[0]:16s}{hdr[1]:>11s}{hdr[2]:^14s}{hdr[3]:>8s}{hdr[4]:>10s}')
for row in table:
	print(f'{row[0]:16s}{row[1]:11.2f}{row[2]:^14s}{row[3]:8d}{row[4]:10.1f}')

print()
