#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 04.07.2016 02:08:24 MSK

import os
import pars
import codecs

pth = '../texts/'

def pars_file(f):
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
                fw = codecs.open('POV_docs/' + POV + '.txt', 'a', 'utf-8')
            else:
                fw = codecs.open('POV_docs/Unknown.txt', 'a', 'utf-8')
            ffl = 1
            tflag = 0
        else:
            if ffl == 1:
                if '<p>' in line:
                    filtered_sent = pars.proc_line(line)
                    sent = '\n'.join(filtered_sent)
                    fw.write(sent)
        if '<title>' in line:
            tflag = 1
            if ffl == 1:
                fw.close()
            ffl = 0

        
def main():
    lst = os.listdir(pth)
    for fl in sorted(lst):
        f = codecs.open(pth + fl, 'r', 'utf-8')
        print fl
        pars_file(f)
        f.close()
    return 0

if __name__ == '__main__':
    main()

