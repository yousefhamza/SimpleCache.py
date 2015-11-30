__author__ = 'yousefhamza'
from problem_a import hexByteAddresses
from cache.DirectMappingCache import DirectMappingCache


def problem_c(cache, allow_print):

    for hexAddress in hexByteAddresses:
        cache.cache(hexAddress, allow_print)

if __name__ == '__main__':
    cache = DirectMappingCache(8, 2, 16)
    problem_c(cache, True)
    print cache.getCacheTable()
    print 'miss(e): %f'% (cache.getMissRate() * 100), '%'