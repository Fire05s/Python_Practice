import random
l1 = []
for loop in range (0,10,1):
    l1.append (random.randint (1,100))

for loop in range (1,len (l1),1):
    current = l1 [loop]
    loop1 = loop - 1
    while loop1 >= 0 and current < l1 [loop1]:
        l1 [loop1 + 1] = l1 [loop1]
        loop1 -= 1
    l1 [loop1 + 1] = current
    print (l1)
print (l1)
