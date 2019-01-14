from random import randint

rand_number = randint(1, 20)
user_number = int(input('Pick a number between 1-20: '))

if user_number in range(1, 21):
    total_lives = 0
    while total_lives < 3:
        if rand_number == user_number:
            return True
        elif rand_number != user_number:
            total_lives += 1
            return False
else:
    return 'Your value is out of range'
