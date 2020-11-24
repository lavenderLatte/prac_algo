'''
HackerRank: 2D Array - DS
Q: Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.


Assumption:
- The arr is always 6 x 6
- There are 16 hourglasses in arr. 
'''

def hourglassSum(arr):

	allSum = []
	initial = True

	hourglass = 0
	hgSum = 0
	for row in range(4):
		for col in range(4):
			# add three values from top row first
			hgSum += arr[row][col]
			hgSum += arr[row][col+1]
			hgSum += arr[row][col+2]
			# add middle 
			hgSum += arr[row+1][col+1]
			# add three from bottom row
			hgSum += arr[row+2][col]
			hgSum += arr[row+2][col+1]
			hgSum += arr[row+2][col+2]

			allSum.append(hgSum)

			if initial:
				maxSum = hgSum
				initial = False
			else:
				if hgSum > maxSum:
					maxSum = hgSum


			hgSum = 0
			hourglass += 1

			if hourglass >= 16:
				break
	return(maxSum)




def main():
	arr = [[-9,-9,-9,1,1,1],[0,-9,0,4,3,2],[-9,-9,-9,1,2,3],[0,0,8,6,6,0],[0,0,0,-2,0,0],[0,0,1,2,4,0]]

	print(hourglassSum(arr))

main()

