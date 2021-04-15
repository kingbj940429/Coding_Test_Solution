''' 9536번 여우는 어떻게 울지? '''

import sys

def solution():
    T = int(sys.stdin.readline())
    for i in range(T):
        sound = list(map(str, sys.stdin.readline().split()))
        Animal = []
        while True:
            animalSound = list(map(str, sys.stdin.readline().split()))
            if len(animalSound) > 3: break
            Animal.append(animalSound[2])

        for word in sound:
            if word in Animal:
                continue
            print(word, end=' ')
solution()
