'''
CTCI 1.5

O(N) + O(M) running time.
In-place solution.
'''

# DEPRECATED 
# def dictContructor(string):
# 	dictionary = {}

# 	for char in string:
# 		if char in dictionary:
# 			dictionary[char] += 1
# 		else:
# 			dictionary[char] = 1


def isOneReplace(s1, s2):
	diffChar = 0
	for i in range(len(s1)):
		if (s1[i] != s2[i]):
			diffChar += 1

	return (diffChar == 1)


def isOneRmvInsert(longer, shorter, lenLong, lenShort):
	i = 0 
	j = 0
	diffChar = 0
	while ((i < lenLong) and (j < lenShort)):
		if longer[i] == shorter[j]:
			i += 1
			j += 1
		else:
			i += 1
			diffChar += 1

	return (diffChar == 1)


def main():

	testSample = ['apple', 'aple', 'a', 'e', 'able']
	s1 = testSample[4]
	s2 = testSample[0]

	LEN1 = len(s1)
	LEN2 = len(s2)

	# length wise, one edit difference means 
	# same length or one length difference 
	# otherwise, two strings can't be one edit away
	if (LEN1 == LEN2):
		print("same len: ", isOneReplace(s1, s2))
		return isOneReplace(s1, s2)
	elif (len(s1)-1 == len(s2)):
		print("first longer: ", isOneRmvInsert(s1, s2, LEN1, LEN2))
		return isOneRmvInsert(s1, s2, LEN1, LEN2)
	elif (len(s1)+1 == len(s2)):
		print("second longer: ", isOneRmvInsert(s2, s1, LEN2, LEN1))
		return isOneRmvInsert(s2, s1, LEN2, LEN1)
	else:
		print ("nope")
		return False

main()



