# Playing with time
import time

cur_time=time.time()
time_struct = time.localtime(cur_time)

import datetime
# today=datetime.today()
today=datetime.datetime.today()
tomorrow = today + datetime.timedelta(1)
yesterday = today - datetime.timedelta(1)

print("today: {t}, tommorow: {tmr}, yesterday: {y}".format(t=today,tmr=tomorrow,y=yesterday))