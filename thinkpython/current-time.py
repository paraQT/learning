import time

unix = time.time()
day = int(unix / 86400)
hour = unix % 86400
minute = hour % 3600
second = minute % 60

print("%s days since epoch" % day)
print("the current time is: " +
    format(int(hour/3600), "02d") + ":" +
    format(int(minute/60), "02d") + ":" +
    format(int(second), "02d"))
