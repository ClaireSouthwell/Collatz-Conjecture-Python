# Given a number, the collatz function will either divide it by 2 (if even) or multiply by 3 and add 1 (if odd) until 1 is reached.

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number
    
print('Enter a number:')        
userInput = int(input())
newNumber = collatz(userInput)
while newNumber > 1:
    newNumber = collatz(newNumber)
