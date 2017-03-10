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



_6_evaluate_beseline_SUFFIX_only.runExperiments()
_9_cycl_SUFFIX_only.py.runExperiments()
_10_cycl_back_SUFFIX_only.runExperiments()
_11_cycl_pro_SUFFIX_only.runExperiments()