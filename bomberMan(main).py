import numpy as np
import os
import sys
import enemy
import time
import random
import livesAndScore
import signal
import getch
import bomb
from termios import tcflush, TCIOFLUSH


class board():
    arr = np.zeros((20, 40), dtype=str)
    l = livesAndScore.livesAndScore()

    def makeBoard(self):

        for i in range(0, 40):
            self.arr[0][i] = 'X'
            self.arr[1][i] = 'X'
            self.arr[17][i] = 'X'
            self.arr[18][i] = 'X'
        for i in range(2, 17):
            for j in range(2, 38):
                self.arr[i][j] = ' '

        for i in range(2, 18):

            self.arr[i][0] = 'X'
            self.arr[i][1] = 'X'
            self.arr[i][38] = 'X'
            self.arr[i][39] = 'X'

        for i in range(3, 17):
            for j in range(4, 37):
                if(i % 2 & j % 2):
                    self.arr[i][j] = 'X'

    def printBoard(self):
        for i in range(0, 20):
            for j in range(0, 40):
                print(self.arr[i][j], end='')

            print('\n', end='')
        print('Lives: ' + str(self.l.lives) + '		Score: ' + str(self.l.score))
        print('\n' * 5)

    def printBricks(self):
        self.arr[2][2] = 'H'


e = enemy.enemy()
e2 = enemy.enemy2()
b = enemy.player()
obj = board()
obj.makeBoard()
bom = bomb.bomb()


def movebom(key):
    if(key == 'w'):
        b.posr -= 1
        if(obj.arr[b.posr][b.posc] == 'X'):
            b.posr += 1
    if(key == 'a'):
        b.posc -= 1
        if(obj.arr[b.posr][b.posc] == 'X'):
            b.posc += 1
    if(key == 's'):
        b.posr += 1
        if(obj.arr[b.posr][b.posc] == 'X'):
            b.posr -= 1
    if(key == 'd'):
        b.posc += 1
        if(obj.arr[b.posr][b.posc] == 'X'):
            b.posc -= 1


def inter(a, b):
    pass


signal.signal(signal.SIGALRM, inter)

bombs_d = []
enemies_a = []


def stateReduce():
    time.sleep(0.01)
    bom.reduceState()


