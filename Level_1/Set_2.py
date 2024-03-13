##for num in range (1,101,1):
##    print ('Brandon',num)

##for num in range (1,21,1):
##    if num % 2 == 0:
##        print (num,'Even')
##    else:
##        print (num,'Odd')

##import time
##print ('How many seconds do you want in the countdown?')
##sec = int (input ())
##for second in range (sec,0,-1):
##    print (second)
##    time.sleep (1)
##print ('BLAST OFF!')
    
##for num in range (100,0,-3):
##    if (num < 100 and num >= 30) or (num <= 20):
##        print (num)
##    elif num > 20 and num < 30:
##        print ('Tick Tock')

##import random
##num = random.randint (1,100)
##print (num)

##import random
##total = 0
##for loop in range (1,21,1):
##    num = random.randint (1,100)
##    print (num)
##    total = total + num
##print (total)

##for num in range (1,201,1):
##    if num % 3 == 0 and num % 2 != 0:
##        print (num)

##import random
##total = 0
##totaln = 0
##numofneg = 0
##for loop in range (1,21,1):
##    num = random.randint (-20,20)
##    print (num)
##    if num > 0:
##        total = total + num
##    else:
##        totaln = totaln + num
##        numofneg = numofneg+1
##avg = totaln/numofneg
##print (total,avg)

##for loop in range (1,6,1):
##    print ('*',end=' ')

##for loop in range (1,5,1):
##    for innerloop in range (1,6,1):
##        print ('*',end = '')
##    print ('')

##for loop in range (1,5,1):
##    for innerloop in range (1,loop+1,1):
##        print ('*',end = '')
##    print ('')

##print ('Enter a string:')
##a = input ()
####for loop in range (0,len(a),1):
####    print (loop,a[loop])
##count = 0
##for loop in a:
##    print (loop,count)
##    count = count + 1

##loop = 1
##while loop <= 50:
##    print (loop)
##    loop = loop + 1

##count = -17
##while count != 25:
##    print (count)
##    count = count + 1
##while count != 7:
##    print (count)
##    count = count - 1
##print ('Bing!')

##import random
##import time
##while True:
##    rand = random.randint (1,100)
##    randdecimal = random.random ()
##    print (rand,randdecimal)
##    time.sleep (3)

##import random
##import time
##print ('How much money would you like to deposit in your account?')
##deposit = int (input ())
##while True:
##    print ('Do you want to roll the dice?')
##    answer = input ()
##    if answer == 'y' or answer == 'Y':
##        num1 = random.randint (1,6)
##        num2 = random.randint (1,6)
##        print ('Waiting a few seconds . . .')
##        time.sleep (2)
##        if num1 == num2:
##            print ('You win! Your acount will be increased by 5.')
##            deposit = deposit + 5
##            print (deposit)
##        else:
##            print ('You lose. Your account will be decreased by 1.')
##            deposit = deposit - 1
##            print (deposit)
##            if deposit == 0 or deposit < 0:
##                print ('Thank You for Playing')
##                break
##    else:
##        break

##import random
##while True:
##    num = random.randint (100,999)
##    print (num)
##    if num % 23 == 0:
##        break


##                                      HW

print ('Type in your password:')
passwrd = input ()
attempt = ' '
while True:
    print ('Type in your password again:')
    attempt = input ()
    if attempt != passwrd:
        print ('Access Denied!')
    else:
        print ('Access Granted.')
        break

print ()
print ('Next Problem:')
print ()

import random
integer = random.randint (20,30)
chances = 0
guess = 0
while integer != guess:
    print ('Pick a number between (and including) 20 and 30.')
    guess = int (input ())
    chances = chances + 1
print ('It took you',chances,'guesses to guess the number.')

print ()
print ('Next Problem:')
print ()

while True:
    print ('Enter a string:')
    string = input ()
    for loop in range (0,len(string),1):
        print (string[loop])
    print ()

print ()
print ('Next Problem:')
print ()

import time
print ('How many seconds for the countdown?')
countdwn = int (input ())
while countdwn != 0:
    print (countdwn)
    countdwn = countdwn - 1
    time.sleep (1)
print ('BLAST OFF!')

print ()
print ('Next Problem:')
print ()

while True:
    for loop1 in range (1,11,1):
        print (loop1)
    for loop2 in range (10,0,-1):
        print (loop2)
