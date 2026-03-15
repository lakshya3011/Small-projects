import random
lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
print("***PYTHON NUMBER GUESSING GAME***")
is_running=True
guesses=0
print(f"Guess a number between {lowest_num} and {highest_num}")
while is_running:
    guess=input("Enter yourr guess:")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<lowest_num or guess>highest_num:
            print("Invalid guess:")
            print(f"PLEASE, Guess a number only between {lowest_num} and {highest_num}")
        elif guess>answer:
            print("Too high, Try again")
        elif guess<answer:
            print("Too low, Try again")
        else:
            print(f"CORRECT!!!!!! YOU GOT IT, THE ANSWER WAS {answer}")
            print(f"Number of guesses you took: {guesses}")
            is_running=False
    else: 
        print("Invalid guess:")
        print(f"PLEASE, Guess a number only between {lowest_num} and {highest_num}")
        
