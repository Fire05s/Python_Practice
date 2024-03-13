##import time,random
##l1 = []
##for loop in range (0,1000,1):
##    l1.append (random.randint (0,1000))
##index = 0
##search = random.randint (0,1000)
##print ('search number',search)
##def lin (l1,num):
##    global index
##    for loop in l1:
##        index += 1
##        if loop == num:
##            break
##start = time.time()
##lin (l1,search)
##end = time.time()
##print (start,end)
##seconds = end - start
##print ('linear',index,seconds)
##def bina (l1,num):
##    global start1,state
##    l1.sort ()
##    print (l1)
##    state = False
##    start1 = time.time()
##    minindex = 0
##    maxindex = len (l1) - 1
##    mid = int ((minindex + maxindex) / 2)
##    print (mid)
##    if l1 [mid] == num:
##        print ('binary',mid)
##    else:
##        while minindex <= maxindex:
##            mid = int ((minindex + maxindex) / 2)
##            if num > l1 [mid]:
##                minindex = mid + 1
##            elif num < l1 [mid]:
##                maxindex = mid - 1
##            if l1 [mid] == num:
##                print ('binary',mid)
##                state = True
##                break
##    print ('state',state)
##bina (l1,5)
##end1 = time.time()
##print (start,end)
##seconds1 = end1 - start1
##print (seconds1)

import random,time
l1 = ['bubsort','selsort','inssort']
a1 = random.choice (l1)
l1.remove (a1)
a2 = random.choice (l1)
numlist = [29,10,14,35,2,87,15]
def bubsort (numlist1):
    current = 0
    nextn = 0
    start1 = time.time ()
    for loop1 in range (0,len (numlist1)-1,1):
        for loop2 in range (0,len(numlist1)-1,1):
            current = numlist1 [loop2]
            nextn = numlist1 [loop2 + 1]
            if current > nextn:
                numlist1 [loop2],numlist1 [loop2 + 1] = nextn,current
    end1 = time.time ()
    seconds1 = end1 - start1
    print ('bubsort:',seconds1,numlist1)
def selsort (numlist1):
    minindex = 0
    smallestindex = 0
    smallestval = 0
    start1 = time.time ()
    for loop in range (minindex,len (numlist1) - 1,1):
        minindex = loop
        for loop1 in range (loop + 1,len (numlist1),1):
            if numlist1 [loop1] < numlist1 [minindex]:
                minindex = loop1
        if minindex != loop:
            numlist1 [loop], numlist1 [minindex] = numlist1 [minindex],numlist1 [loop]
    end1 = time.time ()
    seconds1 = end1 - start1
    print ('selsort:',seconds1,numlist1)
def inssort (numlist1):
    curindex = 0
    start1 = time.time ()
    for loop1 in range (1,len (numlist1),1): #bottom boundary
        done = False
        previouscompared = loop1
        currentcompared = loop1 - 1
        while done == False and currentcompared >= 0:
            if numlist1 [currentcompared] > numlist1 [previouscompared]:
                numlist1 [currentcompared],numlist1 [previouscompared] = numlist1 [previouscompared],numlist1 [currentcompared]
            else:
                done = True
            previouscompared -= 1
            currentcompared -= 1
    end1 = time.time ()
    seconds1 = end1 - start1
    print ('inssort:',seconds1,numlist1)
if a1 == 'bubsort' or a2 == 'bubsort':
    bubsort (numlist)
if a1 == 'selsort' or a2 == 'selsort':
    selsort (numlist)
if a1 == 'inssort' or a2 == 'inssort':
    inssort (numlist)
