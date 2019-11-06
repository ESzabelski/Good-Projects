import random


secretword=input("Please pick a secret word for the other person to match.\
It must be 4 letters or longer.")


listb=[]
listb.extend(secretword)
lengthb=len(listb)
#eg. result is v a n q  u i s h AND length 8

while lengthb <4:
    secretword=input("Try again.  It must be 4 letters or longer.")
    listb=[]
    listb.extend(secretword)
    lengthb=len(listb)
for x in range(40):
    print()

guess = ""
totalGuesses=0
victory=0
how_many_guesses_are_allowed = 5

random_tip=[1,2,3,4,5,6]
random.shuffle(random_tip)

#should 1st tip always be length?
def clues(random_tip):
    if random_tip ==1:
        print("Wrong answer.  The secret word is" , lengthb , " letters long.")
    if random_tip ==2:
        print("Hint: the FIRST letter is: " , listb[0])
    if random_tip ==3:
        print("Hint: the SECOND letter is: " , listb[1])
    if random_tip ==4:
        print("Hint: the THIRD letter is: " , listb[2])        
    if random_tip ==5:
        print("Hint: the FOURTH letter is: " , listb[3])
    if random_tip ==6:
        print("Hint: the LAST letter is: " , listb[lengthb-1])        


while guess != secretword:
    print()
    guess = input("Enter your guess for the secret word: ")
    if guess == secretword:
        victory=1
        break
    totalGuesses +=1

    if totalGuesses==1:
        print()
        print("You have", how_many_guesses_are_allowed-1, "guesses left")
        clues(random_tip[0])

    if totalGuesses==2:
        print()
        print("You have", how_many_guesses_are_allowed-2, "guesses left")
        clues(random_tip[1])

    if totalGuesses==3:
        print()
        print("You have ", how_many_guesses_are_allowed-3, " guesses left")
        clues(random_tip[2])
        
    if totalGuesses==4:
        print()
        print("You have ", how_many_guesses_are_allowed-4, " guess left!!   You get one more clue: ")
        clues(random_tip[3])


    #total guesses before game is over
    if totalGuesses >= how_many_guesses_are_allowed:
        victory=2
        break



if victory == 1:
    print()
    print ("Nice job, you win!")
    print()
elif victory == 2:
    print()
    print("No, you lose.")
    print("The answer was: ", secretword)

    




    
