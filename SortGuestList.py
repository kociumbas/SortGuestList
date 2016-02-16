#ask the user to enter the names of everyone attending a party, print the list in alphabetical order

guests = [] #declare an empty list
guestName = " "

while guestName.upper() != 'DONE' :
    guestName = input("Who would you like to invite? If finished, write 'DONE' ")
    if guestName.upper() != 'DONE':
        guests.append(guestName)

#guests.remove('DONE')
guests.sort()

for guest in guests:
    print(guest)