import random
print('''
hello 
plz guess a number 
      ''')
number = int(input(''))
num_guess = random.randint(1, 3)
guess = False
counter = 0
while guess == False:
    if number == num_guess:
        print(
            f'good job you are correct , you succeed with {counter+1} guesses')
        break
        guess = True
    elif number < num_guess:
        print('It is too far down guess..')
        counter += 1
    elif number > num_guess:
        print('It is too far up guess..')
        counter += 1

    elif number+10 == num_guess or number-10 == num_guess:
        print('BUT YOU ARE CLOSE!')
    print('''
    hello 
    plz guess a number 
    ''')
    number = int(input(''))
