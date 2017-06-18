time= float(raw_input("Enter the time (in seconds) between seeing \nlightening and hearing thunder "))
#A storm is 1 mile away for every 5 second time gap between lightening and thunder

#if one side of the division is float python automatically makes the calculation as float
#But you loose accuracy for very accurate scientific calculations
#Ooptions are to use double or decimal type

distance=0.2*time #distance = time/5.0
 
print("The Storm is {0:.2f} miles away").format(distance)

