'''
CTCI 1.4

Assumption Clearing Questions:
	1) case sensitive?
	2) significance of white spaces?
	3) significance of special char (.,?!)?

'''

def toLower(s):
	char = ''
	if ord(s) < 91:
		# upper-case -> lower-case
		char = chr(ord(s) + 32)
	else:
		char = s

	return char


def buildDict(sinput, dictionary):
	for s in sinput:
		char = toLower(s)
		if char in dictionary:
			dictionary[char] += 1
		else:
			dictionary[char] = 1

	return dictionary


def isPalindrome(dictionary, oddnum, evennum, sinput):
	'''
	Not palindrome when:
		1) even trueLen & having characters that occurs at odd num frequency
		2) odd trueLen & having characters that occurs at odd num frequency more than once
	'''

	trueLen = len(sinput) - dictionary['@']
	# to check whether palindrome, knowing num of whitespace is noise
	del dictionary['@']
	print(dictionary)

	for char in dictionary:
		if oddnum > 1:
			return False

		if dictionary[char] % 2 == 0:
			evennum += 1
		else:
			# when length of input string is even, having odd num of char won't make palindrome
			if trueLen % 2 == 0:
				return False
			else:
				oddnum += 1

	return True 


def main():
	inputSample = ['Tact Coa', 'Never odd or even', 'Stressed desserts', 'Stressed desserts ski' ]
	sinput = inputSample[3]
	sdict = {}
	oddnum = 0 # tally of char that occurs at odd frequency
	evennum = 0

	tally = buildDict(sinput, sdict)
	#print(tally)

	print(isPalindrome(tally, oddnum, evennum, sinput))



main()

