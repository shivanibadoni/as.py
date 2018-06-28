#Q1.handle the exception occured in the program

"""
This code generates a "divide by zero error" which in python is called ZeroDivisionError.
This error occurs whenever a denominator in a fraction is assigned or provided with value equal to Zero.
The above error can be handled in the following way:

"""
a=3
try:
  if a<4:
    a=a/(a-3)
except ZeroDivisionError:
  print("Divide by zero error occured. Handling this...")
  a=0
print("Value of a: ",a)


#Q2.handle the exception occurred in the program
"""

This code generates a  "list index out of range" error . It is handled by the IndexError exception
This error occurs whenever we try to access elements whose index is greater than length of list i.e. here
the max index is 2 but we are trying to access third index element of the list.
The above error can be handled in the following way:

"""
l = [1,2,3]
try:
  print(l[3])
except IndexError as e:
  print(e, ". Handling this....")



#Q3. output of the program

"""
OUTPUT:

An exception
Traceback (most recent call last):
  File "python", line 42, in <module>
NameError: Hi there


Explaination:
When we try to raise the name error, we get it and hence our control goes to except case.
Here the print statement is executed & when we raise the error we print the error message provided in the 
try block as the handler can use the message.
"""


#Q4. output of the program
"""

OUTPUT:
-5.0
a/b result in 0


Explaination:

Case1: AbyB(2.0,3.0)
Here a = 2.0, b = 3.0. So, c = ((2.0 + 3.0)/(2.0 - 3.0 )) = 5.0 /-1.0 = -5.0
Hence, no exceptions occurs in try block so our control goes to else block to print the value of c

Case2: AbyB(3.0,3.0)
Here a = 3.0, b = 3.0. So, c = ((3.0 + 3.0)/(3.0 - 3.0)) = 6.0/0 = Undefined/Infinty
Hence we get a divide by zero error this time. Thus, try block sends control to ZeroDivisionError exception
block where we print our error message.
"""

#Q5. program to show and handle Import error, Value Error & Index error

"""
#Generation of errors

l= [1,2,3]       
print(l[4])                   #Index Error as list element we are trying to access is out of range of list
x = int(('Please enter a number: '))            #Value Error when input is not of integer type 
from math import Gaurav                         #Import error occurs when path for import is not correct

The above errors can be handled in the following way: 
"""
    
l = [1,2,3]
try:
 print(l[4])                  
 x = int(('Please enter a number: '))            
 from math import Gaurav                         
except IndexError as E:                         
  print(E)
except ValueError:
  print("OOPS!! Kindly enter digits/integers, nothing else")
except ImportError:
  print(error.__class__.__name__ + ": Sahi se import karo dost")


#Q6. Create a user defined error & run the program until user input is not correct

class Error(Exception):
  pass
class AgeTooSmallError(Error):                                         #User-defined error
  pass
while True:
  val = int(input("Enter age: "))
  try:
    if val < 18:
      raise AgeTooSmallError                                           #Raise error when age is less than 18
    else:
      print("Your age: ",val)
      break
  except AgeTooSmallError:
    print("Age is less than 18. Enter value equal to or greater than 18. Try again!!")
    print()
print("You are out of loop")
