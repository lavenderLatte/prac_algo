'''
1.2 Permutation 

Assumptions
	1) case sensitive
	2) significant white spaces
'''

def arePermutations(s1, s2, charTally):
	# if permutations, they must be equal in length
	if len(s1) != len(s2):
		return False

	increment(s1, charTally)
	# return decrement(s2, charTally)
	result = decrement(s2, charTally)
	if result == False:
		return result

	# not permutations: less char in s2
	for char in charTally:
		if charTally[char] > 0:
			print("not permutations")
			return False

	return True


def increment(s, tally):
	# building dictionary from s1, O(N)
	for char in s:
		if char in tally:
			tally[char] += 1
		else:
			tally[char] = 1


def decrement(s, tally):
	# if permutations, all the values should become zero, O(N)
	for char in s:
		if char in tally:
			tally[char] -= 1
			# not permutations: extra char in s2
			if tally[char] < 0:
				print("not permutations")
				return False
		# not permutations: non-overlapping char exist in s2 
		else:
			print("not permutations")
			return False



def main():
	testcases = ['god ', 'dog', 'Dog ', 'dog ', 'GDO', 'dogg']
	dictionary = {}

	arePermutations(testcases[0], testcases[3], dictionary)
	print(dictionary)


main()

