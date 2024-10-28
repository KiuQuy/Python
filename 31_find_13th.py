from datetime import date, timedelta

def friday_the_13th():

    # Ngay bat dau:
    today = date.today()
    
    # Neu ngay bat dau la ngay 13 -> return
    if today.day == 13 and today.weekday() == 4:  
    # 0-thu2, 1-thu3,...
        return today.strftime("%Y-%m-%d")
    
    # Tang dan so ngay cho toi khi thoa ma
    next_day = today + timedelta(days=1)
    while not (next_day.day == 13 and next_day.weekday() == 4):
        next_day += timedelta(days=1)
    
    # Return the date in YYYY-MM-DD format
    return next_day.strftime("%Y-%m-%d")


# Test
print (friday_the_13th())
