print('###############################')
print('Wellcome to the guessing game!')
print('###############################')
guess = 0
secret_number = 42
above = guess > secret_number
under = guess < secret_number
attempts = 5
while attempts > 0 and guess != secret_number:
    print('attempts left:', attempts)
    guess = int(input('Type your guess:\n'))

    print('\nYou guessed:', guess,'\n')

    if secret_number == guess:
        print('You won. Congratulations\n')
    else:
        if above:
            print('Your guess is above the right number.\n')
            attempts = attempts - 1
            if attempts > 0:
                print('Pls try again')
            else:
                print('you loose')
        elif under:
            print('Your guess is under the right number.\n')
            attempts = attempts - 1
            if attempts > 0:
                print('Pls try again')
            else:
                print('you loose')
            
