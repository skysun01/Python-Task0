#This program is done developed by Ansuman Rautray.
#Regd.No-1901106571,Brnch-I&E.
#This program gives sum of n numbers.
#Function to add n numbers
def sum_int(n):
    result=0
    for y in range(1,n+1):
        result=result+y
    return result
try:
  num=int(input('Enter the Nth number '))
except:
  num=int(input('Enter an integer Please '))  
#str_num(num)
#num=int(num)
result=sum_int(num)
print('The sum of 1 to' ,num ,'is', result)
print('Thnanx for using ^_^')
print('Visit Again')
