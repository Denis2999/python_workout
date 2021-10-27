def convert(seconds):
    SECONDS_IN_DAY = 86400
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    day = seconds // SECONDS_IN_DAY
    seconds -= day * SECONDS_IN_DAY

    hour = seconds // SECONDS_IN_HOUR
    seconds -= seconds // SECONDS_IN_HOUR

    minute = seconds // SECONDS_IN_MINUTE
    seconds -= seconds // SECONDS_IN_MINUTE
    print(f'{day}:{hour}:{minute}:{seconds}')

print(convert(86400))
