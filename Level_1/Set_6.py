##string1 = 'This is a string'
##print (string1 [3:-4])
##print (string1 [:])
##print (string1 [::-1])

##print (string1.capitalize())
##print (string1.title())
##print (string1.lower())
##print (string1.upper())
##print (string1.replace("a","b"))
##print (string1.find ("s"))

##print (string1.endswith('ing'))
##print (string1.isalpha())
##print (string1.isnumeric())
##print (string1.isupper())
##print (string1.islower())

##date = '8/24/19'
##month,day,year = date.split('/')
##print (month,day,year)

##print ('Enter your name:')
##name = input()
##first,last = name.split(' ')
##print (first,last)

##string1 = '   string   '
##print (len(string1))
##string1 = string1.strip ()
##print (len(string1))

##string1 = 'string'
##for loop in range (0,len(string1),1):
##    print (string1[loop],end = '-')

##print ('Enter your name:')
##name = input()
##first,last = name.split(' ')
##username = first[0]+last
##print (username.lower())

##print ('Enter a string:')
##string1 = input()
##for loop in string1:
##    print(ord(loop))

##for loop in range (33,257,1):
##    print (chr(loop))

##print ('Enter your name,age, and your state:')
##name = input()
##age = int(input())
##state = input()
##print ('My name is {0}. I am {1} years old. I live in the state of {2}.'.format(name,age,state))

##print ('Enter a string:')
##string1 = input()
##string1 = string1.replace (' ',',')
##list1 = string1.split (',')
##for loop in list1:
##    print (loop)

##                                      HW

##print ('Enter a string of numbers:')
##numstr = input ()
##list1 = numstr.split()
##num1 = 0
##for loop in list1:
##    num1 = int(loop)
##    if num1 % 2 == 0:
##        print (loop)

##print ('Enter a string:')
##string1 = input()
##palindrome = string1[::-1]
##if string1 == palindrome:
##    print ('Given string is a palindrome.')
##else:
##    print ('Given string is not a palindrome.')

##                                      ***

##import time
##var1 = open ('Names.txt','r')
##print (var1.read())
##count = 1
##for loop in var1:
##    print (count,loop)
##    time.sleep (1)
##    count = count+1
##var1.close ()

##import random
##var1 = open ('Numbers.txt','w')
##for loop in range (0,1000,1):
##    var1.write (str(random.randint (1,100))+'\n')
##var1.close ()

##var1 = open ('Numbers.txt','r')
##sum = 0
##for loop in var1:
##    sum = sum + int(loop)
##print (sum)
##var1.close ()

##print ('What is the name of the destination file?')
##destfile = input()
##var1 = open (destfile+'.txt','w')
##var2 = open ('Name_1.txt','r')
##for loop in var2:
##    first,last = loop.split (' ')
##    username = (first[0]+last).lower ()
##    var1.write  (username+'\n')
##    print (username)
##var1.close()
##var2.close()

##question = open ('Questions.txt','r')
##answer = open ('Answers.txt','r')
##print ('What is your name?')
##user = input()
##userp = open (user+'.txt','w')
##score = 0
##for loop in question:
##    for loop1 in answer:
##        loop1 = loop1.strip ()
##        print (loop)
##        a = input()
##        userp.write (a)
##        if a == loop1:
##            print ('Your answer is right.')
##            score = score + 1
##            break
##        else:
##            print ('Your answer is wrong.')
##            break
##print (score)
##question.close ()
##answer.close ()
##userp.close ()


##def wordnum ():
##    var1 = open ('Words.txt','r')
##    count = 0
##    for loop in var1:
##        count = count + 1
##    if count == 0:
##        print ('No words found.')
##    return (count)

##var2 = open ('Words.txt','r')
##dict1 = {}
##count1 = 0
##for loop1 in var2:
##    loop1 = loop1.strip ()
##    if loop1[0] == 'a':
##        count1 = count1 + 1
##        dict1 ['a'] = count1
##
##    letter = loop1[0]
##    if letter not in dict1:
##        dict1 [letter] = 1
##    else:
##        dict1 [letter] = dict1 [letter] + 1
##print (dict1)
##for loop2 in dict1:
##    if dict1[loop2] == max(dict1.values()):
##        print (loop2)

##print ('Enter a letter:')
##letter1 = input()
##print ('Enter a letter:')
##letter2 = input()
##print ('Enter a letter:')
##letter3 = input()
##for loop in var2:
##    loop = loop.strip()
##    if letter1 and letter2 and letter3 in loop:
##        print (loop)

##for loop in var2:
##    loop = loop.strip ()
##    if loop[-1] == 'y':
##        count1 = count1 + 1
##print (count1)

##for loop in var2:
##    loop = loop.strip ()
##    if loop == loop [::-1]:
##        print (loop)
##var1.close ()
##var2.close ()

##var1 = open ('Name_1.txt','r')
##for loop in var1:
##    loop = loop.strip ()
##    newstr = loop.replace (' ','_')
##    print (newstr)

##import os.path
##print ('Enter the file:')
##filename = input()
##if os.path.isfile (filename):
##    print ('File Found')
##    print (os.path.abspath(filename))
##else:
##    print ('File not Found')
