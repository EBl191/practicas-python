number = input("This program will tell you if a number of your choice is multiple of ten. Write a number: ")
number = int(number)

if number % 10 == 0:
    print(f'The number {number} is a multiple of 10.')
else: 
    print(f'The number {number} is not a multiple of 10.')