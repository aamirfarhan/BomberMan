import random
import time


class enemy():
    posr = 16
    posc = 37

    def move(self):
        #	while (1):
        #		time.sleep(1)
        rand = random.randint(1, 4)
        if(rand == 1):
            self.posc -= 1  # left
        elif(rand == 2):
            self.posr += 1  # up
        elif(rand == 3):
            self.posc += 1  # right
        else:
            self.posr -= 1  # down


class enemy2():
    posr = 3
    posc = 37


class player():
    posr = 2
    posc = 3
