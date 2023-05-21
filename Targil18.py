import random

# generate random number
ran = str(random.randint(1000, 9999))
print(ran)

# ask user for guess
user_guess = input('Guess 4-digit number: ')

# initialize cows and bulls counts
cows = 0
bulls = 0

# loop until user guesses correct number
while cows < 4:
    cows = 0
    bulls = 0

    # compare each digit of user's guess to random number
    for i in range(4):
        if ran[i] == user_guess[i]:
            cows += 1 
        elif user_guess[i] in ran:
            bulls += 1 

    # print number of cows and bulls
    print(f"{cows} cows, {bulls} bulls")

    # ask user for another guess
    if cows < 4:
        user_guess = input('Guess 4-digit number: ')

# print message when user guesses correct number
print('You guessed the number!')

