pesel = ""
while len(pesel) != 11 or pesel.isdigit() == False:
    print("Insert pesel(11 numbers). Insert q or Q to quit.")
    pesel = input()
    if pesel == 'q' or pesel == 'Q':
        print("Application has been closed.") 
        break
    elif len(pesel) != 11:
        if pesel.isdigit() == False:
            print("You have inserted wrong type of data.")
        else:
            print("You have inserted wrong number of digits.")
    elif pesel.isdigit() == False:
        print("You have inserter wrong type of data.")
if pesel != 'q' and  pesel != 'Q':   
    forumla_digits = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    cheking = (sum([int(pesel[i]) * forumla_digits[i] for i in range(11)])) % 10    
    if cheking == 0:
        print("Pesel is correct")
    else:
        print("PESEL IS WRONG!")  