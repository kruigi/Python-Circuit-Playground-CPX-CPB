def main():
    print("Starting Code Challenge")

    
    user_input = input("Enter an integer number 20 or greater > ")

    
    if user_input.isdigit():
        user_number = int(user_input)

        if user_number >= 20:
            print("Your number {user_number} is a valid Integer 20 or greater.  Thanks")

            count = 0
            print("Starting While Loop - Print Count Variable")
            print("The user input started as ", user_number)

            
            while user_number > 1:
                user_number = user_number / 2
                count += 1
                print("The current value of the user input after some math is", user_number)
                print(f"The while loop has looped {count} time")

            print("Ending While Loop")
            print(f"The While Loop, looped a total of {count} times")
        else:
            print("Number must be 20 or greater.")
    else:
        print("That is not a valid integer.")

    print("Ending Code Challenge")


main()
