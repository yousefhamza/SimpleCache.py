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
        # Delete self._cache for safety to make sure it's not used somewhere hidden
        del self._cache
        # add a variables caches to hold an array of caches equal to number of sets
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
                # Get word index in block
                base = len(address)
                if self._byte_addressed:
                    base -= 2
                word_index = 0
                if self._words_per_block > 1:
                    word_index = int(address[base - self._word_index_size: base], 2)
                # Get word at that index and compare it
                word_at_index_int = int(words[word_index], 2)
                if address_int == word_at_index_int:
                    # Update that block last time used parameter
                    cache[index] = self._cache_block(datetime.now().microsecond, cache[index].tag, *words)
                    return True
        return False

    def _addToCache(self, index, tag, words):
        cache_index_to_add, min_last_time_used = 0, sys.maxint
        for i, cache in enumerate(self._caches):
            # If that index is empty at one of the sets add it to it
            if not cache[index]:
                cache_index_to_add = i
                break
            # If not update variables to get the LRU from all sets
            else:
                if cache[index].lastUsedTime < min_last_time_used:
                    cache_index_to_add = i
                    min_last_time_used = cache[index].lastUsedTime
        self._caches[cache_index_to_add][index] = self._cache_block(datetime.now().microsecond,
                                                   tag,
                                                   *words)
    def getCacheTable(self):
        # Print each set and append it to string table_string
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
