#!/usr/bin/env python3
from __future__ import print_function
import heapq

# Huffman encoding

class HuffmanNode(object):
    def __init__(self, item, freq=None, left=None, right=None):
        if freq is None:
            freq = 0
            if left is not None:
                freq += left.freq
            if right is not None:
                freq += right.freq
        self.item = item
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        assert isinstance(other, HuffmanNode)
        return self.freq < other.freq

class HuffmanTree(object):

    def BuildHuffmanCodeTree(self, chars, freqs):
        '''Build a Hufman code tree with given characters and frequencies'''
        charfreqlist = [HuffmanNode(char, freq) 
          for char, freq in sorted(zip(chars, freqs), key=lambda fr: fr[1])]
        heapq.heapify(charfreqlist)
        while len(charfreqlist) >= 2:
            # Extract two min
            left = heapq.heappop(charfreqlist)
            right = heapq.heappop(charfreqlist)
            # combine. Note that the item of non-leaf node is not necessary
            newnode = HuffmanNode(None, left=left, right=right)
            # Put back to the heap
            heapq.heappush(charfreqlist, newnode) 
        self.huffmanRoot = charfreqlist[0]
        self.encodeDict = {}
        self._getEncodeList(self.huffmanRoot, '')
        return

    def BuildHuffmanCodeTreeFromFile(self, chars_file, freqs_file):
        with open(chars_file, 'r') as fin:
            charsstr = fin.read()
        with open(freqs_file, 'r') as fin:
            freqstr = fin.read()
        chars = list(charsstr[::2]) # attention: the characters may contain ","
        freqs = [int(i) for i in freqstr.split(',')[:len(chars)]]
        assert(len(chars) == len(freqs))
        return self.BuildHuffmanCodeTree(chars, freqs)

    def _getEncodeList(self, huffmannode, prefix):
        '''Traverse the huffman tree and get the encode book'''
        if huffmannode.item is None:
            self._getEncodeList(huffmannode.left, prefix+'0')
            self._getEncodeList(huffmannode.right, prefix+'1')
        else:
            self.encodeDict[huffmannode.item] = prefix

    def Encode(self, article):
        return ''.join(self.encodeDict[ch] for ch in article)

    def Decode(self, encoded):
        article = ''
        # Set the initial position to be the root
        curPoint = self.huffmanRoot
        for i in encoded:
            if i == '0':
                curPoint = curPoint.left
            else:
                curPoint = curPoint.right
            if curPoint.item is not None:
                print(curPoint.item, end='')
                curPoint = self.huffmanRoot
        return article

    def __init__(self):
        self.huffmanRoot = None
        self.encodeDict = {}

    def __init__(self, chars_file, freq_file):
        self.BuildHuffmanCodeTreeFromFile(chars_file, freq_file)


if __name__ == '__main__':
    chars_file = '../test/Alphabet1.txt'
    freq_file = '../test/Frequency1.txt'
    hf = HuffmanTree(chars_file, freq_file)
    print('-----Huffman encoding dict:-----')
    for kv in hf.encodeDict.items():
        print('%s: %s' % kv)
    print('-----Original article:-----')
    with open('../test/Message1.txt') as fin:
        article = fin.read()
    print(article)
    print('-----Encoded message:-----')
    encoded = hf.Encode(article)
    print(encoded)
    print('-----Decoded message:-----')
    decoded = hf.Decode(encoded)
    print()
