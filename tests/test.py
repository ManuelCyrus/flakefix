#!/bin/python3




def verify(f):
    def chek(n):
        try:
            return n
        except ValueError as e:
            print("value error",e)
    chek()

@verify
def printg(n):
    print(n,"funcionou eitaaaa")


printg(10)