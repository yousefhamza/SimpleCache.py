__author__ = 'yousefhamza'
from collections import namedtuple
from math import log
from texttable import Texttable
from Cache import Cache


class DirectMappingCache(Cache):

    def isHit(self, address, index):
        address_int = int(address, 2)
        if self._cache[index]:
            for word in self._cache[index][2:]:
                current_address_int = int(word, 2)
                if address_int == current_address_int:
                    return True
        return False

    def _addToCache(self, index, tag, words):
        self._cache[index] = self._cache_block(1, tag, *words)

    def getCacheTable(self):
        table = Texttable()
        table.set_cols_dtype(['t', 'i', 't'] + (['t'] * self._words_per_block))
        rows = [['index', 'valid', 'tag'] +
                ['word (%d)' % i for i in range(self._words_per_block)]
        ]
        for index, item in enumerate(self._cache):
            row = [bin(index)[2:].zfill(self._index_size)]
            if not item:
                row += [0, 'XXXX'] + (['XXXX'] * self._words_per_block)
            else:
                hexSize = self._memory_address_size / 4
                row += [item.valid, item.tag] + \
                       [hex(int(word, 2))[2:].zfill(hexSize).upper() for word in item[2:]]
            rows.append(row)
        table.add_rows(rows)
        return table.draw()