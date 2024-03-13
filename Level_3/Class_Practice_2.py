##class birthday:
##    def __init__ (self):
##        self.dictionary = {}
##    def add (self):
##        name = input ('What is the person\'s name? - ')
##        name = name.lower ()
##        bday = input ('What is the person\'s birthday? (M/D/Y) - ')
##        self.dictionary [name] = bday
##    def display (self):
##        disname = input ('Whose birthday do you want to know? - ')
##        disname = disname.lower ()
##        if disname in self.dictionary:
##            print (disname+'\'s Birthday is',self.dictionary [disname])
##        else:
##            print ('This person is not on the list.')
##blist = birthday ()
##blist.add ()
##blist.add ()
##blist.display ()
##blist.display ()
##blist.display ()

##class quiz:
##    def __init__ (self):
##        self.science = {'How many legs does a dog have? - ':'4','What is the topmost layer of the atmosphere? - ':'thermosphere','What layer of the Earth do you live on? - ':'crust','What type of animal can live both in water and on land? (plural) - ':'amphibians','What is another term for "basic" machines? - ':'simple'}
##        self.math = {'2+2 - ':4.0,'6^3 - ':216.0,'log 10^2 - ':2.0,'sin30 (degrees) - ':0.5,'pi/6 (radians -> degrees) - ':30.0}
##        self.sports = {'What is a miss in baseball called? - ':'strike','What is a score in soccer (US) called? - ':'goal','What is a score in football (US) called? - ':'touchdown','What is the final point in tennis called? (one word) - ':'matchpoint','What is a smaller version of tennis? (one word) - ':'tabletennis'}
##        self.score = 0
##    def takequiz (self):
##        choice = input ('Which type of quiz do you want to take? (Science, Math, or Sports) - ')
##        choice = choice.lower ()
##        if choice == 'science':
##            for loop in self.science:
##                answer = input (loop)
##                answer = answer.lower ()
##                if answer == self.science [loop]:
##                    self.score = self.score + 1
##                else:
##                    print ('Sorry, the correct answer is',self.science [loop])
##
##        elif choice == 'math':
##            for loop in self.math:
##                answer = float (input (loop))
##                if answer == self.math [loop]:
##                    self.score = self.score + 1
##                else:
##                    print ('Sorry, the correct answer is',self.math [loop])
##
##        elif choice == 'sports':
##            for loop in self.sports:
##                answer = input (loop)
##                answer = answer.lower ()
##                if answer == self.sports [loop]:
##                    self.score = self.score + 1
##                else:
##                    print ('Sorry, the correct answer is',self.sports [loop])
##test = quiz ()
##test.takequiz ()
##print ('Your score ended up as',test.score)

class bank:
    def __init__ (self,n,accountnum,balance):
        self.name = n
        self.accnum = accountnum
        self.bal = balance
    def withdrawal (self):
        amount = int (input ('How much do you (' + self.name + ') want to withdraw? - '))
        self.bal = self.bal - amount
        print (self.name+'\'s Balance is now',self.bal)
    def deposit (self):
        amount = int (input ('How much do you (' + self.name + ') want to deposit? - '))
        self.bal = self.bal + amount
        print (self.name+'\'s Balance is now',self.bal)
    def receive (self,amount):
        self.bal = self.bal + amount
    def transfer (self):
        amount = int (input ('How much do you (' + self.name + ') want to transfer? - '))
        self.bal = self.bal - amount
##account = bank ('John',1,500)
##print ('Account #'+ str (account.accnum) + ':',account.name+', $' + str (account.bal))
##account.withdrawal ()
##account.deposit ()
john = bank ('john',111,100)
alice = bank ('alice',222,200)
print (john.bal)
print (alice.bal)
john.transfer ()
print (john.bal)
print (alice.bal)
