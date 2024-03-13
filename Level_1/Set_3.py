##var1 = ['variable1','num2','entity3','element4','apple']
##var1.append ('orange')
##var1.insert (0,'grape')
##var1.pop (3)
##var1.remove ('num2')
##var1.sort (reverse = 1)
##var1.reverse ()
##print (var1)

##loop = ' '
##for loop in range (1,len(var1),1):
##    print (var1[loop])

##print (var1 [0:3])
##print (var1 [-1])
##var1 [1] = 'replacement'
##print (var1)


##print ('Enter a string:')
##string = input ()
##list1 = string.split ('a')
##print (list1)

##print ('Enter a string:')
##string = input()
##list1 = list (string)
##print (list1)
##list1.sort ()
##string2 = ''.join (list1)
##print (string2)

##tries = []
##print ('Type in your password:')
##passwrd = input ()
##attempt = ' '
##while True:
##    print ('Type in your password again:')
##    attempt = input ()
##    if attempt != passwrd:
##        print ('Access Denied!')
##        tries.append (attempt)
##    else:
##        print ('Access Granted.')
##        print (tries)
##        break

##import random
##list1 = []
##for loop in range (1,21,1):
##    randomnum = random.randint (1,20)
##    list1.append (randomnum)
##print (list1)
##print (max(list1),min(list1))

##import random
##for loop in range (1,11,1):
##    random.shuffle (var1)
##    print (var1)
##print (var1 [0])

##import random
##var2 = random.choice (var1)
##var3 = random.sample (var1,3)
##print (var2,var3)

##import random
##fruits = ['pear','apple','orange','grapes']
##while True:
##    randfruit = random.choice (fruits)
##    if 'p' in randfruit:
##        print (randfruit)
##        break

##print ('Enter a string:')
##inputstr = input ()
##words = inputstr.split (' ')
##for loop in range (0,len(words),1):
##    print (words[loop])
##for loop in words:
##    print (loop)

##import random
##wordset = ['rhyme','reason','apple','dog','happy']
##characters = list (wordset)
##word = random.choice (wordset)
##blanks = ['_']*len(word)
##chances = 10
##print (blanks)
##while '_' in blanks:
##    print ('Guess a letter:')
##    guess = input ()
##    for loop in range (0,len(word),1):
##        if guess == word[loop]:
##            blanks[loop] = guess
##            print (blanks)
##    if guess not in word:
##        print ('Wrong Guess.')
##        print (blanks)
##        chances = chances - 1
##    if chances == 0:
##        print ('You have run out of chances')
##        break
##    if '_' not in blanks:
##        print ('You have guessed the word correctly')

##ClassMark = ['Math','Writing','History','Science']
##BillMarks = [86,80,78,94]
##TomMarks = [65,78,79,87]
##MikeMarks = [89,76,87,75]
##mainlist = [ClassMark,BillMarks,TomMarks,MikeMarks]
##print (mainlist)
##print (mainlist [2][2])
##print ('Enter which subject to average:')
##subject = input()
##if subject == 'Math':
##    average = ((mainlist [1][0])+(mainlist [2][0])+(mainlist [3][0]))/3
##    print (average)
##if subject == 'Writing':
##    average = ((mainlist [1][1])+(mainlist [2][1])+(mainlist [3][1]))/3
##    print (average)
##if subject == 'History':
##    average = ((mainlist [1][2])+(mainlist [2][2])+(mainlist [3][2]))/3
##    print (average)
##if subject == 'Science':
##    average = ((mainlist [1][3])+(mainlist [2][3])+(mainlist [3][3]))/3
##    print (average)

##var1 = ('apple','grape','orange','pear','fruits','apple')
##print (var1.index ('orange'))
##print (var1.count ('apple'))
##var2 = ('element','object')
##var3 = (var1 + var2)
##print (var3)
##print (var3*4)

##numtup1 = (21,31,72,39)
##print (max (numtup1))
##print (min (numtup1))

##import random
##numlist = []
##for loop in range (0,20,1):
##    num = random.randint (1,100)
##    numlist.append (num)
##    numlist.sort (reverse = 1)
##print (numlist)
##topnum = max (numlist)
##numlist.remove (topnum)
##print (max (numlist))
##print (numlist [1])

##var1 = []
##wordlist = ['cat','hats','commas','penalties','multiple','varying','elements']
##for loop in range (0,7,1):
##    countlist = wordlist [loop]
##    var1.append (len (countlist))
##print (var1)
