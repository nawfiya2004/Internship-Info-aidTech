import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    name = input("What's your name? ")
    print(f"Hello, {name}! I'm thinking of a number between 1 and 100. Can you guess what it is?")

    play_again = True
    while play_again:
        secret_number = random.randint(1, 100)
        attempts = 0
        while attempts < 10:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations, {name}! You've guessed the number {secret_number} correctly in {attempts} attempts!")
                break
        
        if attempts == 10:
            print(f"Game over! The number I was thinking of was {secret_number}.")
        
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input.startswith('y')

    print("Thanks for playing!")

if __name__ == "__main__":
    number_guessing_game()
