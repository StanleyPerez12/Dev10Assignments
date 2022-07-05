import random
import threading


PlayersList = []
usedwords = []
round = 1
guesses = 3
vowelguesses = 1
vowellist = []

# function ran when program is started
def start_up():

    players_input = input("Welcome! Are you ready to play? Enter Y/N: ")
    # pass the answer to players_input function to input names
    players(players_input)
    
# function used to input player names
def players(x):

    global player1Bank
    player1Bank = 0

    global player2Bank
    player2Bank = 0

    global player3Bank
    player3Bank = 0

    global rounddict 
    rounddict = {}

    x = x.capitalize()
    
    #determine what to do for starting the game
    if x != 'Y' and x != 'N':
        print("please enter Y or N")
        start_up()
    elif x == 'Y':
        #add players name to a list
        player1 = input("Name of player 1: ")
        PlayersList.append(player1)
        player2 = input("Name of player 2: ")
        PlayersList.append(player2)
        player3 = input("Name of player 3: ")
        PlayersList.append(player3)
        if len(PlayersList) == 3:
            print("3 players registered")
            bank = "Bank totals \n" + PlayersList[0] + " = $" + str(player1Bank) + "\n" + PlayersList[1] + " = $" + str(player2Bank) + "\n" + PlayersList[2] + " = $" + str(player3Bank)
            print(bank)
            #move on to readwheel data function in order to determine next steps in the game
            readwheeldata()
        else:
            print("something went wrong, try again")
            start_up()
    elif x == 'N':
        print("Ok, come back when you do!")

# function for when it's player 1's turn
def player1turn(x):
    
    global PlayersList
    
    x = 0 # variable to determine who's turn it is

    print("It's " + PlayersList[0] + "'s turn")
    print("Bank totals so far")
    print(PlayersList[0] + " = $" + str(player1Bank))
    print(PlayersList[1] + " = $" + str(player2Bank))
    print(PlayersList[2] + " = $" + str(player3Bank))
    print("The word has " + str(len(word)) + " letters in it")
    print(underscore)

    whatwouldplayerliketodo(x)
 
# function for when it's player 2's turn
def player2turn(x):

    x = 1 # variable to determine who's turn it is 
 
    global PlayersList

    print("It's " + PlayersList[1] + "'s turn")
    print("Bank totals so far")
    print(PlayersList[0] + " = $" + str(player1Bank))
    print(PlayersList[1] + " = $" + str(player2Bank))
    print(PlayersList[2] + " = $" + str(player3Bank))
    print("The word has " + str(len(word)) + " letters in it")
    print(underscore)

    whatwouldplayerliketodo(x)
 
# function for when it's player 3's turn
def player3turn(x):

    x = 2  # variable to determine who's turn it is

    global PlayersList

    print("It's " + PlayersList[2] + "'s turn")
    print("Bank totals so far")
    print(PlayersList[0] + " = $" + str(player1Bank))
    print(PlayersList[1] + " = $" + str(player2Bank))
    print(PlayersList[2] + " = $" + str(player3Bank))
    print("The word has " + str(len(word)) + " letters in it")
    print(underscore)

    whatwouldplayerliketodo(x)
  
# function to read the sections on the wheel
def readwheeldata(): 

    f = open('/Users/stanleyperez/Documents/Dev10/PythonAssignments/Wheel of Fortune/Data TXT Files/wheeldata.txt')
    wheelsections = f.readlines()

    global wheelsectionsmodified
    # add each section to a list
    wheelsectionsmodified = []
    f.close()

    global player1Bank
    player1Bank = 0

    global player2Bank
    player2Bank = 0

    global player3Bank
    player3Bank = 0
    
    # modify list so it doesn't include \n
    for element in wheelsections:
        wheelsectionsmodified.append(element.strip())
    #move to generate random word
    random_word()

