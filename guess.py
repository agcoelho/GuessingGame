print('###############################')
print('Wellcome to the guessing game!')
print('###############################')

secret_number = 42

guess = int(input('type your guess:\n'))

print('\nyou guessed:', guess,'\n')

if secret_number != guess:
    print('\nyou loose.\ngood luck next time.\n')
else:
    if guess > secret_number:
        print('your guess is above the right number')

    if guess < secret_number:
        print('your guess is under the right number')
        
