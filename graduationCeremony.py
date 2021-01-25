import time

def numberOfWaysToAttendClass(number):
    if number <0:
       print("invalid input.Please enter number positive number");exit();
    #dictionary for storing absent values on ceremony day   
    absentCeremony = dict()
    absentCeremony[0] = 0
    absentCeremony[1] = 1
    absentCeremony[2] = 2
    #below dictionary to store no of ways to attend class
    waysToAttendClass  = dict()
    waysToAttendClass[0] = 1
    waysToAttendClass[1] = 2
    waysToAttendClass[2] = 4
    for count in range(3,number+1):
        waysToAttendClass[count] = waysToAttendClass[count - 1] + waysToAttendClass[count - 2] + waysToAttendClass[count - 3]
        absentCeremony[count] = absentCeremony[count - 1] + absentCeremony[count - 2] + absentCeremony[count - 3]
        
    print(waysToAttendClass[number])
    print(str(absentCeremony[number])+'/'+str(waysToAttendClass[number]))
	


if __name__ == '__main__':
    inputNumber = int(input())
    start_time = time.time()	
    numberOfWaysToAttendClass(int(inputNumber))		
    print("total time Execution--- %s seconds ---" % (time.time() - start_time))