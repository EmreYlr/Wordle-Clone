from colorama import Fore, Back, Style


def clear():
    print("\n" * 50)


while 1:
    answer = int(input("1-Game Start\n2-How To Play\n3-Game Exit\n>"))
    clear()
    if answer == 1:
        break
    elif answer == 2:
        a = Fore.LIGHTBLACK_EX + Back.GREEN + " A " + Style.RESET_ALL
        b = Fore.LIGHTBLACK_EX + Back.YELLOW + " İ " + Style.RESET_ALL
        c = Back.LIGHTBLACK_EX + Fore.WHITE + " Z " + Style.RESET_ALL
        print("WORDLE'i 6 denemede bulun.\n"
              "Her tahmin 5 harfli doğru bir kelime olmalıdır. Göndermek için enter'a basın.\n"
              "Her tahminden sonra kutucukların renkleri tahmininizin yakınlığına göre değişecektir.\n\n"
              "Örnekler\n"
              "¯¯¯¯¯¯¯¯")
        print(
            " +---+---+---+---+---+\n"
            " |{}| B | O | N | E |\n".format(a),
            "+---+---+---+---+---+\n"
            " A harfi kelimede var ve doğru yerde.\n\n"
            " +---+---+---+---+---+\n"
            " | G |{}| Z | E | M |\n".format(b),
            "+---+---+---+---+---+\n"
            " İ harfi kelimede var fakat yanlış yerde.\n\n"
            " +---+---+---+---+---+\n"
            " | F | A | L | E |{}|\n".format(c),
            "+---+---+---+---+---+\n"
            " Z harfi kelimede yok.\n\n"

            " Her gün yeni bir WORDLE gelir!\n"
        )
        while 1:
            back = int(input("1-Back\n>"))
            if back == 1:
                clear()
                break
            else:
                print("Wrong Key\n")
    elif answer == 3:
        exit(0)
    else:
        print("Wrong Key\n")
