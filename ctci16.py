'''
CTCI 1.6

construct freq cnt list: O(N) 
create compressed str: O(M) * 2 (where M is size of freq cnt list)
'''

# NOT A WORKING SOLUTION
# while i in range(len(s)):
# 	# already exist and 
# 	if s[i] == newstr[charPointer]:
# 		cnt += 1
# 		newstr[freqPointer] = cnt # update the freq --> since string is immutable, this won't work!!!!
# 	# new entry
# 	else:
# 		newstr.append(char)
# 		charPointer += 2
# 		cnt += 1
# 		newstr.append(cnt)
# 		freqPointer += 2
# 	i += 1



def freqCounter(s):
	charFreq = []
	freqPointer = -1
	oldChar = ''
	i = 0

	while (i < len(s)):
		newChar = s[i]
		print(newChar)
		# update
		if oldChar == newChar: 
			charFreq[freqPointer] += 1
		# add new
		else:
			oldChar = newChar
			charFreq.append(1)
			freqPointer += 1

		i += 1

	return charFreq


def strCompressor(testString, freqTally):
	compressed = ''
	stri = 0
	tallyi = 0
	while (stri < len(testString)):
		compressed += (testString[stri])
		compressed += str(freqTally[tallyi])
		stri += freqTally[tallyi]
		tallyi += 1
		
		# 0 'a' + 2
		# 2 'b' + 1
		# 3 'c' + 5
		# 8 'a' + 3

	return compressed



def main():
	testingSample = ['aabcccccaaa', 'abcd', 'abcaa', 'abcaaa', 'abcaaaaaa', 'abcaaabcaaa']
	testString = testingSample[5] 
	print ("TESTING:", testString)

	freqTally = freqCounter(testString)
	print(freqTally)

	compressed = strCompressor(testString, freqTally)
	print(compressed, len(compressed))

	# if compressed string would not become smaller than the original string, return original string
	if (len(compressed) >= len(testString)):
		result = testString
	else:
		result = compressed

	print(result)


main()





