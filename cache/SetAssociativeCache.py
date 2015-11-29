__author__ = 'yousefhamza'
from collections import namedtuple
from datetime import datetime
import sys
from texttable import Texttable
from Cache import Cache


class SetAssociativeCache(Cache):
    def __init__(self, numberOfSets, number_of_blocks, words_per_block, memory_address_size, byte_addressed=True):
        Cache.__init__(self, number_of_blocks, words_per_block,
                                                   memory_address_size, byte_addressed=True)
        del self._cache
        self._caches = [[None] * number_of_blocks]
        for i in range(numberOfSets -1):
            self._caches.append([None] * number_of_blocks)

        words_string = "word0"
        for i in range(words_per_block - 1):
            words_string += " word%d" % (i + 1,)
        self._cache_block = namedtuple("cache_block", "lastUsedTime tag %s" % words_string)


    def isHit(self, address, index):
        address_int = int(address, 2)
        for cache in self._caches:
            if cache[index]:
                words = cache[index][2:]
                for word in words:
                    current_address_int = int(word, 2)
                    if address_int == current_address_int:
                        cache[index] = self._cache_block(datetime.now().microsecond, cache[index].tag, *words)
                        return True
        return False

    def _addToCache(self, index, tag, words):
        cache_index_to_add, min_last_time_used = 0, sys.maxint
        for i, cache in enumerate(self._caches):
            if not cache[index]:
                cache_index_to_add = i
                break
            else:
                if cache[index].lastUsedTime < min_last_time_used:
                    cache_index_to_add = i
                    min_last_time_used = cache[index].lastUsedTime
        self._caches[cache_index_to_add][index] = self._cache_block(datetime.now().microsecond,
                                                   tag,
                                                   *words)
        print self.getCacheTable()
    def getCacheTable(self):
        table_string = ""
        for cache in self._caches:
            table = Texttable()
            table.set_cols_dtype(['t', 'i', 't'] + (['t'] * self._words_per_block))
            rows = [['index', 'timeLastUsed', 'tag'] +
                    ['word (%d)' % i for i in range(self._words_per_block)]
            ]
            for index, item in enumerate(cache):
                row = [bin(index)[2:].zfill(self._index_size)]
                if not item:
                    row += [0, 'XXXX'] + (['XXXX'] * self._words_per_block)
                else:
                    hexSize = self._memory_address_size / 4
                    row += [item.lastUsedTime, item.tag] + \
                           [hex(int(word, 2))[2:].zfill(hexSize).upper() for word in item[2:]]
                rows.append(row)
            table.add_rows(rows)
            table_string += table.draw() + '\n'
        return table_string
