from pathlib import Path
import json

username = input("What is your name?: ")
userlastname = input("What is your lastname?: ")
age = input("How old are you?: ")
email = input("What is your mail direction?:")

def create_user():
   
    user_dict = {
        'name': username,
        'lastname': userlastname,
        'age': age,
        'e-mail': email
    }
    path = Path('username.json')
    contents = json.dumps(user_dict)
    path.write_text(contents)

    return print(user_dict)

create_user()