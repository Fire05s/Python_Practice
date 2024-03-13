##class bank:
##    def __init__ (self,name,account,balance):
##        self.name = name
##        self.account = account
##        self.balance = balance
##    def printmethod (self):
##        print (self.name,self.account,self.balance)
##    def withdraw (self):
##        print ('Put in the amount you want to withdraw:')
##        withdrawamt = float (input ())
##        self.balance = self.balance - withdrawamt
##    def deposit (self):
##        print ('Put in the amount you want to deposit:')
##        depositamt = float (input ())
##        self.balance = self.balance + depositamt

##john = bank ('John','1',1000)
##print (john.name,john.account,john.balance)
##john.printmethod ()
##steve = bank ('Steve','2',2000)
##print (steve.name,steve.account,steve.balance)
##steve.printmethod ()

##user = bank ('User 1','#1',1000)
##user.withdraw ()
##print (user.balance)
##user.deposit ()
##print (user.balance)

##class shopping:
##    def __init__ (self,name):
##        self.name = name
##        self.item = {}
##    def cart (self,item,amount):
##        self.item [item] = amount
##    def remove (self):
##        remitem = input ('Which item would you like to remove? ')
##        remamt = int (input ('How much would you like to remove? '))
##        if remitem in self.item:
##            self.item [remitem] = self.item [remitem] - remamt
##            if self.item [remitem] == 0:
##                del (self.item [remitem])
##        else:
##            print ('Item is not present')

##store = shopping ('Store1')
##store.cart ('Apple',5)
##store.cart ('Orange',7)
##print (store.item)
##store.remove ()
##print (store.item)

##class phonebook:
##    def __init__ (self,name,num):
##        self.phname = name
##        self.phnum = num
##        self.phone = {}
##    def add (self,name,num):
##        self.phone [name] = num
##    def update (self):
##        reply = input ('Do you want to update an existing phone number? ')
##        if reply.lower () == 'yes':
##            self.phname = input ("What is the entry's name? ")
##            self.phnum = input ('What is the new phone number? ')
##            self.phone [self.phname] = self.phnum
##        else:
##            print ('Ok, the phone number shall remain the same.')
##    def remove (self):
##        reply = input ('Do you want to remove an entry? ')
##        if reply.lower () == 'yes':
##            self.phname = input ('Which entry would you like to remove? ')
##            if self.phname in self.phone:
##                reply = input ('Would you like to remove this entry? ')
##                if reply.lower () == 'yes':
##                    del (self.phone [self.phname])
##                else:
##                    print ('Ok, no entry shall be removed.')
##        else:
##            print ('Ok, no entry shall be removed.')

##phbook = phonebook ('P1',1)
##phbook.add ('P2',2)
##phbook.add ('P3',3)
##phbook.add ('P4',4)
##print (phbook.phone)
##phbook.update ()
##print (phbook.phone)
##phbook.remove ()
##print (phbook.phone)

