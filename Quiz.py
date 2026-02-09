import random
# Functions - Passing Arguments
print('''Functions - Passing Arguments
Learn more about Functions here:
https://www.w3schools.com/python/python_functions.asp
''')      
print('''
Challenge #1
Run this code
Run, then Edit the code in the template example:
      
Can you follow and explain
- How arguments are passed from the main code to the function?
- Can you explain how a value is 'returned'
      ''')
print('''
----------------------------------------------------
''')

def my_math(x,y) :
  z=x+y
  return z

def main():
  my_num_1 = 5
  my_num_2 = 2
  sum = my_math(my_num_1, my_num_2)
  print("The sum of", my_num_1, "+", my_num_2, "=",sum)
  my_num_1 = 5
  my_num_2 = 2
  mult = multi(my_num_1, my_num_2)
  print("The multiplyed value of", my_num_1, "+", my_num_2, "=",mult)
  my_num_1 = 5
  my_num_2 = 2
  ev = even(my_num_1, my_num_2)
  print('The evened out value of', my_num_1, '+', my_num_2, '=', ev)
  my_num_1 = 5
  my_num_2 = 2
  rando = choose(my_num_1, my_num_2, False)
  print('value of the random choice function is', '=', rando)

# print('Done with Challenge 1')
print('''
----------------------------------------------------
''')

print('''
Challenge #2
Create a function that multiplies 2 numbers and returns the result
Enter Code Here:
----------------------------------------------------      ''')
# Enter Code Here:
def multi(x, y):
    z = x * y
    return z

    
print('''
----------------------------------------------------
''')

print('''
Challenge #3
Create a function that adds 2 numbers and if the result is odd, adds 1, then returns the result
Enter Code Here:
----------------------------------------------------      ''')
def even(x,y):
    z = x + y
    if(z%2 == 1):
        z = z + 1
    return z

print('''
----------------------------------------------------
''')
print('''
Challenge #4
Create a single function that takes the 2 argument numbers x,y 
and a 3rd argument, that selects between Addition, Subtraction, 
Multiplication, and Division, with the default being Addition. 
Then returns the result
Enter Code Here:
----------------------------------------------------      ''')
def choose(x,y,b):
    if (b == False):
        v = random.randint(1, 3)
        if (v==1):
            return multi(x, y)
        if (v==2):
            return x - y
        if (v==3):
            return x/y
    else:
        return my_math(x, y)


print('''
----------------------------------------------------
''')
main()
