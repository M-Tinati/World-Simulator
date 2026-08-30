def show_status(health):
    if Health >= 70:
        return "Healthy"
    elif Health >= 30:
        return "Weak"
    else:
        return "Critical"
    
status = show_status(80)
print(status)
