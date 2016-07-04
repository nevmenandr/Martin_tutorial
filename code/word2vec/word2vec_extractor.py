#!/usr/local/python/python2.7/bin/python2.7
# coding: utf-8

import sys
import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
our_model = 'model/SIF.model'
words = ['power', 'love', 'war', 'death', 'honor', 'family', 'house']
model = gensim.models.Word2Vec.load(our_model)
model.init_sims(replace=True)

for word in words:
    if word in model:
        print word
        print model[word][:10]
        for i in model.most_similar(positive=[word], topn=10):
            print i[0], i[1],
        print '\n'
    else:
        print word + ' is not present in the model'

# находим косинусную близость пары слов
print model.similarity(u'stark', u'lannister')

# найди лишнее
print model.doesnt_match(u'arryn baratheon tyrell lannister stark throne'.split())

# реши пропорцию
#print model.most_similar(positive=['woman', 'king'], negative=['man'])[0][0] 
