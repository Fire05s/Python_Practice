##pair = {'apples':5,'pears':3,'oranges':6,'grapes':20,'fruits':34}
##pair ['banana'] = 3
##print (pair)
##pair ['oranges'] = 10
##print (pair)
##del (pair ['fruits'])
##print (pair)
##pair.pop ('grapes')
##print (pair)
##for i in pair:
##    print (i,pair[i])
##print (pair.keys())
##print (pair.values())

##                                      HW

##numbers = []
##for loop in range (1,1001,1):
##    if loop % 5 == 0:
##        if loop % 15 != 0:
##            numbers.append (loop)
##print (numbers)

##print ('Enter the month number:',end = ' ')
##monthnum = int (input ())
##months = ['','Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
##print (months [monthnum])

##*****************************************************************************
##wrdlist = ['cat','zebra','umbrella','magic','cunning','ox']
##print (wrdlist)
##print ('Enter a letter:')
##letter = input ()
##for loop in wrdlist:
##    if letter in loop:
##        print (loop)
##        word = loop
##        for loop1 in range (0,len(word),1):
##            if word[loop1] == letter:
##                print (loop1)
##*****************************************************************************

##*****************************************************************************
##import random
##wrdlist = ['cat','bug','common','evil','rhyme']
##word = random.choice (wrdlist)
##list1 = list(word)
##random.shuffle (list1)
##jumbled = ''.join (list1)
##while True:
##    print ('Guess what',jumbled,'is:')
##    guess = input ()
##    if guess == word:
##        print ('Correct!')
##        break
##*****************************************************************************

##list1 = ['cat','zebra','umbrella','magic','cunning','ox','bug','common','evil','rhyme']
##print (list1)
##for loop in range (1,6,1):
##    if loop % 2 == 0:
##        list1.pop (loop)
##    if loop % 2 == 1:
##        list1.pop (loop)
##print (list1)

##list1 = ['cat','bug','common','evil','rhyme']
##for loop in range (0,5,1):
##    print (list1 [loop],end = ' ')
##print ()
##for loop in range (0,5,1):
##    print (list1 [loop],end = '-')
##print()
##for loop in range (0,5,1):
##    print (list1 [loop])

##*****************************************************************************
##dictionary = {'key1':5,'key2':7,'key3':2,'key4':9,'key5':3}
##for loop in dictionary:
##    print (loop,dictionary[loop])
##*****************************************************************************

##stock = {'apples':2,'pears':2,'oranges':1,'grapes':2,'peaches':2}
##print (stock.keys())
##print ('What would you like to purchase:')
##purchase = input ()
##if purchase in stock:
##    print (stock[purchase])
##else:
##    print ('I recommend looking elsewhere for',purchase,'.')

##accounts = {'member1':'password1','member2':'password2','member3':'password3','member4':'password4'}
##print ('Enter Account Name:')
##accname = input ()
##if accname in accounts:
##    print ('Enter the password:')
##    passwrd = input ()
##    if passwrd == accounts[accname]:
##        print ('Access Granted')
##    else:
##        print ('Access Denied')
##else:
##    print ('No Account Found')

##                                      ***

##questions = {'5+5':10,'13*7':51,'9*9':81,'5*9':45,'4*3':12}
##score = 0
##for loop in questions:
##    print ('Solve',loop)
##    answer = int (input())
##    if answer == questions[loop]:
##        print ('Correct!')
##        score = score + 1
##    else:
##        print ('Wrong.')
##        print ('The right answer was',questions[loop],'.')
##print ('Your score was',score)

##num1 = {1:'',2:'',3:'',4:'',5:''}
##for loop in num1:
##    square = loop*loop
##    num1[loop] = square
##print (num1)

##print ('Enter a string:')
##string1 = input ()
##dictionary = {}
##list1 = list(string1)
##for loop in range (0,len(list1),1):
##    dictionary [list1 [loop]] = loop
##print (dictionary)

##                                      HW

