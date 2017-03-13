'''
This file was created to manage running of experiments.

## settings are in the shared variables file
Author; Anton Yeshchenko
'''


# This will run whole set of experiments
from src.inference_algorithms import _10_cycl_back_SUFFIX_only
from src.inference_algorithms import _11_cycl_pro_SUFFIX_only
from src.inference_algorithms import _6_evaluate_beseline_SUFFIX_only
from src.inference_algorithms import _9_cycl_SUFFIX_only
from src.shared_variables import activateSettings


formula1 = "WEAK"
formula2 = "STRONG"

formula_used = formula1

logNumber = 2


#_6_evaluate_beseline_SUFFIX_only.runExperiments()
#_9_cycl_SUFFIX_only.py.runExperiments()
#_10_cycl_back_SUFFIX_only.runExperiments()


#_6_evaluate_beseline_SUFFIX_only.runExperiments(logNumber,formula_used)
#_9_cycl_SUFFIX_only.runExperiments(logNumber,formula_used)
_10_cycl_back_SUFFIX_only.runExperiments(logNumber,formula_used)
#_11_cycl_pro_SUFFIX_only.runExperiments(logNumber,formula_used)
#
# formula_used = formula2
#
# _6_evaluate_beseline_SUFFIX_only.runExperiments(logNumber,formula_used)
# _9_cycl_SUFFIX_only.runExperiments(logNumber,formula_used)
# _10_cycl_back_SUFFIX_only.runExperiments(logNumber,formula_used)
# _11_cycl_pro_SUFFIX_only.runExperiments(logNumber,formula_used)