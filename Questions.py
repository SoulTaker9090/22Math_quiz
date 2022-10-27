def statement_generator (statement, decoration):

    sides = decoration * 3


    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""
score = 0

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
    print("{} times {} is".format(x,times_table))
    user_answer = int(input("Please input your answer"))
    if user_answer == answer:
        print(statement_generator("Congratulations you got The question right", "!"))
        score += 1
