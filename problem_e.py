__author__ = 'yousefhamza'
from problem_a import hexByteAddresses
from cache.FullAssociativeCache import FullAssociativeCache


def problem_e(cache, allow_print):

    for hexAddress in hexByteAddresses:
        cache.cache(hexAddress, allow_print)

if __name__ == '__main__':
    cache = FullAssociativeCache(16, 1, 16)
    problem_e(cache, True)
    print cache.getCacheTable()
    print 'miss(e): %f'% (cache.getMissRate() * 100), '%'