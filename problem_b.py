__author__ = 'yousefhamza'
from problem_a import hexByteAddresses
from cache.DirectMappingCache import DirectMappingCache


def problem_b(cache):

    for hexAddress in hexByteAddresses:
        cache.cache(hexAddress)

if __name__ == '__main__':
    cache = DirectMappingCache(16, 1, 16)
    problem_b(cache)
    print 'miss(e): %f'% (cache.getMissRate() * 100), '%'