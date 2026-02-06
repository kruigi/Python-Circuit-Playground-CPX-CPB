def main():
    print("Starting Code Challenge")
    # Print The User Input
    print("Starting While Loop - Print Count Variable, input integer from 0-9")
    y = 0
    print("Starting While Loop - Print Count Variable")
    while y <= 10:
        
        
        try:
            x = int(input())
            print(x)
            if x == y:
                print("the user input and count are equal")
        except:
            print("please put an integer in")
        y = y + 1    
    
    print("Ending While Loop")
    print("Ending Code Challenge")

main()
