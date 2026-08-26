Temperature = 24.5

print("========== WORLD SIMULATOR ==========")

World_Name = input("Enter world name : ")
Population = int(input("Enter Population  : "))
World_Active = int(input("Is the game active? "))
hungry = int(input("Hungry: "))
thirsty = int(input("Thirsty: "))
alive = bool(int(input("Alive: ")))

print("========== WORLD CREATED ==========")
print("World : ", World_Name)

if Population > 0:

    Creatures = []

    for i in range(Population):
        Creature_Name = input("Enter creature name: ")
        Creature_Name = input("Enter creature name: ")
        Creature_Name = input("Enter creature name: ")
        Creature_Name = input("Enter creature name: ")
        Creatures.append(Creature_Name)
        
    print("Creatures created:")

    for creature in Creatures:
        print(creature)

else:
    print("Invalid population.")

print("Temperature : ", Temperature)

if World_Active == 1:
    print("========== WORLD STATUS ==========")
    print("World is running...")
    print("The world can continue.")

elif World_Active == 0:
    print("========== WORLD STATUS ==========")
    print("World is stopped.")
    print("Simulation cannot continue.")

if not alive:
    print("Creature is dead.")
else:
    print("Creature is alive.")

if hungry == 1 or thirsty == 1:
    print("Creature needs food or water.")
else:
    print("Creature is fine.")

if Population > 0:
    print("Population Next Day:", Population + 1)

print("============")



