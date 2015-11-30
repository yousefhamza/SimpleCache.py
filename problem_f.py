__author__ = 'yousefhamza'
from problem_a import hexByteAddresses
from problem_b import problem_b
from problem_c import problem_c
from problem_d import problem_d
from problem_e import problem_e
from cache.DirectMappingCache import DirectMappingCache
from cache.SetAssociativeCache import SetAssociativeCache
from cache.FullAssociativeCache import FullAssociativeCache

# printing purposes
allow_print = False

#Problem B
print("\n\n############ Part B ############\n")
cache = DirectMappingCache(16, 1, 16)
for i in range(100):
    if(i < 2):
        allow_print = True
        print "\nLoop %s" %(i,)
    else:
        allow_print = False

    problem_b(cache, allow_print)
print cache.getCacheTable()
print 'miss(b): %f'% (cache.getMissRate() * 100), '%'

#Problem C
print("\n\n############ Part C ############\n")
cache = DirectMappingCache(8, 2, 16)
for i in range(100):
    if(i < 2):
        allow_print = True
        print "\nLoop %s" %(i,)
    else:
        allow_print = False
    problem_c(cache, allow_print)
print cache.getCacheTable()
print 'miss(c): %f'% (cache.getMissRate() * 100), '%'

#Problem D
print("\n\n############ Part D ############\n")
cache = SetAssociativeCache(2, 4, 2, 16)
for i in range(100):
    if(i < 2):
        allow_print = True
        print "\nLoop %s" %(i,)
    else:
        allow_print = False
    problem_d(cache, allow_print)
print cache.getCacheTable()
print 'miss(d): %f'% (cache.getMissRate() * 100), '%'

#Problem E
print("\n\n############ Part E ############\n")
cache = FullAssociativeCache(16, 1, 16)
for i in range(100):
    if(i < 2):
        allow_print = True
        print "\nLoop %s" %(i,)
    else:
        allow_print = False
    problem_e(cache, allow_print)
print cache.getCacheTable()
print 'miss(e): %f'% (cache.getMissRate() * 100), '%'