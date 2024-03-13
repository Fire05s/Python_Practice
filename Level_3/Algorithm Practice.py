##def linearsearch (inlist,wanted):
##    for loop in inlist:
##        if loop == wanted:
##            print (inlist [loop])
##l1 = [1,235,6,7,7,8,2,43,9,5]
##var1 = 2
##linearsearch (l1,var1)

##def binarysearch (inlist,wanted):
##    found = False
##    maxl1 = len (l1)
##    mid = (0 + maxl1)//2
##    while found == False:
##        if l1 [mid] == var1:
##            found = True
##        elif mid < var1:
##            mid += 1
##        elif mid > var1:
##            mid -= 1
##        print (mid)
##l1 = [1,235,6,7,7,8,2,43,9,5]
##l1.sort ()
##var1 = 43
##binarysearch (l1,var1)

##def bubsort (inlist):
##    changed = False
##    swapped = True
##    while swapped == True:
##        for loop in range (len (inlist) - 1):
##            if loop != len (inlist) - 1:
##                prev = inlist [loop]
##                after = inlist [loop + 1]
##                if prev > after:
##                    inlist [loop + 1] = prev
##                    inlist [loop] = after
##                    print (inlist)
##                    changed = True
##        if changed == False:
##            swapped = False
##            print ('final list:',inlist)
##        else:
##            changed = False
##            print ('has swapped; list after one iteration:',inlist)
##l1 = [1,235,6,7,7,8,2,43,9,5]
##bubsort (l1)

##def selsort (inlist):
##    minindex = 0
##    smallestindex = 0
##    smallestval = 0
#Wrong:
##    while minindex < len (inlist) - 1:
##        for loop in range (minindex,len (inlist) - 1,1):
##            if loop != len (inlist) - 1:
##                if inlist [loop] < inlist [loop + 1]:
##                    smallestindex = loop
##                    smallestval = inlist [loop]
##        if smallestval < inlist [minindex]:
##            inlist [smallestindex], inlist [minindex] = inlist [minindex], inlist [smallestindex]
##            print ('list after one iteration:',inlist)
##        minindex += 1

##    for loop in range (minindex,len (inlist) - 1,1):
##        minindex = loop
##        for loop1 in range (loop + 1,len (inlist),1):
##            if inlist [loop1] < inlist [minindex]:
##                minindex = loop1
##        if minindex != loop:
##            inlist [loop], inlist [minindex] = inlist [minindex],inlist [loop]
##        print ('list after one iteration:',inlist)
##l1 = [1,235,6,7,7,8,2,43,9,5]
##selsort (l1)

def inssort (inlist):
    curindex = 1
    for loop in range (curindex,len (inlist),1):
        curvalue = inlist [curindex]
        previndex = loop
        print ('one iteration previndex:',previndex)
        cond = True
##        previndex = loop - 1
##        while inlist [previndex] > inlist [previndex + 1]:
##            inlist [previndex], inlist [previndex + 1] = inlist [previndex + 1],inlist [previndex]
##            previndex -= 1

        while cond == True:
            previndex -= 1
            print (previndex)
            #prevvalue = inlist [previndex]
            if previndex > 0:
                if inlist [previndex] > inlist [previndex + 1]:
                    cond = False
                elif inlist [previndex] < inlist [previndex + 1]:
                    inlist [previndex], inlist [previndex - 1] = inlist [previndex - 1],inlist [previndex]
                    print ('swap: ',inlist)
            else:
                cond = False
        print ('list after one iteration:',inlist)
l1 = [1,235,6,7,7,8,2,43,9,5]
inssort (l1)

#Recursion
##def factorial(n):
##    if n == 1: #This is the base case
##        return 1  #when this condition holds true tells the program to stop and return all the values in sequential order.
##    return n * factorial(n-1)
##n = int(input("Number? "))
##print(factorial(n))

##def sumdigits (n):
##    ones = n % 10
##    tens = (n % 100) // 10
##    hundreds = (n % 1000) // 100
##    print (ones,tens,hundreds)
##    return ones + tens + hundreds

##    nsum = 0
##    for loop in str (n):
##        nsum = nsum + int (loop)
##    while n != 0:
##        nsum = nsum + n % 10
##        n = n // 10

##    if n // 10 == 0:
##        return n
##    return n % 10 + sumdigits (n // 10)
##n = int (input ('Number - '))
##print (sumdigits (n))

##def reverse (s):
##    if s == '':
##        return ''
##    return s[-1] + reverse (s [0:-1])
##s = input ('String - ')
##print (reverse (s))

##def highdivisor (n1,n2):
##    if n2 % n1 == 0:
##        return n1
##    return highdivisor (n2 % n1,n1)

##    if n2 % n1 == 0:
##        return n1
##    return highdivisor (

##    cond = True
##    highdiv = 1
##    if n1 > n2:
##        larger = n1
##        smaller = n2
##    else:
##        smaller = n1
##        larger = n2
##    for loop in range (1,smaller + 1,1):
##        print (smaller,larger)
##        if larger % loop == 0 and smaller % loop == 0:
##            highdiv = loop
##    return highdiv
##n1 = int (input ('Num1 - '))
##n2 = int (input ('Num2 - '))
##print (highdivisor (n1,n2))

##def prime (n,step):
##    print (n,step)
##    if step == n:
##        return prime (n,step - 1)
##    elif step != 1:
##        if n % step == 0:
##            return 'not prime'
##        return prime (n,step - 1)
##    elif step == 1:
##        return 'prime'
##n = int (input ('Num - '))
##print (prime (n,n))

##def fibonacci (n):
##    if n == 1:
##        return 0
##    elif n == 2:
##        return 1
##    return fibonacci (n-1) + fibonacci (n-2)
##num = int (input ('Num - '))
##print (fibonacci (num))

##def pascal (layer):
##    while len (layer) <= 10:
##        print (layer)
##        newl = []
##        for loop in range (1,len (layer),1):
##            newl.append (layer [loop] + layer [loop - 1])
##        newl = [1] + newl + [1]
##        pascal (newl)
##print (1)
##pascal ([1,1])
