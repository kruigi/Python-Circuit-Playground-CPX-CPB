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
def greet(lang):
  if lang == 'es':
    return'Hola'
  elif lang == 'fr':
    return'Bonjour'
  elif lang == 'sw':
    return 'Jambo'
  elif lang == 'Ukr':
      return 'pryvit'
  elif lang == 'El':
      return 'Le suilon'
  else:
    return'Hello'

def main():
    print(greet('en'),'Glenn')
    print(greet('fr'),'Sabine')
    print(greet('es'),'Carlos')
    print(greet('sw'),'Carlos')
    print(greet('Ukr'),'Carlos')
    print(greet('El'),'Carlos')
    
    x = input("what is your name?")
    y = input("what is your language?")
    
    print(greet(y) + ' ' + x)
main()

print('''
Challenge #2
Add a few new Languages…
Swahili, Ukrainian, Middle Earth Elven, or maybe Klingon

Challenge #3
Add asking the User for their name and language, then say hi.
      ''')
