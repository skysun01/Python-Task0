#This program is done developed by Ansuman Rautray.
#Regd.No-1901106571,Brnch-I&E.
#This program prints the prime nos in an interval.
#This program cheks the number is prime or not.
def interval_check(start,end): 
 for val in range(start, end + 1):
     if val > 1:
        for n in range(2, val//2): 
            if (val % n) == 0: 
                break
        else:
          print(val,'is a prime no')
def prime_check(no):
    for n in range(2,no//2):
        if (no%n)==0:
            print(no,' is not a prime number')
            break
    else :
      print(no,'is a prime number')
print('Enter 1 to print the prime no in an interval ')
print('or Enter 2 to check whether a number is prime or not')
a=int(input())
if (a==1):
    try:
       start=int(input('Enter the starting no of interval '))
    except:
       start=int(input('Enter an integer Please '))
    try:
        end=int(input('Enter the ending no of interval '))
    except:
        end=int(input('Enter an integer Please '))
    interval_check(start,end)
    print('Thanx for using')
if(a==2):
   try:
      no=int(input('Enter the number '))
   except:
      no=int(input('Enter an integer Please '))
   prime_check(no)
   print('Thanx for using')
            
else :
    print('You did not choose anything')
    print('Visit again to use ^_^')
print('Vigit again ^_^')
