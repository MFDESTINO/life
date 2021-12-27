#!/usr/bin/env python3
import os
from src.screen import Screen
from src.life import Life
import time

def main():
    w, h = (80, 40)
    N = 1000
    screen = Screen(w, h)
    life = Life(w, h)
    life.import_frame('examples/amogus.txt')

    for i in range(N):
        screen.refresh(life.frame)
        life.tick()
        time.sleep(0.01)

if __name__ == "__main__":
    main()
