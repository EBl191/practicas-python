def repeated_letter(text):
    text_lower = text.lower()
    text_no_spaces = text_lower.replace(" ", "")
    list_letters = [] 

    for letter in text_no_spaces:
        if letter in list_letters:
            return f"The repeated letter is < {letter} >"
        else:
            list_letters.append(letter)
    
    return None

print(repeated_letter("Hola"))

print(repeated_letter("Hola mundo"))
