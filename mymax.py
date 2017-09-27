array = list()
num = raw_input("Enter how many elements you want:")
for i in range(int(num)):
	n = raw_input("num: ")
	array.append(int(n))
print "The max value of the array is ", max(array)
