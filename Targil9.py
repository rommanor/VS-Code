#usr/bin/python3
import random
ran = random.randint(1, 9)
print(ran)
number = int(input('Guess the number: '))


while number != ran:
 
    
    if number > ran:
       print ("too high!")
    elif number < ran: 
       print ("too low!")
    number = int(input('Guess the number again: '))

print ("exactly right!")