# function to generate random word from dictionary.txt file and choose which player goes first
def random_word():

    global usedwords
    with open('/Users/stanleyperez/Documents/Dev10/PythonAssignments/Wheel of Fortune/Data TXT Files/dictionary.txt', 'r') as File:
        words = File.readlines()

    # add all words to a list
    words_modified = []

    # modify list to exclude \n
    for elements in words:
        words_modified.append(elements.strip())

    # generate random word
    global word
    word = random.choice(words_modified)
    word = word.lower()

    # add random word to usedwords list so no word is repeated
    usedwords.append(word)

    if word in usedwords:
        random_word()
    else:

        # underscore used to keep track of correctly guessed words
        global underscore
        underscore = "_" * len(word)

        #create list from random word to modify each letter as an index
        global underscorelist
        underscorelist = list(underscore)

        # choose random player to determine who will start the game
        startingplayer = random.choice(PlayersList)
        print("The player who will start the game is " + startingplayer)
        print(word)

        # determine which players function to run first depending on which player was chosen to start
        if PlayersList.index(startingplayer) == 0:
            player1turn(startingplayer)
        elif PlayersList.index(startingplayer) == 1:
            player2turn(startingplayer)
        elif PlayersList.index(startingplayer) == 2:
            player3turn(startingplayer)
        else:
            print("There was an error")

#function for when the player has to decide what to do
def whatwouldplayerliketodo(x) : 

    print("What would you like to do?")
    print("1. Spin the wheel ")
    print("2. Buy a Vowel ($250) ")
    print("3. Guess the word ")
    directory = input("Enter the number of what you'd like to do: ") 
    if directory == '1':
        spinthewheel(x)
    elif directory == '2':
        if x == 0:
            if player1Bank >= 250:
                buyavowel(x)
            elif player1Bank < 250:
                print("You don't have enough to buy a vowel")
                whatwouldplayerliketodo(x)
        elif x == 1:
            if player2Bank >= 250:
                buyavowel(x)
            elif player2Bank < 250:
                print("You don't have enough to buy a vowel")
                whatwouldplayerliketodo(x)
        elif x == 2:
            if player3Bank >= 250:
                buyavowel(x)
            elif player3Bank < 250:
                print("You don't have enough to buy a vowel")
                whatwouldplayerliketodo(x)
    elif directory == '3':
        guesstheword(x)
    else:
        print("Please enter a number 1-3")
        whatwouldplayerliketodo(x) 

#function for when the player chooses to spin the wheel
def spinthewheel(x):

    global word
    global underscore
    global underscorelist 

    wheels_choice = random.choice(wheelsectionsmodified)

    def playerguess(x, y):

        global word
        global underscore
        global underscorelist 

        if wheels_choice == 'Bankrupt':
            print("Wheel landed on Bankrupt")
            update_bank(x, y)
        elif wheels_choice == 'Lose a Turn':
            print("Wheel landed on lose a turn")
            if x == 0:
                player2turn(x)
            elif x == 1:
                player3turn(x)
            elif x == 2:
                player1turn(x)
            else:
                print("Something went wrong, game restarted.")
                start_up()
        else:
            print("You have a chance to win $" + y)
            print(underscore)
            guess = input("Guess a consonant: ")
            guess = guess.lower()

            if guess in underscore:
                print("Letter has already been guessed, try again")
                playerguess(x,y)
            elif len(guess) > 1 or len(guess) < 1:
                print("Guess is more than 1 letter, or no letter was guessed. Please try again")
                playerguess(x,y)
            elif guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':
                print("No guessing vowels! Consonants only. Try again")
                playerguess(x,y)
            elif word.count(guess) > 1:
                occurrence = [index for index, value in enumerate(list(word)) if value == guess]
                for occurrence in occurrence:
                    underscorelist[occurrence] = guess
                underscore = ''.join(underscorelist)
                print(underscore)
                if  underscore == word:
                    print("Correct! Congratulations")
                    update_bank(x,y)
                else:
                    user_answer = input("What do you think the word is? ")
                    user_answer = user_answer.lower()
                    if user_answer == word:
                        underscore = word
                        print("Correct! Congratulations")
                        update_bank(x,y)
                    else:
                        print(user_answer + " is incorrect")
                        update_bank(x,y)
            elif guess in word:
                index = word.index(guess)
                underscorelist[index] = guess
                underscore = ''.join(underscorelist)
                print(underscore)
                if underscore == word:
                    print("Correct! Congrats")
                    update_bank(x,y)
                else:
                    user_answer = input("What do you think the word is? ")
                    user_answer = user_answer.lower()
                    if user_answer == word:
                        underscore = word
                        print("Correct! Congratulations")
                        update_bank(x,y)
                    else:
                        print(user_answer + " is incorrect")
                        update_bank(x,y)
            elif guess not in word: 
                print("Guess wasn't in word. Turn end")
                if x == 0:
                    player2turn(x)
                elif x == 1:
                    player3turn(x)
                elif x == 2:
                    player1turn(x)
                else:
                    print("Error switching turns")
            else:
                print("Guess wasn't in word")

    playerguess(x, wheels_choice)

