#type casting to float, can also typecast to int

deposit_amount=float(raw_input("Enter intial deposit amount $")) 
balance=deposit_amount 
#calculating SI for each year and adding it to balance to make it a cumulative interest
for i in range(0,3): 
    simple_interest = balance*0.05
    balance+=simple_interest

#Alternative way to calculate balance
#balance=balance * 1.05**3

print ("Final balance is ${0:.2f}").format(balance) 


# {0:.2f} first 0 is the placeholder, 
# : indicates formatting, .2f means 2 decimal places after float
#control+/ = comments out blcoks of code
#Green colour - function : We can use key words but then the original function cannot be used. 
#for Eg you can use sum=x but then original sum will not work
# the limit per line is 80 characters (the solid line at the right for readability)

print("this is a \ndemo of \nchanging lines")

prompt ='I want to use a really long line to tell you that your\n'
prompt+='balance after three years is ${0:.2f}'.format(balance)