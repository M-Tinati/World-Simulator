# World_Name = "Earth"
# Population = 10
Temperature = 24.5
World_Active = True

print("========== WORLD SIMULATOR ==========")
World_Name = input("Enter world name : ")
Creature_Name = input("Enter creature name : ")
Population = int(input("Enter Population  : "))
print("========== WORLD CREATED ==========")
print("World : " ,World_Name)
print("First Creature:" ,  Creature_Name)
print("Population : " , Population )
print("Temperature : " , Temperature )
print("Active : " , World_Active )
print("Population Next Day:" , Population + 1)
print("============")


