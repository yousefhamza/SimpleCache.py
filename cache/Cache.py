__author__ = 'yousefhamza'
import abc
from collections import namedtuple
from math import log


class Cache:
    __metaclass__ = abc.ABCMeta
    def __init__(self, number_of_blocks, words_per_block, memory_address_size, byte_addressed=True):
        """
        :param number_of_blocks: number of blocks in cache
        :param words_per_block: number of words in block
        :param memory_address_size: number of bits of memory addresses
        :param byte_addressed: if false means word addressing
        :return: nothing
        """
        assert words_per_block % 2 == 0 or words_per_block == 1 , 'words per block multiple of 2 or 1'
        assert memory_address_size % 4 == 0, 'address memory size multiple of 4 only' #To make consistent hex numbers
        self._memory_address_size = memory_address_size
        self._words_per_block = words_per_block
        self._byte_addressed = byte_addressed

        # Calculate word index size, and index size
        self._word_index_size = int(log(words_per_block, 2))
        self._index_size = int(log(number_of_blocks, 2))

        """
            Here I construct something called "named tuples" it's basically
            the same as "struct" in C programming language.

            So below I create a struct and name it "cache_block" and save that new "type"
            to global protected variable "self._cache_block" to use later.

            Syntax for it: namedtuple(name, variables)
            variables: string spaced variable names
        """
        words_string = "word0"
        for i in range(words_per_block - 1):
            words_string += " word%d" % (i + 1,)
        # The loop above create a space separated string of words as: "word0 word1 word2 word3"
        # This string is added to named tuple to make variables for words in block
        self._cache_block = namedtuple("cache_block", "valid tag %s" % words_string)
        # Init cache as empty
        self._cache = [None] * number_of_blocks

        self._hits = 0
        self._misses = 0

        # add a variable to hold a counter used for the last recently used entry (used only for cache types that need it)
        self._last_recently_used_counter = 0;

    def cache(self, address):
        """
        :param address: the address in hex decimal of type stirng
        :return: nothing
        """
        assert len(address) * 4 == self._memory_address_size
        binary_address = self._hexStringToBinary(address)

        base = len(binary_address)
        if self._byte_addressed:
            base -= 2

        # Get a list of words contains all words in block with the right word index for each
        words = self._completeBlock(binary_address, base - self._word_index_size, base)
        base -= self._word_index_size

        # Calculate index
        index = binary_address[base - self._index_size: base]
        index = int(index, 2)
        base -= self._index_size

        # After the index assign the rest of the bits to tag
        tag = binary_address[:base]

        if self.isHit(binary_address, index):
            self._hits += 1
        else:
            self._misses += 1
            self._addToCache(index, tag, words)

    @abc.abstractmethod
    def isHit(self, address, index):
        """
        :param address: address to save
        :param index: index to save in (not used for full associative)
        :return: True if in cache, false if not
        """
        return

    @abc.abstractmethod
    def _addToCache(self, index, tag, words):
        """
        :param index: index to add to in cache (not used for full associative)
        :param tag: tag of the address to add
        :param words: the list of words per block
        :return: nothing
        """
        return

    @abc.abstractmethod
    def getCacheTable(self):
        """
        :return: a string of the table to print using "texttable"
        """
        return

    def getMissRate(self):
        """
        Prints cache statistics
        :return: nothing
        """
        print 'miss: ', self._misses
        print 'hit: ',  self._hits
        return self._misses / float(self._hits + self._misses)

    def _hexStringToBinary(self, hexString):
        """
        :param hexString: hex decimal number of type string
        :return: binary number of type string
        """
        if hexString[:2] == "0x":
            return bin(int(hexString, 0))[2:].zfill(self._memory_address_size)
        else:
            return bin(int(hexString, 16))[2:].zfill(self._memory_address_size)

    def _completeBlock(self, binaryAddress, startIndex, endIndex):
        """
        :param binaryAddress: address to add to block
        :param startIndex: word address start index in binary address
        :param endIndex: word address end index in binary address "== startIndex if 1 word/block"
        :return:
        """
        size = endIndex - startIndex
        # size = 0 means 1 work per block
        if size == 0:
            return [binaryAddress]
        words = []
        currentAddress = list(binaryAddress)
        for i in range(size + 1):
            # Increment the word_index bits from 0 to size and assign it to that part
            # Of the binary address that's the word index
            currentAddress[startIndex: endIndex] = bin(i)[2:].zfill(size)
            words += [''.join(currentAddress)]
        return words


    def _generateRecentlyUsedCode(self):
        """
        Get a higher recently used code and update the recently used counter.
        :return: number
        """
        tmp = self._last_recently_used_counter
        self._last_recently_used_counter += 1
        return tmp;