# I am certain of nothing but of the holiness of the heart's affections and the truth of imagination
import mouse
import time
import random
import numpy as np
from bool_converter import strtobool

times_to_repeat = 999

for t in range(times_to_repeat):
    try:
        is_repeat = np.random.choice(a=[True, False], size=(1,), p=[0.1, 0.9])
        is_repeat = strtobool(''.join([str(x) for x in is_repeat]))

        if is_repeat == False or t == 0:
            x, y = 870, 630
            x, y = random.uniform(x - 10, x + 10), random.uniform(y - 20, y + 20)
            
        t += 1
        z = random.uniform(0.4, 0.6)
    
        mouse.move(x, y)
        mouse.click()
        
        if t % 2 == 0 and t % 10 != 0:
            alt_z = random.uniform(0.7, 1)
            choice = random.choice([z, alt_z])
            time.sleep(choice)

        elif t % 3 == 0:
            alt_z = random.uniform(1, 3)
            choice = random.choice([z, alt_z])
            time.sleep(choice)

        elif t % 5 == 0:
            alt_z = random.uniform(3, 5)
            choice = random.choice([z, alt_z])
            time.sleep(choice)

        elif t % 7 == 0:
            alt_z = random.uniform(5, 7)
            choice = random.choice([z, alt_z])
            time.sleep(choice)

        elif t % 10 == 0:
            alt_z = random.uniform(0.4, 23)
            choice = random.choice([z, alt_z])
            time.sleep(choice)

        else:
            choice = z
            time.sleep(choice)

        print('Click: {}'.format(str(t)), '| Slept: {}'.format(str(choice)))
        t -= 1

    except KeyboardInterrupt:
        break
