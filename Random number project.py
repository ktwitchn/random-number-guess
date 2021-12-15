import random

rules = input("Welcome to my game, would you like to hear the rules?: ")

if rules != "yes".lower():
    pass
else:
    print("To play you first enter a number to dictate the top of the range. \n A random number will be generated and your job is to guess the number.")

number_of_guesses = 0

user_range_limit = input("Give a range: ")

if user_range_limit.isdigit():
    user_range_limit = int(user_range_limit)

    if user_range_limit <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number")
    quit()
    
random_number = random.randint(0, user_range_limit)


while True:
    number_of_guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You guess correct!")
        break
    elif user_guess == "end":
        end()
    elif user_guess == 9999999:
        print(random_number)    
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")
        

print("It took you", number_of_guesses, "tries to get the right answer!")
