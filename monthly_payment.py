principal = float(raw_input("Enter amount borrowed: $"))
rate = float(raw_input("Enter rate: "))
time = float(raw_input("Enter time: "))

temp = rate/1200.0 #use .0 otherwise it will do an integar division and give quotient
payment = temp*principal/(1-(1+temp)**(-12*time))

print("Your monthly payment is ${0:.2f}").format(payment)