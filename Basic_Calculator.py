# Create Simple Calculator 

while True:
    try:
        
        # Takes input from the user. 
        
        number_1 = float(input("Enter First Number: ")) 
        
        number_2 = float(input("Enter Second Number: "))

        operator = input("Press '+' for Addition\tPress '*' for Multiplication\tPress '-' for Subtraction\tPress '/' for Division: ")

        def conditions(number_1, number_2, operator):
            """This functions checks conditions and prints accordingly"""
        
            match operator:     # Using Match-Case.
        
                case "+":       # In case of Addition.
                    add = number_1 + number_2   # Variable name add(Addition)  
                    print(f"Addition of {number_1} + {number_2} = {add}")
        
                case "-":       # In case of Subtraction. 
                    sub = number_1 - number_2       # Variable name sub(Subtraction)  
                    print(f"Subtraction of {number_1} - {number_2} = {sub}")

                case "*":       # In case of Multiplication.
                    mul = number_1 * number_2       # Variable name mul(Multiplication)  
                    print(f"Multiplication of {number_1} X {number_2} = {mul}")

                case "/":       # In case of Division.
                    div = number_1 / number_2       # Variable name div(Division)  
                    print(f"Division of {number_1} / {number_2} = {div}")

                case wrong_input:      # In case of Invalid input entered by the user.
                    print("Please enter Valid Operator for calculations[+, -, *, /]")

        conditions(number_1, number_2, operator)        # Calling Function / Output.
        
        
        choice = input("Do you want to recalculate?(y/n): ")    # Giving choice to the user to repeat.

        if choice == "n" or choice == "n".upper():      # If n or N entered by the user, it will stop working.
            break
        

    except ValueError:
        print("Please enter number, enter valid input!") 

    except ZeroDivisionError:
        print("Can't Divide the number by Zero!")       
