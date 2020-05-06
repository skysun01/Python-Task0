#This program is done developed by Ansuman Rautray.
#Regd.No-1901106571,Brnch-I&E.
#This program gives sum or produt of two numbers.
#function to add or multiply
def product_or_sum(n1,n2):
  product =n1*n2
  if(product <= 1000):
   print('The product of these two number is ',product)
  else:
      print('The sum of these two number is ',n1+n2)     
try:
  a=int(input('Enter first no '))
except:
  a=int(input('Enter an integer '))
try:
    b=int(input('Enter second no '))
except:
    b=int(input('Enter an integer '))
product_or_sum(a,b)
print('Thnanx for using ^_^')
print('Visit Again')
