##var1 = 15
##var2 = 2
##print ('Remainder:',var1%var2)
##print ('Quotient:',var1//var2)

##print ('Enter year of birth:')
##year = int(input())
##age = 2019 - year
##days = age*365
##print ('You are',age,'years old.')
##print ('You are',days,'days old.')

##a = 10
##if a > 10:
##    print ('Hello')
##elif a > 10:
##    print ('World')
##elif a == 1:
##    print ('Hello_2')
##else:
##    print ('Else')
##if a > 5:
##    print ('Hello')
##if a == 10:
##    print ('Brandon')
    
##print ('Enter your name:')
##name = input()
##if len(name) > 5:
##    print ('Hello')
##else:
##    print ('World')

##print ('Do you have an upcoming vacation?')
##reaction = input()
##if reaction == 'Yes':
##    print ('What grade are you in?')
##    grade = int (input())
##    if grade != 12:
##        print ('Have an adventurous vacation')
##    elif grade == 12:
##        print ('Great time to study for SAT')
##else:
##    print ('Study Hard at School.')

##import random
##total = 0
##for loop in range (1,21,1):
##    int1 = random.randint (1,20)
##    total = total + int1
##print (total)

##for loop in range (1,6,1):
##    print ('*',end='')

##for loop in range (1,5,1):
##    for loop in range (1,6,1):
##        print ('*',end='')
##    print ()

##print ('Enter a string:')
##string1 = input()
##count = 0
##for loop in string1:
##    print (loop,count)
##    count = count + 1
##for loop1 in range (0,len(string1),1):
##    print (string1[loop1],loop1)

##import random
##while True:
##    int1 = random.randint (100,999)
##    if int1 % 23 == 0:
##        print (int1)
##        break

##count = -17
##while count != 25:
##    print (count)
##    count = count + 1
##while count != 7:
##    print (count)
##    count = count - 1
##print ('Bing!')

##while True:
##    for loop in range (1,11,1):
##        print (loop)
##    for loop in range (9,1,-1):
##        print (loop)

##list1 = ['apple','orange','grape','peach','bananna']
##print (list1[-2])
##list1[4] = 'pear'
##print (list1)
##list1.append ('bananna')
##print (list1)
##list1.insert (3,'var1')
##print (list1)
##list1.pop (2)
##list1.remove ('bananna')
##print (list1)
##list1.sort ()
##print (list1)
##list1.reverse ()
##print (list1)

##import random
##list1 = [32,35,15,47,79]
##for loop in range (1,6,1):
##    random.shuffle (list1)
##maximum = max (list1)
##list1.remove (maximum)
##maximum = max (list1)
##print (list1)
##print (maximum)

##import random
##print (random.sample (list1,3))

##for loop in range (0,5,1):
##    list1 [loop] = list1[loop]+5
##print (list1)

##dict1 = {'apple':3,'orange':5,'grape':1,'peach':7,'bananna':9}
##dict1 ['pear'] = 3
##print (dict1)
##dict1.pop ('pear')
##print (dict1)
##del (dict1 ['bananna'])
##print (dict1)

##dict1 ['grape'] = 10
##print (dict1)
##print (dict1.keys ())
##print (dict1.values ())

##for loop in dict1:
##    print (loop,dict1[loop])

##for loop in dict1:
##    dict1[loop] = dict1[loop] + 5
##print (dict1)

##print ('Enter a string:')
##string1 = input()
##list1 = string1.split ()
##print (list1)
##list1 = list (string1)
##print (list1)
##list1.sort ()
##print (list1)
##string2 = ' '.join (list1)
##print (string2)

##import random
##def integers ():
##    list1 = []
##    for loop in range (1,6,1):
##        int1 = random.randint (1,20)
##        list1.append (int1)
##    return (list1)
##print (integers ())

##def mean (int1,int2,int3,int4):
##    average = (int1+int2+int3+int4)/4
##    return (average)
##print ('Enter a number:')
##int1 = int(input())
##print ('Enter a number:')
##int2 = int(input())
##print ('Enter a number:')
##int3 = int(input())
##print ('Enter a number:')
##int4 = int(input())
##print (mean (3,4,8,19))

##def reversestr (string1):
##    list1 = list (string1)
##    list1.reverse ()
##    string2 = ''.join (list1)
##    return (string2)
##print ('Enter a string:')
##string1 = input()
##print (reversestr(string1))

##from area_functions import rectangle
##print ('Enter the length:')
##length = int(input())
##print ('Enter the width:')
##width = int(input())
##print (rectangle (length,width))

##string1 = 'This is a sentence'
##print (string1[::-1])

##date = '9/14/19'
##month,day,year = date.split ('/')
##print (month,day,year)

##string1 = '   FredFlintstone   '
##print (len(string1))
##string2 = string1.strip ()
##print (len(string2))

##string1 = 'words'
##for loop in string1:
##    print (loop,end='-')

##dict1 = {'apples':1,'pears':2,'peaches':3}
##dict1.pop ('apples')
##print (dict1)
##del (dict1 ['pears'])
##print (dict1)
