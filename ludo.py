import random
def dice_roll():
    return random.randint(1, 6)

def move(player, position):
    dice = dice_roll()
    print(f"{player} was roled to get {dice}")
    position += dice
    if position > 57:
        print(f"{player} cannot move{position - dice}")
        position -= dice
    elif position == 57:
        print(f"{player} reached the last point")
    else:
        print(f"{player} moves to the {position}")
    return position

def turn(player, position):
    input(f"{player} player trun:\n Press enter to Roll the dice")
    position = move(player, position)
    return position

def ludo_start():
    players = {"First": 0, "Second": 0}
    game_winner = None
    print("First 57  to reach exactly win:\n ")
    while game_winner is None:
        for player in players.keys():
            players[player] = turn(player,players[player])
            if players[player] == 57:
                winner = player
                print(f"Congratulations! {player} wins the game!")
                break
print("Welcome to the Ludo Game \n Start The Game")
ludo_start()









