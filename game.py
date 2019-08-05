#!/usr/bin/python3
from random import random
def power() :
    powerA=eval(input())
    powerB=eval(input())
    n=eval(input())
    return powerA,powerB,n
def game(powerA,powerB,n) :
    nA,nB=0,0
    for i in range(n) :
        scoreA,scoreB=simgame(powerA,powerB)
        if scoreA>scoreB :
            nA+=1
        else :
            nB+=1
    return nA,nB
def simgame(powerA,powerB) :
    scoreA,scoreB=0,0
    serving="A"
    while scoreA!=15 and scoreB!=15 :
        if serving=="A" :
            if random()<powerA :
                scoreA+=1
            else :
                serving="B"
        else :
            if random()<powerB :
                scoreB+=1
            else :
                serving="A"
    return scoreA,scoreB
def main() :
    A,B,n=power()
    winA,winB=game(A,B,n)
    print("A获胜场次为{} 胜率为{:0.1%}    B获胜场次为{} 胜率为{:0.1%}  ".format(winA,winA/n,winB,winB/n))
main()
