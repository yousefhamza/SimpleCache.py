__author__ = 'yousefhamza'
from problem_a import hexByteAddresses
from problem_b import problem_b
from problem_c import problem_c
from problem_d import problem_d
from problem_e import problem_e
from cache.DirectMappingCache import DirectMappingCache
from cache.SetAssociativeCache import SetAssociativeCache
from cache.FullAssociativeCache import FullAssociativeCache

#Problem B
cache = DirectMappingCache(16, 1, 16)
for i in range(100):
    problem_b(cache)
print cache.getCacheTable()
print 'miss(b): %f'% (cache.getMissRate() * 100), '%'

#Problem C
cache = DirectMappingCache(8, 2, 16)
for i in range(100):
    problem_c(cache)
print cache.getCacheTable()
print 'miss(c): %f'% (cache.getMissRate() * 100), '%'

#Problem D
cache = SetAssociativeCache(2, 4, 2, 16)
for i in range(100):
    problem_d(cache)
print cache.getCacheTable()
print 'miss(d): %f'% (cache.getMissRate() * 100), '%'

#Problem E
cache = FullAssociativeCache(16, 1, 16)
for i in range(100):
    problem_e(cache)
print cache.getCacheTable()
print 'miss(e): %f'% (cache.getMissRate() * 100), '%'