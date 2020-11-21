'''
CTCI 1.8 

- don't change values until finding all the cells with zeros

- O(N*M), quadratic solution inevitably.

'''
def findZero(mtrx):
	row = []
	col = []
	i = 0
	for i in range(len(mtrx)): # len == # rows
		j = 0
		for j in range(len(mtrx[i])): # len == # cols
			if mtrx[i][j] == 0:
				row.append(i)
				col.append(j)
	return row, col


def setToZero(row, col, mtrx):

	for r in row:
		i = 0
		for i in range(len(mtrx[i])):
			mtrx[r][i] = 0
	# print("after row changes: ", mtrx)

	for c in col:
		i = 0
		for i in range(len(mtrx)):
			mtrx[i][c] = 0
	# print("after col chagnes: ", mtrx)

	return mtrx


def main():
	A = [[1, 4, 5, 12], [-5, 8, 9, 0], [-6, 0, 11, 19]]

	zeroLoc = findZero(A)
	result = setToZero(zeroLoc[0], zeroLoc[1], A)

	print(result)



main()