#function for when the player chooses to buy a vowel
def buyavowel(x):

    global player1Bank
    global player2Bank
    global player3Bank

    if x == 0: 

        if player1Bank < 250:
            print("You don't have enough in the bank to buy a vowel")
            player2turn(x)
        elif 'a' not in word and 'e' not in word and 'i' not in word and 'o' not in word and 'u' not in word:
            print("word doesn't have a vowel")
            player1Bank = player1Bank - 250
            player2turn(x)
        else:
            player1Bank = player1Bank - 250
            vowelbought(x)      

    elif x == 1:

        if player2Bank < 250:
            print("You don't have enough in the bank to buy a vowel")
            player3turn(x)
        elif 'a' not in word and 'e' not in word and 'i' not in word and 'o' not in word and 'u' not in word:
            print("word doesn't have a vowel")
            player2Bank = player2Bank - 250
            player3turn(x)
        else:
            player2Bank = player2Bank - 250
            vowelbought(x)

    elif x == 2:

        if player3Bank < 250:
            print("You don't have enough in the bank to buy a vowel")
            player1turn(x)
        elif 'a' not in word and 'e' not in word and 'i' not in word and 'o' not in word and 'u' not in word:
            print("word doesn't have a vowel")
            player3Bank = player3Bank - 250
            player1turn(x)
        else:
            player3Bank = player3Bank - 250
            vowelbought(x)

#function for when the player can buy a vowel
def vowelbought(x):

    global underscore
    global underscorelist
    global player1Bank
    global player2Bank
    global player3Bank

    vowelchose = input("Which vowel would you like to buy? ")
    vowelchose = vowelchose.lower()

    def vowelboughtloop(x):

        global player1Bank
        global player2Bank
        global player3Bank

        continuevowelbuying = input("Would you like to buy another vowel? Y/N : ")

        continuevowelbuying = continuevowelbuying.upper()

        if continuevowelbuying == 'Y':
            buyavowel(x)
        elif continuevowelbuying == 'N':
            if x == 0:
                player2turn(x)
            elif x == 1:
                player3turn(x)
            elif x == 2:
                player1turn(x)
        else:
            vowelboughtloop(x)

    if 'a' in word and 'a' not in underscore and vowelchose == 'a':
        occurrence = [index for index, value in enumerate(list(word)) if value == 'a']
        for occurrence in occurrence:
            underscorelist[occurrence] = 'a'
        underscore = ''.join(underscorelist)
        print("The vowel bought was 'a'")
        print(underscore)
        if underscore == word:
            round2(x)
        else:
            vowelboughtloop(x)
        

    elif 'e' in word and 'e' not in underscore and vowelchose == 'e':
        occurrence = [index for index, value in enumerate(list(word)) if value == 'e']
        for occurrence in occurrence:
            underscorelist[occurrence] = 'e'
        underscore = ''.join(underscorelist)
        print("The vowel bought was 'e'")
        print(underscore)
        if underscore == word:
            round2(x)
        else:
            vowelboughtloop(x)

    elif 'i' in word and 'i' not in underscore and vowelchose == 'i':
        occurrence = [index for index, value in enumerate(list(word)) if value == 'i']
        for occurrence in occurrence:
            underscorelist[occurrence] = 'i'
        underscore = ''.join(underscorelist)
        print("The vowel bought was 'i'")
        print(underscore)
        if underscore == word:
            round2(x)
        else:
            vowelboughtloop(x)

    elif 'o' in word and 'o' not in underscore and vowelchose == 'o':
        occurrence = [index for index, value in enumerate(list(word)) if value == 'o']
        for occurrence in occurrence:
            underscorelist[occurrence] = 'o'
        underscore = ''.join(underscorelist)
        print("The vowel bought was 'o'")
        print(underscore)
        if underscore == word:
            round2(x)
        else:
            vowelboughtloop(x)

    elif 'u' in word and 'u' not in underscore and vowelchose == 'u':
        occurrence = [index for index, value in enumerate(list(word)) if value == 'u']
        for occurrence in occurrence:
            underscorelist[occurrence] = 'u'
        underscore = ''.join(underscorelist)
        print("The vowel bought was 'u'")
        print(underscore)
        if underscore == word:
            round2(x)
        else:
            vowelboughtloop(x)

    else:
        print("Vowel is not in word")
        if x == 0:
            player2turn(x)
        elif x == 1:
            player3turn(x)
        elif x == 2:
            player1turn(x)

