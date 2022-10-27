# this will ask wether the user has played the game befor
def yes_no(question):
    valid = False
    while not valid:
        responce = input(question).lower().strip()

        if responce == "yes" or responce == "y":
            responce = "yes"
            return responce
        elif responce == "no" or responce == "n":
            responce = "no"
            return responce

        else:
            print("please answer yes / no")

show_instructions = yes_no ("have you played this game before:")

print("you chose {}".format(show_instructions))
