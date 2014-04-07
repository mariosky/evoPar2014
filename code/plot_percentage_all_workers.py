__author__ = 'mariosky'

from pylab import *
import os

PERCENT = '90'

#file_names = [file_name for file_name in os.listdir('.') if file_name.endswith('%s-p512.dat' % PERCENT ) ]
#file_names =[ 'w4a-30-p512.dat', 'w4b-30-p512.dat', 'w8a-30-p512.dat', 'w8b-30-p512.dat','w16a-30-p512.dat', 'w16b-30-p512.dat' ]

file_names = ['w4g-90-p512.dat', 'w4h-90-p512.dat', 'w8g-90-p512.dat', 'w8h-90-p512.dat', 'w16g-90-p512.dat', 'w16h-90-p512.dat']

print file_names
opened_files = map(open, file_names)
times = [[ map(float,line[:-1].split(","))[1] for line in f if len(line.split(",")) == 3 ] for f in opened_files ]


fig = figure()
ax1 = fig.add_subplot(111)

bp = plt.boxplot(times)

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)

ax1.set_axisbelow(True)
ax1.set_title('Number of Workers, %s Percent of Returned Samples' %(PERCENT) )
ax1.set_xlabel('Re-Insert (left)   Random (right)')
ax1.set_ylabel('Time in seconds')

xtickNames = plt.setp(ax1, xticklabels= [f.split('-')[0][1:-1] for f in file_names] )
plt.setp(xtickNames)

#show()
plt.savefig('plot_percent_%s.eps' % ( PERCENT) )

map(file.close, opened_files)

