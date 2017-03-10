'''
This script prepares data in the format for the testing
algorithms to run

Author: Anton Yeshchenko
'''

from __future__ import division

import copy
import csv
import re
import time
from collections import Counter
from datetime import datetime
from itertools import izip

import numpy as np

from src.formula_verificator import  verify_formula_as_compliant
from src.shared_variables import getUnicode_fromInt


def prepare_testing_data(eventlog, only_compliant = False):
    csvfile = open('../../data/%s' % eventlog, 'r')
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
    print('divisor: {}'.format(divisor))
    divisor2 = np.mean([item for sublist in timeseqs2 for item in sublist])
    print('divisor2: {}'.format(divisor2))
    divisor3 = np.mean(map(lambda x: np.mean(map(lambda y: x[len(x) - 1] - y, x)), timeseqs2))
    print('divisor3: {}'.format(divisor3))

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
    print('total chars: {}, target chars: {}'.format(len(chars), len(target_chars)))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))
    target_char_indices = dict((c, i) for i, c in enumerate(target_chars))
    target_indices_char = dict((i, c) for i, c in enumerate(target_chars))
    print(indices_char)

    # we only need the third fold, because first two were used for training

    fold3 = lines[2 * elems_per_fold:]
    fold3_t = timeseqs[2 * elems_per_fold:]
    fold3_t2 = timeseqs2[2 * elems_per_fold:]
    fold3_t3 = timeseqs3[2 * elems_per_fold:]

    lines = fold3
    lines_t = fold3_t
    lines_t2 = fold3_t2
    lines_t3 = fold3_t3

    # set parameters
    predict_size = maxlen


    return lines, lines_t, lines_t2, lines_t3, maxlen, chars, char_indices,divisor, divisor2, divisor3, predict_size,target_indices_char,target_char_indices


def selectFormulaVerifiedTraces(lines, lines_t, lines_t2, lines_t3, prefix = 0):
    # select only lines with formula verified
    lines_v = []
    lines_t_v = []
    lines_t2_v = []
    lines_t3_v = []
    for line, times, times2, times3 in izip(lines, lines_t, lines_t2, lines_t3):
        if verify_formula_as_compliant(line,prefix):
            lines_v.append(line)
            lines_t_v.append(times)
            lines_t2_v.append(times2)
            lines_t3_v.append(times3)

    return lines_v, lines_t_v, lines_t2_v, lines_t3_v


# define helper functions
# this one encodes the current sentence into the onehot encoding
def encode(sentence, times, times3, maxlen, chars, char_indices, divisor, divisor2):
    num_features = len(chars) + 5
    X = np.zeros((1, maxlen, num_features), dtype=np.float32)
    leftpad = maxlen - len(sentence)
    times2 = np.cumsum(times)
    for t, char in enumerate(sentence):
        midnight = times3[t].replace(hour=0, minute=0, second=0, microsecond=0)
        timesincemidnight = times3[t] - midnight
        multiset_abstraction = Counter(sentence[:t + 1])
        for c in chars:
            if c == char:
                X[0, t + leftpad, char_indices[c]] = 1
        X[0, t + leftpad, len(chars)] = t + 1
        X[0, t + leftpad, len(chars) + 1] = times[t] / divisor
        X[0, t + leftpad, len(chars) + 2] = times2[t] / divisor2
        X[0, t + leftpad, len(chars) + 3] = timesincemidnight.seconds / 86400
        X[0, t + leftpad, len(chars) + 4] = times3[t].weekday() / 7
    return X

# modify to be able to get second best prediction
def getSymbol(predictions, target_indices_char, ith_best=0):
    i = np.argsort(predictions)[len(predictions) - ith_best - 1]
    return target_indices_char[i]

#modify to be able to get second best prediction
def getSymbolAmpl(predictions, target_indices_char,target_char_indices, start_of_the_cycle_symbol, stop_symbol_probability_amplifier_current, ith_best = 0):
    a_pred = list(predictions)
    if start_of_the_cycle_symbol in target_char_indices:
        place_of_starting_symbol = target_char_indices[start_of_the_cycle_symbol]
        a_pred[place_of_starting_symbol] =  a_pred[place_of_starting_symbol] / stop_symbol_probability_amplifier_current
    i = np.argsort(a_pred)[len(a_pred) - ith_best - 1]
    return target_indices_char[i]


#find repetitions
def repetitions(s):
   r = re.compile(r"(.+?)\1+")
   for match in r.finditer(s):
       yield (match.group(1), len(match.group(0))/len(match.group(1)))


def amplify(s):
    list_of_rep = list(repetitions(s))
    if list_of_rep:
        str_rep = list_of_rep[-1][0]
        if s.endswith(str_rep):
            #return np.math.exp(np.math.pow(list_of_rep[-1][-1],3)), list_of_rep[-1][0][0]
            return np.math.exp(list_of_rep[-1][-1]), list_of_rep[-1][0][0]
            # return np.math.pow(list_of_rep[-1][-1],2)
            #return list_of_rep[-1][-1]
        else:
            return 1, list_of_rep[-1][0][0]
    return 1, " "


#the match.group(0) finds the whole substring that contains 1+ cycles
# #the match.group(1) finds the substring that indicates the cycle









