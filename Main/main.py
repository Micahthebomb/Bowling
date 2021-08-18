from Chart import drawChart


def initiate():
    players = 0

    while players == 0:
        try:
            players = int(input("How many players?: "))
        except ValueError:
            print("Only input numbers please")
    drawChart(abs(players))

if __name__ == '__main__':
    initiate()
