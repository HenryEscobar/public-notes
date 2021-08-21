
from collections import Counter
a = Counter
b = Counter(a=5, b=2)  # set counters
a.update("abaaaba")
a['a'] # will return 4

# can do set math on counters

import sched
import time

s = sched.scheduler(time.time, time.sleep)
s.enter(2,1,print, argument=('first',))
s.run()



