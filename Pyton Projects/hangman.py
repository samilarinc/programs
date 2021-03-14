import random
a = random.randint(1,851)

def graphMaker(counter):
    if counter == 1:
        print("\n\n\n|\n|\n|")
    elif counter == 2:
        print("\n__________\n|\n|\n|\n|\n|")
    elif counter == 3:
        print("\n__________\n|        |\n|        O\n|\n|\n|\n|")
    elif counter == 4:
        print("\n__________\n|        |\n|        O\n|        |\n|        |\n|        |\n| \n")
    elif counter == 5:
        print("\n__________\n|        |\n|        O\n|        |\n|       /|\\ \n|        |\n|\n")
    elif counter == 6:
        print("\n__________\n|        |\n|        O\n|        |\n|       /|\\ \n|        |\n|       / \\ \n")

WL = open("words.txt" , "r")
NOL = 0
totLetters = ''
i = 0
alphabet = 'qwertyuopasdfghjklzxcvbnmi'
harf = ''
fail = 0
for i in range(0,a):
    word = WL.readline().lower()
word = word.strip()
say = 0
wordletter= ''
search = ''
#print(word)
for search in alphabet:
    if search in word:
        wordletter+=search
for say in range(len(word)):
    print("_ ",end="")
while fail < 6:
    letter = input("\nEnter a letter : ")
    letter=letter.lower()
    if len(letter) > 1:
        print("Do not enter more than 1 letter...")
    else:
        #print(wordletter)
        #print(totLetters)
        if letter in word:
            totLetters+=letter
            for harf in word:
                if harf in totLetters:
                    print(harf+" ",end="")
                else:
                    print("_ ",end="")
            if sorted(wordletter) == sorted(totLetters):
                print("\n\nCONGRATULATIONS ! ! !")
                break
            graphMaker(fail)
        else:
            for harf in word:
                if harf in totLetters:
                    print(harf+" ",end="")
                else:
                    print("_ ",end="")
            fail+=1
            graphMaker(fail)
if fail > 6:
    print("YOU LOSE ! ! !")
print("\nThe Game is Over !")
print("The Word Was "+ word.upper())
input()
input()
