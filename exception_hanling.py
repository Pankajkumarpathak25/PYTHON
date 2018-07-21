#!/usr/bin/python


try:
    f_no=input("enter first No :")
    s_no=input("Enter Second No :")
    
   
   
    print "add :",f_no+s_no
    
    print "subtract :",f_no-s_no
    
    print "Multiply :",f_no*s_no   
   
    print "Divide :",float(f_no/s_no)
    

#except is used for customized error 

except NameError:
    print "please enter No not character !!"
except SyntaxError:
    print "you are using symbol ?? Go and read maths  "   
except ZeroDivisionError:
    print "integer division or modulo by zero"

#finally is used for all types of error customization
finally : 
    print "bye bye"

		
