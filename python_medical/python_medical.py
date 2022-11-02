class Disease:
	
	# constructor
	def __init__(self, name):
		self.name = name
		self.score = 0

	def __str__(self):
		return f'Disease: {self.name}: score = {self.score}'

class Symptom:

	# constructor
	def __init__(self, name, diseases):
		self.name = name
		self.diseases = diseases

	def __str__(self):
		return f'Symptom: {self.name}'

hbp = Symptom('high blood pressure', {Disease('stroke'):45,Disease('heart attack'):15})

stroke = Disease('stroke')
heart_attack = Disease('heart attack')

print(hbp)
print(stroke)
print(heart_attack)

