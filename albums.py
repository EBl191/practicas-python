# def make_album(name, artist):
#     """Builds a dict """
#     album = {'album': name, 'artist': artist}

#     return album

# print(make_album('Fallen', 'Evanescence'))

def greet_users(names):

    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    
    
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)