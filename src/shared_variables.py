'''
This file was created in order to bring
common variables and functions into one file to make
code more clear

Author: Anton Yeshchenko
'''
# evaluate_suffix_start_from = 2
# evaluate_suffix_end = 3

ascii_offset = 161

def getUnicode_fromInt(ch):
    return unichr(int(ch) + ascii_offset)

def getInt_fromUnicode(unch):
    return (int(ord(unch)) - ascii_offset)

#
# eventlog = "env_permit.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_env_permit/model.h5'

# eventlog = "helpdesk.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_helpdesk/model.h5'


# eventlog = "bpi_11.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_11/model.h5'

# eventlog = "bpi_12_w_no_repeat.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_12_norep/model.h5'
#
eventlog = "bpi_13_incidents.csv"
path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_13_incidents/model.h5'
#
# eventlog = "bpi_12_w.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_12_w/model_23-1.67.h5'

# eventlog = "bpi_17.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_17/model.h5'


prefix_size_fed = 2
beam_size = 3

prefix_size_pred_from = 5
prefix_size_pred_to = 9



