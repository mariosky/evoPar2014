__author__ = 'mariosky'

__author__ = 'mariosky'


from pylab import *
import itertools, operator, time

_file = open("w16-256-p512-Real.dat")

_records = [ map(float,line[:-1].split(",")) for line in _file if len(line.split(",")) > 3 ]


totals = []
for key, group in itertools.groupby(_records, key=operator.itemgetter(0)):
    rows = [row[5] for row in group]
    totals.append(sum(rows)/len(rows))

get_times = []
for key, group in itertools.groupby(_records, key=operator.itemgetter(0)):
    rows = [row[6] for row in group]
    get_times.append(sum(rows)/len(rows))


evol_times = []
for key, group in itertools.groupby(_records, key=operator.itemgetter(0)):
    rows = [row[7] for row in group]
    evol_times.append(sum(rows)/len(rows))

set_times = []
for key, group in itertools.groupby(_records, key=operator.itemgetter(0)):
    rows = [row[8] for row in group]
    set_times.append(sum(rows)/len(rows))






data = [totals,get_times, evol_times, set_times]
# multiple box plots on one figure
fig = figure()
ax1 = fig.add_subplot(111)

bp = plt.boxplot(data)

ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

# Hide these grid behind plot objects
ax1.set_axisbelow(True)
ax1.set_title('Time spend by each worker in a single sample 28 Workers')
ax1.set_xlabel('Worker Method')
ax1.set_ylabel('Time in seconds, log scale')
ax1.set_yscale('log')

xtickNames = plt.setp(ax1, xticklabels= ["Total time","Get sample","Evolve","Set sample"] )

#plt.setp(xtickNames, rotation=45, fontsize=8)
plt.setp(xtickNames)

#ytickNames = plt.setp(ax1, yticklabels= ["0","1","10","100"] )
#plt.setp(ytickNames)


plt.savefig('plot_ges_%d.eps' % time.time() )

_file.close()

