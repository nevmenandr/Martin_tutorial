#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 09.07.2014 09:19:35 MSK

import os
import re

def lst():
    lst_f = os.listdir('.')
    return lst_f

def col(iword, tokens, comdic, ichapter, word, fwords):
    ltok = len(tokens) - 1
    ipos = 1
    while ipos <= 6:
        spos = iword + ipos
        if spos > ltok:
            break
        if tokens[spos] in fwords:
            ipos += 1
            continue
        else:
            coll = tokens[spos]
            if word in comdic[ichapter]['collocation']:
                if coll in comdic[ichapter]['collocation'][word]:
                    comdic[ichapter]['collocation'][word][coll] += 1
                else:
                    comdic[ichapter]['collocation'][word][coll] = 1
            else:
                comdic[ichapter]['collocation'][word] = {}
                comdic[ichapter]['collocation'][word][coll] = 1
            if ipos == 1:
                if word in comdic[ichapter]['definition']:
                    if coll in comdic[ichapter]['definition'][word]:
                        comdic[ichapter]['definition'][word][coll] += 1
                    else:
                        comdic[ichapter]['definition'][word][coll] = 1
                else:
                    comdic[ichapter]['definition'][word] = {}
                    comdic[ichapter]['definition'][word][coll] = 1
        ipos += 1
    ipos = 1
    while ipos <= 6:
        spos = iword - ipos
        if spos < 0:
            break
        if tokens[spos] in fwords:
            ipos += 1
            continue
        else:
            coll = tokens[spos]
            if word in comdic[ichapter]['collocation']:
                if coll in comdic[ichapter]['collocation'][word]:
                    comdic[ichapter]['collocation'][word][coll] += 1
                else:
                    comdic[ichapter]['collocation'][word][coll] = 1
            else:
                comdic[ichapter]['collocation'][word] = {}
                comdic[ichapter]['collocation'][word][coll] = 1
        ipos += 1
    return comdic



def person(tokens, comdic, word, ichapter):
    persons = ['aegon', 'targaryen', 'aemon', 'frey', 'greyjoy', 'aerys', 'alester', 'alliser', 'thorne', 'arya', 'asha', 'azor', 'ahai', 'baelor', 'balon', 'barristan', 'selmy', 'stark', 'benjen', 'hornwood', 'beric', 'dondarrion', 'brandon', 'bran', 'bronn', 'brienne', 'cersei', 'cleon', 'craster', 'daario', 'naharis', 'daenerys', 'dorea', 'doreah', 'drogo', 'karstark', 'eddard', 'winterfell', 'elia', 'martell', 'tyrell', 'gregor', 'clegane', 'hodor', 'hoster', 'tully', 'jaime', 'joffrey', 'jorah', 'mormont', 'jorgen', 'jory', 'cassel', 'kevan', 'mace', 'melisandre', 'olene', 'petyr', 'baelish', 'rhaegar', 'rickard', 'rickon', 'robb', 'catelyn', 'arryn', 'robert', 'samwell', 'tarly', 'sandor', 'sansa', 'shae', 'shagga', 'stannis', 'baratheon', 'syrio', 'trystane', 'tyrion', 'tysha', 'tytos', 'tywin', 'lannister', 'varys', 'vickon', 'tyrell', 'viserys', 'walda', 'walder', 'ygritte', 'yoren', 'zhoe', 'pycelle', 'davos', 'seaworth', 'margaery']
    for t in tokens:
        if t in persons:
            if word in comdic[ichapter]['person']:
                if t in comdic[ichapter]['person'][word]:
                    comdic[ichapter]['person'][word][t] += 1
                else:
                    comdic[ichapter]['person'][word][t] = 1
            else:
                comdic[ichapter]['person'][word] = {}
                comdic[ichapter]['person'][word][t] = 1
    return comdic
    

