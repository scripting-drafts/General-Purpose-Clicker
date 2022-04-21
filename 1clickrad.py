import mouse
import time
import random

times_to_repeat = 40

for t in range(times_to_repeat):
    try:
        t += 1
        x, y = random.uniform(770, 790), random.uniform(740, 780)
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
