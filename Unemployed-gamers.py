registrations = {}
game_requests = {}
registration_open = True
while registration_open:
    name = input("Student name or quit: ").strip()
    if name.lower() == 'quit':
        registration_open  = False
        break
    else:
        print(f"That dingus is already registered")
    age_input = input("Age:")
    age = int(age_input)
    if age < 12:
        print("Sorry nigga u must be at least 12")    
        continue #
    games = input("Choose a game (Chess/minecraft/roblox): ").strip().lower()
    if games not in ['chess', 'minecraft', 'roblox']:
        print("Pleased choose chess, minecraft, or roblox.")
        continue #
    registrations[name] = games
    game_requests[name] =  games
    print(f"Registered: {name} - {games}")
    loopy = input("Register another student? (yes/no): ")
    if loopy == 'no':
        registration_open = False
        print("Roblox is unavailable. Removing all Roblox requests")
        while "Roblox" in game_requests:
            game_requests.remove("roblox")


