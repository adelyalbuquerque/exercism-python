def is_leap_year(year = ''):
    if int(year) % 4 == 0:
        if int(year) % 100 == 0 and int(year) % 400 == 0:
            return True
        elif int(year) % 100 == 0 and int(year) % 400 != 0:
            return False
        else:
            return True
    else:
        return False
    