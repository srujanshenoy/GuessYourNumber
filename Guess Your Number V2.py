# General format
# replace (var) with the variable name

#    (var) = input("slide (number): \n (numbers) \n")

# Verify value of (var)
# if (var) == "Y":
#    (var) = 1
# elif (var) == "N":
#    (var) = 0
# else:
#    print("Oops! This input is not valid. Re-run the program")
#    break

# after this, you have to add a STR_(var) variable where var is the name of the variable.
# and then add it to the All variable


print("chose a number from 1 - 16 (0 is included and 16 is not.).")
while True:
    X = input(
        """(CASE SENSITIVE) Enter a capital Y if your number appears in a slide and a capital N if not.
        enter 0 to stop.
slide 1:
1 3 5 7 9 11 13 15
"""
    )

    # VERIFY VALUE OF X
    if X == "Y":
        X = 1
    elif X == "N":
        X = 0
    elif X == "0":
        print("OK. We will stop. Bye Bye!")
        break
    else:
        print("Oops! This input is not valid. Re-run the program")
        break

    Y = input("slide 2: \n2 3 6 7 10 11 14 15\n")

    # Verify value of Y
    if Y == "Y":
        Y = 1
    elif Y == "N":
        Y = 0
    elif X == "0":
        print("OK. We will stop. Bye Bye!")
        break
    else:
        print("Oops! This input is not valid. Re-run the program")
        break

    Z = input("slide 3: \n4 5 6 7 12 13 14 15\n")

    # verify value of Z
    if Z == "Y":
        Z = 1
    elif Z == "N":
        Z = 0
    elif X == "0":
        print("OK. We will stop. Bye Bye!")
        break
    else:
        print("Oops! This input is not valid. Re-run the program")
        break

    W = input("slide 4: \n8 9 10 11 12 13 14 15\n")

    # VERIFY VALUE OF W
    if W == "Y":
        W = 1
    elif W == "N":
        W = 0
    elif X == "0":
        print("OK. We will stop. Bye Bye!")
        break
    else:
        print("Oops! This input is not valid. Re-run the program")
        break

    # "STR" in the following is a short form for string
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
