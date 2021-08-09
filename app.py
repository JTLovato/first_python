MENU_PROMPT = "Enter 'a' to add a player, 'l' to see your player, 'f' to find a player by name, or 'q' to quit: "
players = [
    {"name": "Joe Sakic", "goals": 625, "points": 1641},
    {"name": "Patrice Bergeron", "goals": 375, "points": 917},
    {"name": "Mark Messier", "goals": 607, "points": 1200},
    {"name": "Steve Yzerman", "goals": 694, "points": 1877},
]


def add_player():
    name = input("Enter the player name: ")
    goals = input("Enter the player goals: ")
    points = input("Enter the player points: ")

    players.append({
        'name': name,
        'goals': goals,
        'points': points
    })


def list_players():
    for player in players:
        print_player(player)


def print_player(player):
    print(f"Name: {player['name'].title()}")
    print(f"Goals: {player['goals']}")
    print(f"Points: {player['points']}")
    print("")


def find_player():
    search_term = input("Enter The player You're Looking For: ")
    for player in players:
        if player['name'].lower() == search_term.lower():
            print_player(player)


user_options = {
    "a": add_player,
    "l": list_players,
    "f": find_player
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()