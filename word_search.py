#!/usr/bin/env python3
import re

if __name__ == "__main__":
    with open('origin.txt', 'r') as in_stream:
        print('Opening origin.txt')
        with open('origin.txt', 'w') as out_stream:
            for line in in_stream:
                line = line.strip()
                herit_patter_str = re.findall(r'\w*herit\w*')
                herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE)
                word_list = line.split()
                word_list.sort()
                for word in word_list:
                    out_stream.write(f'{word}\n')    



