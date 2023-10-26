income=int(input('Enter your monthly income : '))
age=input("Enter your age:")
if income>=35000:
  if(age>=30):
    print("You have to pay 12 percent tax")
  else:
    print("You have to pay 10 percent tax")
else:
   print('You can pay less than 12 percent tax')
 
   