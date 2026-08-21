Temperature = 24.5


print("========== WORLD SIMULATOR ==========")
World_Name = input("Enter world name : ")
Creature_Name = input("Enter creature name : ")
Population = int(input("Enter Population  : "))
World_Active = int(input("Is the game active?"))
print("========== WORLD CREATED ==========")
print("World : " ,World_Name)
print("First Creature:" ,  Creature_Name)
print("Population : " , Population )
print("Temperature : " , Temperature )
print("Active : " , bool(World_Active) )
print("Population Next Day:" , Population + 1)
print("============")


