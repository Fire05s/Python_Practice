import random,time
l1 = []
for loop in range (0,10,1):
    l1.append (random.randint (1,100))

##l1.sort ()
##minn = 0
##maxx = 1000
##search = 50
##found = False
##repeat = 0
##print (l1)
##while not found:
##    try:
##        half = (minn + maxx) // 2
##        if search < l1 [half]:
##            maxx = half - 1
##        elif search == l1 [half]:
##            found = True
##            print ('found')
##        elif search > l1 [half]:
##            minn = half + 1
##        print (l1[half],'; index =',half)
##    except:
##        found = True
##        print ('not found')

##start = time.time ()
##for loop in range (0,len (l1),1):
##    for loop1 in range (loop,len (l1),1):
##        if l1 [loop1] < l1 [loop]:
##            l1[loop1],l1[loop] = l1[loop],l1[loop1]
####    print (l1)
##end = time.time ()
##total = end - start
##print (l1,total)

start = time.time ()
current = 0
print ('start',l1)
for loop in range (1,len (l1),1):
##    current = l1 [loop]
##    index = loop
##    swap = False
##    for loop1 in range (loop,-1,-1):
##        if l1 [loop1] < l1 [loop]:
####            print (l1[loop],l1[loop1],loop,loop1)
##            index = loop1
##            swap = True
##            break
##        elif loop1 == 0:
##            swap = 
##    if swap == True:
##        print (loop,loop1,current)
##        l1.pop (loop)
##        l1.insert (loop1,current)
    
    current = l1 [loop]
    loop1 = loop - 1
    while loop1 >= 0 and current > l1 [loop1]:
        l1 [loop1 + 1] = l1 [loop1]
        loop1 -= 1
    l1 [loop1 + 1] = current
    print (l1)
end = time.time ()
total = end - start
print (l1,total)

##start = time.time ()
##smallest = 0
##for loop in range (0,len (l1),1):
##    smallest = loop
##    for loop1 in range (loop + 1,len (l1),1):
##        if l1 [smallest] > l1 [loop1]:
##            smallest = loop1
##    l1 [loop],l1[smallest] = l1[smallest],l1[loop]
####    print (l1)
##end = time.time ()
##total = end - start
##print (l1,total)
