Num= int(input ("Enter a number: "))

lastdigit=Num%10

if (lastdigit%3==0):
    print("It is divisible by 3")
else:
    print("Sorry it is not divisible by 3")