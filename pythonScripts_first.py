def returnBitNumber(number,limit):
	value = format(number,"b")
	noOfZeroToadd = limit-len(value)
	value = value.rjust(noOfZeroToadd+len(value),'0')
	return value
 	
def validCaseToAttendClass(value):
	if len(value) < 3:	
		return 1
	else:
		if value.count('000'):
			return 0
		else:
			return 1
def numberOfWaysToAttendClass(number):
	resultAttendCount = 0
	resultCountAttendCeremony = 0
	numberOfPossibleWays = (1<<number)
	
	for i in range(0,numberOfPossibleWays):	
        value = returnBitNumber(i,number)
        if validCaseToAttendClass(value):
            resultAttendCount +=1
            if int(value[-1]) == 1 :
                resultCountAttendCeremony +=1
	print(resultAttendCount)

	print(str(resultAttendCount-resultCountAttendCeremony)+'/'+str(resultAttendCount))


if __name__ == '__main__':
    inputNumber = int(input())
	
    numberOfWaysToAttendClass(int(inputNumber))		