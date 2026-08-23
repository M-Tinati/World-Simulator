# Temperature = 24.5


# print("========== WORLD SIMULATOR ==========")
# World_Name = input("Enter world name : ")
# Creature_Name = input("Enter creature name : ")
# Population = int(input("Enter Population  : "))
# World_Active = int(input("Is the game active?"))
# hungry = int(input("Hungry: "))
# thirsty = int(input("Thirsty: "))
# alive = bool(int(input("Alive: ")))
# print("========== WORLD CREATED ==========")
# print("World : " , World_Name)
# print("First Creature:" ,  Creature_Name)
# if Population > 0:
#     print("World has life")
# elif Population == 0 :
#     print("World is empty")
# else:
#     print("Invalid population")
# print("Temperature : " , Temperature )
# if World_Active == 1:
#     print("========== WORLD STATUS ==========") 
#     print("World is running...") 
#     print("The world can continue.") 
# elif World_Active == 0:
#     print("========== WORLD STATUS ==========") 
#     print("World is stopped.") 
#     print("Simulation cannot continue.")
# if not alive:
#     print("Creature is dead.")
# else:
#     print("Creature is alive.")
# if hungry == 1 or thirsty == 1:
#     print("Creature needs food or water.")
# else:
#     print("Creature is fine.")
# print("Population Next Day:" , Population + 1)
# print("============")










# for i in range(1,11):
#     while World_Active == 1:
#         print("Day" ,  i + 1)
#         i += 1
#         if i == 5:
#             print("Rain started!")
#             continue
#         else:
#             World_Active = 0
        
# print("========== SIMULATION END ==========")



# World_Active = int(input("Is the game active? 1 or 0 : "))
# print("========== WORLD SIMULATOR ==========")
# if World_Active == 1:
#     for i in range(1,11):
#             print("Day" ,i)
#             if i == 5:
#                 print("Rain started!")
# elif World_Active == 0:
#     print("World is stopped.")
# print("========== SIMULATION END ==========")


print("========== WORLD SIMULATOR ==========")
creatures = []
while len(creatures) < 4:
    Creature_Name = input("Enter creature name : ")
    creatures.append(Creature_Name)
for creature  in creatures:
        print(creature)
print("========== SIMULATION END ==========")    


print("========== WORLD SIMULATOR ==========")

creatures = []

creature1 = {
    "name": "Monster",
    "age": 2500,
    "health": 100
}
creatures.append(creature1)

creature2 = {
    "name": "Wolf",
    "age": 7,
    "health": 85
}
creatures.append(creature2)

creature3 = {
    "name": "Human",
    "age": 30,
    "health": 95
}
creatures.append(creature3)

for creature in creatures:
    print()
    print("Creature:", creature["name"])
    print("Age:", creature["age"])
    print("Health:", creature["health"])

print()
print("========== SIMULATION END ==========")