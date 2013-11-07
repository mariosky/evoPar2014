__author__ = 'mariosky'


from pylab import *
import itertools, operator




# w2_file = open("w2-256-p512-Real.dat")
# w4_file = open("w4-256-p512-Real.dat")
# w8_file = open("w8-256-p512-Real.dat")
# w16_file = open("w16-256-p512-Real.dat")
# w28_file = open("w28-256-p512-Real.dat")


w2_file = open("w2-256-p512-Standard.dat")
w4_file = open("w4-256-p512-Standard.dat")
w8_file = open("w8-256-p512-Standard.dat")
w16_file = open("w16-256-p512-Standard.dat")
w28_file = open("w28-256-p512-Standard.dat")


w2_records = [ map(float,line[:-1].split(",")) for line in w2_file if len(line.split(",")) > 3 ]
w4_records = [ map(float,line[:-1].split(",")) for line in w4_file if len(line.split(",")) > 3 ]
w8_records = [ map(float,line[:-1].split(",")) for line in w8_file if len(line.split(",")) > 3 ]
w16_records = [ map(float,line[:-1].split(",")) for line in w16_file if len(line.split(",")) > 3 ]
w28_records = [ map(float,line[:-1].split(",")) for line in w28_file if len(line.split(",")) > 3 ]



w2_evaluations = []
for key, group in itertools.groupby(w2_records, key=operator.itemgetter(0)):
    w2_evaluations.append( sum([row[9] for row in group]))

w4_evaluations = []
for key, group in itertools.groupby(w4_records, key=operator.itemgetter(0)):
    w4_evaluations.append( sum([row[9] for row in group]))

w8_evaluations = []
for key, group in itertools.groupby(w8_records, key=operator.itemgetter(0)):
    w8_evaluations.append( sum([row[9] for row in group]))

w16_evaluations = []
for key, group in itertools.groupby(w16_records, key=operator.itemgetter(0)):
    w16_evaluations.append( sum([row[9] for row in group]))

w28_evaluations = []
for key, group in itertools.groupby(w28_records, key=operator.itemgetter(0)):
    w28_evaluations.append( sum([row[9] for row in group]))

local_file = open("512-p512-1362772104.dat")
local_evaluations = [ map(float,line[:-1].split(","))[3] for line in local_file ]


data = [local_evaluations,w2_evaluations, w4_evaluations,w8_evaluations, w16_evaluations, w28_evaluations]

print map(len,data)
# multiple box plots on one figure
fig = figure()
ax1 = fig.add_subplot(111)

bp = plt.boxplot(data)

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

# Hide these grid behind plot objects
ax1.set_axisbelow(True)
ax1.set_title('Evaluations to solution. 256 peaks/512 bits')
ax1.set_xlabel('Local Execution/ Standard workers')
ax1.set_ylabel('Number of evaluations')

xtickNames = plt.setp(ax1, xticklabels= ["Local Core i7","2","4","8","16","28"] )
#plt.setp(xtickNames, rotation=45, fontsize=8)
plt.setp(xtickNames)

plt.savefig('plot_evals.eps')

w2_file.close()
w4_file.close()
w8_file.close()
w16_file.close()
w28_file.close()
local_file.close()



