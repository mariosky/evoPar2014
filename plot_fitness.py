__author__ = 'mariosky'


from pylab import *
import itertools, operator

w16_file = open("w16a-30-p512.dat")
w28_file = open("w16-50-p512.dat")
w32_file = open("w16-70-p512.dat")

w16_records = [ map(float,line.split(",")[:-2]) for line in w16_file if len(line.split(",")) > 3 ]
w28_records = [ map(float,line.split(",")[:-2]) for line in w28_file if len(line.split(",")) > 3 ]
w32_records = [ map(float,line.split(",")[:-2]) for line in w32_file if len(line.split(",")) > 3 ]

w16_evaluations = []
for key, group in itertools.groupby(w16_records, key=operator.itemgetter(0)):
    w16_evaluations.append( sum([row[9] for row in group]))

w28_evaluations = []
for key, group in itertools.groupby(w28_records, key=operator.itemgetter(0)):
    w28_evaluations.append( sum([row[9] for row in group]))

w32_evaluations = []
for key, group in itertools.groupby(w32_records, key=operator.itemgetter(0)):
    w32_evaluations.append( sum([row[9] for row in group]))

print w16_evaluations