##days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
##activities = ['Tennis','Swimming','Piano','Guitar','Math','Reading','Programming']
##print (days)
##print (activities)
##dictionary = {}
##count = 0
##for loop in days:
##    dictionary [days[count]] = activities[count]
##    count = count + 1
##print (dictionary)

##animals = {'dog':'','cat':'','elephant':'','duck':'','lion':''}
##for loop in animals:
##    print ('What sound does a',loop,'make?')
##    noise = input ()
##    animals [loop] = noise
##print (animals)

##students = {'John':87,'Billy':54,'Samantha':91}
##print (students)
##for loop in students:
##    newValue = students[loop]+5
##    students [loop] = newValue
##print (students)
##upstudents = students
##for loop in students:
##    if students[loop] <= 60:
##        del (upstudents [loop])
##        students ['Deleted'] = 100
##print (upstudents)
##for loop in students:
##    if students[loop] >= 90:
##        students [loop] = 'A'
##    elif students[loop] >= 80:
##        students [loop] = 'B'
##    elif students [loop] >= 70:
##        students [loop] = 'C'
##    elif students [loop] > 60:
##        students [loop] = 'D'
##print (students)

##print ('Enter an account number:')
##accnum = int (input())
##print ('Enter your initial deposit:')
##deposit = int (input())
##dictionary = {}
##dictionary [accnum] = deposit
##for loop in dictionary:
##    print ('Your balance is $',dictionary [loop])
##while True:
##    print ('Do you want to Add Money or Withdraw Money or End?')
##    reply = input ()
##    if reply == 'Add Money':
##        print ('How much money do you want to add?')
##        addition = int (input())
##        deposit = deposit + addition
##        dictionary [accnum] = deposit
##        print ('Your balance is $',dictionary [loop])
##    elif reply == 'Withdraw Money':
##        print ('How much money do you want to withdraw?')
##        withdrawal = int (input())
##        deposit = deposit - withdrawal
##        dictionary [accnum] = deposit
##        print ('Your balance is $',dictionary [loop])
##    elif reply == 'End':
##        break
##    else:
##        print ('Please write a stated option.')

##turn = 0
##dict1 = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
##for loop in dict1:
##    print (loop,':',dict1[loop],end = ' ')
##    if loop == 3 or loop == 6:
##        print ()
##for loop1 in range (0,9,1):
##    print ('\n Enter a number from 1 to 9:')
##    num1 = int (input())
##    if dict1[num1] == '':
##        if turn % 2 == 1:
##            dict1 [num1] = 'X'
##        if turn % 2 == 0:
##            dict1 [num1] = 'O'
##        turn = turn + 1
##    else:
##        print ()
##        print ('Please enter another number')
##    for loop in dict1:
##        print (loop,':',dict1[loop],end = ' ')
##        if loop == 3 or loop == 6:
##            print ()
##    if dict1[1] == dict1[2] == dict1[3] != '':
##        print ()
##        print (dict1[1],'Wins')
##        break
##    if dict1[4] == dict1[5] == dict1[6] != '':
##        print ()
##        print (dict1[4],'Wins')
##        break
##    if dict1[7] == dict1[8] == dict1[9] != '':
##        print ()
##        print (dict1[7],'Wins')
##        break
##    if dict1[1] == dict1[4] == dict1[7] != '':
##        print ()
##        print (dict1[1],'Wins')
##        break
##    if dict1[2] == dict1[5] == dict1[8] != '':
##        print ()
##        print (dict1[2],'Wins')
##        break
##    if dict1[3] == dict1[6] == dict1[9] != '':
##        print ()
##        print (dict1[3],'Wins')
##        break
##    if dict1[1] == dict1[5] == dict1[9] != '':
##        print ()
##        print (dict1[1],'Wins')
##        break
##    if dict1[3] == dict1[5] == dict1[7] != '':
##        print ()
##        print (dict1[3],'Wins')
##        break
##    if '' not in list (dict1.values ()):
##        print ()
##        print ('Tie')
