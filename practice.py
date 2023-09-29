games = {"Super Mario bro's": ["adventure", "2-D platformer", "singleplayer"], "Overwatch": ["fps", "3-D", "multiplayer"], "Inside": ["Horror", "2-D", "singleplayer"], "Portal 2": ["mystery", "3-D", "singleplayer"], "Terraria": ["adventure", "2-D", "singleplayer"]}
recs = []

print("Welcome to the ShimmyJimmy game recomendation program! Enter A if you would like to give it a try, or Q to quit ")
def findrec(games) :
    typ = input("What type of games do you like to play? multiplayer or singleplayer ")
    genre = input("Enter a genre,(ex: adventure,horror etc) ")
    for game in games:
        if games[game][0] == genre and games[game][2] == typ:
            return game
    for game in games: 
        if games[game][0] == genre or games[game][2] == typ:
            return game
    return"no game"
        
addquit = input("A / Q ")
while addquit == "A":
    recs.append(findrec(games))
    addquit = input("Would you like to try another game? A / or quit? Q ")

print(recs)
print("Thanks for trying out Shimmy Jimmys game recommendation program! ")