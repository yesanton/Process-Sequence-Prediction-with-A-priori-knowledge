import csv

import time

eventlog_in = "bpi_11_big.csv"
csvfile_in = open('%s' % eventlog_in, 'r')
spamreader = csv.reader(csvfile_in, delimiter=';', quotechar='|')
next(spamreader, None)  # skip the headers

dictionary = {}
dictionary["a"] = 1

give_number = 0

eventlog_out = "bpi_11.csv"
with open('%s' % eventlog_out, 'wb') as csvfile_out:
    writer = csv.writer(csvfile_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["CaseID","ActivityID","CompleteTimestamp"])

    mark = True

    current_event = 0
    for row in spamreader:
        timestamp = row[85] #timestamp in hospital log
        split_time = timestamp.split("T")

        timestamp = split_time[0]+" "+ split_time[1].split("+")[0]

        if row[1] not in dictionary:
            dictionary[row[1]] = give_number
            give_number = give_number + 1


        output = []
        output.append(row[0])
        output.append(dictionary[row[1]])
        output.append(timestamp)

        if mark:
            mark = False
            trace_save = [output]
        if current_event != row[0]:
            current_event = row[0]
            if len(trace_save) < 200:
                for i in range(len(trace_save)):
                    writer.writerow(trace_save[i])
            trace_save = [output]
        else:
            trace_save.append(output)








