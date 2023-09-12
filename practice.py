restraunts = ("Canes", "In-N-out", "Chick-fil-a", "Tacobell", "mcdonalds")

new_resraunt = input("what restraunt would you like to add? ")

def rank_restraunt(new_resraunt, restraunts):

 for i in range(len(restraunts)):
    str = "Do you like A)" + new_resraunt + "or B)" + restraunts[1] + "more? A/B"
    ranking = input(str)
    if ranking =="A":
        restraunts,insert(1, new_resraunt)
        break
    elif ranking == "B":
     continue

    return restraunts

print("Your new ranking is", rank_restraunt(new_resraunt, restraunts))