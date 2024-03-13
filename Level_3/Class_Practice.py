##class animal:
##    def __init__ (self,legs,col,sound):
##        self.numlegs = legs
##        self.color = col
##        self.ansound = sound
##tiger = animal (4,'yellowblack','roar')
##print ('Tiger:',str (tiger.numlegs) + ',',tiger.color + ',',tiger.ansound)
##penguin = animal (2,'blackwhite','squawk')
##print ('Penguin:',str (penguin.numlegs) + ',',penguin.color + ',',penguin.ansound)
##goat = animal (4,'white','bleet')
##print ('Goat:',str (goat.numlegs) + ',',goat.color + ',',goat.ansound)


##class bank:
##    def __init__ (self,n,accountnum,balance):
##        self.name = n
##        self.accnum = accountnum
##        self.bal = balance
##    def withdrawal (self):
##        amount = int (input ('How much do you (' + self.name + ') want to withdraw? - '))
##        self.bal = self.bal - amount
##        print (self.name+'\'s Balance is now',self.bal)
##    def deposit (self):
##        amount = int (input ('How much do you (' + self.name + ') want to deposit? - '))
##        self.bal = self.bal + amount
##        print (self.name+'\'s Balance is now',self.bal)
##account = bank ('John',1,500)
##print ('Account #'+ str (account.accnum) + ':',account.name+', $' + str (account.bal))
##account.withdrawal ()
##account.deposit ()


class ship:
    def __init__ (self,n,crew,col):
        self.name = n
        self.crewn = crew
        self.color = col
    def expansion (self):
        crewadd = int (input ('How many more crewmembers do you want to add? - '))
        self.crewn = self.crewn + crewadd
        print ('The',self.name,'now has',self.crewn,'members.')
boat = ship ('Skipper',2,'lightblue')
print ('This boat is named',boat.name,'with',boat.crewn,'members and a',boat.color,'color.')
boat.expansion ()
yacht = ship ('Peace',10,'yellow')
print ('This yacht is named',yacht.name,'with',yacht.crewn,'members and a',yacht.color,'color.')
yacht.expansion ()
cruise = ship ('Luxury',70,'blue&green')
print ('This cruise ship is named',cruise.name,'with',cruise.crewn,'members and a',cruise.color,'color.')
cruise.expansion ()
