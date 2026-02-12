# Functions - Passing Arguments
print('''Functions - Passing Arguments
Learn more about Functions here:
https://www.w3schools.com/python/python_functions.asp
''')      
print('''
Challenge #4
Run this code, then edit
Create a single function that takes the 2 argument numbers x,y 
and a 3rd argument, that selects between Addition, Subtraction, 
Multiplication, and Division, with the default being Addition. 
Then returns the result

Print the math operation and then the resulting equation

Enter Code Here:
----------------------------------------------------      ''')
# Edit and Enter Code Here:
def my_math(x, y, operation="add"):
    
    if operation == "add":
        result = x + y
        print(f"Addition: {x} + {y} = {result}")
        
    elif operation == "subtract":
        result = x - y
        print(f"Subtraction: {x} - {y} = {result}")
        
    elif operation == "multiply":
        result = x * y
        print(f"Multiplication: {x} * {y} = {result}")
        
    elif operation == "divide":
        if y == 0:
            print("Error: Cannot divide by zero.")
            return None
        result = x / y
        print(f"Division: {x} / {y} = {result}")
        
    else:
        print("Invalid operation. Defaulting to addition.")
        result = x + y
        print(f"Addition: {x} + {y} = {result}")
    
    return result


def main():
    my_num_1 = 5
    my_num_2 = 2
    
    my_math(my_num_1, my_num_2)
    my_math(my_num_1, my_num_2, "subtract")
    my_math(my_num_1, my_num_2, "multiply")
    my_math(my_num_1, my_num_2, "divide")
    
while True:
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        break   
        
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    
operation = input("Choose operation (add, subtract, multiply, divide): ")
    
my_math(x, y, operation)
    


main()
print('Done with Challenge 4')


print('''
----------------------------------------------------
''')
print('''
Challenge #5
in the main() function, add an input() request to get the x,y values.
- make sure they are numbers.
- in a while loop keep asking for the 2 values if one or both are 
  not a number
- make sure you do valid Error and Exception testing.
    ''')
