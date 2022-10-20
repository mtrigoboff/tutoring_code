class Employee:
	def __init__(self, name):
		self.name = name
		self.nHours = None

	def print(self):   
		print(f'name = {self.name}')
		print(f'hours = {self.nHours}')

class Receptionist(Employee):
	def __init__(self, name, typingSpeed):
		super().__init__(name)
		self.nHours = 40
		self.typingSpeed = typingSpeed

	def print(self):
		print('Receptionist')
		super().print()
		print(f'typing speed = {self.typingSpeed} words per minute')

class Programmer(Employee):
	def __init__(self, name, language):
		super().__init__(name)
		self.language = language

	def print(self):
		print(f'{self.language} Programmer')
		super().print()

class PythonProgrammer(Programmer):
	def __init__(self, name):
		super().__init__(name, 'Python')
		self.nHours = 60

class CProgrammer(Programmer):
	def __init__(self, name):
		super().__init__(name, 'C')
		self.nHours = 50

class JavaScriptProgrammer(Programmer):
	def __init__(self, name):
		super().__init__(name, 'JavaScript')
		self.nHours = 40

anna = Receptionist('Anna', 50)
anna.print()
print()

robert = CProgrammer('Robert')
robert.print()
print()

michael = PythonProgrammer('Michael')
michael.print()
print()

jane = JavaScriptProgrammer('Jane')
jane.print()
print()

