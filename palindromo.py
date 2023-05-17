def palindromo(text):
    low_text = text.lower()
    text_no_space = low_text.replace(" ", "")
    return text_no_space == text_no_space[::-1]

print(palindromo("Anita lava la tina"))
print(palindromo("oro"))