print('###############################')
print('Wellcome to the guessing game!')
print('###############################')
guess = 0
secret_number = 42
while guess != secret_number:
    guess = int(input('Type your guess:\n'))

    print('\nYou guessed:', guess,'\n')

    if secret_number == guess:
        print('You won. Congratulations\n')
    else:
        if guess > secret_number:
            print('Your guess is above the right number\n Pls try again.')

        if guess < secret_number:
            print('Your guess is under the right number\nPls try again')

