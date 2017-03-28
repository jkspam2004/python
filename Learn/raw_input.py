from datetime import datetime
now = datetime.now()

print 'today is %s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)


hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Rate per Hour:")
r = float(rate)


gross = 40 * r + (h - 40) * r * 1.5


print gross
