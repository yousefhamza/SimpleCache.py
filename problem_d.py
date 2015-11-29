__author__ = 'yousefhamza'
from problem_a import hexByteAddresses
from cache.SetAssociativeCache import SetAssociativeCache

def problem_d(cache):

    for index, hexAddress in enumerate(hexByteAddresses):
        cache.cache(hexAddress)

if __name__ == '__main__':
    cache = SetAssociativeCache(2, 4, 2, 16)
    problem_d(cache)
    print cache.getCacheTable()
    print 'miss(e): %f'% (cache.getMissRate() * 100), '%'