'''
this script takes as input the output of evaluate_suffix_and_remaining_time.py
therefore, the latter needs to be executed first

Author: Niek Tax
'''

from __future__ import division

import string
import csv
import unicodecsv
from jellyfish._jellyfish import damerau_levenshtein_distance
import nltk




averageTraceLengths = []

resss = [[]]

#
# def output(eventlogs, number_logs = 6):
#     res_dict = dict()
#     res_dict['total'] = []
#     res_dict['damerau'] = []
#     res_dict['wrong'] = []
#     averageTraceLengthsGroundTruth = 0
#     mark = False
#
#     for i in range(number_logs):
#         csvfile = open('output_files/results/suffix_and_remaining_time' + str(i) + '_%s' % eventlog, 'r')
#         r = unicodecsv.reader(csvfile ,encoding='utf-8')
#         r.next() # header
#         vals = dict()
#
#         average_trace_length = 0
#
#         damerau = 0
#         count = 0
#         for row in r:
#             l = list()
#             count += 1
#             damerau += float(row[4])
#             if row[0] in vals.keys():
#                 l = vals.get(row[0])
#             if len(row[1])==0 and len(row[2])==0:
#                 l.append(1)
#             elif len(row[1])==0 and len(row[2])>0:
#                 l.append(0)
#             elif len(row[1])>0 and len(row[2])==0:
#                 l.append(0)
#             else:
#                 l.append(int(row[1][0]==row[2][0]))
#             vals[row[0]] = l
#             #print(vals)
#
#             average_trace_length += len(row[2])
#
#             if not mark:
#                 averageTraceLengthsGroundTruth += len(row[1])
#
#         if not mark:
#             mark = True
#             res_dict['average trace lenght ground truth'] = averageTraceLengthsGroundTruth / count
#             res_dict['traces'] = count
#
#         averageTraceLengths.append(str(float(average_trace_length)/count))
#
#
#         l2 = list()
#         for k in vals.keys():
#             #print('{}: {}'.format(k, vals[k]))
#             l2.extend(vals[k])
#             res = sum(vals[k])/len(vals[k])
#             if k not in res_dict:
#                 res_dict[k] = ['{:6.5f}'.format(res)]
#             else:
#                 res_dict[k].append('{:6.5f}'.format(res))
#         res_dict['total'].append('{:6.5f}'.format(sum(l2)/len(l2)))
#         res_dict['damerau'].append('{:6.5f}'.format(damerau/count))
#
#     return res_dict

