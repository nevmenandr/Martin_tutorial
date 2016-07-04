#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 04.07.2016 02:08:24 MSK

import os
import pars
import codecs

pth = '../texts/'

def pars_file(f):
    lines = []
    for line in f:
        filtered_sent = pars.proc_line(line)
        sent = '\n'.join(filtered_sent)
        lines.append(sent)
    return lines
        
def main():
    lst = os.listdir(pth)
    crpf = codecs.open('corpus.txt', 'w', 'utf-8')
    for fl in sorted(lst):
        #if fl.startswith('5'):
        f = codecs.open(pth + fl, 'r', 'utf-8')
        #else:
            #f = codecs.open(pth + fl, 'r', 'cp1251')
        print fl
        lines = pars_file(f)
        f.close()
        lines = '\n'.join(lines)
        crpf.write(lines)
    crpf.close()
    return 0

if __name__ == '__main__':
    main()

