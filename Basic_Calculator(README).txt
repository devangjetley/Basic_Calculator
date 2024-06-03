# Basic Calculator

## Introduction

This Python script is a user-friendly calculator that performs basic arithmetic operations (Addition, Subtraction, Multiplication, and Division) with clear instructions and error handling.

## Features

1. **Match Case**: Uses a match case for cleaner and more readable code.
2. **Continuous Calculation**: Calculates until the user decides to exit.
3. **Error Handling**: Handles errors for invalid input and division by zero.
4. **f-string**: Uses f-strings to make the code cleaner and easier to maintain.

## How to Use

1. **Run the Program**: Execute the script.
2. **Enter Inputs**: Enter two numbers and select an operator ['+', '-', '*', '/'] when prompted.
3. **View Result**: The program will display the output.
4. **Continue or Exit**: You will be given a choice if you wish to continue. Enter 'y' to continue or 'n' to stop.

## Code Explanation

1. The script uses a `while True` loop that runs continuously, prompting the user for input.
2. Inside the loop, the script uses a `try-except` block to handle any `ValueError` exceptions that may occur when the user enters invalid input.
3. The `number_1` and `number_2` variables store the user-provided numbers, and the `operator` variable stores the selected operator.
4. The `conditions` function checks the selected operator and prints the output accordingly.
5. Then the user is asked, "Do you want to recalculate? (y/n):" to determine whether they want to continue or exit the program.
6. If the user presses 'n', the `break` statement is executed; otherwise, the script runs again.
