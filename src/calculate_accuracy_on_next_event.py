'''
this script takes as input the output of evaluate_suffix_and_remaining_time.py
therefore, the latter needs to be executed first

Author: Niek Tax
'''

from __future__ import division

import string

import unicodecsv

from src.shared_variables import eventlog

averageTraceLengths = []
print "For event log : " , eventlog
def output(eventlogs, number_logs = 3):
    res_dict = dict()
    res_dict['total'] = []
    res_dict['damerau'] = []

    averageTraceLengthsGroundTruth = 0
    mark = False

    for i in range(number_logs+1):
        csvfile = open('output_files/results/suffix_and_remaining_time' + str(i) + '_%s' % eventlog, 'r')
        r = unicodecsv.reader(csvfile ,encoding='utf-8')
        r.next() # header
        vals = dict()

        average_trace_length = 0

        damerau = 0
        count = 0
        for row in r:
            l = list()
            count += 1
            damerau += float(row[4])
            if row[0] in vals.keys():
                l = vals.get(row[0])
            if len(row[1])==0 and len(row[2])==0:
                l.append(1)
            elif len(row[1])==0 and len(row[2])>0:
                l.append(0)
            elif len(row[1])>0 and len(row[2])==0:
                l.append(0)
            else:
                l.append(int(row[1][0]==row[2][0]))
            vals[row[0]] = l
            #print(vals)

            average_trace_length += len(row[2])

            if not mark:
                averageTraceLengthsGroundTruth += len(row[1])

        if not mark:
            mark = True
            res_dict['average trace lenght ground truth'] = averageTraceLengthsGroundTruth / count
            res_dict['traces'] = count

        averageTraceLengths.append(str(float(average_trace_length)/count))


        l2 = list()
        for k in vals.keys():
            #print('{}: {}'.format(k, vals[k]))
            l2.extend(vals[k])
            res = sum(vals[k])/len(vals[k])
            if k not in res_dict:
                res_dict[k] = ['{:6.5f}'.format(res)]
            else:
                res_dict[k].append('{:6.5f}'.format(res))
        res_dict['total'].append('{:6.5f}'.format(sum(l2)/len(l2)))
        res_dict['damerau'].append('{:6.5f}'.format(damerau/count))

    return res_dict

res = output(eventlog)

print "Unmod pred  --  backtracking  --  protracking"
for key in res:
    if not (key == 'total' or key == 'damerau' or key == 'average trace lenght ground truth' or key == 'traces'):
        print key, ' === ', string.join(res[key], ' - ')

print 'total', ' === ', string.join(res['total'])
print 'damerau', ' === ', string.join(res['damerau'])

print 'average trace lenght === ', string.join(averageTraceLengths, ' - ')
print 'average trace length ground truth === ', res['average trace lenght ground truth']
print 'number of traces ===', res['traces']

