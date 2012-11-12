# -*- coding: utf-8 -*-
numbers = []

def functionWhile(final, incr):
    for i in range(0, final, incr):
        print "At the top i is %d" % i
        numbers.append(i)

        i += incr
        print "Numbers now: ", numbers    
        print "At the bottom i is %d" % i

functionWhile(6, 2)
print "The numbers:"
for num in numbers:
    print num