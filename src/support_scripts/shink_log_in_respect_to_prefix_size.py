'''
This script to cut the prefixes from the log
in order to infer formulas later using prom Declare miner

Author: Anton Yeshchenko
'''

import csv

import time

eventlog_in = "./../../data/bpi_11.csv"

prefix_size = 20


csvfile_in = open('%s' % eventlog_in, 'r')
spamreader = csv.reader(csvfile_in, delimiter=',', quotechar=' ')
next(spamreader, None)  # skip the headers

eventlog_out = eventlog_in[:-4] + "_cut_" + str(prefix_size) + ".csv"

with open('%s' % eventlog_out, 'wb') as csvfile_out:
    writer = csv.writer(csvfile_out, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["CaseID","ActivityID","CompleteTimestamp"])

    case_id = None
    buffer = []
    for row in spamreader:

        if (row[0] != case_id):
            case_id = row[0]
            for i in range(len(buffer)):
                if not i < prefix_size:
                    writer.writerow(buffer[i])
            buffer = []
        buffer.append(row)





