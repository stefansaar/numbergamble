import random

def number_guessing_game():
    # Initialize scores
    player_score = 0
    computer_score = 0
    
    # Define the reward/penalty scale
    def calculate_reward(attempts):
        if attempts == 1:
            return 50
        elif attempts == 2:
            return 40
        elif attempts == 3:
            return 30
        elif attempts == 4:
            return 20
        elif attempts == 5:
            return 10
        elif attempts == 6:
            return 0
        else:
            # After 6 attempts, start losing money
            # 7 attempts = -10, 8 attempts = -20, etc.
            return -10 * (attempts - 6)
    
    play_again = "yes"
    
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 0 and 100")
    print("Scoring system:")
    print("  1st guess: +$50")
    print("  2nd guess: +$40")
    print("  3rd guess: +$30")
    print("  4th guess: +$20")
    print("  5th guess: +$10")
    print("  6th guess: $0")
    print("  After 6 guesses, you start losing money!")
    print("  7th guess: -$10, 8th guess: -$20, and so on...")
    
    while play_again.lower() in ["yes", "y"]:
        # Generate a random number between 0 and 100
        secret_number = random.randint(0, 100)
        attempts = 0
        
        print("\nI'm thinking of a number between 0 and 100.")
        
        while True:
            # Get user input
            try:
                guess = int(input("Enter your guess: "))
                if guess < 0 or guess > 100:
                    print("Please enter a number between 0 and 100.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
                
            # Increment attempt counter
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                # Calculate reward/penalty
                reward = calculate_reward(attempts)
                
                if reward >= 0:
                    print(f"Congratulations! You guessed the number in {attempts} {'attempt' if attempts == 1 else 'attempts'}!")
                    print(f"You win ${reward}!")
                    player_score += reward
                else:
                    print(f"Finally! You guessed the number in {attempts} attempts.")
                    print(f"You lose ${abs(reward)}!")
                    player_score += reward
                    computer_score += abs(reward)
                
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.\n")
            else:
                print("Too high! Try a lower number.\n")
        
        # Display current scores
        print(f"\nCurrent Score:")
        print(f"Player: ${player_score}")
        print(f"Computer: ${computer_score}")
        
        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ")
    
    print("\nFinal Score:")
    print(f"Player: ${player_score}")
    print(f"Computer: ${computer_score}")
    
    if player_score > computer_score:
        print("You beat the computer! Well done!")
    elif player_score < computer_score:
        print("The computer wins this time. Better luck next time!")
    else:
        print("It's a tie!")
    
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()