'''
1.1 is unique 


Improve: 
	(1) memeory in place solution (like sorting)
	
	(2) using dict.keys() will create a list of all the keys -- slow!
		SOLVED: if char in dictionary (instead of if char in dictionary.keys():)
'''

def isUnique(string, dictionary):
	# create dictionary while iterate through the string
	for char in string:
		#if already exist in dict, duplication found
		if char in dictionary: 
			return False
		else:
			dictionary[char] = 1	

	return True


def main():
	s = 'exampleString'
	sdict = {}

	print(isUnique(s, sdict))
	print(sdict)


main()