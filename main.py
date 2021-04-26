# Solution 6000 Wiegand Calculator

from art import *
import numpy as np

art = text2art("Wiegand Calculator")


def mci():
    sc = hex(int(input("Enter your Site code: ")))[2:]
    cn = int(input("Enter first card in your card range: "))
    num = int(input("Enter the amount of cards you would like to iterate: "))
    print(" ")
    endcn = int(cn + num)
    array = []
    for x in np.arange(cn, endcn, 1):
        array = np.append(array, x)
    vector = np.vectorize(int)
    array = vector(array)
    for x in array:
        cn = hex(x)[2:]
        if len(cn) <= 1:
            cn = str("000") + str(cn)
        elif len(cn) <= 2:
            cn = str("00") + str(cn)
        elif len(cn) <= 3:
            cn = str("0") + str(cn)
        elif len(cn) > 4:
            print("Card range invalid")
            menu1 = input("Type 1 to return to main menu or 2 to create another: ")
            if menu1 == str(1):
                choice()
            elif menu1 == str(2):
                mci()
        elif len(sc) < 1:
            print("Site code invalid")
            menu1 = input("Type 1 to return to main menu or 2 to create another: ")
            if menu1 == str(1):
                choice()
            elif menu1 == str(2):
                mci()
        if len(sc) > 6:
            print("Site code invalid")
            menu1 = input("Type 1 to return to main menu or 2 to create another: ")
            if menu1 == str(1):
                choice()
            elif menu1 == str(2):
                mci()
        elif len(sc) <= 1:
            sc = str("00000") + str(sc)
        elif len(sc) <= 2:
            sc = str("0000") + str(sc)
        elif len(sc) <= 3:
            sc = str("000") + str(sc)
        elif len(sc) <= 4:
            sc = str("00") + str(sc)
        elif len(sc) <= 5:
            sc = str("0") + str(sc)

        output = sc + cn
        print(output)
    print(" ")
    menu1 = input("Type 1 to return to main menu or 2 to create another: ")
    if menu1 == str(1):
        choice()
    elif menu1 == str(2):
        mci()


def sci():
    while True:
        sc = hex(int(input("Enter your Site code: ")))[2:]
        cn = hex(int(input("Enter your card number: ")))[2:]

        if len(cn) <= 1:
            cn = str("000") + str(cn)
        if len(cn) <= 2:
            cn = str("00") + str(cn)
        if len(cn) <= 3:
            cn = str("0") + str(cn)
        if len(cn) < 1:
            print("Card range invalid (too short)")
            menu1 = input("Type 1 to return to main menu or 2 to create another: ")
            if menu1 == str(1):
                choice()
            elif menu1 == str(2):
                mci()
        if len(cn) > 4:
            print("Card range invalid (too long)")
            menu1 = input("Type 1 to return to main menu or 2 to create another: ")
            if menu1 == str(1):
                choice()
            elif menu1 == str(2):
                mci()
        if len(sc) < 1:
            print("Site code invalid (too short)")
            menu1 = input("Type 1 to return to main menu or 2 to create another: ")
            if menu1 == str(1):
                choice()
            elif menu1 == str(2):
                mci()
        if len(sc) > 6:
            print("Site code invalid (too long)")
            menu1 = input("Type 1 to return to main menu or 2 to create another: ")
            if menu1 == str(1):
                choice()
            elif menu1 == str(2):
                mci()
        if len(sc) <= 1:
            sc = str("00000") + str(sc)
        if len(sc) <= 2:
            sc = str("0000") + str(sc)
        elif len(sc) <= 4:
            sc = str("000") + str(sc)
        elif len(sc) <= 4:
            sc = str("00") + str(sc)
        elif len(sc) <= 5:
            sc = str("0") + str(sc)

        output = sc + cn
        print(" ")
        print("Combined output for input into database: ")
        print(output)
        print(" ")
        menu1 = input("Type 1 to return to main menu or 2 to create another: ")
        if menu1 == str(1):
            choice()
        elif menu1 == str(2):
            sci()


def choice() -> object:
    print(art)
    print("Please select from these options:")
    print("1. Create user data from range of card numbers")
    print("2. Create user data from single card number")
    print("(P.S. Enter any other number to exit)")
    menu = int(input("Enter: "))

    if menu == 1:
        mci()
        exit()
    elif menu == 2:
        sci()
        exit()
    else:
        exit()


if __name__ == "__main__":
    choice = choice()
