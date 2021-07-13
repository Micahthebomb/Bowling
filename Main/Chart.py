import random

chart_border = "-----------------------------------------"
chart_modules = "|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|"
turns = ["", "", "", "", "", "", "", "", "", ""]






def printHeader():
    print("* = Strike, ^ = Spare")


def initiateTurns():
    rounds = 0
    while True:
        turns[rounds] = getTurns()
        rounds += 1
        if rounds == 10:
            break


def drawChart(Players):

    printHeader()
    start = 0
    print(chart_border)
    total_score = 0
    while True:
        initiateTurns()
        Player_Score = getScore(turns)
        total_score += Player_Score[0]
        start += 1
        if Player_Score[1] == 11:
            print(chart_modules.format(turns[0], turns[1], turns[2], turns[3], turns[4], turns[5], turns[6], turns[7]
                                       , turns[8], turns[9]) + "  Player " + str(start) + "'s Score: " + str(
                Player_Score[0]))
        else:
            print(chart_modules.format(turns[0], turns[1], turns[2], turns[3], turns[4], turns[5], turns[6], turns[7],
                                       turns[8], turns[9]) + "  Player " + str(start) + "'s Score: " + str(
                Player_Score[0]) +
                  "  Tenth Frame Extra Points: " + str(Player_Score[1]))

        if start == Players:
            break
        print(chart_border)

    print(chart_border)
    print("Total score across all players: " + str(total_score))


def getTurns():
    roll_one = random.randint(0, 10)
    if roll_one == 10:
        return "*" + str(roll_one)
    else:
        roll_two = random.randint(0, 10 - roll_one)
        if roll_two == 10:
            return "^" + str(roll_two)
        else:
            return str(roll_one) + "," + str(roll_two)


def getScore(turns):
    first_roll = ["", "", "", "", "", "", "", "", "", ""]
    second_roll = ["", "", "", "", "", "", "", "", "", ""]

    start = 0
    while True:
        if turns[start][:1] == "*":
            first_roll[start] = 10
            second_roll[start] = 0
        elif turns[start][:1] == "^":
            first_roll[start] = 0
            second_roll[start] = 10
        else :
            first_roll[start] = turns[start][:1]
            second_roll[start] = turns[start][2:]


        start += 1
        if start == 10:
            break

    index = 0
    sumOfBrackets = 0
    tenth_bracket_extra = 11
    while True:
        if first_roll[index] == 10 and index == 9:
            tenth_bracket_extra = random.randint(0, 10)
            sumOfBrackets += (int(first_roll[index]) + int(tenth_bracket_extra))  # Strike on last bracket

        elif second_roll[index] == 10 and index == 9:
            tenth_bracket_extra = random.randint(0, 10)
            sumOfBrackets += (int(second_roll[index]) + int(tenth_bracket_extra))  # Spare on second roll and on last bracket

        elif (int(first_roll[index]) + int(second_roll[index])) == 10 and index == 9:
            tenth_bracket_extra = random.randint(0, 10)
            sumOfBrackets += (int(first_roll[index]) + int(second_roll[index]) + int(tenth_bracket_extra))  # Regular Spare on last bracket

        elif first_roll[index] == 10:
            sumOfBrackets += int(int(first_roll[index]) + int(first_roll[index+1]) + int(second_roll[index+1]))  #Strike

        elif second_roll[index] == 10:
            sumOfBrackets += (int(second_roll[index]) + int(first_roll[index + 1]))   #Spare on second roll

        elif (int(first_roll[index]) + int(second_roll[index])) == 10:
            sumOfBrackets += (int(first_roll[index]) + int(second_roll[index]) + int(first_roll[index + 1]))  # Regular Spare

        else:
            sumOfBrackets += int(first_roll[index])
            sumOfBrackets += int(second_roll[index])

        index += 1
        if index == 10:
            break
    return [sumOfBrackets,tenth_bracket_extra]
