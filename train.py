def show_status(Health):
    if Health >= 70:
        print("Healthy")
    elif Health >= 30:
        print("Weak")
    else:
        print("Critical")
    
show_status(80)