while True:
    ask_ticket_price = input("Which is your age? ")
    

    if ask_ticket_price == 'quit':
        break
    
    ask_ticket_price = int(ask_ticket_price)

    if ask_ticket_price <= 3:
        print("The ticket is free.")
    elif ask_ticket_price <= 12:
        print("The price for the ticket is $10.")
    else:
        print("The price for the ticket is $15.")
    

