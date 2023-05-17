#Initial guests:

dinner_guests = ["Miguel", "Naroa", "Bel", "Sandra", "Yair", "Eduardo", "Pantera"]

#Invitation:

message = "I am glad to invite you to my house for a dinner. I hope you will come ;) ... With love, Ed."

#Notifications:

#print(f'{dinner_guests[0]} can not come with us this time, so I have invited Eimy')
dinner_guests.insert(0, "Eimy")

#print(f'more friends will arrive')
dinner_guests.insert(1, "Daniel")
dinner_guests.insert(3, "Silvia")
dinner_guests.append("Anne")

#Final guests

invitation_1 = f'Dear {dinner_guests[0]}, {message}'
invitation_2 = f'Dear {dinner_guests[1]}, {message}'
invitation_3 = f'Dear {dinner_guests[2]}, {message}'
invitation_4 = f'Dear {dinner_guests[3]}, {message}'
invitation_5 = f'Dear {dinner_guests[4]}, {message}'
invitation_6 = f'Dear {dinner_guests[5]}, {message}'
invitation_7 = f'Dear {dinner_guests[7]}, {message}'
invitation_8 = f'Dear {dinner_guests[8]}, {message}'
invitation_9= f'Dear {dinner_guests[9]}, {message}'
invitation_10 = f'Dear {dinner_guests[10]}, {message}'

# print(invitation_1)
# print("------")
# print(invitation_2)
# print("------")
# print(invitation_3)
# print("------")
# print(invitation_4)
# print("------")
# print(invitation_5)
# print("------")
# print(invitation_6)
# print("------")
# print(invitation_7)
# print("------")
# print(invitation_8)
# print("------")
# print(invitation_9)
# print("------")
# print(invitation_10)
# dinner_guests.sort(reverse=True)
# print(dinner_guests)

#print(f'We have invited to our diner {len(dinner_guests)} guests')

places_to_visit = ["Todnauberg, Black forest", "Hölderlinturm, Tübingen", "Bollingen Tower, Suiza", "Eleusis, Grecia", "Sagrada Familia, Barcelona"]

#print(places_to_visit)
#print(sorted(places_to_visit))
places_to_visit.reverse()
#print(places_to_visit)
places_to_visit.sort()
#print(places_to_visit[3])

for place in places_to_visit:
    print(f'{place} is a place that I really crave for visit at least once in my life')