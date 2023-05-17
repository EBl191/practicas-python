def books(author, book_name, **book_info):
    book_info['author'] = author
    book_info["book's name"] = book_name
    return book_info

books('María Zambrano', 'Cartas de La Pièce', editor='Agustín Andreu', editorial='Pre-Textos', año=2002)

print(books('María Zambrano', 'Cartas de La Pièce', editor='Agustín Andreu', editorial='Pre-Textos', año=2002))