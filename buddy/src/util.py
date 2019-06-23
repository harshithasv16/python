# utilities
import datetime

def getdate():
    '''return current date'''
    today = datetime.date.today()
    d = str(today.day)
    m = str(today.month)
    y = str(today.year)

    # make sure date is in format of ddmmyyyy
    if len(d) < 2:
        d = '0' + d
    if len(m) < 2:
        m = '0' + m
    date = '%s%s%s' % (d, m, y)
    return date
