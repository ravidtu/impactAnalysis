import time

def numberOfWaysToAttendClass(number):
    attendCeremony = dict()
    attendCeremony[0] = 1
    attendCeremony[1] = 1
    attendCeremony[2] = 3
    attendCeremony[3] = 7
    attendCeremony[4] = 13
    attendCeremony[5] = 24  #series start from here
    for count in range(6,number+1):
        attendCeremony[count] = attendCeremony[count-1] + attendCeremony[count-2] + attendCeremony[count-3]

    print(attendCeremony[number])
    print(str(attendCeremony[number]-attendCeremony[number-1])+'/'+str(attendCeremony[number]))
	


if __name__ == '__main__':
    inputNumber = int(input())
    start_time = time.time()	
    numberOfWaysToAttendClass(int(inputNumber))		
    print("total time Execution--- %s seconds ---" % (time.time() - start_time))