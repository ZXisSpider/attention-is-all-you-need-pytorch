import os
import sys
import helpers

def split_bilingual(file):
    with open(file, 'r') as fp1, open('test.en', 'w') as fp2, open('test.spa', 'w') as fp3:
        for line in fp1.readlines():
            pair = [helpers.normalize_string(s) for s in line.rstrip().split('\t')]
            en_sentence = pair[0] + "\n"
            spa_sentence = pair[1] + "\n"
            fp2.write(en_sentence)
            fp3.write(spa_sentence)


if __name__ == '__main__':
    split_bilingual('test_spa.txt')
