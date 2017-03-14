import csv

import time

import datetime

eventlog_in = "bpi_2014_detail_incident_non_processed.csv"
eventlog_out = "bpi_14_detail_incident.csv"

CASE_ID = 0
ACTIVITY_ID = 3
TIMESTAMP_ID = 1


csvfile_in = open('%s' % eventlog_in, 'r')
spamreader = csv.reader(csvfile_in, delimiter=';', quotechar='|')
next(spamreader, None)  # skip the headers

dictionary = {}
#dictionary["a"] = 1

give_number = 0


with open('%s' % eventlog_out, 'wb') as csvfile_out:
    writer = csv.writer(csvfile_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["CaseID","ActivityID","CompleteTimestamp"])

    mark = True

    current_event = 0
    for row in spamreader:
        timestamp = row[TIMESTAMP_ID] #timestamp in hospital log
  #      split_time = timestamp.split("T")

 #       timestamp = split_time[0]+" "+ split_time[1].split("+")[0]

        timestamp = datetime.datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S") #.%f")

        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        if row[ACTIVITY_ID] not in dictionary:
            dictionary[row[ACTIVITY_ID]] = give_number
            give_number = give_number + 1


        output = []
        output.append(row[CASE_ID])
        output.append(dictionary[row[ACTIVITY_ID]])
        output.append(timestamp)

        if mark:
            mark = False
            trace_save = [output]
        if current_event != row[CASE_ID]:
            current_event = row[CASE_ID]
            if len(trace_save) < 200:
                for i in range(len(trace_save)):
                    writer.writerow(trace_save[i])
            trace_save = [output]
        else:
            trace_save.append(output)








