__author__ = 'mariosky'


from pylab import *
import itertools, operator

_file = open("w16a-30-p512.dat")

_records = [ map(float,line.split(",")[:-1]) for line in _file if len(line.split(",")) > 3 ]

sample_numbers = {}


#for r in _records[:10]:
#    print r


#### MUESTRA
for r in _records:
    sample_num = int(r[4])
    if sample_num in sample_numbers:
        sample_numbers[sample_num].append(float(r[10]))
    else:
        sample_numbers[sample_num]=[float(r[10])]

results = [ [k, sum(sample_numbers[k])/len(sample_numbers[k]),max(sample_numbers[k]),min(sample_numbers[k])]
             for k in sample_numbers ]
results = array(results)

print results
fig = figure()
ax1 = fig.add_subplot(111)

plt.plot(results[:,0], results[:,2],'g')
plt.plot(results[:,0], results[:,1],'g--')
plt.plot(results[:,0], results[:,3],'g-.')
plt.legend(( 'Maximum','Average',  'Minimum'),
           'lower right', shadow=True)

sample_numbers = {}

### REGRESADOS
for r in _records:
    sample_num = int(r[4])
    if sample_num in sample_numbers:
        sample_numbers[sample_num].append(float(r[3]))
    else:
        sample_numbers[sample_num]=[float(r[3])]

results = [ [k, sum(sample_numbers[k])/len(sample_numbers[k]),max(sample_numbers[k]),min(sample_numbers[k])]
             for k in sample_numbers ]
results = array(results)

print results

plt.plot(results[:,0], results[:,2],'b',linewidth = 2)
plt.plot(results[:,0], results[:,1],'b--',linewidth = 2)
plt.plot(results[:,0], results[:,3],'b-.',linewidth = 2)
plt.legend(( 'Maximum','Average',  'Minimum'),
           'lower right', shadow=True)







ax1.set_axisbelow(True)
ax1.set_title('16 Workers, 30% returned, Re-Insert')
ax1.set_xlabel('Sample number')
ax1.set_ylabel('Fitness')

#plt.show()
plt.savefig('Fitness-w16-30-reinsert.eps')


