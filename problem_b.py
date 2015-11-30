__author__ = 'yousefhamza'
from problem_a import hexByteAddresses
from cache.DirectMappingCache import DirectMappingCache


def problem_b(cache, allow_print):

    for hexAddress in hexByteAddresses:
        cache.cache(hexAddress, allow_print)

if __name__ == '__main__':
    cache = DirectMappingCache(16, 1, 16)
    problem_b(cache, True)
    print cache.getCacheTable()
    print 'miss(e): %f'% (cache.getMissRate() * 100), '%'