print("========== WORLD SIMULATOR ==========")

Temperature = 24.5

World_Name = input("Enter world name: ")
Population = int(input("Enter Population: "))
World_Active = int(input("Is the game active? (1/0): "))

print()
print("========== WORLD CREATED ==========")
print("World:", World_Name)
print("Temperature:", Temperature)

if Population >= 3:

    Creatures = []

    for i in range(Population):

        print()
        print("Enter information for Creature", i + 1)

        Creature_Name = input("Name: ")
        Creature_Age = int(input("Age: "))
        Creature_Health = int(input("Health: "))

        x = int(input("Position X: "))
        y = int(input("Position Y: "))

        Creature = {
            "name": Creature_Name,
            "age": Creature_Age,
            "health": Creature_Health,
            "position": (x, y)
        }

        Creatures.append(Creature)

    print()
    print("========== CREATURES ==========")

    for creature in Creatures:
        print("Creature:", creature["name"])
        print("Age:", creature["age"])
        print("Health:", creature["health"])
        print("Position:", creature["position"])
        print()

else:
    print("Population must be at least 3.")

if World_Active == 1:
    print("========== WORLD STATUS ==========")
    print("World is running...")
    print("The world can continue.")

elif World_Active == 0:
    print("========== WORLD STATUS ==========")
    print("World is stopped.")
    print("Simulation cannot continue.")

else:
    print("Invalid world status.")

print("============")