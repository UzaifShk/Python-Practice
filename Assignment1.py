# Write a program to take user input and check whether the number is positive, if it's check whether 
# it is single, double, or three digits.

user_input = input("Enter any Number to check Positive and Digits: ")
user_input_length = len(user_input)

if int(user_input) >= 0:
    if len(user_input) == 1:
        print(f"Your Number is Positive and Digits is {user_input_length}")
    elif len(user_input) == 2:
        print(f"Your Number is Positive and Digits is {user_input_length}")
    elif len(user_input) == 3:
        print(f"Your Number is Positive and Digits is {user_input_length}")
    else:
        print(f"Your Number is Positive but more than four Digits {user_input_length}")

else:
    print("You Entered a Negative Number")

# Write a program to take three user inputs and find the smallest number.
a = int(input("Enter First Number: "))
b = int(input("Enter your Second Number: "))
c = int(input("Enter your Third Number: "))

if a <= b and a <= c :
    print(f"a is tha Smallest Number: {a}")
elif b <= c and b <= a:
    print(f"b is the Smallest Number: {b}")
else:
    print(f"c is the Smallest Number: {c}")


