print("chose a number for 1 - 16 (0 is included and 16 is not.).")
X = input(
""" 
(CASE SENSITEVE) Enter a capital Y if your number appears in a slide and a capital N if not.
slide 1:
1 3 5 7 9 11 13 15
"""
)
Y = input("slide 2: \n2 3 6 7 10 11 14 15\n")
Z = input("slide 3: \n4 5 6 7 12 13 14 15\n")
W = input("slide 3: \n8 9 10 11 12 13 14 15\n")
All = W+Z+Y+X
if All == "NNNN":
    print("your number is 0") 
elif All == "NNNY":
    print("your number is 1")
elif All == "NNYN":
    print("your number is 2")
elif All == "NNYY":
    print("your number is 3")
elif All == "NYNN":
    print("your number is 4")
elif All == "NYNY":
    print("your number is 5")
elif All == "NYYN":
    print("your number is 6")
elif All == "NYYY":
    print("your number is 7") 
elif All == "YNNN":
    print("your number is 8")
elif All == "YNNY":
    print("your number is 9")
elif All == "YNYN":
    print("your number is 10")
elif All == "YNYY":
    print("your number is 11")
elif All == "YYNN":
    print("your number is 12")
elif All == "YYNY":
    print("your number is 13")
elif All == "YYYN":
    print("your number is 14")
elif All == "YYYY":
    print("your number is 15")
else:
    print("Sorry, but we can't calculate this. plese check your inputs and rerun the program\n")