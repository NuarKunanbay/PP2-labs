import datetime
#1
now = datetime.datetime.now()
print(now.day - 5, now.month, now.year)
#2
yes = now.day - 1, now.month, now.year
tod = now.day, now.month, now.year
tom = now.day + 1, now.month, now.year
print("Yesterday - {0}\n Today - {1}\n Tomorrow - {2}".format(yes, tod, tom))
#3
print(now.strftime("%f"))
#4
def diff(sum_date):
    chetam = now.day - sum_date
    return chetam*86400
