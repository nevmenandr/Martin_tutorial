#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 04.07.2016 03:34:14 MSK

import sys
import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
argument = 'corpus.txt'
data = gensim.models.word2vec.LineSentence(argument)
model = gensim.models.Word2Vec(data, size=300, window=3, min_count=3, sg=0)
model.init_sims(replace=True)
model.save('model/SIF.model')
