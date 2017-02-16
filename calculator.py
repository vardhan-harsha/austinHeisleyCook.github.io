import sys
import os
import winsound
import time
counter = 1


while True:
 os.system("title my calculator && color 1b ")	
 x = int(input("first integer:"))
 y = int(input("second integer:"))
 operator = input("operation:") 
 if operator == "+":
  print("\tresult:")	 
  print(x + y)
  counter=counter-1
  restart = input("do you want to try another calculation? type yes/no")
  if restart == "no":
   sys.exit()	
  if restart == "yes":
   counter = 1 
 if operator == "-":
  print("result:")	 
  print(x - y)
  counter=counter-1
  restart = input("do you want to try another calculation? type yes/no")
  if restart == "no":
   sys.exit()	
  if restart == "yes":
   counter = 1 
 if operator == "/":
  print("result:")	 
  print(x / y)
  counter=counter-1
  restart = input("do you want to try another calculation? type yes/no")
  if restart == "no":
   sys.exit()	
  if restart == "yes":
   counter = 1 	
 if operator == "*":
  print("result:")	 
  print(x * y)	  	
  counter=counter-1
  restart = input("do you want to try another calculation? type yes/no")
  if restart == "no":
   print("created by technowizard")	  
   time.sleep(4)	  
   sys.exit()	
  if restart == "yes":
   counter = 1
  if restart != "no" or restart != "yes" or restart == "":
   winsound.Beep(90,90)  
   os.system("color a3")
   restart = input(restart +" is not a valid answer do you want to try another calculation? type yes/no")
    	  
   
 
 		


