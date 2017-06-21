#!/usr/bin/env python

import re
import collections
import numpy
import scipy.spatial.distance

numpy.set_printoptions(threshold=numpy.nan)

lines = []
counts = []
words = []

with open('sentences.txt', 'r') as f:
    lines = [l.lower().strip() for l in f.readlines()]

unique = {}
for l in lines:
    words_list = [w for w in re.split(r'[^a-z]', l) if w.strip() != '']
    counts.append(collections.Counter(words_list))
    for w in words_list:
        if not unique.has_key(w):
            words.append(w)
            unique[w] = True

A = numpy.zeros((len(lines), len(words)))
for i in range(0, len(lines)):
    for j in range(0, len(words)):
        A[i,j] = counts[i][words[j]]

distances = []
for i in range(0, A.shape[0]):
    distances.append((i, scipy.spatial.distance.cosine(A[0], A[i])))

distances = sorted(distances, key = lambda x: x[1])
print "Two shortest distances:", distances[1], distances[2]
