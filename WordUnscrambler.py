'''
	Word unscrambler by Riley Knybel

	The actual algorithm is in the unscramble function. It takes a scrambled word string and a list of words and
	outputs a list of unscrambled words that match the length and number of characters.

	Paired with words.txt from https://github.com/dwyl/english-words/
'''

print("Word Unscrambler\nLoading word list...")

with open("words.txt") as wordFile:
	wordList = wordFile.readlines()

#remove the newline character from each word in the list
for line in range(0, len(wordList)):
	if wordList[line].endswith("\n"):
		wordList[line] = wordList[line][:-1].lower()

print("Done loading {} words.".format(len(wordList)))

#unscrambler algorithm:
def unscramble(scrambledWord, wordList):

	#For each word in a ~400k word list, 
	#see if it's the same length as the input 
	#and check if each character in the input 
	#appears in the word the same number of times

	scrambledWord = scrambledWord.lower()
	wordNotFound = True
	results = []

	for word in wordList: #for every word in the dictionary...
		wordNotFound = False

		if len(word) == len(scrambledWord):
			for character in word:
				if word.count(character) != scrambledWord.count(character):
					wordNotFound = True
					break
				elif scrambledWord.count(character) == 0:
					wordNotFound = True
					break
		else:
			wordNotFound = True	

		if wordNotFound == False:
			results.append(word)

	return results

while True:
	sw = input("Type in a scrambled word:")

	resultsList = unscramble(sw, wordList)
	
	#Print result(s) if there are any, otherwise say that there were none
	if len(resultsList) > 0:
		print("Results: ", end="")
		for result in resultsList:
			print(result, ", ", end="", sep="")
		print("")
	else:
		print("There were no results for that scrambled word.")