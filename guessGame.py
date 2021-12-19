#Guessing Game 

import random

greeting = "Welcome to Guess The Number"
print(greeting)
game_greet = input("What is your name: ")
print(game_greet)

start_game = "Hello " + game_greet + ", I'm thinking of a number between 1 and 100."
print(start_game)

intro = 'Try to guess my number'
print(intro)
range = input("Your guess: ")

if range.isdigit():    #makes sure user insert number 
    range = int(range) #convert string int into int

    if range <= 0:
        print('Type a number larger than 0')
        quit()
else:
    print('Please type a number.')
    quit()

num = random.randint(0, 100)
guesses = 0

while True:
    guesses += 1 #  starts incrementing as soon as loop begins
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():    #makes sure user insert number 
        user_guess = int(user_guess) #convert string int into int
    else:
        print('Please type a number.')
        continue #continue brings us back to the top of the loop 
    
    if user_guess == num:
        print('You got it correct')
        break
    else:
        if user_guess > num:
            print("Ouch! You were above the number, keep guessing")
        else: 
            print("Too Low! You were below the number, keep guessing")

print('You got it in', guesses, "attempts")
    

# while user_guess != num: 
#     print('Try Again')
#     break 
# else: 
#     print('You guessed correct')
    
    
    

