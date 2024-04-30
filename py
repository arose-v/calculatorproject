import sys

# Define the calculator function.
def calculator():
    # Ask the user to input the type of calculation they want to perform.
    print("What type of calculation would you like to perform?")
    op = input("Enter + - * / : ")

    # Ask the user to input their first number and convert into a floating point.
    print("Enter your first number")
    first_num = float(input())

    # Ask the user to input their second number and convert into a floating point.
    print("Enter your second number")
    second_num = float(input())

    # Use the user's input to perform the calculation.
    if(op == "+"):
        first_num = first_num + second_num
        print(f"Total: {first_num}")

    elif (op == "-"):
        first_num = first_num - second_num
        print(f"Total: {first_num}")

    elif (op == "*"):
        first_num = first_num * second_num
        print(f"Total: {first_num}")

    elif (op == "/"):
            first_num = first_num / second_num
            print(f"Total: {first_num}")

    # Ask the user if they would like to perform another calculation by inputting yes or no.
    print("Would you like to go again?")
    restart = input("Yes or No: ")

    # If yes, restart the calculator function.
    if restart.upper() == "YES":
            calculator()

    # If no, exit the program.
    else:
        sys.exit("See you next time!")

# Call the calculator function.
calculator()

