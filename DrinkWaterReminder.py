import time
timetamp = time.strftime('%H:%M:%S')
print(timetamp)
waterTime = int(time.strftime('%H'))
if (waterTime < 11):
    print('You had to drink water after every hour.')
else:
    print('You are ok.')