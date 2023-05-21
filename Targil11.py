#usr/bin/python3

# ask the user for a number
num = int(input("Enter a positive integer: "))

# check if the number is prime or not
if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
     

    