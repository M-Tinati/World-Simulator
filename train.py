def check_population(population):
    if population > 0:
        return "World has life"
    elif population == 0:
        return "World is empty"
    elif  population < 0:
        return "Invalid population"
    
status_population = check_population(10)
print(status_population)
