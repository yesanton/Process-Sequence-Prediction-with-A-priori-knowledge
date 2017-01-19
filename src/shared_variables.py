'''
This file was created in order to bring
common variables and functions into one file to make
code more clear

Author: Anton Yeshchenko
'''

ascii_offset = 161

def getUnicode_fromInt(ch):
    return unichr(int(ch) + ascii_offset)

def getInt_fromUnicode(unch):
    return (int(ord(unch)) - ascii_offset)

#eventlog = "helpdesk.csv"
#eventlog = "bpi_11.csv"
#eventlog = "bpi_12_w.csv"
eventlog = "bpi_13_incidents.csv"

#path_to_model_file = '../output_files/models/model_89-1.50__.h5'
#path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_11/model_27-2.04.h5'
path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_13_incidents/model_51-1.06.h5'







