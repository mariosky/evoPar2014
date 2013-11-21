__author__ = 'mariosky'


from pylab import *
import itertools, operator
import os

WORKERS = 'w16'

file_names = [file_name for file_name in os.listdir('.') if file_name.startswith(WORKERS) and file_name.endswith('p512.dat') ]
opened_files = map(open, file_names)

records = [[ map(float,line.split(',')[:-1]) for line in f if len(line.split(",")) > 3 ] for f in opened_files ]

data = []

for dataset in records:
    recs = []
    for key, group in itertools.groupby(dataset, key=operator.itemgetter(0)):
        recs.append( sum([row[9] for row in group]))
    data.append(recs)


print map(len,data)

# multiple box plots on one figure
fig = figure()
ax1 = fig.add_subplot(111)

bp = plt.boxplot(data)

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

# Hide these grid behind plot objects
ax1.set_axisbelow(True)
ax1.set_title('Evaluations to solution. 512 peaks/256 bits')
ax1.set_xlabel('%s Workers' % (WORKERS[1:]))
ax1.set_ylabel('Number of evaluations')

xtickNames = plt.setp(ax1, xticklabels= [f.split('-')[1] for f in file_names] )
plt.setp(xtickNames)

plt.savefig('%s_plot_evals.eps' % (WORKERS[1:]))
map(file.close, opened_files)


