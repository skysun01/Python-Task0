#This program is done developed by Ansuman Rautray.
#Regd.No-1901106571,Brnch-I&E.
#This program prints the letter at even position.
#Function to check letters' at even position
def even_position(str):
  for i in range(1, len(str), 2):
    print("position ",i+1,"", str[i] )
Str = input("Enter String ")
print("Printing the letters present at even position")
even_position(Str)
print('Thnanx for using ^_^')
print('Visit Again')
