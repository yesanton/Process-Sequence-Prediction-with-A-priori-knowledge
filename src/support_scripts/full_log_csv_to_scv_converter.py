import csv

import time

import datetime

eventlog_in = "bpi_2014_detail_incident_non_processed.csv"
csvfile_in = open('%s' % eventlog_in, 'r')
spamreader = csv.reader(csvfile_in, delimiter=';', quotechar='|')
next(spamreader, None)  # skip the headers

dictionary = {}
#dictionary["a"] = 1

give_number = 0

eventlog_out = "bpi_14_detail_incident.csv"
with open('%s' % eventlog_out, 'wb') as csvfile_out:
    writer = csv.writer(csvfile_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["CaseID","ActivityID","CompleteTimestamp"])

    mark = True

    current_event = 0
    for row in spamreader:
        timestamp = row[1] #timestamp in hospital log
  #      split_time = timestamp.split("T")

 #       timestamp = split_time[0]+" "+ split_time[1].split("+")[0]

        timestamp = datetime.datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S") #.%f")

        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        if row[3] not in dictionary:
            dictionary[row[3]] = give_number
            give_number = give_number + 1


        output = []
        output.append(row[0])
        output.append(dictionary[row[3]])
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








