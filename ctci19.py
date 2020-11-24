def main():
	s1 = "waterbottle"
	s2 = "erbottlewat"
	
	#first check if the length of those two are same
	if len(s1) == len(s2):
		s2_doubled =  s2 + s2 # be aware that this could take quadratic time. 

	print (s1 in s2_doubled)


main()
