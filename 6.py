#This program is done developed by Ansuman Rautray.
#Regd.No-1901106571,Brnch-I&E.
#This program prints fibonacci sequence and can checks the no is fibonacci or not..
#function to print the sequence
import math
def Fib_Seq(n):
  # first two terms
  n1=0
  n2=1
  count = 0
  #check if the number of terms is valid
  if (n == 1):
    print("Fibonacci sequence upto",n,":")
    print(n1)
  else:
    print("Fibonacci sequence:")
    while (count < n):
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1   
#Function to check a number is perfect square or not.
def Perfect_Sqr(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
#Function to check the number is fibonacci or not.
def Is_Fibonacci(y): 
   return Perfect_Sqr(5*y*y + 4) or Perfect_Sqr(5*y*y - 4)
print('If you a want to check a number is fibonacci or not them enter 1')
print('or If you want to print N fibonacci numbers then enter 2')
a=int(input())
if (a==1):
  try:
     no=int(input('Enter the number you want to check '))
  except:
     no=int(input('Enter an integer Please '))
  if (Is_Fibonacci(no)==True):
          print (no, 'is a Fibonacci Number')
          print('Thanx for using')
  else:
      print(no,' is not a Fibonacci Number')
      print('Thanx for using')
if (a==2):
  try:
    no=int(input('Enter the no of terms You want to print '))
  except:
     no=int(input('Enter an integer Please '))
  Fib_Seq(no)
  print('Thanx for using')
else :
   print('You did not choose anything')
   print('Visit again to use ^_^')
print('Vigit again ^_^')
