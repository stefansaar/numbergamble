import random

def number_guessing_game():
    # Initialize scores
    player_score = 0
    computer_score = 0
    
    print("\nWelcome to the Number Guessing Game!")
    print("\nGuess a number between 0 and 100")
    
    # Choose game mode
    while True:
        print("\nGame Modes:")
        print("1. Fixed Difficulty - Difficulty level stays the same for all rounds")
        print("2. Increasing Difficulty - Difficulty increases by 1 after each round\n")
        
        try:
            mode = int(input("Choose a game mode (1 or 2): "))
            if mode not in [1, 2]:
                print("Please enter 1 or 2.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Set initial difficulty
    while True:
        try:
            difficulty = int(input("\nChoose starting difficulty (number of free guesses before losing money): "))
            if difficulty < 1:
                print("Difficulty must be at least 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    continue_playing = True
    current_difficulty = difficulty
    
    while continue_playing:
        # Define the reward/penalty scale based on difficulty
        def calculate_reward(attempts, diff):
            if attempts <= diff:
                # Keep the 10$ increments
                return 10 * (diff - attempts + 1)
            else:
                # After free attempts, start losing money
                # -10, -20, etc.
                return -10 * (attempts - diff)
        
        # Show scoring system
        print(f"\nScoring system for difficulty {current_difficulty}:")
        for i in range(1, current_difficulty + 1):
            print(f"  {i}th guess: +${calculate_reward(i, current_difficulty)} (computer pays you)")
        print(f"  {current_difficulty+1}th guess: -$10 (you pay computer)")
        print(f"  {current_difficulty+2}th guess: -$20, and so on...")
        
        # Generate a random number between 0 and 100
        secret_number = random.randint(0, 100)
        attempts = 0
        
        print("\nI'm thinking of a number between 0 and 100.")
        
        while True:
            # Get user input
            try:
                guess = int(input("\nEnter your guess: "))
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
                reward = calculate_reward(attempts, current_difficulty)
                
                if reward >= 0:
                    print(f"\nCongratulations! You guessed the number in {attempts} {'attempt' if attempts == 1 else 'attempts'}!")
                    print(f"You win ${reward}! Computer pays you.")
                    player_score += reward
                    computer_score -= reward  # Computer loses the same amount player wins
                else:
                    print(f"\nFinally! You guessed the number in {attempts} attempts.")
                    print(f"You lose ${abs(reward)}! You pay the computer.")
                    player_score += reward
                    computer_score -= reward  # Computer gains what player loses
                
                break
            elif guess < secret_number:
                print("\n----------------------------------------------\nToo low! Try a higher number.")
            else:
                print("\n----------------------------------------------\nToo high! Try a lower number.")
        
        # Display current scores
        print(f"\nCurrent Score:")
        print(f"Player: ${player_score}")
        print(f"Computer: ${computer_score}")
        
        # In increasing difficulty mode, increase difficulty by 1
        if mode == 2:
            current_difficulty += 1
            print(f"\nDifficulty increased to {current_difficulty} for the next round!")
        
        # Ask about cashing out/paying up instead of asking to play again
        if player_score > 0:
            decision = input(f"\nYou're ahead by ${player_score}! Would you like to cash out and end the game? (yes/no): ")
            if decision.lower() in ["yes", "y"]:
                print(f"\nCongratulations! The computer has paid you ${player_score}. Game over!")
                continue_playing = False
            else:
                print("\nYou've decided to let your winnings ride. Let's play another round!")
        elif player_score < 0:
            decision = input(f"\nYou're down by ${abs(player_score)}. Would you like to pay up and end the game? (yes/no): ")
            if decision.lower() in ["yes", "y"]:
                print(f"\nThank you for paying the computer ${abs(player_score)}. Game over!")
                continue_playing = False
            else:
                print("\nYou've decided to try to win back your losses. Let's play another round!")
        else:
            decision = input("\nYou're currently breaking even. Would you like to end the game? (yes/no): ")
            if decision.lower() in ["yes", "y"]:
                print("\nYou've broken even with the computer. Game over!")
                continue_playing = False
            else:
                print("\nYou've decided to keep playing. Let's go for another round!")
    
    print("\nFinal Score:")
    print(f"Player: ${player_score}")
    print(f"Computer: ${computer_score}")
    
    if player_score > computer_score:
        print("\nYou beat the computer! Well done!")
    elif player_score < computer_score:
        print("\nThe computer wins this time. Better luck next time!")
    else:
        print("\nIt's a tie!")
    
    print("\nThanks for playing!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()