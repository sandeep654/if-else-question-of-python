cost_price=int(input("Enter a cost price: ")) #take input from user 

 #int variable

if(cost_price>100000):
    cost_price=(cost_price*15)/100
    print(cost_price)
elif(100000>=cost_price>50000):
    cost_price=(cost_price*10)/100
    print(cost_price)
elif(50000>=cost_price>0):
     cost_price=(cost_price*5)/100
     print(cost_price)
else:
    print("You Entered invalid cost_price")

