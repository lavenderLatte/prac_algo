'''
1.3 URLify

input: "Mr John Smith     ", 13
output: "Mr%20John%20Smith"
'''

s = "Mr John Smith     "
trueLen = 13
snew = ''

for i in range(trueLen):
	if s[i] == ' ':
		snew += '%20'
	else:
		snew += s[i]

print(snew)
