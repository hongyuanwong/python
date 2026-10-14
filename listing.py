Games = ["Minecraft", "Roblox", "Fortnite", "Mario Kart", "Tetris"]
print(Games[0])
print(Games[-1])
Games[2] = 'Zelda'
Games.append('Pokemon')
Games.insert(0,  'Super mario')
del Games[2]
print(Games)
popped_Games = Games
print(Games)
print([popped_Games])
last_owned = Games.pop()
print(f"The game I removed from my game library was {last_owned.title()}.")
list_length = len(Games)
print(list_length)
sorted_Games = sorted(Games)
print(sorted_Games)
Games.reverse()
print(Games)