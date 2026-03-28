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
        rolls_left[last_player] = 2
        if game_won == True:
            break
        else: 
            print("\nPlayer", player_idx + 1, "turn has just started!\n")
            print("Your total score is:", players_scores[player_idx], "\n")
            current_score = 0
            while True:
                should_roll = input("would you like to roll (y) ")

                if should_roll.lower() != "y":
                    break

                if should_roll.lower() == "y" and rolls_left[player_idx] == 2:
                    value = [roll(), roll()]
                    rolls_left[player_idx] -= 2
                    print(value)

                if should_roll.lower() == "y" and 1 in value and rolls_left[player_idx] == 1 and single_roll == True:
                    value = [1, roll()]
                    rolls_left[player_idx] -= 1 
                    print(value)
                    if value[1] != 1 and value[1] != 5:
                        last_player = player_idx
                        current_score = 0
                        break
                    else:
                        single_roll = False

                
                if should_roll.lower() == "y" and 5 in value and rolls_left[player_idx] == 1 and single_roll == True:
                    value = [5, roll()]
                    rolls_left[player_idx] -= 1
                    print(value)
                    if value[1] != 1 and value[1] != 5:
                        last_player = player_idx
                        current_score = 0
                        break
                    else:
                        single_roll = False
            
                if value[0] == value[1] and value[0] == 1:
                    print("Snake Eyes!")
                    current_score = 1000
                    print("You score is:", current_score)
                    game_won = True
                
                if value [0] == value[1] and value[0] != 1:
                    print("Doubles!")
                    current_score += value[0] * 100
                    rolls_left[player_idx] += 2
                    print("You score is:", current_score)
                
                if 1 in value and 5 in value:
                    current_score += 150
                    rolls_left[player_idx] += 2
                    print("You score is:", current_score)

                if 1 in value and 5 not in value or 5 in value and 1 not in value and value[0] != value[1]:
                    if 1 in value: 
                        current_score += 100
                        print("You score is:", current_score)
                        rolls_left[player_idx] += 1
                        single_roll = True
                    else:
                        current_score += 50
                        print("You score is:", current_score)
                        rolls_left[player_idx] += 1
                        single_roll = True

                if rolls_left[player_idx] <= 0 and game_won == False:
                    last_player = player_idx
                    current_score = 0
                    break
                
            
            players_scores[player_idx] += current_score
            if players_scores[player_idx] >= max_score:
                game_won = True
                break
            print("Your total score is:", players_scores[player_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)

