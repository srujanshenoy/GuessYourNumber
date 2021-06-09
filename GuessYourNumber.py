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
    print("your number is 0\nAm I right?\nBYE.") 
elif All == "NNNY":
    print("your number is 1\nAm I right?\nBYE.")
elif All == "NNYN":
    print("your number is 2\nAm I right?\nBYE.")
elif All == "NNYY":
    print("your number is 3\nAm I right?\nBYE.")
elif All == "NYNN":
    print("your number is 4\nAm I right?\nBYE.")
elif All == "NYNY":
    print("your number is 5\nAm I right?\nBYE.")
elif All == "NYYN":
    print("your number is 6\nAm I right?\nBYE.")
elif All == "NYYY":
    print("your number is 7\nAm I right?\nBYE.") 
elif All == "YNNN":
    print("your number is 8\nAm I right?\nBYE.")
elif All == "YNNY":
    print("your number is 9\nAm I right?\nBYE.")
elif All == "YNYN":
    print("your number is 10\nAm I right?\nBYE.")
elif All == "YNYY":
    print("your number is 11\nAm I right?\nBYE.")
elif All == "YYNN":
    print("your number is 12\nAm I right?\nBYE.")
elif All == "YYNY":
    print("your number is 13\nAm I right?\nBYE.")
elif All == "YYYN":
    print("your number is 14\nAm I right?\nBYE.")
elif All == "YYYY":
    print("your number is 15\nAm I right?\nBYE.")
else:
    print("\nSorry, but we can't calculate this. Please check your inputs and rerun the program.\nEnter ONLY capital letters\n And no numbers like 6 or 7 or letters like m,j,h,b,Spaces,etc... .\nAnd if your number is not there and you typed 'Y' by mistake, don't do the mistake again.\n")