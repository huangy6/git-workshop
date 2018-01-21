#!/usr/bin/env python

def fuzzbuzz(n):
    for i in range(n):
        if i % 15 == 0:
            print "fuzzbuzz"
        elif i % 3 == 0:
            print "fuzz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i

if __name__ == "__main__":
    fuzzbuzz(100)
