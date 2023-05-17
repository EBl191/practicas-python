fruits = ["pineapple", "coconut", "banana", "guanabana", "mango"]

# for fruit in fruits:
#     print(f'\nI love {fruit}\n')
# print(f'I love so much all these fruits')

# for fruit in fruits:
#     print(f'{fruit} is so sweet. I love this fruit in any presentation')
#     print(f"{fruits} has a lovely texture, I also like the {fruit}'s scents and flavors")
# print("\nAll of these fruits are sweet and have lovely textures and flavors")

list_of_numbers = list(range(2, 101, 2))

# print(min(list_of_numbers))
# print(max(list_of_numbers))
# print(sum(list_of_numbers))

#List comprehensions:
# name_list = [values_for_new_list for value in iterable]
squares = [value**2 for value in range(1, 11)]
print (squares)

for i in range(1, 21):
    print(i)

numbers_to_twenty = [i for i in range(1, 21)]
print(numbers_to_twenty)