def outputPrefixLe(eventlogs, mode = 'STRONG', prefixLessThan_orEqual = 0, prefixMoreEqal = 0, number_logs = 6):
    res_dict = dict()
    res_dict['total'] = []
    res_dict['damerau'] = []
    res_dict['wrong'] = []
    res_dict['abs_err'] = []
    res_dict['bleu'] = []
    averageTraceLengthsGroundTruth = 0
    mark = False

    traces_wrong = 0
    absolute_dis_DL = 0
    mark2 = True
    for i in range(0,4):#number_logs):
        csvfile = open('output_files/results/' + mode + '/suffix_and_remaining_time' + str(i) + '_%s' % eventlog, 'r')
        r = unicodecsv.reader(csvfile ,encoding='utf-8')
        r.next() # header
        vals = dict()
        lens = dict()


        average_trace_length = 0

        bleu_abs = 0
        damerau = 0
        count = 0

        lensOfGroundTruthDifferentPrefixesLengths = list()
        lensOfGroundTruthDifferentPrefixesLengthsDICT = list()

        for row in r:
            if prefixLessThan_orEqual != 0 and not ((len(row[1]) + int(row[0])) <=  prefixLessThan_orEqual):
                continue
            if prefixMoreEqal != 0 and not ((len(row[1]) + int(row[0])) >= prefixMoreEqal):
                continue
            l = list()
            len1 = list()
            count += 1
            if False:#float(row[4]) < 0.00001:
                #here means that the traces are totally different
                count -= 1
                traces_wrong += 1
            else:
                damerau += float(row[4])
            if row[0] in vals.keys():
                l = vals.get(row[0])
            elif lensOfGroundTruthDifferentPrefixesLengths:
                lensOfGroundTruthDifferentPrefixesLengthsDICT.append(
                    str(int(row[0])-1)+" : " +
                    str(sum(lensOfGroundTruthDifferentPrefixesLengths) /
                        len(lensOfGroundTruthDifferentPrefixesLengths)) + " numOf: " + \
                        str(len(lensOfGroundTruthDifferentPrefixesLengths)))
                del lensOfGroundTruthDifferentPrefixesLengths[:]


            if row[0] in lens.keys():
                len1 = lens.get(row[0])

            lensOfGroundTruthDifferentPrefixesLengths.append(len(row[1]))
            l.append(float(row[4]))
            len1.append(len(row[2]))
            # if len(row[1])==0 and len(row[2])==0:
            #     l.append(1)
            # elif len(row[1])==0 and len(row[2])>0:
            #     l.append(0)
            # elif len(row[1])>0 and len(row[2])==0:
            #     l.append(0)
            # else:
            #     l.append(int(row[1][0]==row[2][0]))
            vals[row[0]] = l
            lens[row[0]] = len1
            #print(vals)




            # str1 = row[1]
            # str2 = row[2]
            # dl = damerau_levenshtein_distance(unicode(str1),unicode(str2))

            # BLEUscore = nltk.translate.bleu_score.sentence_bleu(
            #     unicode(str1),unicode(str2),weights = (0.5, 0.5),
            #     smoothing_function=nltk.translate.bleu_score.SmoothingFunction().method0)
            # absolute_dis_DL += dl
            # bleu_abs += BLEUscore
            # m = max(len(row[1]),len(row[2]))
            # dls = 1 - dl/m

            average_trace_length += len(row[2])

            if not mark:
                averageTraceLengthsGroundTruth += len(row[1])

        lensOfGroundTruthDifferentPrefixesLengthsDICT.append(
            str(row[0]) + " : " +
            str(sum(lensOfGroundTruthDifferentPrefixesLengths) /
                len(lensOfGroundTruthDifferentPrefixesLengths)) + " numOf: " + \
                str(len(lensOfGroundTruthDifferentPrefixesLengths)))

        if not mark:
            mark = True
            res_dict['average trace lenght ground truth'] = averageTraceLengthsGroundTruth / count
            res_dict['traces'] = count

        averageTraceLengths.append(str(float(average_trace_length)/count))


        l2 = list()
        lens2 = list()

        resOUT1 = []
        resOUT2 = []
        for k in vals.keys():
            #print('{}: {}'.format(k, vals[k]))
            l2.extend(vals[k])
            res = sum(vals[k])/len(vals[k])
            if k not in res_dict:
                res_dict[k] = ['{:6.5f}'.format(res)]
            else:
                res_dict[k].append('{:6.5f}'.format(res))

            lens2.extend(lens[k])
            lenRes = sum(lens[k]) / len(lens[k])
            mStr = str(k) + "_avLen"
            if mStr not in res_dict:
                res_dict[mStr] = ['{:6.5f}'.format(lenRes)]
            else:
                res_dict[mStr].append('{:6.5f}'.format(lenRes))

            resOUT1.append(k)
            resOUT2.append(mStr)

        if mark2:
            resss.append(resOUT1)
            resss.append(resOUT2)
            mark2 = False

        res_dict["len_ground_truth_with_resp_to_prefixes"] = lensOfGroundTruthDifferentPrefixesLengthsDICT
        res_dict['total'].append('{:6.5f}'.format(sum(l2)/len(l2)))
        res_dict['damerau'].append('{:6.5f}'.format(damerau/count))
        res_dict['wrong'].append(traces_wrong)
        res_dict['abs_err'].append(absolute_dis_DL/count)
        res_dict['bleu'].append(bleu_abs/count)
        traces_wrong = 0
        absolute_dis_DL = 0
    return res_dict


#res = output(eventlog)

#if you want to experiment with prefix size




logs = ["env_permit.csv","helpdesk.csv","bpi_11.csv","bpi_12_w_no_repeat.csv","bpi_13_incidents.csv","bpi_12_w.csv","bpi_17.csv"]
logs = ["env_permit.csv", "helpdesk.csv","bpi_11.csv","bpi_12_w.csv","bpi_13_incidents.csv","bpi_17.csv"]
with open('output_files/table_all_results.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for eventlog in logs:
        for mode in ['WEAK', 'STRONG']:
            output = []
            output.append(eventlog)
            output.append(mode)
            spamwriter.writerow(output)

            res = outputPrefixLe(eventlog, mode, 0, 0)

            for i in resss:
                for j in i:
                    output = []
                    output.append(j)
                    for k in res[j]:
                        output.append(k)
                    spamwriter.writerow(output)


            print "For event log : ", eventlog, "  mode ", mode
            print "Unmod pred  --  backtracking  --  protracking -- cycles -- cycles#back -- cycles#pro"
            for key in res:
                if not (key == 'total' or key == 'damerau' or key == 'average trace lenght ground truth'
                        or key == 'traces' or key == "wrong" or key == 'abs_err' or key == 'bleu'):
                    print key, ' === ', string.join(res[key], '   ')


            print 'total', ' === ', string.join(res['total'])
            print 'damerau', ' === ', string.join(res['damerau'])

            output = []
            output.append('ALL')
            for i in res['damerau']:
                output.append(i)
            spamwriter.writerow(output)

            print 'average trace lenght === ', string.join(averageTraceLengths, '  ')

            output = []
            output.append('av trace lengths')
            for i in averageTraceLengths:
                output.append(i)
            spamwriter.writerow(output)


            print 'average trace length ground truth === ', res['average trace lenght ground truth']


            output = []
            output.append('average trace lenght ground truth')
            output.append(res['average trace lenght ground truth'])
            spamwriter.writerow(output)

            print 'number of totaly wrong traces === ', res['wrong']
            print 'absolute === ', res['abs_err']
           # print 'BLEU SCORE === ', res['bleu']
            print 'number of traces ===', res['traces']

            output = []
            averageTraceLengths = []
            resss = [[]]

