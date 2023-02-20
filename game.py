guessed=""
letters = []
hangman = ['']
stages = ['________ ','|     \n________' ,'| /   \n________', 
          '| / \\ \n________', '|  |  \n| / \\ \n________',
          '| /|  \n| / \\ \n________', '| /|\\ \n| / \\ \n________',
          '|    \n| /|\\ \n| / \\ \n________', '|  0 \n| /|\\ \n| / \\ \n________',
          '|    \n|  0 \n| /|\\ \n| / \\ \n________', '___  \n|    \n|  0 \n| /|\\ \n| / \\ \n________',
          '___  \n|  | \n|  0 \n| /|\\ \n| / \\ \n________']
            
def check_letter(word):
    show =""
    for letter in word:
        letter = letter.lower()
        if letter in letters:
            show += letter
        else:
            show += "_"
    return show
            
def guess(word):
    guessed=""
    letter = input("Guess a letter! ").lower()
    if len(letter)!=1:
        print("This is not a letter...")
    elif letter in letters:
        print("Letter already guessed")
    else:
        letters.append(letter)
        guessed = check_letter(word)
        print(guessed, '\n')
        if letter not in word:
            hangman.append(stages[len(hangman)-1])
        print(hangman[-1],'\n')
        print(letters,'\n')
    return guessed
 
        

word="snowflake"
while guessed!=word:
    guessed = guess(word)
    if guessed == word:
        print("YOU WIN! :D")
    elif len(hangman)==len(stages)+1:
        print("YOU LOST!\nthe word was: ", word)
        break
    

