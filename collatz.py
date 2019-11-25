# Given a number, the collatz function will either divide it by 2 (if even) or multiply by 3 and add 1 (if odd) until 1 is reached.

def collatz(number):
    try:
        if int(number) % 2 == 0:
            number = int(number) // 2
            print(number)
            if number > 1:
                collatz(number)
            return number
        else:
            number = 3 * int(number) + 1
            print(number)
            collatz(number)
            return number
    except ValueError:
        print('Please enter an integer.')
        
print('Enter a number:')        
userInput = input()
collatz(userInput)
