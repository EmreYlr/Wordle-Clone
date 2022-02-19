import random
from colorama import Fore, Back, Style
import HowToPlay


def clear():
    print("\n" * 50)


def word_of_the_day():
    f = open("word.txt", "r")
    rand = random.randint(1, 4974)
    file = f.readlines()
    return file[rand]


# Does the word make sense
def search(s_key):
    f = open("word.txt", "r")
    count = 0
    file = f.readlines()
    while 1:
        if s_key.capitalize() + "\n" == file[count].capitalize():
            return 1
        else:
            count += 1
            if count == 4974:
                return 0


check = 0  # game lose control
x_axis = 0
entered_word = []  # Entered word control

# word remove \n , difference list and keys upper
word = word_of_the_day()
lose_word = word
word = word.upper()
word = list(word)
word.remove("\n")
# print(word)  # WORD
print("WORDLE TR \n")
char = \
    [["   ", "   ", "   ", "   ", "   "],
     ["   ", "   ", "   ", "   ", "   "],
     ["   ", "   ", "   ", "   ", "   "],
     ["   ", "   ", "   ", "   ", "   "],
     ["   ", "   ", "   ", "   ", "   "],
     ["   ", "   ", "   ", "   ", "   "]]
while check < 6:
    key = input("Enter A Word:")
    if not search(key):
        continue
    else:
        if key in entered_word:
            print("Same Word")
            continue
        else:
            entered_word.append(key)
    if len(key) != 5:
        print("Wrong Word")
    else:
        key = key.upper()
        key_list = list(key)
        i = 0
        j = 0
        cntr = 0  # Game win control
        while i < 5:
            if key[i] == word[i]:
                char[x_axis][i] = Fore.LIGHTBLACK_EX + Back.GREEN + " " + key_list[i] + " " + Style.RESET_ALL
                i += 1
                cntr += 1
            else:
                while j < 5:
                    if key[i] == word[j]:
                        char[x_axis][i] = Fore.LIGHTBLACK_EX + Back.YELLOW + " " + key_list[i] + " " + Style.RESET_ALL
                        break
                    else:
                        j += 1
                        if j == 5:
                            char[x_axis][i] = Back.LIGHTBLACK_EX + Fore.WHITE + " " + key_list[
                                i] + " " + Style.RESET_ALL

                j = 0
                i += 1
        clear()
        print(" +---+---+---+---+---+\n"
              " |{}|{}|{}|{}|{}|\n".format(char[0][0], char[0][1], char[0][2], char[0][3], char[0][4]),
              "+---+---+---+---+---+\n"
              " |{}|{}|{}|{}|{}|\n".format(char[1][0], char[1][1], char[1][2], char[1][3], char[1][4]),
              "+---+---+---+---+---+\n"
              " |{}|{}|{}|{}|{}|\n".format(char[2][0], char[2][1], char[2][2], char[2][3], char[2][4]),
              "+---+---+---+---+---+\n"
              " |{}|{}|{}|{}|{}|\n".format(char[3][0], char[3][1], char[3][2], char[3][3], char[3][4]),
              "+---+---+---+---+---+\n"
              " |{}|{}|{}|{}|{}|\n".format(char[4][0], char[4][1], char[4][2], char[4][3], char[4][4]),
              "+---+---+---+---+---+\n"
              " |{}|{}|{}|{}|{}|\n".format(char[5][0], char[5][1], char[5][2], char[5][3], char[5][4]),
              "+---+---+---+---+---+\n"
              )
        if cntr == 5:
            print("Game Win")
            exit(0)
        cntr = 0
        check += 1
        x_axis += 1
print("Word: {}".format(lose_word.capitalize()))
print("Game Lose")
exit(0)
