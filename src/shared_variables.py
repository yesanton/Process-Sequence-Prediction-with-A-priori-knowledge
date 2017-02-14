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
#eventlog = "bpi_12_w.csv"



#eventlog = "bpi_12_w_no_repeat.csv"
#eventlog = "bpi_13_incidents.csv"




#path_to_model_file = '../output_files/models/model_89-1.50__.h5'
#path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_11/model_27-2.04.h5'
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_13_incidents/model_51-1.06.h5'
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_13_incidents/model_51-1.06.h5'
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models/model.h5'
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_11/model_27-2.04.h5'

# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models/model_56-1.50.h5'
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_11/model_27-2.04.h5'


eventlog = "env_permit.csv"
path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_env_permit/model.h5'

# eventlog = "helpdesk.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_helpdesk/model.h5'


# eventlog = "bpi_11.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_11/model.h5'

#  eventlog = "bpi_12_w_no_repeat.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_12_norep/model.h5'

# eventlog = "bpi_13_incidents.csv"
# path_to_model_file = '/home/yeshch/PycharmProjects/ProcessSequencePrediction/src/output_files/models_bpi_13_incidents/model.h5'



prefix_size_fed = 2
beam_size = 3