def perstring(fl, fwords, colors):
    count_words = 1
    f = open(fl)
    comdic = {}
    tflag = 0
    ichapter = 0
    for line in f:
        line = line.rstrip()
        line = re.sub('^\s+', '', line)
        line = line.replace('</style>', '')
        if '<p>' in line:
            txtline = re.sub('</?p>', '', line)
        else:
            txtline = line
        if '<title>' in line:
            tflag = 1
            continue
        if '</title>' in line:
            tflag = 0
        if tflag == 1:
            POV = txtline
            if re.search('[A-Z]{2,}', POV):
                POV = re.sub('<.+?>', '', POV)
                POV = re.sub('’', "'", POV)
                print POV
                ichapter += 1
                comdic[ichapter] = {}
                comdic[ichapter]['POV'] = POV
                comdic[ichapter]['collocation'] = {}
                comdic[ichapter]['definition'] = {}
                comdic[ichapter]['person'] = {}
                continue
        txtline = re.sub('[();:.,!“”?“-]', '', txtline)
        txtline = re.sub('<.+?>', '', txtline)
        txtline = txtline.lower()
        tokens = txtline.split(' ')
        iword = 0
        for word in tokens:
            if re.search('[a-z]', word):
                count_words += 1
                if '’' in word:
                    word, add = word.split('’')
                if word in colors:
                    if word in comdic[ichapter]:
                        comdic[ichapter][word] += 1
                    else:
                        comdic[ichapter][word] = 1
                    comdic = col(iword, tokens, comdic, ichapter, word, fwords)
                    comdic = person(tokens, comdic, word, ichapter)
                        
            iword += 1
    f.close()
    return comdic, count_words

def pars_globdic(gdic, colors, count_words):
    persons = ['aegon', 'targaryen', 'aemon', 'frey', 'greyjoy', 'aerys', 'alester', 'alliser', 'thorne', 'arya', 'asha', 'azor', 'ahai', 'baelor', 'balon', 'barristan', 'selmy', 'stark', 'benjen', 'hornwood', 'beric', 'dondarrion', 'brandon', 'bran', 'bronn', 'brienne', 'cersei', 'cleon', 'craster', 'daario', 'naharis', 'daenerys', 'dorea', 'doreah', 'drogo', 'karstark', 'eddard', 'winterfell', 'elia', 'martell', 'tyrell', 'gregor', 'clegane', 'hodor', 'hoster', 'tully', 'jaime', 'joffrey', 'jorah', 'mormont', 'jorgen', 'jory', 'cassel', 'kevan', 'mace', 'melisandre', 'olene', 'petyr', 'baelish', 'rhaegar', 'rickard', 'rickon', 'robb', 'catelyn', 'arryn', 'robert', 'samwell', 'tarly', 'sandor', 'sansa', 'shae', 'shagga', 'stannis', 'baratheon', 'syrio', 'trystane', 'tyrion', 'tysha', 'tytos', 'tywin', 'lannister', 'varys', 'vickon', 'tyrell', 'viserys', 'walda', 'walder', 'ygritte', 'yoren', 'zhoe', 'pycelle', 'davos', 'seaworth', 'margaery']
    p = len(gdic) + 1
    book_color = {}
    chapter_color = {}
    POV_color = {}
    POV_color_g = {}
    coolocation_colors = {}
    definition_colors = {}
    person_colors = {}
    for color in colors:
        POV_color_g[color] = {}
        coolocation_colors[color] = {}
        definition_colors[color] = {}
        person_colors[color] = {}
    f1 = open('/home/boris/Perl/SIF/glob_colors.csv', 'w')
    f2 = open('/home/boris/Perl/SIF/pov_colors.csv', 'w')
    f3 = open('/home/boris/Perl/SIF/collocation_colors.csv', 'w')
    f4 = open('/home/boris/Perl/SIF/definition_colors.csv', 'w')
    f5 = open('/home/boris/Perl/SIF/person_colors.csv', 'w')
    f6 = open('/home/boris/Perl/SIF/book_colors.csv', 'w')
    f7 = open('/home/boris/Perl/SIF/book_colors_ipm.csv', 'w')
    af = [f1, f2, f3, f4, f5, f6, f7]
    clr = ';'.join(colors)
    for fl in af:
        fl.write(';' + clr + '\n')
    for x in range(1, p):
        chdic = gdic[x]
        ch = len(chdic) + 1
        book_color[x] = {}
        for xx in range(1, ch):
            chpt = chdic[xx]
            pov = chpt['POV']
            collocations_dic = chpt['collocation']
            definition_dic = chpt['definition']
            person_dic = chpt['person']
            if ' ' in pov:
                continue
            if 'ACKNOWLEDGMENTS' in pov:
                continue
            if 'WESTEROS' in pov:
                continue
            f1.write(str(x) + '.' + str(xx) + '.' + pov)
            if pov in POV_color:
                pov_i = len(POV_color[pov]) + 1
            else:
                pov_i = 1
                POV_color[pov] = {}
            POV_color[pov][pov_i] = {}
            for color in colors:
                if color in chpt:
                    v = chpt[color]
                else:
                    v = 0
                f1.write(';' + str(v))
                if color in book_color[x]:
                    book_color[x][color] += v
                else:
                    book_color[x][color] = v
                POV_color[pov][pov_i][color] = v
                if pov in POV_color_g[color]:
                    POV_color_g[color][pov] += v
                else:
                    POV_color_g[color][pov] = v
                if color in collocations_dic:
                    col_small_dic = collocations_dic[color]
                else:
                    col_small_dic = {}
                if color in definition_dic:
                    def_small_dic = definition_dic[color]
                else:
                    def_small_dic = {}
                if color in person_dic:
                    pers_small_dic = person_dic[color]
                else:
                    pers_small_dic = {}
                for word in col_small_dic:
                    if word in coolocation_colors[color]:
                        coolocation_colors[color][word] += col_small_dic[word] 
                    else:
                        coolocation_colors[color][word] = col_small_dic[word]
                for word in def_small_dic:
                    if word in definition_colors[color]:
                        definition_colors[color][word] += def_small_dic[word] 
                    else:
                        definition_colors[color][word] = def_small_dic[word]
                for word in pers_small_dic:
                    if word in person_colors[color]:
                        person_colors[color][word] += pers_small_dic[word] 
                    else:
                        person_colors[color][word] = pers_small_dic[word]
            f1.write('\n')
    for pov in POV_color:
        fpov = open('/home/boris/Perl/SIF/pov/' + pov + '.csv', 'w')
        fpov.write(';' + clr + '\n')
        for pov_i in range(1, len(POV_color[pov]) + 1):
            fpov.write(str(pov_i))
            cols = POV_color[pov][pov_i]
            for color in colors:
                if color in cols:
                    v = cols[color]
                else:
                    v = 0
                fpov.write(';' + str(v)) 
            fpov.write('\n')
        fpov.close()
        f2.write(pov)
        for color in colors:
            f2.write(';' + str(POV_color_g[color][pov]))
        f2.write('\n')
    col_words = {}
    def_words = {}
    #print len(coolocation_colors[color])
    for color in colors:
        for word in coolocation_colors[color]:
            v = coolocation_colors[color][word]
            if word in col_words:
                col_words[word] += v
            else:
                col_words[word] = v
            if word in definition_colors[color]:
                v = definition_colors[color][word]
                if word in def_words:
                    def_words[word] += v
                else:
                    def_words[word] = v
    for word in col_words:
        if col_words[word] < 5:
            continue
        f3.write(word)
        for color in colors:
            if word in coolocation_colors[color]:
                f3.write(';' + str(coolocation_colors[color][word]))
            else:
                f3.write(';0')
        f3.write('\n')
    for word in def_words:
        if def_words[word] < 3:
            continue
        f4.write(word)
        for color in colors:
            if word in definition_colors[color]:
                f4.write(';' + str(definition_colors[color][word]))
            else:
                f4.write(';0')
        f4.write('\n')    
    for person in persons:
        f5.write(person)
        for color in colors:
            if person in person_colors[color]:
                v = person_colors[color][person]
            else:
                v = 0
            f5.write(';' + str(v))
        f5.write('\n')
    for x in range(1, p):
        f6.write(str(x))
        f7.write(str(x))
        for color in colors:
            if color in book_color[x]:
                f6.write(';' + str(book_color[x][color]))
                raw_qu = 1000000.0 / int(count_words[x])
                ant = book_color[x][color] / raw_qu
                f7.write(';' + str(ant))
            else:
                f6.write(';0')
                f7.write(';0')
        f6.write('\n')
        f7.write('\n')
    for fl in af:
        fl.close()
                
    
                    
