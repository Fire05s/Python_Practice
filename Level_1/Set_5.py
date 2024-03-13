##def info ():
##    print ('Brandon')
##    print ('13')
##    print ('Minions')
##for loop in range (0,3,1):
##    info ()

##def average (num1,num2,num3,num4):
##    mean = (num1 + num2 + num3 + num4) / 4
##    print (mean)
##print ('Enter num1')
##n1 = int (input ())
##print ('Enter num2')
##n2 = int (input ())
##print ('Enter num3')
##n3 = int (input ())
##print ('Enter num4')
##n4 = int (input ())
##average (n1,n2,n3,n4)
##average (9,4,14,2)

##                                      HW

##import random
##def integers ():
##    list1 = []
##    for loop in range (1,6,1):
##        int1 = random.randint (1,20)
##        list1.append (int1)
##    print (list1)
##integers ()

##print ("What is your family member's name?")
##name = input ()
##print ('What is his or her relationship with you?')
##relation = input ()
##print ('What is his or her city?')
##city = input ()
##print ('What is his or her state?')
##state = input ()
##def info (name,relation,city,state):
##    print ()
##    print ('Name:',name)
##    print ('Relation:',relation)
##    print ('City:',city)
##    print ('State:',state)
##info (name,relation,city,state)

##print ('Enter a string:')
##string1 = input ()
##def reversestr (string1):
##    list1 = []
##    list1.append (string1)
##    list1 = list (string1)
##    list1.reverse ()
##    string1 = ''.join (list1)
##    print (string1)
##reversestr (string1)

##print ('Enter a number:')
##num1 = int (input ())
##def factor (num1):
##    list1 = []
##    for loop in range (1,num1+1,1):
##        if num1 % loop == 0:
##            list1.append (loop)
##    print (list1)
##    return (list1)
##var1 = factor (num1)
##print (var1)

##print ('Enter a string:')
##string1 = input ()
##def alphabet (string1):
##    list1 = []
##    list1.append (string1)
##    list1 = list (string1)
##    list1.sort ()
##    print (list1)
##alphabet (string1)

##                                      ***

##def total (price,tax):
##    actualp = price - ((tax/100)*price)
##    return (actualp)
##print ('What is the price of your item?')
##price = int (input())
##print ('How much is the tax?')
##tax = int (input())
##print (total (price,tax))

##print ('How many quarters,dimes,nickels,and pennies do you have?')
##quarters = int(input())
##dimes = int(input())
##nickels = int(input())
##pennies = int(input())
##def quarter (quarters):
##    qvalue = quarters*0.25
##    return (qvalue)
##def dime (dimes):
##    dvalue = dimes*0.1
##    return (dvalue)
##def nickel (nickels):
##    nvalue = nickels*0.05
##    return (nvalue)
##def penny (pennies):
##    pvalue = pennies*0.01
##    return (pvalue)
##total = quarter(quarters) + dime(dimes) + nickel(nickels) + penny(pennies)
##print (total)

##a = 5
##def addition ():
##    global a
##    a = a + 5
##    return (a)
##for loop in range (1,4,1):
##    print (addition ())

##print ('Enter the first string:')
##string1 =  input()
##print ('Enter the second string:')
##string2 = input()
##def function1 (string1,string2):
##    if len(string1) == len(string2):
##        return 1
##    else:
##        return 0
##print (function1 (string1,string2))

##print ("How many columns do you want?")
##column = int (input())
##print ('How many rows do you want?')
##row = int (input())
##def asterisks (row,column):
##    for loop1 in range (0,row,1):
##        for loop2 in range (0,column,1):
##            print ('*',end = '')
##        print ()
##asterisks (row,column)

##                                      HW

##def rectangle (length,width):
##    area = length*width
##    print (area)
##def triangle (base,height):
##    area = 0.5*base*height
##    print (area)
##def circle (radius):
##    area = 3.14*radius*radius
##    print (area)
##print ('Which area do you want to find: rectangle,triangle,circle')
##shape = input()
##if shape == 'rectangle':
##    print ('Type the length:')
##    length = int (input())
##    print ('Type the width:')
##    width = int (input())
##    rectangle (length,width)
##if shape == 'triangle':
##    print ('Type the base:')
##    base = int (input())
##    print ('Type the height:')
##    height = int (input())
##    triangle (base,height)
##if shape == 'circle':
##    print ('Type the radius:')
##    radius = int (input())
##    circle (radius)

##from area_functions import *
##print ('Which area do you want to find: rectangle,triangle,circle')
##shape = input()
##if shape == 'rectangle':
##    print ('Type the length:')
##    length = int (input())
##    print ('Type the width:')
##    width = int (input())
##    print (rectangle (length,width))
##if shape == 'triangle':
##    print ('Type the base:')
##    base = int (input())
##    print ('Type the height:')
##    height = int (input())
##    print (triangle (base,height))
##if shape == 'circle':
##    print ('Type the radius:')
##    radius = int (input())
##    print (circle (radius))
