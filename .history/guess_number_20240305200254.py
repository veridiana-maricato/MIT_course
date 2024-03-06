highest = 100
lowest = 0
number = int(input("choose a number between 0 and 100 "))
guessed = False
number_of_tries = 0

def verify_yes_or_no(answer):
    if answer.lowercase() != "yes" and answer.lowercase() != "no":
        new_ans = input("I don't understand. Please type 'yes' or 'no' ")
        verify_yes_or_no(new_ans)
    return answer.lowercase()

def ask_questions():
    number_of_tries += 1
    if (highest - lowest) <=1:
        guessed = True 
        ans = input(f"Is the number {highest}? Type 'yes' or 'no'. ")        
        clean_ans = verify_yes_or_no(ans)
        if clean_ans == 'yes':
            print("Game over, the machines won. Muahaha.")
        else:
            print(f"Then the number is {lowest}.")
            print("Game over, the machines won. Muahaha.")
        play_again = input("Play again? Type 'yes' or 'no'. ")
        clean_ans = verify_yes_or_no(play_again)
        if clean_ans == 'yes':
            highest = 100
            lowest = 0
            number_of_tries = 0
            ask_questions()

    ans = input(f"Question number {number_of_tries}: is the number between {(highest + lowest)/ 2} and {highest}, including {(highest + lowest)/ 2}? Type 'yes' or 'no'. ")
    clean_ans = verify_yes_or_no(ans)
    if clean_ans == "yes":
        lowest = (highest + lowest) / 2
    else:
        highest = (highest + lowest) / 2

    while not guessed:
        ask_questions()
 

    



# def guess():
#     global highest, lowest, guessed, number_of_tries
#     number_of_tries += 1
#     if(number > (highest + lowest)/2):
#         lowest = int((highest + lowest)/2)
#     else:
#         highest = int((highest + lowest)/2)
#     if highest == number or lowest == number:
#         guessed = True


# while (guessed == False):
#     guess()
#     print(int(highest), int(lowest), number_of_tries)
  

    

