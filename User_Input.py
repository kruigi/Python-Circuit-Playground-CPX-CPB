x = input('enter a number > ')
x = int(x)
y = 23
if(x==y):
    print(x, 'is equal to', y)
    print('something else')
elif(x>y):
    print(x, 'greater than ', y)
    print('something else')
else:
    print(x, 'is less than', y)
    print('else')
print('done')
