# Python if statment syntax example
# If the number is negative, we print an appropriate message

num=40
if num>0:
    print(num,"is the a positve number.")
    print("This is always printed.")

num=-1
if num > 0:
    print(num,"is a positive number.")
print("This is also always printed.")

# Program checks if the number is positive or negative
# And displays an appropriate message
num =2
if num>=0:
    print("Positive or Zero")
else:
    print("Negative number")  

# Example of if elif else 
# num=3.5
# num=-4.5
num=4
if num>0:
    print("Positive number")
elif num==0:
    print("Zero")
else:
    print("Negative number")  


# Python Nested if examle 
num=float(input("Enter a number: "))
if num>=0:
    if num==0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")



    
