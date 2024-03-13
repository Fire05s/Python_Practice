import threading
import random
##def f1 (num):
##    for loop in range (0,num,1):
##        print ('hello')
##def f2 (num):
##    for loop in range (0,num,1):
##        print ('hi')
##t1 = threading.Thread (target = f1,args = (5,))
##t2 = threading.Thread (target = f2,args = (3,))
##t1.start ()
##t1.join ()
##t2.start ()
##t2.join ()

##t1.start ()
##t1.join ()
##t2.start ()
##t1.join ()

##t1.start ()
##t2.start ()
##t1.join ()
##t2.join ()
##print ('thread completed')


##from threading import Thread
##def print_double(num):
##    print('The double of {} is {}'.format(num, num*2))
##double_maker = Thread(target=print_double, args=(10,))
##double_maker.start()
##print('Thread ended')

##from threading import Thread
##def get_squares(start, end):
##    for num in range(start, end+1, 1):
##        print('The square of {} is {}'.format(num, num*num))
##square_thread = Thread(target=get_squares, args=(10, 20))
##square_thread.start()
###square_thread.join()
##print('Message One')
##print('Message Two')
##print('Message Three')


##from threading import Thread
##def prime_checker(num):
##    prime = True
##    for d in range(2, int(num**0.5) + 1, 1):
##        print('{} checked with {}'.format(num, d))
##        if num % d == 0:
##            prime = False
##    if prime == True:
##        print('{} is a prime number'.format(num))
##    else:
##        print('{} is a not prime number'.format(num))
##
##
##def primes(numbers):
##    for num in numbers:
##        t = Thread(target=prime_checker, args=(num,))
##        t.start()
###        t.join()
##        print('Completed check for {}!'.format(num))
##
##
##
##prime_thread = Thread(target=primes, args=([4483, 4493, 4507, 4561, 4567, 4583, 4591], ))
##prime_thread.start()
###prime_thread.join()
##print('The program ended')


##from threading import Thread
##from time import sleep
##letters = ['A', 'B', 'C', 'D']
##
##
##def func():
##    for letter in letters:
##        print(letter)
##        sleep(2)
##
##
##
##thread = Thread(target=func)
##thread.start()
##print('E')


##from threading import Thread
##from time import sleep
##
##
##def number_printer():
##    for number in range(1, 6, 1):
##        print(number)
##        sleep(1)
##
##
##
##thread = Thread(target=number_printer)
##thread.start()
##print('A')
##thread.join()
##print('B')

##m1 = []
##l1 = []
##for loop in range (0,5,1):
##    for loop in range (0,10,1):
##        l1.append (random.randint (1,10))
##    m1.append (l1)
##    l1 = []
##print (m1)
##def product (givenl):
##    s = 1
##    for loop1 in givenl:
##        s = s * loop1
##    print (s,'\n')
##for loop in m1:
##    thread1 = threading.Thread (target = product,args = (loop,))
##    thread1.start ()

##def length (givenf):
##    counter = 0
##    for loop1 in givenf:
##        counter += 1
##    print (givenf,'has',counter,'lines.')
##for loop in range (1,4,1):
##    file1 = open ('file' + str (loop) + '.txt','r')
##    thread1 = threading.Thread (target = length, args = (file1,))
##    thread1.start ()
##    thread1.join ()

##file1 = open ('expressions.txt','w')
##file2 = open ('answers.txt','w')
##for loop in range (0,100,1):
##    n1 = random.randint (0,100)
##    n2 = random.randint (1,100)
##    operator = random.randint (1,4)
##    opsymbol = ''
##    ans = 0
##    if operator == 1:
##        opsymbol = '+'
##        ans = n1 + n2
##    elif operator == 2:
##        opsymbol = '-'
##        ans = n1 - n2
##    elif operator == 3:
##        opsymbol = '*'
##        ans = n1 * n2
##    elif operator == 4:
##        opsymbol = '/'
##        ans = n1 / n2
##    line1 = str (n1) + opsymbol + str (n2)
##    line2 = ans
##    file1.write (line1 + '\n')
##    file2.write (str (line2) + '\n')
##file1.close ()
##file2.close ()
##def expr (givenf):
##    file1 = open (givenf,'r')
##    explist = []
##    for loop in file1:
##        loop = loop.strip ()
##        explist.append (loop)
##    print (explist)
##    file1.close ()
##def answrs (givenf):
##    file1 = open (givenf,'r')
##    anslist = []
##    for loop in file1:
##        loop = loop.strip ()
##        anslist.append (loop)
##    print (anslist)
##    file1.close ()
##thread1 = threading.Thread (target = expr,args = ('expressions.txt',))
##thread1.start ()
##thread2 = threading.Thread (target = answrs,args = ('answers.txt',))
##thread2.start ()
##thread1.join ()
##thread2.join ()
##print ('Done')

##from threading import Thread
##def user_input():
##    while True:
##        number = int(input('Please enter a non-zero number: '))
##        if number == 0:
##            print('You entered zero')
##            break
##        print(number * 2)
##def checker_function():
##    while user_input_thread.is_alive():
##        pass
##    print('The thread is not alive')
##user_input_thread = Thread(target=user_input)
##checker_thread = Thread(target=checker_function)
##user_input_thread.start()
##checker_thread.start()

##def nums ():
##    for loop in range (0,100,1):
##        print (random.randint (0,100))
##    if thread1.is_alive ():
##        print ('The thread has finished execution')
##        print (thread1.is_alive ())
##thread1 = threading.Thread (target = nums)
##thread1.start ()

##def nums ():
##    l1 = []
##    for loop in range (0,10,1):
##        l1.append (random.randint (0,10))
##    if thread1.is_alive ():
##        print (l1)
##thread1 = threading.Thread (target = nums)
##thread1.start ()
##thread2 = threading.Thread (target = nums)
##thread2.start ()
##thread3 = threading.Thread (target = nums)
##thread3.start ()
##thread4 = threading.Thread (target = nums)
##thread4.start ()
##thread5 = threading.Thread (target = nums)
##thread5.start ()
