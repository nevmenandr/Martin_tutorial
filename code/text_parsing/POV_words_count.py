#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 04.07.2016 02:08:24 MSK

import os
import pars
import codecs

pth = '../texts/'

def pars_file(f, d):
    tflag = 0
    ffl = 0
    for line in f:
        if tflag == 1:
            if 'A Song of Ice and Fire' in line or 'A Game of Thrones' in line:
                tflag = 0
                continue
            #print line
            POV = pars.POV_extr(line)
            if POV:
                p = POV
            else:
                p = ' '
            ffl = 1
            tflag = 0
        else:
            if ffl == 1:
                if '<p>' in line:
                    filtered_sent = pars.proc_line(line)
                    for snt in filtered_sent:
                        wrds = snt.split()
                        if p in d:
                            d[p] += len(wrds)
                        else:
                            d[p] = len(wrds)
                    
        if '<title>' in line:
            tflag = 1
            if ffl == 1:
                pass
            ffl = 0
    return d

        
def main():
    d = {}
    lst = os.listdir(pth)
    for fl in sorted(lst):
        f = codecs.open(pth + fl, 'r', 'utf-8')
        print fl
        d = pars_file(f, d)
        f.close()
    fwd = codecs.open('POV_wordcount', 'w', 'utf-8')
    for p in d:
        fwd.write(p + '\t' + str(d[p]) + '\n')
    return 0

if __name__ == '__main__':
    main()

