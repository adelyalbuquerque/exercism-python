
def add_gigasecond(data):
    from datetime import timedelta
    novadata = data + timedelta(seconds=10 ** 9)
    return novadata