# Global Variables 
player1 =''
player2 = ''
game_on = True
player1_count = 0 
player2_count = 0 
tie = 0 
game_count =1
    
# Check the value of input  
def read_required_string(prompt):
    value = ''
    while not value:
        value = input(prompt).strip()
    return value

# Game banner 
def game_banner():
    print("\n")
    print("------Rock | Paper | Scissors--------")
    print("\n")
    
# Ask the players' names    
def intro(player_num):
    player= read_required_string(f"What's your name, {player_num}? ")
    print("--"*20)
    return player
    
# Welcome banner for the players 
def welcome(player1, player2):
    print(f"Welcome to the game, {player1.upper()} and {player2.upper()}!!")

# Count the number of wins, and ties 
def game_rules(choice1, choice2, player1, player2):
    global player1_count, player2_count, tie
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"} 
    print (f"\n| {player1} chose {choices[choice1]} |")
    print (f"| {player2} chose {choices[choice2]} | \n")
    
    if (choice1 == 1 and choice2 == 2) or (choice1 == 2 and choice2 == 3) or (choice1 == 3 and choice2 == 1):
        player2_count += 1
        print(f"{player2.upper()} wins!   {player1} | {player1_count}:{player2_count} | {player2}   Tie: {tie}")
    elif choice1 == choice2: 
        tie+=1
        print(f"It's a tie!   {player1} | {player1_count}:{player2_count} | {player2}   Tie: {tie}")
    else: 
        player1_count += 1
        print(f"{player1.upper()} wins!   {player1} | {player1_count}:{player2_count} | {player2}   Tie: {tie}") 

def play(player):
    while True:
        print("--"*20)
        print(f"{player}, choose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice=input("Select[1-3]: ")
        if choice.isdigit() and int(choice) in range (1,4):
            choice = int(choice)
            break
        else:
            print("Please enter a number from 1 to 3: ")
    return choice

# Main game loop 
def game(player1, player2):
    global game_on, game_count
    while game_on:
        choice1 = play(player1)
        choice2 = play(player2)
        game_rules(choice1, choice2, player1, player2)
        ask_to_play = input("\nDo you what to continue [y/n] ?")

        if ask_to_play == 'y':
            game_on = True
            game_count+=1
        elif ask_to_play == 'n':
            print("--"*20)
            print(f"Total games: {game_count}")
            print(f"{player1} wins: {player1_count}")
            print(f"{player2} wins: {player2_count}")
            print(f"Ties: {tie}")
            print("--"*20)
            print("\n-------Goodbye!-------\n")
            game_on = False
        else: 
            ask_to_play=input('Please enter y for "Yes" or n for "No"')





def run():
    game_banner()
    player1 = intro("Player 1")
    player2 = intro("Player 2")
    welcome(player1, player2)
    game(player1, player2)

run()