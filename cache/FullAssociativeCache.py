__author__ = 'yousefhamza'
from collections import namedtuple
from datetime import datetime
import sys
from texttable import Texttable
from Cache import Cache

class FullAssociativeCache(Cache):
    def __init__(self, number_of_blocks, words_per_block, memory_address_size, byte_addressed=True):
        Cache.__init__(self, number_of_blocks, words_per_block, memory_address_size, byte_addressed=True)

        words_string = "word0"
        for i in range(words_per_block - 1):
            words_string += " word%d" % (i + 1,)
        self._cache_block = namedtuple("cache_block", "lastUsedTime tag %s" % words_string)

    #index is ignored
    def isHit(self, address, index):
        address_int = int(address, 2)
        for item in self._cache:
            if item:
                words = item[2:]
                for word in words:
                    current_address_int = int(word, 2)
                    if address_int == current_address_int:
                        item = self._cache_block(datetime.now().microsecond, item.tag, *words)
                        return True
        return False

    def _addToCache(self, index, tag, words):
        cache_index_to_add, min_last_time_used = 0, sys.maxint
        for i, item in enumerate(self._cache):
            if not item:
                cache_index_to_add = i
                break
            else:
                if item.lastUsedTime < min_last_time_used:
                    cache_index_to_add = i
                    min_last_time_used = item.lastUsedTime
        self._cache[cache_index_to_add] = self._cache_block(datetime.now().microsecond,
                                                            tag,
                                                            *words)

    def getCacheTable(self):
        table = Texttable()
        table.set_cols_dtype(['i', 't'] + (['t'] * self._words_per_block))
        rows = [['lastUsedTime', 'tag'] +
                ['word (%d)' % i for i in range(self._words_per_block)]
        ]
        for index, item in enumerate(self._cache):
            row = []
            if not item:
                row += [0, 'XXXX'] + (['XXXX'] * self._words_per_block)
            else:
                hexSize = self._memory_address_size / 4
                row += [item.lastUsedTime, item.tag] + \
                       [hex(int(word, 2))[2:].zfill(hexSize).upper() for word in item[2:]]
            rows.append(row)
        table.add_rows(rows)
        return table.draw()