def func_words():
    f = open('/home/boris/Dropbox/docs/A_Song_of_Ice_and_Fire/function_words')
    fw = f.read()
    fwords = fw.split('\n')
    f.close()
    return fwords
                        
def perfile(l, colors):
    gdic = {}
    fwords = func_words()
    arr_count_words = {}
    for fl in l:
        if '.xml' not in fl:
            continue
        print fl
        fr = re.match('(\d)_.+', fl)
        num = fr.group(1)
        cdic, count_words = perstring(fl, fwords, colors)
        gdic[int(num)] = cdic
        arr_count_words[int(num)] = str(count_words)
    return gdic, arr_count_words

def count_w(count_words):
    f = open('/home/boris/Perl/SIF/count.csv', 'w')
    r = len(count_words) + 1
    for x in range(1, r):
        f.write(str(x) + ';' + count_words[x] + '\n')
    f.close()
    

def main():
    colors = ["amber", "amethyst", "apricot", "azure", "black", "blue", "brown", "burgundy", "cerulean", "cobalt", "coral", "crimson", "emerald", "grey", "green", "indigo", "ivory", "jade", "lavender", "lilac", "lime", "magenta", "maroon", "olive", "orange", "ochre", "peach", "pear", "pink", "plum", "purple", "red", "rose", "ruby", "salmon", "sapphire", "scarlet", "silvery", "tan", "teal", "turquoise", "violet", "white", "yellow"]
    l = lst()
    globdic, count_words = perfile(l, colors)
    count_w(count_words)
    pars_globdic(globdic, colors, count_words)
    return 0

