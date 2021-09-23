print("chose a number from 1 - 16 (0 is included and 16 is not.).")
while True:
    X = input(
        """(CASE SENSITEVE) Enter a capital Y if your number appears in a slide and a capital N if not.
slide 1:
1 3 5 7 9 11 13 15
"""
    )

    # VERIFY VALUE OF X
    if X == "Y":
        X = 1
    elif X == "N":
        X = 0
    else:
        print("Oops! This input is not valid. Retun the program")
        break

    Y = input("slide 2: \n2 3 6 7 10 11 14 15\n")

    # Verify value of Y
    if Y == "Y":
        Y = 1
    elif Y == "N":
        Y = 0
    else:
        print("Oops! This input is not valid. Retun the program")
        break

    Z = input("slide 3: \n4 5 6 7 12 13 14 15\n")

    # verify value of Z
    if Z == "Y":
        Z = 1
    elif Z == "N":
        Z = 0
    else:
        print("Oops! This input is not valid. Retun the program")
        break

    W = input("slide 4: \n8 9 10 11 12 13 14 15\n")

    # VERIFY VALUE OF W
    if W == "Y":
        W = 1
    elif W == "N":
        W = 0
    else:
        print("Oops! This input is not valid. Retun the program")
        break

    # "STR" in the folowing is a short form for string
    STR_X = str(X)
    STR_Y = str(Y)
    STR_Z = str(Z)
    STR_W = str(W)
    All = STR_W+STR_Z+STR_Y+STR_X

    # define their value and put it in a var
    Their_Number = int(All, 2)

    # print it
    print(
        f"your number is {Their_Number}\n am i right?\n anyway.. here we go again!")
