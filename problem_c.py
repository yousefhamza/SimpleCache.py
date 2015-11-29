__author__ = 'yousefhamza'
from problem_a import hexByteAddresses
from cache.DirectMappingCache import DirectMappingCache

def problem_c(cache):

    for hexAddress in hexByteAddresses:
        cache.cache(hexAddress)

if __name__ == '__main__':
    cache = DirectMappingCache(8, 2, 16)
    problem_c(cache)
    print 'miss(e): %f'% (cache.getMissRate() * 100), '%'