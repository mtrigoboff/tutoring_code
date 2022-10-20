line = 'This line, has punctuation.'
print(line)

def getWords(line):
	words = []
	for word in line.split():
		words.append(word.strip(',.'))

	#for i in range(0, len(lineSplit)):
	#	print(words[i])

	return words

wordsRet = getWords(line)
print(wordsRet)
