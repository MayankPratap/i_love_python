# A simple hangman game powered by ASCII ART AND PYTHON

import random
HANGMANPICS=['''

    +----+
    |    |
         |
         |
         |
         |
         |
         |
    ====== ''','''

    +----+
    |    |
    0    |
         |
         |
         |
         |
         |
    ====== ''','''

    +----+
    |    |
    0    |
    |    |
         |
         |
         |
         |
    ====== ''','''

    +----+
    |    |
    0    |
   /|    |
         |
         |
         |
         |
    ====== ''','''
    +----+
    |    |
    0    |
   /|\   |
         |
         |
         |
         |
    ====== ''','''

    +----+
    |    |
    0    |
   /|\   |
         |
         |
         |
         |
    ====== ''','''
    +----+
    |    |
    0    |
   /|\   |
   /     |
         |
         |
         |
    ====== ''','''

    +----+
    |    |
    0    |
   /|\   |
   / \   |
         |
         |
         |
   ======= ''' ]

words='kane,undertaker,rock,brock,lita,hogan,edge,show,hbk,cena,orton,henry,sheamus'.split(',')

def getRandomWord(wordList):
    # This function returns a random string from passes list of strings.
    wordIndex=random.randint(0,len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
 
    print('Missed letters:',end=' ')
    for letter in missedLetters:
        print(letter,end=' ')
    print()

    blanks='_'*len(secretWord)
    
    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]

    for letter in blanks:
        print(letter,end=' ')

    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess=input()
        guess=guess.lower()
        
        if len(guess)!=1:
            print('Please enter a single letter')

        elif guess in alreadyGuessed:
            print('You have already guessed that letter.Choose Again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
    # This function returns True if player wants to play again

    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters=''
correctLetters=''

secretWord=getRandomWord(words)
gameIsDone=False

while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    
    # Let the player type in a letter
    guess=getGuess(missedLetters+correctLetters)
 
    foundAllLetters=False

    if guess in secretWord:
        correctLetters=correctLetters+guess
        foundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break

    if foundAllLetters:
        print('Yes! The secret word is "' + secretWord + ' "! You have won!')
        gameIsDone=True

    if guess not in secretWord:
        missedLetters=missedLetters+guess
        
        # Check if player has taken too many guesess and lost

        if len(missedLetters)==len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
            print('You have run out of guesses!\nAfter '+str(len(missedLetters))+' missed guesses and '+str(len(correctLetters))+' correct guesses,the word was "'+secretWord+'"')

            gameIsDone=True
 
    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone=False
            secretWord=getRandomWord(words)
        else:
            break

