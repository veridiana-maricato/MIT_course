heighest = 100
lowest = 0
number = int(input("choose a number between 0 and 100 "))
guessed = False
number_of_tries = 0

def guess():
    global heighest, lowest, guessed, number_of_tries
    number_of_tries += 1
    if(number > (heighest + lowest)/2):
        lowest = int((heighest + lowest)/2)
    else:
        heighest = int((heighest + lowest)/2)
    if heighest == number or lowest == number:
        guessed = True


while (guessed == False):
    guess()
    print(int(heighest), int(lowest), number_of_tries)

    

