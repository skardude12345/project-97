import random

chances = 5
number = random.randint(1, 50)
while chances <= 5:
    guess = int(input("Guess the number between 1 and 50: "))
    
    if guess != number and chances > 0:
        if guess < number:
            chances -= 1
            print("You didn't get it right. The number is higher than",guess)
            
        elif guess > number:
            chances -= 1
            print("You didn't get it right. The number is lower than",guess)
        
    
    if guess == number:
        print("You got it right! Congratulations! :)")
        break
    
    if chances == 0:
        print("You lost all your chances. The number was",number)
        break