fl1 = 0
fl2 = 0
fl3 = 0
fl4 = 0
fl5 = 0
fl6 = 0
while (1):

    if(obj.arr[bom.posr + 1][bom.posc] == '*'):
        obj.arr[bom.posr + 1][bom.posc] = ' '
    if(obj.arr[bom.posr + 2][bom.posc] == '*'):
        obj.arr[bom.posr + 2][bom.posc] = ' '
    if(obj.arr[bom.posr - 1][bom.posc] == '*'):
        obj.arr[bom.posr - 1][bom.posc] = ' '
    if(obj.arr[bom.posr - 2][bom.posc] == '*'):
        obj.arr[bom.posr - 2][bom.posc] = ' '
    if(obj.arr[bom.posr][bom.posc + 1] == '*'):
        obj.arr[bom.posr][bom.posc + 1] = ' '
    if(obj.arr[bom.posr][bom.posc + 2] == '*'):
        obj.arr[bom.posr][bom.posc + 2] = ' '
    if(obj.arr[bom.posr][bom.posc - 1] == '*'):
        obj.arr[bom.posr][bom.posc - 1] = ' '
    if(obj.arr[bom.posr][bom.posc - 2] == '*'):
        obj.arr[bom.posr][bom.posc - 2] = ' '

    if(obj.arr[bom.posr + 1][bom.posc] == '|'):
        fl3 = 1
    if(obj.arr[bom.posr + 2][bom.posc] == '|'):
        fl3 = 1
    if(obj.arr[bom.posr - 1][bom.posc] == '|'):
        fl3 = 1
    if(obj.arr[bom.posr - 2][bom.posc] == '|'):
        fl3 = 1
    if(obj.arr[bom.posr][bom.posc + 1] == '|'):
        fl3 = 1
    if(obj.arr[bom.posr][bom.posc + 2] == '|'):
        fl3 = 1
    if(obj.arr[bom.posr][bom.posc - 1] == '|'):
        fl3 = 1
    if(obj.arr[bom.posr][bom.posc - 2] == '|'):
        fl3 = 1

    key = None

    signal.alarm(1)
    try:
        key = getch.getch()
        movebom(key)

    except:
        pass
    signal.alarm(0)
    # tcflush(sys.stdin,TCIOFLUSH)

    # time.sleep(0.10)
    rand = random.randint(1, 4)
    rand2 = random.randint(1, 4)
    if(rand == 1):
        e.posc -= 1  # left
        if(obj.arr[e.posr][e.posc] == 'X'):
            e.posc += 1
    elif(rand == 2):
        e.posr += 1  # up
        if(obj.arr[e.posr][e.posc] == 'X'):
            e.posr -= 1
    elif(rand == 3):
        e.posc += 1  # right
        if(obj.arr[e.posr][e.posc] == 'X'):
            e.posc -= 1
    else:
        e.posr -= 1  # down
        if(obj.arr[e.posr][e.posc] == 'X'):
            e.posr += 1

    if(rand2 == 1):
        e2.posc -= 1  # left
        if(obj.arr[e2.posr][e2.posc] == 'X'):
            e2.posc += 1
    elif(rand2 == 2):
        e2.posr += 1  # up
        if(obj.arr[e2.posr][e2.posc] == 'X'):
            e2.posr -= 1
    elif(rand2 == 3):
        e2.posc += 1  # right
        if(obj.arr[e2.posr][e2.posc] == 'X'):
            e2.posc -= 1
    else:
        e2.posr -= 1  # down
        if(obj.arr[e2.posr][e2.posc] == 'X'):
            e2.posr += 1
    if(key == 'b'):
        bom = bomb.bomb()
        # obj.arr[b.posr][b.posc]=bomb.bomb().state
        # bombs_d.append(obj.arr[b.posr][b.posc])
        bom.posr = b.posr
        bom.posc = b.posc

    obj.arr[bom.posr][bom.posc] = bom.state

    obj.arr[e.posr][e.posc] = 'E'
    obj.arr[b.posr][b.posc] = 'B'
    obj.arr[e2.posr][e2.posc] = 'E'
    if(fl1 == 1):
        obj.arr[e.posr][e.posc] = ' '
    if(fl2 == 1):
        obj.arr[e2.posr][e2.posc] = ' '
    if(bom.state > 0):
        stateReduce()
    elif(bom.state == 0):
        stateReduce()
        bom.explode()
        obj.arr[bom.posr][bom.posc] = '0'
        if(obj.arr[bom.posr + 1][bom.posc] != 'X'):
            obj.arr[bom.posr + 1][bom.posc] = '*'
        if(obj.arr[bom.posr + 2][bom.posc] != 'X'):
            obj.arr[bom.posr + 2][bom.posc] = '*'
        if(obj.arr[bom.posr - 1][bom.posc] != 'X'):
            obj.arr[bom.posr - 1][bom.posc] = '*'
        if(obj.arr[bom.posr - 2][bom.posc] != 'X'):
            obj.arr[bom.posr - 2][bom.posc] = '*'
        if(obj.arr[bom.posr][bom.posc + 1] != 'X'):
            obj.arr[bom.posr][bom.posc + 1] = '*'
        if(obj.arr[bom.posr][bom.posc + 2] != 'X'):
            obj.arr[bom.posr][bom.posc + 2] = '*'
        if(obj.arr[bom.posr][bom.posc - 1] != 'X'):
            obj.arr[bom.posr][bom.posc - 1] = '*'
        if(obj.arr[bom.posr][bom.posc - 2] != 'X'):
            obj.arr[bom.posr][bom.posc - 2] = '*'

    if(board.l.lives > 0):
        if(obj.arr[e.posr][e.posc] == '*'or obj.arr[e.posr][e.posc] == '0'):
            obj.arr[e.posr][e.posc] = ' '
            fl1 = 1
            obj.l.score += 100
        if(obj.arr[e2.posr][e2.posc] == '*'or obj.arr[e2.posr][e2.posc] == '0'):
            obj.arr[e2.posr][e2.posc] = ' '
            fl2 = 1
            obj.l.score += 100

        if(fl1 == 1 and fl2 == 1):
            print("You Won!")
            break

        if(obj.arr[b.posr][b.posc] == obj.arr[e.posr][e.posc]):
            print("Wasted!")
            board.l.lives -= 1
            b.posr = 2
            b.posc = 3
            time.sleep(1)

        if(obj.arr[b.posr][b.posc] == '*'or obj.arr[b.posr][b.posc] == '0'):
            print("Wasted!")
            board.l.lives -= 1
            b.posr = 2
            b.posc = 3
            time.sleep(1)

        obj.printBoard()
        obj.makeBoard()
        if(fl3 == 0):
            obj.arr[10][20] = '|'
        else:
            obj.arr[2][2] = ' '

    else:
        print("Game Over.")
        break
