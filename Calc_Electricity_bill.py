unit = int(input("Enter a units : "))

amt=0

if(0<unit<=100):
    print("no charge")
elif(100<unit<=200):
    amt=(unit-100)*5
    print("Electricity bill is ",amt)
elif(unit>200):
    amt=500+(unit-200)*10
    print("Electricity bill is " , amt)

