num1 = int(input("Enter a num1 value : "))
num2 = int(input("ENter a num2 value : "))

user = int(input("Select Operation: \n 1.Additon \n 2.Subtraction \n 3.Multiplication \n 4.Division : \n"))

if user == 1: 
    add = num1 + num2
    print(f"The addition of {num1} + {num2} is : {add} ")

elif user == 2:
    sub = num1 - num2
    print(f"The subraction of {num1} - {num2} is : {sub} ")

elif user == 3:
    mul = num1 * num2
    print(f"The multiplication of {num1} * {num2} is : {mul} ")

elif user == 4:
    if num2 !=0:
        div = num1 / num2 
        print(f"The division of {num1} / {num2} is : {div:.2f} ")
    else:
        print("Division is not support by zero")

else:
    print("Please enter the given operation")
