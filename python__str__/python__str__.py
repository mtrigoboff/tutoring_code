class Student:
	def __init__(self, name, gpa):
		self.name = name
		self.gpa = gpa

	def __str__(self):
		return f'student: {self.name}, {self.gpa}'

bob = Student('Bob', 3.12)
mary = Student('Mary', 2.83)

print(bob)
print(mary)
print()