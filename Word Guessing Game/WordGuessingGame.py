import random

                       #    WORD GUESSING GAME


# Read text file to extract lines
with open('words.txt', "r") as File:
    contents = File.readlines()

# Create blank list to insert words already used by user
global usedwords 
usedwords = []

# Variables to keep track of user score
global Wins
global Losses
Wins = int(0)
Losses = int(0)

# Function to generate random word from text file. variable = contents
def random_word():


    global Word 

    # Create variable to store random word
    Word = random.choice(contents)
    # have random word be lowercase
    Word = Word.lower()
    # Create list from random word where each letter is an index
    WordList = list(Word)
    # Pop the last index because it is a space
    WordList.pop()
    # Join the indexes to have word without the space
    Word = ''.join(WordList)

    # if statement to make sure no word is used twice and each word gets added to a list usedwords
    if Word in usedwords:
        random_word()
    else:
        usedwords.append(Word)


    

    global Length
    # Get the length of the word
    Length = len(Word)

    global Blank
    # Create _ equal to the amount of letters in said word so user can know which letters have been guessed correctly
    Blank = "_" * (Length)

    global BlankList
    # Create a list where each index represents a letter in the word
    BlankList = list(Blank)

    global GuessesRemaining
    # Variable for the amount of guesses remaining
    GuessesRemaining = int(7)

    # Tells user the amount of letters in the word
    print("Your word has " + str(Length) + " letters in it")


# Function used when user starts the game
def User_Guest(): 

# Run the function to generate random word
    random_word()

# Game function is ran when user is making a guess
    def Game():

# Access these variables to change them globally 
        global Blank
        global BlankList
        global GuessesRemaining
        global Wins
        global Losses

# Variable used to store user's input and have it lowercase
        Guess = str(input("Guess a Letter ")).lower()

# If statement used if the user guesses more than one letter at a time            
        if len(Guess) > 1:
            print("Guess one letter, try again")
            Game()

# If user doesn't input anything
        elif Guess == '':
            print("Input a letter")
            Game()

# If user input is NOT one of the letters
        elif Guess not in Word:
            GuessesRemaining = GuessesRemaining - 1
            print("You have " + str(GuessesRemaining) + " guesses remaining")
            if GuessesRemaining == 0:
                print("Game is over, you've lost, the word was " + Word)
                Losses = Losses + 1
                continue_playing()
            elif GuessesRemaining > 0:
                print("Incorrect, try again")
                print(Blank)
                Game()

# If the user has already guessed this letter
        elif Guess in Blank:
            print("You've already guessed this letter! Try again")
            Game()

# If the word has more than one occurrence of guessed letter
        elif Word.count(Guess) > 1:

            occurrence = [index for index, value in enumerate(list(Word)) if value == Guess]
            for occurrence in occurrence:
                BlankList[occurrence] = Guess
            Blank = ''.join(BlankList)

            if Blank == Word:
                print("You got it! The word was" + Word)
                Wins = Wins + 1
                continue_playing()
       
            else:
                print(Blank)
                Game()
            
# If the letter is in the word with only one occurrence 
        elif Guess in Word:

            Index = (Word.index(Guess))
            BlankList[Index] = Guess
            Blank = ''.join(BlankList)
            print(Blank)
            if Blank == Word: 
                print("You got it!")
                Wins = Wins + 1
                continue_playing()


            else:
                Game()

# Function is called when program is ran. Determines what to do with user guess
    Game()


# Function is ran when user is done playing the game and has either won or loss
def continue_playing():

    print("You have " + str(Wins) + " wins and " + str(Losses) + " losses")
    keep_going = str(input("Would you like to keep playing? Enter Y or N "))
    keep_going = keep_going.capitalize()
    

    if keep_going == "Y":
        print("Lets get it")
        User_Guest()

    elif keep_going == "N":
        print("Ok, goodbye")

    elif keep_going != "Y" or keep_going != "N":
        continue_playing()

User_Guest()

print("Github test")



    
