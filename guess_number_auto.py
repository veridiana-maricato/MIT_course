highest = 100
lowest = 0
number = int(input("choose a number between 0 and 100 "))
guessed = False
number_of_tries = 0

def guess():
    global highest, lowest, guessed, number_of_tries
    number_of_tries += 1
    if(number > (highest + lowest)/2):
        lowest = int((highest + lowest)/2)
    else:
        highest = int((highest + lowest)/2)
    if highest == number or lowest == number:
        guessed = True


while (guessed == False):
    guess()
    print(int(highest), int(lowest), number_of_tries)
  

    