if __name__ == '__main__':
    main()

# cor
# collostruct anal

#gl <- read.csv('glob_colors.csv', sep=';', header=TRUE)
#pov <- read.csv('pov_colors.csv', sep=';', header=TRUE)
#person <- read.csv('person_colors.csv', sep=';', header=TRUE)

#book <- read.csv('book_colors.csv', sep=';', header=TRUE)
#bookcl <- data.frame("amber" = book$amber, "amethyst" = book$amethyst, "apricot" = book$apricot, "azure" = book$azure, "burgundy" = book$burgundy, "cobalt" = book$cobalt, "coral" = book$coral, "crimson" = book$crimson, "emerald" = book$emerald, "indigo" = book$indigo, "ivory" = book$ivory, "jade" = book$jade, "lavender" = book$lavender, "lilac" = book$lilac, "lime" = book$lime, "maroon" = book$maroon, "olive" = book$olive, "ochre" = book$ochre, "peach" = book$peach, "pear" = book$pear, "plum" = book$plum, "ruby" = book$ruby, "scarlet" = book$scarlet, "salmon" = book$salmon, "sapphire" = book$sapphire, "tan" = book$tan, "turquoise" = book$turquoise, "violet" = book$violet, "black" = book$black, "blue" = book$blue, "brown" = book$brown, "crimson" = book$crimson, "grey" = book$grey, "green" = book$green, "orange" = book$orange, "pink" = book$pink, "purple" = book$purple, "red" = book$red, "rose" = book$rose, "silvery" = book$silvery, "white" = book$white, "yellow" = book$yellow)
#cor(bookcl)

#bookipm <- read.csv('book_colors_ipm.csv', sep=';', header=TRUE)
#bookclipm  <- data.frame("amber" = bookipm$amber, "amethyst" = bookipm$amethyst, "apricot" = bookipm$apricot, "azure" = bookipm$azure, "burgundy" = bookipm$burgundy, "cobalt" = bookipm$cobalt, "coral" = bookipm$coral, "crimson" = bookipm$crimson, "emerald" = bookipm$emerald, "indigo" = bookipm$indigo, "ivory" = bookipm$ivory, "jade" = bookipm$jade, "lavender" = bookipm$lavender, "lilac" = bookipm$lilac, "lime" = bookipm$lime, "maroon" = bookipm$maroon, "olive" = bookipm$olive, "ochre" = bookipm$ochre, "peach" = bookipm$peach, "pear" = bookipm$pear, "plum" = bookipm$plum, "ruby" = bookipm$ruby, "scarlet" = bookipm$scarlet, "salmon" = bookipm$salmon, "sapphire" = bookipm$sapphire, "tan" = bookipm$tan, "turquoise" = bookipm$turquoise, "violet" = bookipm$violet, "black" = bookipm$black, "blue" = bookipm$blue, "brown" = bookipm$brown, "crimson" = bookipm$crimson, "grey" = bookipm$grey, "green" = bookipm$green, "orange" = bookipm$orange, "pink" = bookipm$pink, "purple" = bookipm$purple, "red" = bookipm$red, "rose" = bookipm$rose, "silvery" = bookipm$silvery, "white" = bookipm$white, "yellow" = bookipm$yellow)
#cor(bookclipm)


#gltb <- data.frame("black" = gl$black, "blue" = gl$blue, "brown" = gl$brown, "crimson" = gl$crimson, "grey" = gl$grey, "green" = gl$green, "orange" = gl$orange, "pink" = gl$pink, "purple" = gl$purple, "red" = gl$red, "rose" = gl$rose, "silvery" = gl$silvery, "white" = gl$white, "yellow" = gl$yellow)
#cor(gltb)