#function for when player chooses to guess the word
def guesstheword(x):

    guess = input("What do you think the word is? ")
    guess = guess.lower()
    if guess == word:
        print("You got it!")
        round2(x)
    else:
        print("Incorrect")
        if x == 0:
            player2turn(x)
        elif x == 1:
            player3turn(x)
        elif x == 2:
            player1turn(x)

#function to have player banks updated
def update_bank(x, y):

    global player1Bank
    global player2Bank
    global player3Bank


    if x == 0 and y == "Bankrupt":
        player1Bank = 0
        print("Player 1 went bankrupt")
        player2turn(x)
    elif x == 1 and y == "Bankrupt":
        player2Bank = 0
        print("Player 2 went bankrupt")
        player3turn(x)
    elif x == 2 and y == "Bankrupt":
        player3Bank = 0
        print("Player 3 went bankrupt")
        player1turn(x)
    elif x == 0:
        player1Bank = int(y) + player1Bank
        if underscore == word:
            round2(x)
        else:
            player2turn(x)
    elif x == 1:
        player2Bank = int(y) + player2Bank
        if underscore == word:
            round2(x)
        else:
            player3turn(x)
    elif x == 2:
        player3Bank = int(y) + player3Bank
        if underscore == word:
            round2(x)
        else:
            player1turn(x)
    else:
        print("error occurred at update bank function")

#function for round 2 
def round2(x):

    global round 
    round = round + 1

    global rounddict

    if round == 2:
        print("The winner of this round is " + PlayersList[x] + "!")
        if x == 0:
            print(PlayersList[0] + " wins $" + str(player1Bank))
            rounddict[PlayersList[0]] = player1Bank
            readwheeldata()
        elif x == 1:
            print(PlayersList[1] + " wins $" + str(player2Bank))
            rounddict[PlayersList[1]] = player2Bank
            readwheeldata()
        elif x == 2:
            print(PlayersList[2] + " wins $" + str(player3Bank))
            rounddict[PlayersList[2]] = player3Bank
            readwheeldata()
        else:
            print("something went wrong at round 2 function of first round")
    elif round == 3:
        print("The winner of this round is " + PlayersList[x] + "!")
        if x == 0:
            print(PlayersList[0] + " wins $" + str(player1Bank))
            rounddict[PlayersList[0]] = player1Bank
            round3player()
        elif x == 1:
            print(PlayersList[1] + " wins $" + str(player2Bank))
            rounddict[PlayersList[1]] = player2Bank
            round3player()
        elif x == 2:
            print(PlayersList[2] + " wins $" + str(player3Bank))
            rounddict[PlayersList[2]] = player3Bank
            round3player()
        else:
            print("something went wrong at round 2 function of second round")

#function to determine who is moving on to round 3
def round3player():

    maxmoney = max(rounddict.values())
    winningplayer = max(rounddict, key=rounddict.get)

    print("The player advancing to round 3 with a whopping $" + str(maxmoney) + " is " + winningplayer + "!" )
    print("Is " + x + " Ready for a chance at $1,000,000?")
    round3(winningplayer)

