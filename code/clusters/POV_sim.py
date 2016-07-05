#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-10-04
# 

from __future__ import print_function

import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
import sys
#from sklearn import feature_extraction

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.externals import joblib

import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab

from sklearn.manifold import MDS
from scipy.cluster.hierarchy import ward, dendrogram

stopwords = nltk.corpus.stopwords.words('english')

def englishTokenizer(text):
    result = text
    result = result.replace('.', ' . ')
    result = result.replace('\n', ' \n ')
    result = result.replace(' .  .  . ', ' ... ')
    result = result.replace(',', ' , ')
    result = result.replace(':', ' : ')
    result = result.replace(';', ' ; ')
    result = result.replace('!', ' ! ')
    result = result.replace('?', ' ? ')
    result = result.replace('\"', ' \" ')
    result = result.replace('\'', ' \' ')
    result = result.replace('(', ' ( ')
    result = result.replace(')', ' ) ') 
    result = re.sub(u'\s+', ' ', result)
    result = result.strip()
    result = result.split(' ')
    return result

def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = englishTokenizer(text)
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search(u'[a-zA-Z]', token):
            #if token not in stopwords:
                filtered_tokens.append(token)
    return filtered_tokens

def main():
    fwr = codecs.open('lemmed_cluster_no_stopwords_4_clusters.txt', 'w', 'utf-8')
    lst = os.listdir('POV_docs')
    titles = []
    contents = []
    names = []
    for fl in lst:
        print (fl)
        titles.append(fl.replace('.txt', ''))
        f = codecs.open('POV_docs/' + fl, 'r', 'utf-8')
        cont = f.read()
        f.close()
        contents.append(cont)
    
    totalvocab_tokenized = []
    for i in contents:
        allwords = tokenize_only(i)
        totalvocab_tokenized.extend(allwords)
        
    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index=totalvocab_tokenized)
    fwr.write('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame\n')
    
    #vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
    
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000, min_df=0.2, use_idf=True, tokenizer=tokenize_only, ngram_range=(1,3))
    tfidf_matrix = tfidf_vectorizer.fit_transform(contents)
    
    for an in tfidf_matrix.shape:
        fwr.write(str(an) + '\t')
        fwr.write('\n')
    #fwr.write('\t'.join(tfidf_matrix.shape))
    terms = tfidf_vectorizer.get_feature_names()
    dist = 1 - cosine_similarity(tfidf_matrix)
    num_clusters = 4
    km = KMeans(n_clusters=num_clusters)
    km.fit(tfidf_matrix)
    clusters = km.labels_.tolist()
    
    joblib.dump(km, 'songs_cluster_4.pkl')
        
    #km = joblib.load('songs_cluster.pkl')
    #clusters = km.labels_.tolist()    


    texts = { 'title': titles, 'content': contents, 'cluster': clusters }
    frame = pd.DataFrame(texts, index=[clusters], columns=['title', 'cluster'])
    fwr.write(str(frame['cluster'].value_counts()))
    
    fwr.write(u'Top terms per cluster:\n')
    order_centroids = km.cluster_centers_.argsort()[:, ::-1] 
    
    
    
    for i in range(num_clusters):
        fwr.write("\nCluster %d words:" % i)
        for ind in order_centroids[i, :20]:
            try:
                #fwr.write(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore') + ', ')
                fwr.write(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0] + ', ')
            #print u' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore')
            except:
                pass
            #pass
        fwr.write("\nCluster %d titles:" % i)
        #for title in frame.ix[i]['title'].values.tolist():
            #title = unicode(title)
            #print (title)
            #fwr.write(u' ' + title + u',')
            
    MDS()
    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
    xs, ys = pos[:, 0], pos[:, 1]
    
    #Visualizing document clusters
    
    #cluster_colors = {0: '#0000A0', 1: '#FF0000'} # #000000, #C0C0C0
    cluster_colors = {0: 'red', 1: 'blue', 2: 'green', 3: 'black'}
    cluster_names = {0: u'1', 
                 1: u'2',
                 2: u'3',
                 3: u'4'}
    
    df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=titles)) 
    groups = df.groupby('label')
    fig, ax = plt.subplots(figsize=(15, 15))
    ax.margins(0.2)
    
    for name, group in groups:
        ax.plot(group.x, group.y, marker='o', linestyle='', ms=22, 
                label=cluster_names[name], color=cluster_colors[name], 
                mec='none')
        ax.set_aspect('auto')
        ax.tick_params(
            axis= 'x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelbottom='off')
        ax.tick_params(
            axis= 'y',         # changes apply to the y-axis
            which='both',      # both major and minor ticks are affected
            left='off',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelleft='off')
        
    ax.legend(numpoints=1)  #show legend with only 1 point
    for i in range(len(df)):
        ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=25) 
    
    #plt.show()
    pylab.savefig('forms_cluster_4.png')
    
    # dendro
    
    linkage_matrix = ward(dist) #define the linkage_matrix using ward clustering pre-computed distances

    fig, ax = plt.subplots(figsize=(12, 10))  # set size
    ax = dendrogram(linkage_matrix, orientation="right", labels=titles)
    
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off')
    
    plt.tight_layout() #show plot with tight layout
    
    #uncomment below to save figure
    plt.savefig('ward_clusters_4.png', dpi=200) #save figure as ward_clusters

    fwr.close()
    return 0

if __name__ == '__main__':
    main()

