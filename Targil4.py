#usr/bin/python3

number = int(input("Enter a number: ")) # ask user for a number

divisors = [] # create an empty list to store the divisors

# iterate over all possible divisors from 1 to number
for i in range(1, number+1):
    # if i divides number exactly (with no remainder), add it to the list of divisors
    if number % i == 0:
        divisors.append(i)

# print out the list of divisors
print("The divisors of", number, "are:", divisors)