#function for round 3
def round3(x): 

    global underscore
    global underscorelist

    
   
    with open('/Users/stanleyperez/Documents/Dev10/PythonAssignments/Wheel of Fortune/Data TXT Files/dictionary.txt', 'r') as File:
        words = File.readlines()

    # add all words to a list
    words_modified = []

    # modify list to exclude \n
    for elements in words:
        words_modified.append(elements.strip())

    # generate random word

    word = random.choice(words_modified)
    word = word.lower()
    print(word)

    if word in usedwords:
        round3(x)
    else:

        # underscore used to keep track of correctly guessed words

        underscore = "_" * len(word)

        #create list from random word to modify each letter as an index

        underscorelist = list(underscore)

        print("The word has " + str(len(word)) + " letters in it")

        lettersrevealed(word, x)

#function to show the letters to be revealed in the word for round 3
def lettersrevealed(word, x):

    global underscore
    global underscorelist

    wordsrevealed = ['e','l','n','r','s','t']

    # Ask professors for help on figuring this out, iterating through list for letters that show up multiple times
    # for i in word:
    #     if i in wordsrevealed :
    #         count = word.index(i)
    #         underscorelist[count] = i 
    #         underscore = ''.join(underscorelist)


    if 'e' in word and 'e' not in underscore:
        if word.count('e') > 1:
            occurrence = [index for index, value in enumerate(list(word)) if value == 'e']
            for occurrence in occurrence:
                underscorelist[occurrence] = 'e'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        elif word.count('e') == 1:
            index = (word.index('e'))
            underscorelist[index] = 'e'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        else:
            print("something went wrong at e")
    elif 'l' in word and 'l' not in underscore:
        if word.count('l') > 1:
            occurrence = [index for index, value in enumerate(list(word)) if value == 'l']
            for occurrence in occurrence:
                underscorelist[occurrence] = 'l'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        elif word.count('l') == 1:
            index = (word.index('l'))
            underscorelist[index] = 'l'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        else:
            print("something went wrong at l")
    elif 'n' in word and 'n' not in underscore:
        if word.count('n') > 1:
            occurrence = [index for index, value in enumerate(list(word)) if value == 'n']
            for occurrence in occurrence:
                underscorelist[occurrence] = 'n'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        elif word.count('n') == 1:
            index = (word.index('n'))
            underscorelist[index] = 'n'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        else:
            print("something went wrong at n")
    elif 'r' in word and 'r' not in underscore:
        if word.count('r') > 1:
            occurrence = [index for index, value in enumerate(list(word)) if value == 'r']
            for occurrence in occurrence:
                underscorelist[occurrence] = 'r'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        elif word.count('r') == 1:
            index = (word.index('r'))
            underscorelist[index] = 'r'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        else:
            print("something went wrong at r")
    elif 's' in word and 's' not in underscore:
        if word.count('s') > 1:
            occurrence = [index for index, value in enumerate(list(word)) if value == 's']
            for occurrence in occurrence:
                underscorelist[occurrence] = 's'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        elif word.count('s') == 1:
            index = (word.index('s'))
            underscorelist[index] = 's'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        else:
            print("something went wrong at s")
    elif 't' in word and 't' not in underscore:
        if word.count('t') > 1:
            occurrence = [index for index, value in enumerate(list(word)) if value == 't']
            for occurrence in occurrence:
                underscorelist[occurrence] = 't'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        elif word.count('t') == 1:
            index = (word.index('t'))
            underscorelist[index] = 't'
            underscore = ''.join(underscorelist)
            lettersrevealed(word,x)
        else:
            print("something went wrong at t")
    else:
        round3guess(x, word)
    
