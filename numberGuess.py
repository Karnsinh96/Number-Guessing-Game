import random
# to create a range of random numbers between 1-100

n = random.randrange(1,100)
print(n)
# to take a user input to enter a number

guess=None
no_of_guesses=0

while n!= guess:
    guess = int(input("Enter any number: "))
    no_of_guesses=no_of_guesses+1
 # means if n is not equal to the input guess

    # if guess is smaller than n
    if guess < n:
        print("Too low")
        # to again ask for input
        guess = int(input("Enter number again: "))

    # if guess is greater than n
    elif guess > n:
        print("Too high!")
    # to again ask for the user input
        guess = int(input("Enter number again: "))
        
    # if guess gets equals to n terminate the while loop
    else:
        break
    print(f"You Have guessed in {no_of_guesses+1} number of guesses...")
print("you guessed it right!!")