number=int(input("Enter a number:"))
last_digit=number%10
first_digit=number//10

number2=first_digit-(last_digit*2)
print (number2)

if(number2%7==0):
    print("yes it is divisible by 7")
else:
    print("no it's not divisible by 7")


