##class shapes:
##    def __init__ (self,sides,name):
##        self.sides = sides
##        self.name = name
##rect = shapes (4,'Rectangle')
##tri = shapes (3,'Triangle')
##circ = shapes (0,'Circle')
##pent = shapes (5,'Pentagon')
##print (rect.name,':',rect.sides,'sides')
##print (tri.name,':',tri.sides,'sides')
##print (circ.name,':',circ.sides,'sides')
##print (pent.name,':',pent.sides,'sides')

##class dog:
##    def __init__ (self,n,ecolor,fcolor,b,a):
##        self.name = n
##        self.ecol = ecolor
##        self.fcol = fcolor
##        self.breed = b
##        self.age = a
##    def show_info (self):
##        print ('My dog\'s name is',self.name+', and he/she is a',self.age,'year old',self.breed+', with',self.ecol,'eyes and',self.fcol,'colored fur.')
##gshep = dog ('Hunter','brown','brown','German Shepherd','5')
##gshep.show_info ()
##bull = dog ('Frenchie','brown','white and brown','French Bulldog','3')
##bull.show_info ()
##poodle = dog ('Poochie','gray','gray','Poodle','6')
##poodle.show_info ()

##class book:
##    def __init__ (self,t,g,a,s):
##        self.title = t
##        self.genre = g
##        self.author = a
##        self.size = s
##    def display (self):
##        print ('I recently read a book named',self.title,'by',self.author,'which is a',self.genre,'book that is of',self.size,'size.')
##b1 = book ('And then there were None','Mystery','Agatha Christie','medium')
##b2 = book ('Murder on the Orient Express','Mystery','Agatha Christie','medium')
##b1.display ()
##b2.display ()

#Skipped Question 4

##class state:
##    def __init__ (self,n,c_c,p):
##        self.name = n
##        self.capc = c_c
##        self.pop = p
##ob1 = state ('California','Sacramento',1000000)
##ob2 = state ('Oregon','Salem',1000000)
##ob3 = state ('Washington','Olympia',1000000)
##ob4 = state ('Nevada','Carson City',1000000)
##ob5 = state ('Colorado','Denver',1000000)
##list1 = [ob1,ob2,ob3,ob4,ob5]
##instate = input ('Which state do you want to know more information about? - ')
##if instate.lower () == ob1.name.lower ():
##    print (ob1.name+'\'s capital city is',ob1.capc,'and has a population of',ob1.pop)
##elif instate == ob2.name:
##    print (ob2.name+'\'s capital city is',ob2.capc,'and has a population of',ob2.pop)
##elif instate == ob3.name:
##    print (ob3.name+'\'s capital city is',ob3.capc,'and has a population of',ob3.pop)
##elif instate == ob4.name:
##    print (ob4.name+'\'s capital city is',ob4.capc,'and has a population of',ob4.pop)
##elif instate == ob5.name:
##    print (ob5.name+'\'s capital city is',ob5.capc,'and has a population of',ob5.pop)
##else:
##    print ('We do not have information for that state')