#gltb1 <- data.frame("amber" = gl$amber, "amethyst" = gl$amethyst, "apricot" = gl$apricot, "azure" = gl$azure, "burgundy" = gl$burgundy, "cobalt" = gl$cobalt, "coral" = gl$coral, "crimson" = gl$crimson, "emerald" = gl$emerald, "indigo" = gl$indigo, "ivory" = gl$ivory, "jade" = gl$jade, "lavender" = gl$lavender, "lilac" = gl$lilac, "lime" = gl$lime, "maroon" = gl$maroon, "olive" = gl$olive, "ochre" = gl$ochre, "peach" = gl$peach, "pear" = gl$pear, "plum" = gl$plum, "ruby" = gl$ruby, "scarlet" = gl$scarlet, "salmon" = gl$salmon, "sapphire" = gl$sapphire, "tan" = gl$tan, "turquoise" = gl$turquoise, "violet" = gl$violet)
#cor(gltb1)

#gltb2 <- data.frame("amber" = gl$amber, "amethyst" = gl$amethyst, "apricot" = gl$apricot, "azure" = gl$azure, "burgundy" = gl$burgundy, "cobalt" = gl$cobalt, "coral" = gl$coral, "crimson" = gl$crimson, "emerald" = gl$emerald, "indigo" = gl$indigo, "ivory" = gl$ivory, "jade" = gl$jade, "lavender" = gl$lavender, "lilac" = gl$lilac, "lime" = gl$lime, "maroon" = gl$maroon, "olive" = gl$olive, "ochre" = gl$ochre, "peach" = gl$peach, "pear" = gl$pear, "plum" = gl$plum, "ruby" = gl$ruby, "scarlet" = gl$scarlet, "salmon" = gl$salmon, "sapphire" = gl$sapphire, "tan" = gl$tan, "turquoise" = gl$turquoise, "violet" = gl$violet, "black" = gl$black, "blue" = gl$blue, "brown" = gl$brown, "crimson" = gl$crimson, "grey" = gl$grey, "green" = gl$green, "orange" = gl$orange, "pink" = gl$pink, "purple" = gl$purple, "red" = gl$red, "rose" = gl$rose, "silvery" = gl$silvery, "white" = gl$white, "yellow" = gl$yellow)
#cor(gltb2)


#plot(gl$black, col='black', type='p', pch = 19, cex = 0.3)
#lines(gl$grey, col='grey', type='p', pch = 19, cex = 0.3)
#lines(gl$green, col='green', type='p', pch = 19, cex = 0.3)
#lines(gl$yellow, col='yellow', type='p', pch = 19, cex = 0.3)
#lines(gl$blue, col='blue', type='p', pch = 19, cex = 0.3)
#lines(gl$pink, col='pink', type='p', pch = 19, cex = 0.3)
#lines(gl$red, col='red', type='p', pch = 19, cex = 0.3)
#lines(gl$purple, col='purple', type='p', pch = 19, cex = 0.3)
#lines(gl$orange, col='orange', type='p', pch = 19, cex = 0.3)

#povtb <- data.frame("black" = pov$black, "blue" = pov$blue, "brown" = pov$brown, "crimson" = pov$crimson, "grey" = pov$grey, "green" = pov$green, "orange" = pov$orange, "pink" = pov$pink, "purple" = pov$purple, "red" = pov$red, "silver" = pov$silver, "white" = pov$white, "yellow" = pov$yellow)
#povtb <- data.frame("black" = pov$black, "blue" = pov$blue, "brown" = pov$brown, "grey" = pov$grey, "green" = pov$green, "orange" = pov$orange, "pink" = pov$pink, "purple" = pov$purple, "red" = pov$red, "white" = pov$white, "yellow" = pov$yellow)
#cor(povtb)

#plot(gl$black, col='black', type='l')
#lines(gl$grey, col='grey', type='l')

#plot(gl$blue, col='blue', type='l')
#lines(gl$green, col='green', type='l')
#lines(gl$yellow, col='yellow', type='l')



#plot(gl$black, col='black', type='p', pch = 19, cex = 0.3)
#lines(gl$grey, col='grey', type='p', pch = 19, cex = 0.3)
#lines(gl$green, col='green', type='p', pch = 19, cex = 0.3)
#lines(gl$yellow, col='yellow', type='p', pch = 19, cex = 0.3)
#lines(gl$blue, col='blue', type='p', pch = 19, cex = 0.3)
#lines(gl$pink, col='pink', type='p', pch = 19, cex = 0.3)
#lines(gl$red, col='red', type='p', pch = 19, cex = 0.3)
#lines(gl$purple, col='purple', type='p', pch = 19, cex = 0.3)
#lines(gl$orange, col='orange', type='p', pch = 19, cex = 0.3)

# for word in sorted(rhyme, key=rhyme.get, reverse=True):
#    val = rhyme[word]
#
# import rpy2.robjects as robjects
# print robjects.r('c <- c(1, 2, 3)')

