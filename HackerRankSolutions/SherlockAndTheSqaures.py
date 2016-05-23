import math
import time

t = int(input().strip())

def isPS(i):
    squareroot = math.sqrt(i)
    if math.ceil(squareroot) == math.floor(squareroot):
        return True
    else:
        return False
       
def getInitPS(arr1,arrn):
    PS = 0
    for i in range(arr1, arrn+1):
        if (isPS(i)):
            PS = i
            break
    return PS
  
def getPrevPS(n):
    num = n-1
    while isPS(num) == False:
        num = num-1
    return num
    
def getNextPS(prevPS,firstPS):
    return firstPS + (firstPS - prevPS + 2)
   
# TIMING: Capture start time
start_time = time.time()   
    

for ti in range(t):
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    
    sumPS = 0
    
    ps1 = getInitPS(arr[0],arr[1])
         
    if ps1 != 0:
        ps0 = getPrevPS(ps1)
        sumPS = sumPS + 1
        psN = getNextPS(ps0,ps1)
        while(psN in range(ps1,arr[1]+1)):
            sumPS = sumPS + 1
            ps0 = ps1
            ps1 = psN
            psN = getNextPS(ps0,ps1)

    print(sumPS)

# TIMING: Return execution time
print("--- %s seconds ---" % (time.time() - start_time))
