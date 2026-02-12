# Python Lab
print('Playing with Builtin Python Functions')
student_name = "Daniel Kumar"
program_creation_date = "2/10/2026"
print(student_name)
print(program_creation_date)
print('''Functions Introduction
There is a big list of built-in functions here:
https://www.w3schools.com/python/python_ref_functions.asp
''')     
print('''This Lab is about using Python Builtin Functions. Try and show code using the following functions, then pick 4 more to try. ...
- print()
- input('enter something here: ')
- int()
- type()
- abs()
- len()

My code follows:''')
# update the 'student_name' and 'program_creation_date' variables and add your code here:
x = 4.2
print(x)
y = input('enter an integer here here: ')
x = int(x)
print(type(y))
print(abs(x - x*2))
print(len(student_name))
z = float(x)
my_list = list(range(4))
for v in range(4):
    my_list[v] = pow(z, v)
    print(my_list[v-1])
