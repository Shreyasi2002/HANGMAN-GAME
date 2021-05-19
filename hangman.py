# Hangman Game
# -----------------------------------
import pyttsx3
import random
import string
from playsound import playsound

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            return False
    return True


def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result=list()
    for i in range(len(secret_word)):
        result.append("_ ")
    for c in letters_guessed:
        if c in secret_word:
            i=get_index_positions(secret_word, c)
            for j in range(len(i)):
                result[i[j]]=c
    result1=""
    for ele in result:
        result1+=ele

    return result1


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    result=string.ascii_lowercase
    for c in letters_guessed:
        result=result.replace(c,'')

    return result
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ",len(secret_word)," letters long.")
    warnings_left=3
    print("You have 3 warnings left.")
    letter=list()

    unique=len(set(secret_word))
    guesses_left=6
    while guesses_left>0:
        print("-----------------")
        print("You have ",(guesses_left)," guesses left")
        print("Available letters: "+ get_available_letters(letter))
        print("Please guess a letter: ")
        st=input()
        

        if st in letter:
            if warnings_left>0:
                print("Oops! You've already guessed that letter. You have ",(warnings_left-1)," warnings left: "+get_guessed_word(secret_word, letter))
                warnings_left-=1
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "+get_guessed_word(secret_word, letter))
                guesses_left-=1
        else:        
           if str.isalpha(st):
               a=str.lower(st)
               letter.append(a)
               if a in secret_word:
                   print("Good guess: "+get_guessed_word(secret_word, letter))
                
               else:
                   print("Oops! That letter is not in my word: "+get_guessed_word(secret_word, letter))
                   if (a=='a')|(a=='e')|(a=='i')|(a=='o')|(a=='u'):
                       guesses_left-=2
                   else:
                       guesses_left-=1
                
           else:
               if warnings_left>0:
                   print("Oops! That is not a valid letter. You have ",(warnings_left-1)," warnings left: "+get_guessed_word(secret_word, letter))
                   warnings_left-=1
               else:
                   print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "+get_guessed_word(secret_word, letter))
                   guesses_left-=1

        
        if is_word_guessed(secret_word, letter):
            print("-----------------")
            print("Congratulations, you won!")
            print("Your total score for this game is: ",((guesses_left)*unique))
            break

    if (guesses_left)==0:
        print("-----------------")
        print("Sorry, you ran out of guesses. The word was "+secret_word)

    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    s=my_word
    for x in range(len(my_word)):
        if my_word[x]==' ':
            s=s.replace(' ','')
                        
    if len(s)!=len(other_word):
        return False
    else:
        for c in s:
            if c!='_':
                i=get_index_positions(s,c)
                j=get_index_positions(other_word,c)
                if len(i)!=len(j):    
                    return False
                else:
                    for a in range(len(i)):
                        if i[a]!=j[a]:
                            return False
                        
    return True
                
                



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    result=""
    for i in range(len(wordlist)):
        if match_with_gaps(my_word, wordlist[i]):
            result+=(wordlist[i]+" ")
            
    if len(result)==0:
        print("No Matches Found")
    else:
        print("Possible word matches are: ")
        print(result)
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    engine.say("Welcome to the game Hangman! ")
    engine.runAndWait()
    engine.say("I am thinking of a word that is "+str(len(secret_word))+" letters long.")
    engine.runAndWait()
    engine.say("You have 3 warnings left.")
    engine.runAndWait()
    engine.say("If you press @, I can make you laugh!")
    engine.runAndWait()
    engine.say("... Wanna try?")
    engine.runAndWait()
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ",len(secret_word)," letters long.")
    warnings_left=3
    print("You have 3 warnings left.")
    letter=list()
    print("You can press @ for some entertainment 🎊")

    unique=len(set(secret_word))
    guesses_left=6
    while guesses_left>0:
        print("-----------------")
        engine.say("You have "+str(guesses_left)+" guesses left")
        engine.runAndWait()
        engine.say("Please guess a letter: ")
        engine.runAndWait()
        print("You have ",(guesses_left)," guesses left")
        print("Available letters: "+ get_available_letters(letter))
        print("Please guess a letter: ")
        st=input()

        if st in letter:
            if warnings_left>0:
                engine.say("Oops! You've already guessed that letter. ")
                engine.runAndWait()
                playsound("Sad_Trombone-Joe_Lamb-665429450.mp3")
                engine.say("You have "+str(warnings_left-1)+" warnings left: ")
                engine.runAndWait()
                print("Oops! You've already guessed that letter. You have ",(warnings_left-1)," warnings left: "+get_guessed_word(secret_word, letter))
                warnings_left-=1
            else:
                engine.say("Oops! You've already guessed that letter.")
                engine.runAndWait()
                playsound("Sad_Trombone-Joe_Lamb-665429450.mp3")
                engine.say(" You have no warnings left so you lose one guess: ")
                engine.runAndWait()
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "+get_guessed_word(secret_word, letter))
                guesses_left-=1
                
        else:        
           if str.isalpha(st):
               a=str.lower(st)
               letter.append(a)
               if a in secret_word:
                   engine.say("Good guess  ")
                   engine.runAndWait()
                   playsound("1_person_cheering-Jett_Rifkin-1851518140.mp3")
                   print("Good guess: "+get_guessed_word(secret_word, letter))
                
               else:
                   engine.say("Oops! That letter is not in my word: ")
                   engine.runAndWait()
                   playsound("Sad_Trombone-Joe_Lamb-665429450.mp3")
                   print("Oops! That letter is not in my word: "+get_guessed_word(secret_word, letter))
                   if (a=='a')|(a=='e')|(a=='i')|(a=='o')|(a=='u'):
                       guesses_left-=2
                   else:
                       guesses_left-=1
                       

           elif st=='*':
               engine.say("Okay I am giving you little hints ")
               engine.runAndWait()
               show_possible_matches(get_guessed_word(secret_word, letter))

           elif st == '@':
               playsound("Maniacal Witches Laugh-SoundBible.com-262127569.mp3")
               playsound("hahaha-Peter_De_Lang-1639076107.mp3")
            
               
           else:
               if warnings_left>0:
                   engine.say("Oops! That is not a valid letter. ")
                   engine.runAndWait()
                   playsound("Sad_Trombone-Joe_Lamb-665429450.mp3")
                   engine.say("You have "+ str(warnings_left-1) +" warnings left: ")
                   engine.runAndWait()
                   print("Oops! That is not a valid letter. You have ",(warnings_left-1)," warnings left: "+get_guessed_word(secret_word, letter))
                   warnings_left-=1
               else:
                   engine.say("Oops! That is not a valid letter. ")
                   engine.runAndWait()
                   playsound("Sad_Trombone-Joe_Lamb-665429450.mp3")
                   engine.say("You have no warnings left so you lose one guess: ")
                   engine.runAndWait()
                   print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "+get_guessed_word(secret_word, letter))
                   guesses_left-=1
        
        if is_word_guessed(secret_word, letter):
            engine.say("Congratulations, you won! Your total score for this game is: "+ str((guesses_left)*unique))
            engine.runAndWait()
            print("-----------------")
            print("Congratulations, you won!")
            print("Your total score for this game is: ",((guesses_left)*unique))
            playsound("SMALL_CROWD_APPLAUSE-Yannick_Lemieux-1268806408.mp3")
            break

    if (guesses_left)<=0:
        engine.say("Sorry, you ran out of guesses. ")
        engine.runAndWait()
        engine.say("The word was "+secret_word)
        engine.runAndWait()
        engine.say("Better luck next time !")
        engine.runAndWait()
        print("-----------------")
        print("Sorry, you ran out of guesses. The word was "+secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

    ###############
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 160)
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines.     
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    engine.say("                                                                                ")
    engine.runAndWait()
    engine.say("Do you want to play again? Press y if yes and n if no")
    engine.runAndWait()
    repeat = input("Do you want to play again? (Y/n): ")
    while repeat == "Y" or repeat == "y":
        secret_word = choose_word(wordlist)
        hangman_with_hints(secret_word)
        engine.say("                                                                                ")
        engine.runAndWait()
        engine.say("Do you want to play again? Press y if yes and n if no")
        engine.runAndWait()
        repeat = input("Do you want to play again? (Y/n): ")

    if repeat == 'n' or repeat == "N":
        engine.say("Ok, then see you soon")
        engine.runAndWait()
        print("Ok, then see you soon ")
