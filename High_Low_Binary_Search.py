
# Get a number from the user
usernumber = input("Give a Number for the computer to guess ")
# Cast number
usernumber = int(usernumber)
# defines a min to our range
computermin = 0
# defines a mid point to our range
computermid = 1024 / 2
# defines a max value to our range
computermax = 1024
# array to push 1 & 0 too.
mybin = []
while (True):
    # checks if the guess is correct
    if usernumber == computermid:
        # outputs your number
        mybin.append(1)
        print("Your Number is {}".format(usernumber))
        break
    # prints the computers guess
    print("My Guess is {}".format(computermid))
    # asks for feedback to learn from
    print("Am I high or low Dave? ")
    # gets anwser from user
    answer = input("Anwser:")
    answer = answer.lower()
    # if answer is low exucute this code
    if answer == "low":
        # set a new min to range being our midpoit
        computermin = computermid
        # set new mid point in the center of our range
        computermid = (computermin + computermax) / 2
        # append 1 to binary array
        mybin.append(1)
    # if answer is high execute this code
    elif answer == "high":
        # set new max to the range
        computermax = computermid
        # set new midpoint to range
        computermid = (computermin + computermax) / 2
        # append 0 to array
        mybin.append(0)
    # invaild user input
    else:
        print("Sorry I don't understand dave, is that a high or low?")
# prints number to binary
print(bin(usernumber))
# prints binary array
print(mybin)
# Cool message
print("The age of AI is upon us")
