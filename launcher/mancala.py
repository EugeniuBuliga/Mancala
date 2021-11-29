import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Not enough arguments!")
        print("Right application call: mancala.py ai/pvp")
    else:
        if str(sys.argv[1]) == "ai":
            print("Starting player vs computer mode...")

        elif  str(sys.argv[1]) == "pvp":
            print("Starting player vs player mode...")

        else:
            print("Wrong argument. Choose either 'ai' or 'pvp'!")