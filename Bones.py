import random

#creates the roll function
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint (min_value, max_value)
    return roll

#loop to begin game, allows for configuration of number of players
while True:
    players = input("Welcome to BONES please enter the number of players (2 - 8): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 8:
            break
        else:
            print("Must be between 2 - 8 players.")
    else:
        print ("Invalid, try again.")

max_score = 1000
rolls_left = [2 for _ in range(players)] 
players_scores = [0 for _ in range(players)]
last_player = 0 
game_won = False
single_roll = False 

while max(players_scores) < max_score:
    for player_idx in range(players):
        if game_won == True:
            break
        value = [0, 0]
        keeper = 0 # Added to track the 'locked' die
        single_roll = False
        rolls_left[player_idx] = 2
        print("\nPlayer", player_idx + 1, "turn has just started!\n")
        print("Your total score is:", players_scores[player_idx], "\n")
        current_score = 0
        while True:
            if game_won == True or current_score + players_scores[player_idx] >= 1000:
                game_won = True
                break
            
            if rolls_left[player_idx] <= 0:
                current_score = 0
                print("Bust! No rolls left!")
                break

            should_roll = input("would you like to roll (y) ")
            if should_roll.lower() != "y":
                break

            # Standard double roll
            if should_roll.lower() == "y" and rolls_left[player_idx] == 2:
                value = [roll(), roll()]
                rolls_left[player_idx] -= 2
                print(f"You rolled: {value}")

            # FIXED: Single roll logic now uses the 'keeper' variable instead of checking 'value'
            elif should_roll.lower() == "y" and rolls_left[player_idx] == 1 and single_roll == True:
                value = [keeper, roll()]
                rolls_left[player_idx] -= 1 
                print(f"You rolled: {value}")
                # If the new second die doesn't score, you bust
                if value[1] != 1 and value[1] != 5:
                    current_score = 0
                    break
                else:
                    single_roll = False
            
            # Scoring Logic
            if value[0] == value[1] and value[0] == 1:
                print("Snake Eyes!")
                game_won = True
                last_player = player_idx
                break
                
            if value[0] == value[1] and value[0] > 1:
                print("Doubles!")
                current_score += value[0] * 100
                rolls_left[player_idx] += 2
                value = [0, 0] 
                print("You score is:", current_score)
                
            if 1 in value and 5 in value:
                current_score += 150
                rolls_left[player_idx] += 2
                value = [0, 0] 
                print("You score is:", current_score)

            if (1 in value and 5 not in value) or (5 in value and 1 not in value and value[0] != value[1]):
                # FIXED: Set the 'keeper' here so it survives the value reset
                keeper = 1 if 1 in value else 5
                if keeper == 1: 
                    current_score += 100
                else:
                    current_score += 50
                
                print("Your score is:", current_score)
                rolls_left[player_idx] += 1
                single_roll = True
                value = [0, 0] 

            # Bust check for non-scoring dice
            if value != [0, 0] and (1 not in value and 5 not in value and value[0] != value[1]):
                print("Bust! No scoring dice.")
                current_score = 0
                break
            
        players_scores[player_idx] += current_score
        if players_scores[player_idx] >= max_score:
            game_won = True
            break
        print("Your total score is:", players_scores[player_idx])
        input("\n--- Turn finished. Press Enter to switch players ---")

if max(players_scores) >= 1000:
    max_score = max(players_scores)
    winning_idx = players_scores.index(max_score)
    print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
else:
    print("Player number", last_player + 1, "is the winner by Snake Eyes!" )