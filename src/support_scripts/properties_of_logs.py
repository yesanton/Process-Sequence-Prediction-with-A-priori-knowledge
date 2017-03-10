from os import listdir
from os.path import isfile, join
import csv
import time
import copy
import datetime

import numpy as np
from datetime import datetime, timedelta
from src.shared_variables import getUnicode_fromInt
from src.support_scripts.prepare_data import repetitions
import statistics
onlyfiles = [f for f in listdir("../../data/") if isfile(join("../../data/", f))]


for i in range(len(onlyfiles)):
    csvfile = open('../../data/%s' % onlyfiles[i], 'r')
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    next(spamreader, None)  # skip the headers

    lastcase = ''
    line = ''
    firstLine = True
    lines = []
    timeseqs = []  # relative time since previous event
    timeseqs2 = []  # relative time since case start
    timeseqs3 = []  # absolute time of previous event
    times = []
    times2 = []
    times3 = []
    numlines = 0
    casestarttime = None
    lasteventtime = None

    for row in spamreader:
        t = time.strptime(row[2], "%Y-%m-%d %H:%M:%S")
        if row[0] != lastcase:
            casestarttime = t
            lasteventtime = t
            lastcase = row[0]
            if not firstLine:
                lines.append(line)
                timeseqs.append(times)
                timeseqs2.append(times2)
                timeseqs3.append(times3)
            line = ''
            times = []
            times2 = []
            times3 = []
            numlines += 1
        line += getUnicode_fromInt(row[1])
        timesincelastevent = datetime.fromtimestamp(time.mktime(t)) - datetime.fromtimestamp(time.mktime(lasteventtime))
        timesincecasestart = datetime.fromtimestamp(time.mktime(t)) - datetime.fromtimestamp(time.mktime(casestarttime))
        midnight = datetime.fromtimestamp(time.mktime(t)).replace(hour=0, minute=0, second=0, microsecond=0)
        timesincemidnight = datetime.fromtimestamp(time.mktime(t)) - midnight
        timediff = 86400 * timesincelastevent.days + timesincelastevent.seconds
        timediff2 = 86400 * timesincecasestart.days + timesincecasestart.seconds
        times.append(timediff)
        times2.append(timediff2)
        times3.append(datetime.fromtimestamp(time.mktime(t)))
        lasteventtime = t
        firstLine = False

    # add last case
    lines.append(line)
    timeseqs.append(times)
    timeseqs2.append(times2)
    timeseqs3.append(times3)
    numlines += 1

    divisor = np.mean([item for sublist in timeseqs for item in sublist])
    #print('divisor: {}'.format(divisor))
    divisor2 = np.mean([item for sublist in timeseqs2 for item in sublist])
    #print('divisor2: {}'.format(divisor2))
    divisor3 = np.mean(map(lambda x: np.mean(map(lambda y: x[len(x) - 1] - y, x)), timeseqs2))
    #print('divisor3: {}'.format(divisor3))

    elems_per_fold = int(round(numlines / 3))

    fold1and2lines = lines[:2 * elems_per_fold]

    step = 1
    sentences = []
    softness = 0
    next_chars = []
    fold1and2lines = map(lambda x: x + '!', fold1and2lines)
    maxlen = max(map(lambda x: len(x), fold1and2lines))

    chars = map(lambda x: set(x), fold1and2lines)
    chars = list(set().union(*chars))
    chars.sort()
    target_chars = copy.copy(chars)
    chars.remove('!')
    #print('total chars: {}, target chars: {}'.format(len(chars), len(target_chars)))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))
    target_char_indices = dict((c, i) for i, c in enumerate(target_chars))
    target_indices_char = dict((i, c) for i, c in enumerate(target_chars))
    #print(indices_char)

    number = 0
    numberOfCycles = 0
    averageLengthOfCycle = 0
    lenMedian = []
    for j in range(len(lines)):
        line = lines[j]
        rep = list(repetitions(line))
        number += len(lines[j])
        lenMedian.append(len(lines[j]))
        for k in range (len(rep)):
            numberOfCycles += 1
            averageLengthOfCycle += rep[k][1]
        #print rep

    averageLengthOfCycle /= float(numberOfCycles)
    averageNumberOfCyclesPerTrace = float(numberOfCycles) / float(len(lines))
    number = float(number)
    number /= float(len(lines))

    print "```File name: " + str(onlyfiles[i])
    print "```Number of traces: " + str(len(lines))
    print "```Average trace length: " + str(number)
    print "```Nubmer of cases: " + str (len(target_indices_char))
    print "`````Average number of cycles per trace: " + str(averageNumberOfCyclesPerTrace)
    print "`````Average length of the cycle: " + str(averageLengthOfCycle)
    print "``@@`` Median length of the trace:  " + str(statistics.median(lenMedian))
    print "_______________________________________________________________________________"
