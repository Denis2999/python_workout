# def make_readable(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - (hours * 3600)) // 60
#     seconds = seconds - (hours * 3600 + minutes * 60)
#     time = [hours, minutes, seconds]
#
#     if hours < 10:
#         hours = "0" + str(hours)
#     if minutes < 10:
#         minutes = "0" + str(minutes)
#     if seconds < 10:
#         seconds = "0" + str(seconds)
#     return "{}:{}:{}".format(hours, minutes, seconds)
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)


print(make_readable(360))
