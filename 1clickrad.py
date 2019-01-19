
from pymouse import PyMouse
import time
import random

# t = random.randint(70,130)
t=300
times_to_repeat = t
m = PyMouse()

while times_to_repeat >= 0:
        x = random.uniform(770,790)
        y = random.uniform(740,780)
        z1 = random.uniform(0,1)
	z2 = random.uniform(0,3)
	z = (z1+z2)/2

        x_dim, y_dim = m.screen_size()
        m.click(x, y, 1)

        times_to_repeat -= 1
        print('[clickin'...]')
        time.sleep(z)
        if times_to_repeat == 0:
                break