##class market:
##    def __init__ (self,timestart,timeend):
##        self.name = input ('What is the market\'s name - ')
##        self.times = timestart
##        self.timeE = timeend
##        print ('The store opens from',self.times,'to',self.timeE+'.')
##        self.priced = {}
##        self.pricen = {}
##    def add (self):
##        while True:
##            reply = input ('Do you want to add an item to the inventory? ')
##            if reply.lower () == 'yes':
##                item = input ('What is the name of the item? ')
##                item = item.lower ()
##                if item in self.priced or item in self.pricen:
##                    print ('This item is already present.')
##                    reply = input ('Do you want to change it\'s price or quantity? ')
##                    if reply.lower () == 'price':
##                        price = float (input ('What is the price of a unit of the item? '))
##                        self.priced [item] = price
##                        print (self.priced)
##                    elif reply.lower () == 'quantity':
##                        quantity = input ('How much of the item is present? ')
##                        self.pricen [item] = quantity
##                        print (self.pricen)
##                    else:
##                        print ('Ok, the existing item will remain the same.')
##                else:
##                    price = input ('What is the price of a unit of the item? ')
##                    quantity = input ('How much of the item is present? ')
##                    self.priced [item] = price
##                    self.pricen [item] = quantity
##                    print (self.priced)
##                    print (self.pricen)
##            stopcond = input ('Do you want to stop adding items? ')
##            if stopcond.lower () == 'yes':
##                print (self.priced)
##                print (self.pricen)
##                break
##            else:
##                print ('Ok.')
##    def purchase (self):
##        buyitem = input ('What do you want to buy? ')
##        if buyitem in self.pricen:
##            purchaseq = int (input ('How much do you want to buy? '))
##            if int (self.pricen [buyitem]) >= purchaseq:
##                self.pricen [buyitem] = int (self.pricen [buyitem]) - purchaseq
##                print ('Here is/are your',purchaseq,buyitem+'(s).')
##                print (self.pricen)
##            else:
##                print ('We don\'t have that much in our inventory, but')
##                print ('we can give you all that we have.')
##                print ('Here is/are your',self.priced [buyitem],buyitem+'(s).')
##                print (self.pricen)
##        else:
##            print ('This item is not in the store.')
##    def returnitem (self):
##        retitem = input ('What do you want to return? ')
##        if retitem in self.pricen:
##            if retitem.lower () != 'milk' or retitem.lower () != 'cheese' or retitem.lower () != 'ice cream':
##                retquantity = int (input ('How much are your returning? '))
##                print ('Ok, sorry for the inconveniance.')
##                self.pricen [retitem] = int (self.pricen [retitem]) + retquantity
##                print (self.pricen)
##            if retitem.lower () == 'milk' or retitem.lower () == 'cheese' or retitem.lower () == 'ice cream':
##                print ('I am sorry, but you are\'nt allowed to return dairy products.')
##        else:
##            print ('We do not carry this item.')
##
##supermarket = market ('7:30','4:00')
##supermarket.add ()
##supermarket.purchase ()
##supermarket.returnitem ()

##class zoo:
##    def __init__ (self):
##        self.name = input ('What is the zoo\'s name? - ')
##        self.population = {}
##        self.food = {}
##        self.habitat = {}
##    def add (self,animal,population,food,habitat):
##        self.population [animal] = population
##        self.food [animal] = food
##        self.habitat [animal] = habitat
##        print (self.population)
##        print (self.food)
##        print (self.habitat)
##    def remove (self,animal):
##        del (self.population [animal])
##        del (self.food [animal])
##        del (self.habitat [animal])
##        print (self.population)
##        print (self.food)
##        print (self.habitat)
##    def display (self,animal):
##        print ('There are',self.population [animal],animal+'(s) who live mostly in',self.habitat [animal],'habitats, and primarily eat',self.food [animal]+'.')

##CAzoo = zoo ()
##while True:
##    reply = input ('Do you want to add an animal? - ')
##    if reply.lower () == 'yes':
##        animal = input ('What is the general name of the animal? - ')
##        if animal in CAzoo.population:
##            print ('This animal is already present.')
##        else:
##            pop = int (input ('Type the number of animals present of this species - '))
##            food = input ('What type of food does the animal eat? - ')
##            hab = input ('What type of habitat does the animal live in? - ')
##            CAzoo.add (animal,pop,food,hab)
##    else:
##        print ('Ok.')
##        break
##while True:
##    reply = input ('Do you want to remove an animal? - ')
##    if reply.lower () == 'yes':
##        animal = input ('What is the general name of the animal? - ')
##        if animal in CAzoo.population:
##            CAzoo.remove (animal)
##        else:
##            print ('This animal is not present.')
##    else:
##        print ('Ok.')
##        break
##while True:
##    reply = input ('Do you want to display the information of an animal? - ')
##    if reply.lower () == 'yes':
##        animal = input ('What is the general name of the animal? - ')
##        if animal in CAzoo.population:
##            CAzoo.display (animal)
##        else:
##            print ('This animal is not present.')
##            break
##    else:
##        print ('Ok.')
##        break

