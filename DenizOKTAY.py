# This program can be used for string handling instead of
# upper(),lower(),capitalize() and title() methods.
# This program does the same thing without using this methods.

#Output which explains the purpose of the program
print("This program is an alternative way to make changes in strings")
print("without using upper(),lower(),capitalize() and title() methods")
#Input the string
mystring = input("Please enter a string: ")

#Find out how long the string is and output 
lengthOfMystring=len(mystring)
print("Length of the String: ",lengthOfMystring)

#Create a new string for to store the modifications.
Newstring=""

#i is index number of mystring.And we will start to modify string
#from the first character of the string.
i=0

#This option does the same thing as  upper() method.
# Ex: INPUT--> Computer Systems Administration
#					OR
#    		   computer systems administration
#					OR
#	 		   CoMpuTer sySteMs AdmIniStration
#     OUTPUT-->COMPUTER SYSTEMS ADMINISTRATION
print("1.Uppercase all letters of the string")

#This option does the same thing as  lower() method.
# Ex: INPUT--> Computer Systems Administration
#					OR
#    		   COMPUTER SYSTEMS ADMINISTRATION
#					OR
#	 		   CoMpuTer sySteMs AdmIniStration
#     OUTPUT-->computer systems administration
print("2.Lowercase all letters of the string")

#This option does the same thing as  capitalize() method.
# Ex: INPUT--> Computer Systems Administration
#					OR
#    		   computer systems administration
#					OR
#	 		   CoMpuTer sySteMs AdmIniStration
#					OR
#    		   COMPUTER SYSTEMS ADMINISTRATION
#     OUTPUT-->Computer systems administration
print("3.Uppercase the first letter and lowercase all remaining")
print("letters of the string")

#This option does the same thing as  title() method.
# Ex: INPUT--> COMPUTER SYSTEMS ADMINISTRATION
#					OR
#	 		   CoMpuTer sySteMs AdmIniStration
#					OR
#    		   computer systems administration
#     OUTPUT-->Computer Systems Administration
print("4.Uppercase the first letter and lowercase all remaining")
print("letters of each word in the string")

#Input the choice
chosen = input("Please choose one of the options above: ")

#Each character has a number from 0 to 65,535.
#The number value for each character is defined by an international 
#standard called Unicode.
#In this program I used Unicode values of 'a','z','A','Z'
#The symbol for the letter A is represented by character number 65.
#The symbol for the letter Z is represented by character number 90.
#The symbol for the letter a is represented by character number 97.
#The symbol for the letter z is represented by character number 122.

if chosen == '1':
	while i<lengthOfMystring:
		#The ord() method returns an integer representing the Unicode  
		#value of the character	
		#If i th character of the string is a lower case
		if ord(mystring[i])>=97 and ord(mystring[i])<=122:
		#By subtraction 32(the difference between lower case and upper
		#case) we will change the lower case character to upper case.
			x=ord(mystring[i])-32
		#The chr() method returns a string representing a character 
		#whose Unicode value is an integer.
			y=chr(x)
		#We will add it to new string 
			Newstring = Newstring + y
		#At next step we will check the next character of string
			i=i+1
			
		#If i th character of the string is not a lower case	
		else:
		#We will add it to new string
			Newstring = Newstring + mystring[i]
		#At next step we will check the next character of string
			i=i+1
	print("After processing, your string is: ",Newstring)
	
elif chosen == '2':
	while i<lengthOfMystring:
		#If i th character of the string is a upper case
		if ord(mystring[i])>=65 and ord(mystring[i])<=90:
		#By summation 32(the difference between lower case and upper
		#case) we will change the upper case character to lower case.
			x=ord(mystring[i])+32
			y=chr(x)
			Newstring = Newstring + y
			i=i+1
		#If i th character of the string is not a upper case
		else:
			Newstring = Newstring + mystring[i]
			i=i+1
	print("After processing, your string is: ",Newstring)

elif chosen == '3':
	#If FIRST character of the string is a lower case
	if ord(mystring[0])>=97 and ord(mystring[0])<=122:
			x=ord(mystring[0])-32
			y=chr(x)
			Newstring = Newstring + y
			i=i+1
	#If FIRST character of the string is not a lower case
	else:
		Newstring = Newstring + mystring[0]
		i=i+1
	while i<lengthOfMystring:
		#If i th character of the string is a upper case
		if ord(mystring[i])>=65 and ord(mystring[i])<=90:
		#By summation 32(the difference between lower case and upper
		#case) we will change the upper case character to lower case.
			x=ord(mystring[i])+32
			y=chr(x)
			Newstring = Newstring + y
			i=i+1
		#If i th character of the string is not a upper case
		else:
			Newstring = Newstring + mystring[i]
			i=i+1
	print("After processing, your string is: ",Newstring)
	
elif chosen == '4':
	#If FIRST character of the string is a lower case
	if ord(mystring[0])>=97 and ord(mystring[0])<=122:
			x=ord(mystring[0])-32
			y=chr(x)
			Newstring = Newstring + y
			i=i+1
	#If FIRST character of the string is not a lower case
	else:
		Newstring = Newstring + mystring[0]
		i=i+1
	while i<lengthOfMystring:
		#If i th character of string is space
		if mystring[i]==' ':
			Newstring = Newstring + mystring[i]
			i=i+1
			#If the character after the space is a lower case
			if ord(mystring[i])>=97 and ord(mystring[i])<=122:
				x=ord(mystring[i])-32
				y=chr(x)
				Newstring = Newstring + y
				i=i+1
			#If the character after the space is not a lower case
			else:
				Newstring = Newstring + mystring[i]
				i=i+1
		#If i th character of string is not space		
		else:
			#If i th character of the string is a upper case
			if ord(mystring[i])>=65 and ord(mystring[i])<=90:
			#By summation 32(the difference between lower case and upper
			#case) we will change the upper case character to lower case.
				x=ord(mystring[i])+32
				y=chr(x)
				Newstring = Newstring + y
				i=i+1
			#If i th character of the string is not a upper case
			else:
				Newstring = Newstring + mystring[i]
				i=i+1
			
	print("After processing, your string is: ",Newstring)
	
else:
	print("Invalid choose")

