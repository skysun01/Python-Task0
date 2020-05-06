#This program is done developed by Ansuman Rautray.
#Regd.No-1901106571,Brnch-I&E.
#This program gives the no of digits present in a number.
#Function to count the digits.
def no_int(n):
    r=int(0) 
    while(n!=0):
        r=r+1
        n=n//10
    else:    
     return r
num=int(input('Enter the number '))
#str_num(num)
#num=int(num)
result=no_int(num)
print('The no of digits in this number is ',result)
print('Thnanx for using ^_^')
print('Visit Again')
