number=int(input('Enter a number'))

if(number%400==0 or (number%4==0 and number%100!=0) ):
    print('yes it is a leap year')
else:
    print("Sorry it is not leap year")