#function for player making guesses in round 3
def round3guess(x, word):
    
    print("You have " + str(guesses) + " guesses remaining and " + str(vowelguesses) + " vowel guess")

    def playerguess(x,word):
        
        global vowelguesses
        global vowellist
        global underscore
        global guesses

        vowels = ['a','e','i','o','u']

        if guesses == 0 and vowelguesses == 0:
            print("Guesses are 0")
            finalguess(x,word)
        elif guesses == 0 and vowelguesses != 0:
            print(underscore)
            guess = input("Guess a consonance or a vowel: ")
            guess = guess.lower()
            print(guess)
            if guess not in vowels:
                print("Enter a vowel")
                playerguess(x,word)
            elif len(guess) > 1:
                print("Enter one letter")
                playerguess(x,word)
            elif guess in underscore:
                print("Letter is already in word, try again")
                playerguess(x,word)
            elif guess in vowellist:
                print("You've already guessed a vowel, try again")
                playerguess(x,word)
            elif guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':
                vowellist.append(guess)
                vowellist.extend(['a','e','i','o','u'])
                vowelguesses = vowelguesses - 1
                if word.count(guess) > 1:
                    occurrence = [index for index, value in enumerate(list(word)) if value == guess]
                    for occurrence in occurrence:
                        underscorelist[occurrence] = guess
                    underscore = ''.join(underscorelist)
                    if underscore == word:
                        print("Congratulations! You've won $1,000,000! The word was " + word)
                    else:
                        print(guess + " was in the word!")
                        round3guess(x,word)
                elif guess in word:
                    index = word.index(guess)
                    underscorelist[index] = guess
                    underscore = ''.join(underscorelist)
                    if underscore == word:
                        print("Congratulations! You've won $1,000,000! The word was " + word)
                    else:
                        print(guess + " was in the word!")
                        round3guess(x,word)
                else:
                    print(guess + " was not in the word")
                    round3guess(x,word)
        else:
            print(underscore)
            guess = input("Guess a consonance or a vowel: ")
            guess = guess.lower()
            if len(guess) > 1:
                print("Enter one letter")
                playerguess(x,word)
            elif guess in underscore:
                print("Letter is already in word, try again")
                playerguess(x,word)
            elif guess in vowellist:
                print("You've already guessed a vowel, try again")
                playerguess(x,word)
            elif guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':
                vowellist.append(guess)
                vowellist.extend(['a','e','i','o','u'])
                vowelguesses = vowelguesses - 1
                if word.count(guess) > 1:
                    occurrence = [index for index, value in enumerate(list(word)) if value == guess]
                    for occurrence in occurrence:
                        underscorelist[occurrence] = guess
                    underscore = ''.join(underscorelist)
                    if underscore == word:
                        print("Congratulations! You've won $1,000,000! The word was " + word)
                    else:
                        print(guess + " was in the word!")
                        round3guess(x,word)
                elif guess in word:
                    index = word.index(guess)
                    underscorelist[index] = guess
                    underscore = ''.join(underscorelist)
                    if underscore == word:
                        print("Congratulations! You've won $1,000,000! The word was " + word)
                    else:
                        print(guess + " was in the word!")
                        round3guess(x,word)
                else:
                    print(guess + " was not in the word")
                    round3guess(x,word)
            elif guess in word:
                guesses = guesses - 1
                if word.count(guess) > 1:
                    occurrence = [index for index, value in enumerate(list(word)) if value == guess]
                    for occurrence in occurrence:
                        underscorelist[occurrence] = guess
                    underscore = ''.join(underscorelist)
                    if underscore == word:
                        print("Congratulations! You've won $1,000,000! The word was " + word)
                    else:
                        print(guess + " was in the word")
                        round3guess(x,word)
                elif guess in word:
                    index = word.index(guess)
                    underscorelist[index] = guess
                    underscore = ''.join(underscorelist)
                    if underscore == word:
                        print("Congratulations! You've won $1,000,000! The word was " + word)
                    else:
                        print(guess + " was in the word")
                        round3guess(x,word)
            else: 
                guesses = guesses - 1
                print(guess + " was not in the word")
                round3guess(x,word)


    def finalguess(x,y):
        

        finalanswer = input("What is the word? ")
        finalanswer = finalanswer.lower()
        print(underscore)
        if finalanswer == y:
            print("Correct! The word was " + y )
            print(x + " has won $1,000,000! Enjoy!")
        else:
            print("Incorrect! The word was " + word)

    playerguess(x,word)

if __name__ == '__main__':    
    start_up()

