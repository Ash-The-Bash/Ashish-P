#User input program for gym membership(INVOICE) and calculate BMI
#BMI = weight(kgs)/height(m^2)
#Get personal details
print('----Welcome to the FITNESS Portal----')
name = str(input('Enter name: '))
age = float(input('Enter Age: '))
address = str(input('Enter Address: '))

#Membership options
print('\n----Memeberships----')
print('> Press 1 for 3 months membership')
print('> Press 2 for 6 months membership')
print('> Press 3 for 12 months membership')

membership = int(input('Enter Membership Number: '))
if membership == 1:
    print('          Thank you              ')
elif membership == 2:
    print('          Thank you             ')
elif membership == 3:
    print('           Thank you              ')
else:
    print('Invalid \n ')

#BMI calculation
print('----BMI----')
height_cm = float(input('Enter Height (cms): '))
height_m = (height_cm/100)
weight = float(input('Enter Weight (kgs): '))
bmi = (weight/(height_m*height_m))
print('-----------')

#Print the bill
print('\nPrinting the bill....')

print('\n|-----------------*Ash Gym*-----------------|')
print(' Name: %s                                    '%name)
print(' Age: %d                                     '%age)
print(' Address: %s                                 '%address)
#print('|-------------------------------------------|')
if membership == 1:
    print('|-------------------------------------------|')
    print('|      3 months membership activated        |')
    print('|-------------------------------------------|')
elif membership == 2:
    print('|-------------------------------------------|')
    print('|       6 months membership activated       |')
    print('|-------------------------------------------|')
elif membership == 3:
    print('|-------------------------------------------|')
    print('|      12 months membership activated       |')
    print('|-------------------------------------------|')

#Healthy weight: BMI of 19 to 24.9
#Overweight: BMI of 25 to 29.9
#Obese: BMI of 30 and above
print('|         Your BMI is ' + '%.4s                  |'%bmi)
if bmi < 19:
    print('|         Result : Underweight              |')
elif bmi >=19 and bmi <=24.9:
    print('|         Result : Healthy                  |')
elif bmi >=25 and bmi <=29.9:
    print('|         Result : Overweight              |')
elif bmi >= 30:
    print('|         Result : Obese                    |')
print('|         Hope to see you soon :)           |')
print('|-------------------------------------------|')

if membership == 1:
    print('|Total                               Euro 25|')
    print('|-------------------------------------------|')
elif membership == 2:
    print('|Total                               Euro 60|')
    print('|-------------------------------------------|')
elif membership == 3:
    print('|Total                              Euro 100|')
    print('|-------------------------------------------|')

#The end





