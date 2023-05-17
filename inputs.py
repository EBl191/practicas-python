prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
prompt = "\nWhat is your lastname? "
lastname = input(prompt)
print(f"\nHello, {name} " + f"{lastname}!")
prompt = "\nWhat is your age? "
age = input(prompt)
age = int(age)
if age >= 18:
    print(True) 