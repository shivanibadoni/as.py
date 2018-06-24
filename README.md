# as.py
#Q1
#This code generates a "divide by zero error" which in python is called
#ZeroDivisionError.This error occurs whenever a denominator in a fraction is assigned or
#provided with value equal to Zero.The above error can be handled in the following
#way:

""
a=3
try:
    if a<4:
        a=a/(a-3)
        except ZeroDivisionError:
            print("Divide by zero error occured.Handling this...")
            a=0
            print("Value of a: ",a)


#Q2
#This code generates a "list index out of range"error.It is handled by the
#IndexError exception This error occurs whenever we try to access elements
#whose index is greater than length of list i.e. here the max index is 2 but
#we are trying to access third index element of the list.
#The above error can be handled in the following way:
""
I=[1,2,3]
try:
    print(I[3])
    except IndexError as e :
        print(e,".Handling this...")

#Q3
#output :
        #An exception
        Traceback(most recent call last):
            File "python",line 42,in<module>
            NameError:Hi there


#Q4
            #output:
            -5.0
            a/b result in 0



#Q5
            #Generation of errors
            I=[1,2,3]
            print(I[4]) 
            x=int(('Please enter a number:'))
            from math import Shivani

            I=[1,2,3]
            try:
                print(I[4])
                x=int(('Please enter a number:'))
                from math import Shivani
                except IndexError as E:
                    print(E)
                    except ValueError:
                        print("oops!! Kindly enter digits/integers,nothing")
                        except ImportError:
                            print(error._class_._name_+":import it")


#Q6
class Error(Exception):
    pass
class AgeTooSmallError(Error):
    #User-defined error
    pass
while True:
    val=int(input("Enter age:"))
    try:
        if val<18:
            raise AgeTooSmallError
                else:
                    print("Your age:",val)
                    break
                except AgeTooSmallError:
                    print("Age is less than 18.Enter value equal to or greater than 18.Try again!!")

print()
print("You are out of loop")
            
            
 
