video_games = { "The Legend of Zelda: Breath of the Wild": {"genre": "Action-Adventure", "platform": "Nintendo Switch", "rating": 4.9},
    "The Witcher 3: Wild Hunt": {"genre": "Action-RPG", "platform": "PlayStation 4", "rating": 4.8},
    "Overwatch": {"genre": "First-Person Shooter", "platform": "PC", "rating": 4.7},
    "Minecraft": {"genre": "Sandbox", "platform": "Multi-platform", "rating": 4.5},
    "Super Mario Odyssey": {"genre": "Platformer", "platform": "Nintendo Switch", "rating": 4.8}
}


def recommend_game():
    print("Welcome to the Jimmy Johns game Recommendation System!")
    print("Please answer the following questions and Jimmy John will find the right game for you:")
    
    genre = input("What genre of game are you interested in? ")
    platform = input("Which gaming platform do you prefer? ")
    min_rating = float(input("What is the minimum rating you are looking for (out of 5)? "))

    recommended_games = []

    for game, attributes in video_games.items():
        if attributes["genre"].lower() == genre.lower() and platform.lower() in attributes["platform"].lower() and attributes["rating"] >= min_rating:
            recommended_games.append(game)

    if recommended_games:
        print("\nBased on your preferences, Jimmy John recommends the following games:")
        for game in recommended_games:
            print("-", game)
    else:
        print("\nSorry, Jimmy John couldn't find any games matching your preferences, he deeply apologizes :( .")

recommend_game()
