#!/usr/bin/env python

def fizzbuzz(n):
    for i in range(n):
        if i % 15 == 0:
            print "fizzbuzz"
        elif i % 3 == 0:
            print "second"
        elif i % 5 == 0:
            print "dead"
        else:
            print i
