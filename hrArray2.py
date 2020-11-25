'''
Arrays: Left Rotation

a : array of int
d: size of left rotation
'''
def rotLeft(a, d):
	# non an in-place solution, creating extra N space
	rotated = a[d:len(a)] + a[0:d] 
	return rotated



def main():
	# a = [1, 2, 3, 4, 5]
	# d = 4

	d = 13
	a = [33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97]

	rotated = rotLeft(a, d)
	# cast each into str and then use join function
	result = " ".join(map(str, rotated))
	print(result)


main()
