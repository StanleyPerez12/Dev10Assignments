import csv


global tournamentlist
tournamentlist = dict({})


def readcsvfile(): 

    global tournamentlist

    with open('tournamentparticipants.csv', mode='r') as inp:
        reader = csv.reader(inp)
        
        print(tournamentlist)
        try:
            first_line = next(reader)
            tournamentlist = {rows[0]:rows[1] for rows in reader}
            start_up()
        except StopIteration:
            print("READCSV TO ADD HEADERS FUNCTION")
            add_headers()

        
    

def add_headers():

        tournamentlistheader = ["Slot #", "Name"]
        filename = "tournamentparticipants.csv"

        with open(filename, 'a') as file:
            writer = csv.DictWriter(file, fieldnames = tournamentlistheader)
            writer.writeheader()
        readcsvfile()


def csvfile():

    global tournamentlist

    tournamentlistheader = ["Slot #", "Name"]
    filename = "tournamentparticipants.csv"

    print(tournamentlist)

    with open(filename, 'a') as file:
        writer = csv.DictWriter(file, fieldnames = tournamentlistheader)
        writer.writerow(tournamentlist)


def start_up():

    print("Welcome to Tournaments R US")
    print("=======================")
    Slots = input("Enter the number of participants: ")

    print("There are " + str(Slots) + " participant slots ready for sign-ups.")
    main_menu()

def main_menu():

    one = sign_up
    two = cancel_sign_up
    # three = view_participants
    # four = save_changes
    # five = exit

    print("Participant Menu")
    print("=================")
    print("1. Sign Up ")
    print("2. Cancel Sign Up ")
    print("3. View Participants ")
    print("4. Save Changes ")
    print("5. Exit ")
    directory = input("Where would you like to go? Enter the number: ")
    if directory == '1' : 
        sign_up()
    elif directory == '2': 
        cancel_sign_up()
    else:
        print("testing 3-5")

    

def sign_up():

    global tournamentlist
    print("Participant Sign Up")
    print("===================")
    participant_name = input("Enter the name of the participant: ")
    print(tournamentlist)
    taken_slot(participant_name)

    

def taken_slot(x):

    global tournamentlist

    desired_starting_slot = int(input("What is the desired starting slot? #[1-50]: "))
    desired_starting_slot = str(desired_starting_slot)
    if desired_starting_slot in tournamentlist:
        print("Spot is already taken")
        print(tournamentlist)
        taken_slot(x)
    else:
        tournamentlist = {
            "Slot #" : desired_starting_slot,
            "Name" : x
        }
        print("Success! " + x + " is signed up in starting slot #" + str(desired_starting_slot))
        csvfile()
        main_menu()

def cancel_sign_up():

    global tournamentlist
    
    val_list = list(tournamentlist.values())
    key_list = list(tournamentlist.keys())
    key = ''

    print("Participant Cancelletation")
    print("===========================")
    cancel_participant = input("What is the name of the person you want to cancel? ")
    cancel_participant = str(cancel_participant)
    print(tournamentlist)

    if cancel_participant in tournamentlist.values():
        key = key_list[val_list.index(cancel_participant)]
        tournamentlist.pop(key)
        csvfile()
  
    else:
        print("This person is not registered in the list")
        cancel_sign_up()




readcsvfile()
