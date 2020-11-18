'''
CTCI 1.6

(1) Construct freq cnt list: O(N)
(2) Create compressed str
	- Concatenate non-repeating char + str(freq) alternatively to compressed = '' --> Naive str appending takes O(N^2)!
	* Modified 
	- Append non-repeating char & str(freq) to compressed = [] --> O(M)+O(K) (where M: len(list1), K: # non-repeating char)
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

# # DEPRECATED: reason O(N^2)
# def strCompressor(testString, freqTally):
# 	compressed = ''
# 	stri = 0
# 	tallyi = 0
# 	while (stri < len(testString)):
# 		compressed += (testString[stri]) # Naive appending takes O(N^2)! 
# 		compressed += str(freqTally[tallyi])
# 		stri += freqTally[tallyi]
# 		tallyi += 1
		
# 		# 0 'a' + 2
# 		# 2 'b' + 1
# 		# 3 'c' + 5
# 		# 8 'a' + 3

# 	return compressed


def fasterStrCompressor(testString, freqTally):
	compressed = []
	stri = 0
	tallyi = 0
	while (stri < len(testString)):
		compressed.append(testString[stri])
		compressed.append(str(freqTally[tallyi]))
		stri += freqTally[tallyi]
		tallyi += 1

	return ''.join(compressed)



def main():
	testingSample = ['aabcccccaaa', 'abcd', 'abcaa', 'abcaaa', 'abcaaaaaa', 'abcaaabcaaa']
	testString = testingSample[1] 
	print ("TESTING:", testString)

	freqTally = freqCounter(testString)
	print(freqTally)

	compressed = fasterStrCompressor(testString, freqTally)
	# compressed = strCompressor(testString, freqTally)
	print(compressed, "length: ", len(compressed))

	# if compressed string would not become smaller than the original string, return original string
	if (len(compressed) >= len(testString)):
		result = testString
	else:
		result = compressed

	print(result)


main()





