##num1 = 5
##num2 = 6
##sum = num1 + num2
##print (sum)

##num1 = 4
##num2 = 2
##num3 = num1 / num2
##num3v2 = num1 // num2
##num4 = num1 % num2
##print ('Quotient',num3)
##print (num3v2)
##print (num4)

##print ('Enter your name - ')
##name = input ()
##print ('Your name is',name)

##print ('1st Number:')
##num1 = int (input ())
##print ('2nd Number:')
##num2 = int (input ())
##print ('3rd Number:')
##num3 = int (input ())
##print ('4th Number:')
##num4 = int (input ())
##total = num1+num2+num3+num4
##print (total)

##print ('What is your year of birth?')
##year = int (input ())
##age = 2019 - year
##agedays = age * 365
##print (age,agedays)

##print ('What is the temperature in Fahrenheit?')
##fahrenheit = (int (input()))
##celsius =5/9*(fahrenheit-32)
##print ('The temperature in Celsius is',celsius)

##print ('What is the speed of your spaceship?')
##speed = (int (input ()))
##time = 384400 // speed
##print ('The time it takes to get to the moon is',time)

##print ('How many quarters do you have?')
##q = (int (input()))
##print ('How many dimes do you have?')
##d = (int (input()))
##print ('How many nickels do you have?')
##n = (int (input()))
##print ('How many pennies do you have?')
##p = (int (input()))
##quar = q*0.25
##nic = n*0.05
##dime = d*0.1
##pen = p*0.01
##total = quar+nic+dime+pen
##print ('The total amount of money you have is $',total)

##a=1
##if a < 1:
##    print ('Hello')
##elif a==1:
##    print ('Hello (elif)')
##elif a >= 1:
##    print ('Hello (2)')
##else:
##    print ('World')
##if a == 1:
##    print ('Hello (elif)')
##else:
##    print ('World')

##print ('Enter your age:')
##age = (int (input ()))
##if age >= 16:
##    print ('You are eligible to drive.')
##elif age < 16:
##    time = 16 - age
##    print ('Sorry, you can" drive yet. You will have to wait',time,'more years.')

##print ('What is your gender? What is your name?')
##gender = input ()
##name = input ()
##if gender == 'male' or gender == 'Male':
##    print ('Hello Mr.',name)
##elif gender == 'female' or gender == 'Female':
##    print ('Hello Ms.',name)

##print ('Type in a number:')
##num = (int (input ()))
##remainder = num % 2
##if remainder == 1:
##    print ('The number is odd')
##elif remainder == 0:
##    print ('The number is even')

##print ('Type in a score:')
##scr = (int (input()))
##if scr <= 100 and scr >= 90:
##    print ('Your grade is A')
##elif scr >= 80:
##    print ('Your grade is B')
##elif scr >= 70:
##    print ('Your grade is C')
##elif scr >= 60:
##    print ('Your grade is D')
##elif scr < 60 and scr > 0:
##    print ('Your grade is F')
##else:
##    print ('Invalid Score')

##print ('What is your age?')
##age = int (input ())
##print ('What is your grade?')
##grade = int (input ())
##if age >= 8 and grade >= 3:
##    print ('Your are eligible to play the game.')
##else:
##    print ('You are not eligible to play the game.')

print ('Do you have an upcoming vacation')
answer = input ()
if answer == 'yes':
    print ('What grade are you in?')
    grade = int (input ())
    if grade != 12:
        print ('Have an adventurous vacation.')
    else:
        print ('Great time to study for SAT.')
else:
    print ('Study hard at School.')
