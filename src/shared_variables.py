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

def activateSettings(logNumber):
    if logNumber == 0:
        eventlog = "bpi_11.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_11/model.h5'
        median = 31
        #BPI11_strong
        formula= "[]( ( \"7\" -> <>( \"15\" ) ) )  /\  []( ( \"0\" -> <>( \"1\" ) ) ) /\ <>\"0\" /\ <>\"7\" "
        #BPI11_weak
        formula  = "<>(\"0\") /\ <>(\"15\")"
    elif logNumber == 1:
        eventlog = "bpi_12_w_no_repeat.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_12_norep/model.h5'
        median = 4
    elif logNumber == 2:
        eventlog = "bpi_12_w.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_12_w/model_23-1.67.h5'
        median = 6
    elif logNumber == 3:
        eventlog = "bpi_13_incidents.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_13_incidents/model.h5'
        median = 6
    elif logNumber == 4:
        eventlog = "bpi_17.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_17/model.h5'
        median = 17
    elif logNumber == 5:
        eventlog = "env_permit.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_env_permit/model.h5'
        median = 43
    elif logNumber == 6:
        eventlog = "helpdesk.csv"
        path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_helpdesk/model.h5'
        median = 4
    beam_size = 3
    prefix_size_pred_from = median - 2
    prefix_size_pred_to =  median + 2

    return eventlog, path_to_model_file, beam_size, \
           prefix_size_pred_from, prefix_size_pred_to, formula

eventlog, path_to_model_file, beam_size, \
    prefix_size_pred_from, prefix_size_pred_to, formula = activateSettings(0)

# eventlog = "bpi_14_detail_incident.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_17/model.h5'



