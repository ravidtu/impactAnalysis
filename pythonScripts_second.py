import time
def isLastBitSet(n): 
    if n & (1 << 0): 
        return 1 
    else: 
        return 0     

def countConsecutiveZero(number,fixedLength):
    count = 0
    temp = number
    bitLeangth = number.bit_length()
    if ((fixedLength - bitLeangth) >= 3):
        return 1
    while(number != 0):
        if(number%2 == 0):  
            count +=1
            if count >= 3:
                #print(temp)
                return 1
        else:
        	count =0
        number=int(number/2)
    return 0
    
def numberOfWaysToAttendClass(number):
    resultAttendCount = 0
    resultCountAttendCeremony = 0
    numberOfPossibleWays = pow(2,number)
    for i in range(1,numberOfPossibleWays):
        if(not countConsecutiveZero(int(i),number)): #return 0 if consecutive 0 is not found else return 1
            resultAttendCount +=1
            if(isLastBitSet(i)):
                resultCountAttendCeremony +=1
    print(resultAttendCount)
    #print(resultCountAttendCeremony)
    print(str(resultAttendCount-resultCountAttendCeremony)+'/'+str(resultAttendCount))
	


if __name__ == '__main__':
    inputNumber = int(input())
    start_time = time.time()
    numberOfWaysToAttendClass(int(inputNumber))
    print("total time Execution--- %s seconds ---" % (time.time() - start_time))