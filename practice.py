video_games = {
    "The Legend of Zelda: Breath of the Wild": {"genre": "Action-Adventure", "platform": "Nintendo Switch", "rating": 4.9},
    "The Witcher 3: Wild Hunt": {"genre": "Action-RPG", "platform": "PlayStation 4", "rating": 4.8},
    "Overwatch": {"genre": "First-Person Shooter", "platform": "PC", "rating": 4.7},
    "Minecraft": {"genre": "Sandbox", "platform": "Multi-platform", "rating": 4.5},
    "Super Mario Odyssey": {"genre": "Platformer", "platform": "Nintendo Switch", "rating": 4.8},
    "Red Dead Redemption 2": {"genre": "Action-Adventure", "platform": "PlayStation 4, Xbox One, PC", "rating": 4.9},
    "Grand Theft Auto V": {"genre": "Action-Adventure", "platform": "Multi-platform", "rating": 4.8},
    "Fortnite": {"genre": "Battle Royale", "platform": "Multi-platform", "rating": 4.6},
    "FIFA 21": {"genre": "Sports", "platform": "Multi-platform", "rating": 4.4},
    "Call of Duty: Warzone": {"genre": "First-Person Shooter", "platform": "Multi-platform", "rating": 4.7},
    "Among Us": {"genre": "Social Deduction", "platform": "Multi-platform", "rating": 4.5},
    "Animal Crossing: New Horizons": {"genre": "Life Simulation", "platform": "Nintendo Switch", "rating": 4.7},
    "Apex Legends": {"genre": "First-Person Shooter", "platform": "Multi-platform", "rating": 4.6},
    "League of Legends": {"genre": "MOBA", "platform": "PC", "rating": 4.8},
    "Halo Infinite": {"genre": "First-Person Shooter", "platform": "Xbox Series X/S, PC", "rating": 4.7}
}


def recommend_game():
    print("Welcome to the  Fungle bungles Game Recommendation System!")
    print("Please answer the following questions to get a game recommendation:")
    
    genre = input("What genre of game are you interested in? ")
    platform = input("Which gaming platform do you prefer? ")
    min_rating = float(input("What is the minimum rating you are looking for (out of 5)? "))
    multiplayer = input("Do you prefer multiplayer games? (yes/no) ").lower() == "yes"

    recommended_games = []

    for game, attributes in video_games.items():
        if attributes["genre"].lower() == genre.lower() and platform.lower() in attributes["platform"].lower() and attributes["rating"] >= min_rating:
            if multiplayer and "Multiplayer" in game:
                recommended_games.append(game)
            elif not multiplayer and "Multiplayer" not in game:
                recommended_games.append(game)

    if recommended_games:
        print("\nBased on your preferences, Professer P recommends the following games:")
        for game in recommended_games:
            print("-", game)
    else:
        print("\nSorry, Jimmy John couldn't find any games matching your preferences he deeply apologizes :( ).")


recommend_game()
