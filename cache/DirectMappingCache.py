__author__ = 'yousefhamza'
from collections import namedtuple
from math import log
from texttable import Texttable
from Cache import Cache


class DirectMappingCache(Cache):

    def isHit(self, address, index):
        address_int = int(address, 2)
        # If cache at that index not None
        if self._cache[index]:
            # Get word index in block
            base = len(address)
            if self._byte_addressed:
                base -= 2
            word_index = 0
            if self._words_per_block > 1:
                word_index = int(address[base - self._word_index_size: base], 2)
            # Get word at that index and compare it
            word_at_index_int = int(self._cache[index][2:][word_index], 2)
            if address_int == word_at_index_int:
                return True
        return False

    def _addToCache(self, index, tag, words):
        self._cache[index] = self._cache_block(1, tag, *words)

    def getCacheTable(self):
        table = Texttable()
        # Defining types of variables at each cols
        table.set_cols_dtype(['t', 'i', 't'] + (['t'] * self._words_per_block))
        # Table header
        rows = [['index', 'valid', 'tag'] +
                ['word (%d)' % i for i in range(self._words_per_block)]
        ]
        # Table rows
        for index, item in enumerate(self._cache):
            row = [bin(index)[2:].zfill(self._index_size)]
            # If item empty
            if not item:
                row += [0, 'XXXX'] + (['XXXX'] * self._words_per_block)
            # If index contains block
            else:
                hexSize = self._memory_address_size / 4
                row += [item.valid, item.tag] + \
                       [hex(int(word, 2))[2:].zfill(hexSize).upper() for word in item[2:]]
            rows.append(row)
        table.add_rows(rows)
        return table.draw()