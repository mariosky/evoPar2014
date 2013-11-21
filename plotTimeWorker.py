__author__ = 'mariosky'

from pylab import *
import os

WORKERS = 'w4'

file_names = [file_name for file_name in os.listdir('.') if file_name.startswith(WORKERS) and file_name.endswith('p512.dat') ]
print file_names
opened_files = map(open, file_names)
times = [[ map(float,line[:-1].split(","))[1] for line in f if len(line.split(",")) == 3 ] for f in opened_files ]


fig = figure()
ax1 = fig.add_subplot(111)

bp = plt.boxplot(times)

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

ax1.set_axisbelow(True)
ax1.set_title('Percentage of Returned Samples')
ax1.set_xlabel('  Re-Insert                                       Random  ')
ax1.set_ylabel('Time in seconds')

xtickNames = plt.setp(ax1, xticklabels= [f.split('-')[1] for f in file_names] )
plt.setp(xtickNames)

#show()
plt.savefig('plot_time_CRS_%s.eps' % ( WORKERS) )

map(file.close, opened_files)

