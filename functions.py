def display_message():
    print("Hi! I'm learning and practicing my Python's habilities for improving them.")

#display_message()

favorite_books = ['Human condition', 'The problem of empathy', 'So spoke Zarathustra', 'Psychological types', 'Symposium, Republic, Phaedro', 'The Lord of The Rings']

def favorite_book(title):
    
    print(f"One of my favorite books is {title}.")

#favorite_book('The Lord of the rings by JRR Tolkien.')

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet('hamster', 'harry')

def make_shirt(size='L', message='I LOVE QKS & TTS'):
    print(f"\nThe shirt's size is {size} and has written this message: ")
    print(message)

#make_shirt()

def describe_city(city, country='Venezuela'):
    print(f"{city} is in {country}")

# describe_city("Caracas")
# describe_city("Valencia")
# describe_city("Bogotá", 'Colombia')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

philosopher = get_formatted_name('María', 'Zambrano.')

#print(philosopher)

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

name = get_formatted_name("eduardo", "blanco", "rafael")
#print(name)

def build_person(first_name, last_name, age=None):
    """Return a dict of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

philosopher = build_person('María', 'Zambrano', '86')
print(philosopher)