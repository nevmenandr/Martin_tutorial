#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 04.07.2016 01:12:18 MSK

import os
import re
import codecs
from nltk.corpus import stopwords

pth = '../texts/'

def pars_file(f):
    tflag = 0
    for line in f:
        if tflag == 1:
            POV = POV_extr(line)
            tflag = 0
        else:
            filtered_words = proc_line(line)
        if '<title>' in line:
            tflag = 1

def POV_extr(POV):
    if re.search('[A-Z]{2,}', POV):
        POV = re.sub('<.+?>', '', POV)
        POV = re.sub('’', "'", POV)
        print POV
        return POV

def proc_line(line):
    sentenses = []
    line = line.rstrip()
    line = re.sub('^\s+', '', line)
    line = line.replace('</style>', '')
    if '<p>' in line:
        txtline = re.sub('</?p>', '', line)
    else:
        txtline = ''
    sents = txtline.split('. ')
    for sn in sents:
        sn = re.sub(u'["();:.,!“”?-]', '', sn)
        sn = re.sub('<.+?>', '', sn)
        sn = sn.lower()
        tokens = sn.split(' ')
        filtered_words = [word for word in tokens if word not in stopwords.words('english')]
        filtered_words = ' '.join(filtered_words)
        sentenses.append(filtered_words)
    return sentenses

def main():
    lst = os.listdir(pth)
    for fl in sorted(lst):
        f = codecs.open(pth + fl, 'r', 'utf-8')
        pars_file(f)
        f.close()
    return 0

if __name__ == '__main__':
    main()

