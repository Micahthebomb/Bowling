from Chart import drawChart,getScore
Players = 0

while Players == 0 :
    try:
        Players = int(input("How many players?: "))
    except ValueError:
        print("Only input numbers please")


drawChart(Players)
