# this will ask weather the user has played the game before
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

# if the user enters no the instructions will be displayed
def instructions():
   print()
   print("Hellow this is how you play")
   print("you will select the times tables you would like to be tested on")
   print()
   print("once that has happen it will ask you the question once it shows you the question")
   print("please try to answer the question.")
   print()
   print()
   return ""
# this will make the questions and results look nicer/adds decoration
def statement_generator (statement, decoration):

    sides = decoration * 3


    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""
score = 0
# this is to add decoration around the words
statement_generator("Welcome to My math quiz", "*")
print()
show_instructions = yes_no ("have you played this game before:")
if show_instructions == "no":
    instructions()
# this will ask use to input what they would like to be tested on and display questions it will also keep score of what you got right
Valid = False
while not Valid:
    try:
        times_table = int(input("Enter a times table that you would like to be tested on:"))
        max_value = int(input("Enter the maximum value for your times table:"))
        Valid = True

    except ValueError:
        print("please enter a whole number:")
print("Here is the {} times table you will be tested on".format(times_table))
for x in range(1,max_value + 1):
    answer = x * times_table
    statement_generator("{} times {} is".format(x,times_table),"*")
    user_answer = int(input("Please input your answer"))
    if user_answer == answer:
        print(statement_generator("Congratulations you got The question right", "!"))
        score += 1

    else:
        statement_generator("Sorry you got The question wrong the answer is : = {} ".format(answer), "?")
print("Your score is:  {}".format(score))
