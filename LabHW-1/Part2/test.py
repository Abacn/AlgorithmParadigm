#!/usr/bin/env python3
from __future__ import print_function, division

import math
from Huffman import HuffmanTree

def getLenUniformEncoding(lenArticle, nLetter):
    '''Calculate the minimum number of bits from uniform length encoding'''
    # Assume nLetter > 1
    return lenArticle*math.ceil(math.log(nLetter)/math.log(2.0))


def test(chars_file, freq_file, art_file, printResults=True):
    hf = HuffmanTree(chars_file, freq_file)
    with open(art_file, 'r') as fin:
        article = fin.read()
    lenArticle = len(article)
    nLetter = len(hf.encodeDict)
    lenUniformEncoding = getLenUniformEncoding(lenArticle, nLetter)
    # encoding message
    encoded = hf.Encode(article)
    lenHuffmanEncoding = len(encoded)
    # Decoding message
    decoded = hf.Decode(encoded)
    if printResults:
        print('\n-----Huffman codes:-----')
        for k, v in hf.encodeDict.items():
            print('%s: %s' % (k, v))
    #print(article, '\n', decoded)
    assert(article == decoded)
    return lenHuffmanEncoding, lenUniformEncoding, lenArticle, nLetter


if __name__ =='__main__':
    prefix = '../test/'
    result1 = test(prefix+'Alphabet1.txt', prefix+'Frequency1.txt', prefix+'Message1.txt')
    result2 = test(prefix+'Alphabet2.txt', prefix+'Frequency2.txt', prefix+'Message2.txt')
    print('Test\tN_char\tN_dst\tHuffman\tUniform\tRatio')
    print('1\t%d\t%d\t%d\t%d\t%.3f' % (result1[2], result1[3], result1[0], result1[1], 1-result1[0]/result1[1]))
    print('2\t%d\t%d\t%d\t%d\t%.3f' % (result2[2], result2[3], result2[0], result2[1], 1-result2[0]/result2[1]))